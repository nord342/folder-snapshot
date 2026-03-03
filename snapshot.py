#!/usr/bin/env python3
"""
snapshot.py — Generate an instant overview of any folder.

Walks a folder and exports a full file tree (with sizes, types, and
folder summaries) to a plain-text file and a CSV you can open in
Google Sheets or Excel.

Usage:
    python3 snapshot.py "/path/to/folder"

Output (saved inside the scanned folder):
    Folder Snapshot.txt
    Folder Snapshot.csv
"""

import os
import sys
import csv
from collections import defaultdict
from datetime import datetime

# ── File type definitions ─────────────────────────────────────────────────────

FILE_TYPES = {
    "Video":    {".mp4", ".mkv", ".mov", ".avi", ".m4v", ".webm", ".flv", ".wmv", ".mpg", ".mpeg"},
    "Audio":    {".mp3", ".wav", ".flac", ".aac", ".m4a", ".ogg", ".wma"},
    "Image":    {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".tiff", ".heic"},
    "PDF":      {".pdf"},
    "Document": {".doc", ".docx", ".odt", ".rtf", ".txt", ".md"},
    "Spreadsheet": {".xls", ".xlsx", ".ods", ".csv"},
    "Presentation": {".ppt", ".pptx", ".odp"},
    "Archive":  {".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"},
    "Code":     {".py", ".js", ".ts", ".html", ".css", ".json", ".xml", ".sh", ".bat", ".php", ".rb", ".go", ".rs", ".c", ".cpp", ".h", ".java"},
    "Ebook":    {".epub", ".mobi", ".azw", ".azw3"},
}

def get_file_type(ext):
    ext = ext.lower()
    for type_name, extensions in FILE_TYPES.items():
        if ext in extensions:
            return type_name
    return "Other"


# ── Size formatting ───────────────────────────────────────────────────────────

def fmt_size(size_bytes):
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 ** 2:
        return f"{size_bytes / 1024:.1f} KB"
    elif size_bytes < 1024 ** 3:
        return f"{size_bytes / 1024**2:.1f} MB"
    else:
        return f"{size_bytes / 1024**3:.2f} GB"


# ── Core walker ───────────────────────────────────────────────────────────────

def walk_folder(root):
    """
    Walk the root folder and return:
      - tree_lines: list of display lines for the TXT tree
      - file_rows:  list of dicts for the CSV (one row per file)
      - stats:      summary counts/sizes
    """
    root = os.path.abspath(root)
    tree_lines = []
    file_rows = []

    stats = {
        "total_files": 0,
        "total_dirs": 0,
        "total_size": 0,
        "by_type": defaultdict(lambda: {"count": 0, "size": 0}),
    }

    def _walk(current_path, prefix=""):
        try:
            entries = sorted(os.scandir(current_path), key=lambda e: (not e.is_dir(), e.name.lower()))
        except PermissionError:
            tree_lines.append(f"{prefix}[Permission Denied]")
            return

        for i, entry in enumerate(entries):
            is_last = i == len(entries) - 1
            connector = "└── " if is_last else "├── "
            extension = "" if entry.is_dir() else os.path.splitext(entry.name)[1]
            file_type = "Folder" if entry.is_dir() else get_file_type(extension)

            if entry.is_dir():
                stats["total_dirs"] += 1
                tree_lines.append(f"{prefix}{connector}{entry.name}/")
                new_prefix = prefix + ("    " if is_last else "│   ")
                _walk(entry.path, new_prefix)
            else:
                try:
                    size_bytes = entry.stat().st_size
                except OSError:
                    size_bytes = 0

                stats["total_files"] += 1
                stats["total_size"] += size_bytes
                stats["by_type"][file_type]["count"] += 1
                stats["by_type"][file_type]["size"] += size_bytes

                size_str = fmt_size(size_bytes)
                tree_lines.append(f"{prefix}{connector}{entry.name}  [{size_str}]")

                rel_path = os.path.relpath(entry.path, root)
                # Parent folder relative to root
                parent = os.path.relpath(os.path.dirname(entry.path), root)
                if parent == ".":
                    parent = "(root)"

                file_rows.append({
                    "Folder": parent,
                    "File Name": entry.name,
                    "Type": file_type,
                    "Extension": extension.lower() if extension else "(none)",
                    "Size": size_str,
                    "Size (bytes)": size_bytes,
                    "Full Path": rel_path,
                })

    _walk(root)
    return tree_lines, file_rows, stats


# ── Writers ───────────────────────────────────────────────────────────────────

def write_txt(output_path, root_name, tree_lines, stats, generated_at):
    lines = []
    lines.append(f"FOLDER SNAPSHOT")
    lines.append(f"Folder  : {root_name}")
    lines.append(f"Created : {generated_at}")
    lines.append("=" * 72)
    lines.append("")
    lines.append(f"{root_name}/")

    for line in tree_lines:
        lines.append(line)

    lines.append("")
    lines.append("=" * 72)
    lines.append("  SUMMARY")
    lines.append("=" * 72)
    lines.append(f"  Total files   : {stats['total_files']}")
    lines.append(f"  Total folders : {stats['total_dirs']}")
    lines.append(f"  Total size    : {fmt_size(stats['total_size'])}")
    lines.append("")
    lines.append("  Files by type:")

    for type_name, info in sorted(stats["by_type"].items()):
        lines.append(
            f"    {type_name:<15} {info['count']:>4} file(s)   {fmt_size(info['size'])}"
        )

    lines.append("=" * 72)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def write_csv(output_path, file_rows, stats, generated_at):
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        # File list sheet
        fieldnames = ["Folder", "File Name", "Type", "Extension", "Size", "Size (bytes)", "Full Path"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(file_rows)

        # Blank row then summary
        f.write("\n")
        f.write("SUMMARY\n")
        f.write(f"Total files,{stats['total_files']}\n")
        f.write(f"Total folders,{stats['total_dirs']}\n")
        f.write(f"Total size,{fmt_size(stats['total_size'])}\n")
        f.write("\n")
        f.write("Type,File Count,Total Size\n")
        for type_name, info in sorted(stats["by_type"].items()):
            f.write(f"{type_name},{info['count']},{fmt_size(info['size'])}\n")


# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    folder = sys.argv[1].strip().rstrip("/")

    if not os.path.isdir(folder):
        print(f"\nError: '{folder}' is not a valid folder.\n")
        sys.exit(1)

    root_name = os.path.basename(os.path.abspath(folder))
    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    print(f"\nfolder-snapshot")
    print(f"{'─' * 40}")
    print(f"Scanning: {folder}")
    print("Building file tree...\n")

    tree_lines, file_rows, stats = walk_folder(folder)

    txt_path = os.path.join(folder, "Folder Snapshot.txt")
    csv_path = os.path.join(folder, "Folder Snapshot.csv")

    write_txt(txt_path, root_name, tree_lines, stats, generated_at)
    write_csv(csv_path, file_rows, stats, generated_at)

    print(f"{'=' * 72}")
    print(f"  Done! Files saved:")
    print(f"    {txt_path}")
    print(f"    {csv_path}")
    print(f"\n  Total files   : {stats['total_files']}")
    print(f"  Total folders : {stats['total_dirs']}")
    print(f"  Total size    : {fmt_size(stats['total_size'])}")
    print(f"{'=' * 72}")
    print("\n  Files by type:")
    for type_name, info in sorted(stats["by_type"].items()):
        print(f"    {type_name:<15} {info['count']:>4} file(s)   {fmt_size(info['size'])}")
    print()


if __name__ == "__main__":
    main()

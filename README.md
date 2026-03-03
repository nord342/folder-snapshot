# folder-snapshot

A simple command-line tool that scans any folder and generates a **complete file tree overview** — with file sizes, file types, and folder summaries — exported as both a plain-text file and a CSV you can open in Google Sheets or Excel.

Works with any files: videos, PDFs, Word documents, spreadsheets, images, ZIPs, audio files, and more.

---

## Why?

Ever downloaded a course, bundle, or archive and wanted to quickly see exactly what's inside — every file, every folder, how big everything is — without clicking through each subfolder one by one? That's what folder-snapshot is for.

Run one command and get a clean, shareable overview of the entire structure saved as a file.

---

## Output

Two files are saved directly inside the scanned folder:

- `Folder Snapshot.txt` — clean, readable file tree with sizes and a summary
- `Folder Snapshot.csv` — one row per file, importable into Google Sheets or Excel

**Sample TXT output:**

```
FOLDER SNAPSHOT
Folder  : My Course
Created : 2026-03-03 21:18
========================================================================

My Course/
├── Resources/
│   ├── Bonus Audio.mp3  [22.0 MB]
│   ├── Course Workbook.pdf  [4.0 MB]
│   └── Reading List.docx  [28.0 KB]
├── Week 1 - Getting Started/
│   ├── 01. Introduction.mp4  [180.0 MB]
│   ├── 02. Setting Up Your Environment.mp4  [95.0 MB]
│   └── Worksheet 1.pdf  [320.0 KB]
├── Week 2 - Core Concepts/
│   ├── 03. Deep Dive Part 1.mp4  [420.0 MB]
│   └── Notes.docx  [48.0 KB]
└── README.txt  [1.0 KB]

========================================================================
  SUMMARY
========================================================================
  Total files   : 13
  Total folders : 4
  Total size    : 1.58 GB

  Files by type:
    Audio              1 file(s)   22.0 MB
    Document           3 file(s)   77.0 KB
    PDF                3 file(s)   4.5 MB
    Video              5 file(s)   1.55 GB
========================================================================
```

**Sample CSV output** (Google Sheets):

| Folder | File Name | Type | Extension | Size | Size (bytes) | Full Path |
|---|---|---|---|---|---|---|
| Week 1 - Getting Started | 01. Introduction.mp4 | Video | .mp4 | 180.0 MB | 188743680 | Week 1.../01. Introduction.mp4 |
| Week 1 - Getting Started | Worksheet 1.pdf | PDF | .pdf | 320.0 KB | 327680 | Week 1.../Worksheet 1.pdf |
| Resources | Course Workbook.pdf | PDF | .pdf | 4.0 MB | 4194304 | Resources/Course Workbook.pdf |

Full sample files: [`sample_output/`](sample_output/)

---

## Requirements

**Python 3** — no extra packages needed.

- macOS & Linux: Python 3 is pre-installed
- Windows: [Download Python 3](https://www.python.org/downloads/)

---

## Installation

No installation required — just download the single script file.

```bash
# Clone the repo
git clone https://github.com/nord342/folder-snapshot.git

# Or download the script directly
curl -O https://raw.githubusercontent.com/nord342/folder-snapshot/main/snapshot.py
```

---

## Usage

```bash
python3 snapshot.py "/path/to/your/folder"
```

**Tip — macOS/Linux shortcut:** Type the command, then drag and drop the folder from Finder/Files directly into your Terminal window to auto-fill the path.

```bash
python3 snapshot.py    # then drag folder in → press Enter
```

---

## Supported File Types

The summary groups files into the following categories:

| Category | Extensions |
|---|---|
| Video | `.mp4` `.mkv` `.mov` `.avi` `.m4v` `.webm` `.flv` `.wmv` |
| Audio | `.mp3` `.wav` `.flac` `.aac` `.m4a` `.ogg` `.wma` |
| Image | `.jpg` `.jpeg` `.png` `.gif` `.bmp` `.svg` `.webp` `.tiff` `.heic` |
| PDF | `.pdf` |
| Document | `.doc` `.docx` `.odt` `.rtf` `.txt` `.md` |
| Spreadsheet | `.xls` `.xlsx` `.ods` `.csv` |
| Presentation | `.ppt` `.pptx` `.odp` |
| Archive | `.zip` `.rar` `.7z` `.tar` `.gz` `.bz2` |
| Ebook | `.epub` `.mobi` `.azw` `.azw3` |
| Code | `.py` `.js` `.ts` `.html` `.css` `.json` and more |
| Other | Anything not in the above categories |

---

## Import CSV into Google Sheets

1. Open [Google Sheets](https://sheets.google.com) → **File → Import**
2. Upload `Folder Snapshot.csv`
3. Set separator to **Comma** → Import

You can then filter by file type, sort by size, search for specific files, and more.

---

## Also made by the same author

Looking to catalogue a **video course** specifically — with video durations and watch-time estimates? Check out:

👉 [video-course-toc-generator](https://github.com/nord342/video-course-toc-generator)

---

## License

MIT — free to use, modify, and share.

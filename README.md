# folder-snapshot

A lightweight command-line tool that scans any folder on your computer and generates a **complete, readable overview** of everything inside it — every file, every subfolder, file sizes, file types, and totals — saved as a plain-text file and a CSV you can open in Google Sheets or Excel.

No GUI, no installation, no dependencies. Just Python 3 and one command.

---

## Why?

Folders accumulate clutter. Projects grow. Downloads pile up. Hard drives fill. Whether you're trying to understand what's taking up space, document a project structure, audit a shared drive, or just get a clear picture of what you actually have — opening folders one by one doesn't cut it.

folder-snapshot gives you the full picture in seconds, saved to a file you can read, share, or search.

---

## Output

Two files are saved directly inside the scanned folder:

- `Folder Snapshot.txt` — a clean, indented file tree with sizes and a type summary
- `Folder Snapshot.csv` — one row per file, filterable and sortable in Google Sheets or Excel

**Sample TXT output:**

```
FOLDER SNAPSHOT
Folder  : My Files
Created : 2026-03-03 21:18
========================================================================

My Files/
├── Archive/
│   ├── assets_2023.zip  [85.0 MB]
│   └── old_backups.zip  [220.0 MB]
├── Documents/
│   ├── Contracts/
│   │   ├── NDA Agreement.pdf  [420.0 KB]
│   │   └── Service Agreement.pdf  [380.0 KB]
│   └── Reports/
│       ├── Annual Summary.docx  [240.0 KB]
│       ├── Q1 Report.xlsx  [1.2 MB]
│       └── Q2 Report.xlsx  [980.0 KB]
├── Photos/
│   └── 2024/
│       ├── Family/
│       │   ├── birthday.jpg  [4.0 MB]
│       │   └── christmas.jpg  [6.0 MB]
│       └── Holiday/
│           ├── beach.jpg  [4.0 MB]
│           └── sunset.jpg  [3.0 MB]
├── Projects/
│   └── Website/
│       ├── app.js  [34.0 KB]
│       ├── index.html  [18.0 KB]
│       └── style.css  [9.0 KB]
└── README.txt  [2.0 KB]

========================================================================
  SUMMARY
========================================================================
  Total files   : 16
  Total folders : 10
  Total size    : 330.2 MB

  Files by type:
    Archive            2 file(s)   305.0 MB
    Code               3 file(s)   61.0 KB
    Document           2 file(s)   242.0 KB
    Image              5 file(s)   22.0 MB
    PDF                2 file(s)   800.0 KB
    Spreadsheet        2 file(s)   2.1 MB
========================================================================
```

**Sample CSV output** (Google Sheets):

| Folder | File Name | Type | Extension | Size | Size (bytes) | Full Path |
|---|---|---|---|---|---|---|
| Documents/Contracts | NDA Agreement.pdf | PDF | .pdf | 420.0 KB | 430080 | Documents/Contracts/NDA Agreement.pdf |
| Documents/Reports | Q1 Report.xlsx | Spreadsheet | .xlsx | 1.2 MB | 1228800 | Documents/Reports/Q1 Report.xlsx |
| Photos/2024/Holiday | beach.jpg | Image | .jpg | 4.0 MB | 4194304 | Photos/2024/Holiday/beach.jpg |
| Archive | old_backups.zip | Archive | .zip | 220.0 MB | 230686720 | Archive/old_backups.zip |

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

**Tip — macOS/Linux:** Type the command, then drag and drop the folder from Finder or your file manager directly into the Terminal window to auto-fill the path. Then press Enter.

```bash
python3 snapshot.py    # drag your folder in here → press Enter
```

**Windows:** Open Command Prompt or PowerShell in the folder where `snapshot.py` lives, then run:

```bash
python snapshot.py "C:\Users\You\Documents\My Folder"
```

---

## Supported File Types

Files are automatically detected and grouped by type in the summary:

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

## Import CSV into Google Sheets or Excel

1. Open [Google Sheets](https://sheets.google.com) → **File → Import**
2. Upload `Folder Snapshot.csv`
3. Set separator to **Comma** → Import

Once imported you can filter by file type, sort by size, search for specific files, or build your own summary views.

---

## Use Cases

- **Audit a folder** — see exactly what's there before moving, sharing, or deleting
- **Document a project** — export a clean file tree to share with a team or client
- **Find what's eating disk space** — spot large files and archives at a glance
- **Organise your downloads** — get a full picture before sorting through everything
- **Back up planning** — know exactly what you have and how much space it takes

---

## Also made by the same author

Need to catalogue a **video course or lecture series** — with video durations and total watch time? Check out:

👉 [video-course-toc-generator](https://github.com/nord342/video-course-toc-generator)

---

## License

MIT — free to use, modify, and share.

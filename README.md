# File-Sorter

A Python automation script that organizes messy directories by scanning files and sorting them into categorized subfolders based on their extensions.

## Features
* **Automated Categorization**: Sorts files instantly into five main categories: Documents, Images, Audio, Videos, and Misc.
* **Smart Extension Parsing**: Evaluates file extensions case-insensitively to ensure accurate structural mapping.
* **File Relocation**: Safely transfers items out of the source directory into an organized local directory hierarchy.
* **Summary Counting**: Tracks and displays an exact summary count of the file distribution upon completion.

## Folder Organization Mapping
* **Documents**: `.pdf`, `.txt`
* **Images**: `.jpg`, `.jpeg`, `.png`, `.svg`
* **Audio**: `.mp3`
* **Videos**: `.mp4`
* **Misc**: Any other extension or unmapped file format

## Usage
Run the script from your terminal:

```bash
python file_sorter.py
```

Enter the full or relative directory path you want to organize when prompted.


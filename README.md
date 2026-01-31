# AutoFileOrganizer

AutoFileOrganizer is a Python script that automatically organizes files in a folder into subfolders by type.

## Features
- Organizes **Images**, **Documents**, **Videos**, **Software**, **Archives**
- Unknown file types go to an **Other** folder
- Automatically creates subfolders based on file extensions
- Easy to configure and extend

## Project Structure
AutoFileOrganizer/
├── organize_files.py
├── examples/sample_files
├── docs/images
├── tests
├── requirements.txt
├── LICENSE
└── .gitignore

## Usage
1. Clone the repository:

```bash
git clone https://github.com/yourusername/AutoFileOrganizer.git
cd AutoFileOrganizer

##Add files to examples/sample_files folder.

Run the script:

python organize_files.py


Your files will be organized into folders by type.

Supported File Types

Images: JPG, PNG, GIF, BMP, PSD, TIFF, WEBP

Documents: PDF, DOCX, DOC, TXT, XLSX, PPTX, ODT, EPUB

Videos: MP4, MKV, AVI, MOV, FLV, WMV, WEBM

Software: EXE, MSI, APK, BAT, SH

Archives: ZIP, RAR, 7Z, TAR, GZ

Other unknown files go into Other folder.
System Administrator File Automation Tool
=========================================

AutoFileOrganizer is a Python-based automation tool designed for system administrators
to efficiently organize files in a directory based on file type and extension.
It helps maintain clean folders, reduces manual effort, and improves operational
efficiency in real-world IT environments.

This tool is especially useful for organizing Downloads folders, shared directories,
and workstation/server file systems.


FEATURES
--------
- Automatically categorizes files into:
  - Images
  - Documents
  - Videos
  - Software Installers
  - Archives
  - Other (unknown formats)
- Creates subfolders based on file extensions (JPG, PDF, EXE, etc.)
- Safely handles unknown file formats
- No external dependencies
- Cross-platform (Windows / Linux / macOS)
- Simple and extensible Python code


SYSTEM ADMIN USE CASES
---------------------
- Clean and organize messy Downloads folders
- Maintain order in shared network directories
- Reduce manual file management workload
- Demonstrates Python automation skills for system administrators


PROJECT STRUCTURE
-----------------
AutoFileOrganizer/
|
|-- organize_files.py
|-- README.md
|-- LICENSE
|-- .gitignore


SUPPORTED FILE TYPES
--------------------

Images:
jpg, jpeg, png, gif, bmp, psd, tiff, webp

Documents:
pdf, doc, docx, txt, xls, xlsx, ppt, pptx, odt, epub

Videos:
mp4, mkv, avi, mov, flv, wmv, webm

Software:
exe, msi, apk, bat, sh

Archives:
zip, rar, 7z, tar, gz

Unknown or unsupported file formats are moved to the "Other" folder.


HOW TO USE
----------

1. Clone the repository:
   git clone https://github.com/samathanaprabu/System-Administrator-File-Automation-Tool
   
   cd AutoFileOrganizer

3. Place files inside:
   examples/sample_files/

4. Run the script:
   python organize_files.py

5. Files will be automatically organized into folders
   based on type and extension.


CUSTOMIZATION
-------------

You can edit file categories in organize_files.py:

FILE_TYPES = {
    "Images": ["jpg", "png"],
    "Documents": ["pdf", "docx"]
}

You can also change the folder to organize by updating:
source_folder = "your_folder_path"


TESTING (OPTIONAL)
------------------
Run tests using:
python tests/test_organize.py


SECURITY NOTES
--------------
- No data is sent to external servers
- Runs completely locally
- Safe for enterprise and personal use


SKILLS DEMONSTRATED
-------------------
- Python automation scripting
- File system management
- IT operations optimization
- System administration automation
- Clean and maintainable code design


LICENSE
-------
This project is licensed under the MIT License.
See the LICENSE file for full details.


AUTHOR
------
Samathanaprabu S
System Administrator | IT Automation | Python Scripting


CONTRIBUTIONS
-------------
Contributions, issues, and feature requests are welcome.
Feel free to fork the repository and submit a pull request.

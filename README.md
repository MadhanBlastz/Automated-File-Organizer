# 📂 Automated File Organizer & Directory Cleaner

A lightweight, interactive Python command-line utility designed to declutter and organize messy directories (such as Downloads, Desktop, or Documents) by automatically sorting files into categorized folders based on their extensions.

---

## 🚀 Key Features

* **Dynamic User Input:** Prompts the user for any target folder path instead of using hardcoded directories.
* **Path Validation:** Checks if the provided directory exists and is valid before running.
* **Smart Extension Categorization:** Automatically identifies file extensions and routes them to their designated folders.
* **Robust Error Handling:** Catches `PermissionError` (Windows `WinError 32`) to gracefully skip files currently open in other programs without crashing.
* **Path Cleanup:** Automatically strips accidental quotation marks and spaces when dragging and dropping folders into the terminal.
* **Execution Summary:** Displays a clean summary of total files organized versus skipped.

---

## 🗂️ File Categorization Mapping

The tool sorts files into the following directory structure:

| Category | File Extensions Handled |
| :--- | :--- |
| **Documents** | `.pdf`, `.docx`, `.doc`, `.txt`, `.xlsx`, `.pptx`, `.csv` |
| **Images** | `.jpg`, `.jpeg`, `.png`, `.gif`, `.svg`, `.webp` |
| **Videos** | `.mp4`, `.mkv`, `.mov`, `.avi` |
| **Music** | `.mp3`, `.wav` |
| **Archives** | `.zip`, `.rar`, `.7z`, `.iso` |
| **Code** | `.py`, `.html`, `.css`, `.js`, `.java`, `.cpp`, `.json` |
| **Installers** | `.exe`, `.msi` |
| **Others** | Any recognized extension not listed above |

---

## 🛠️ Tech Stack & Modules

* **Language:** Python 3.x
* **Standard Modules Used:**
  * `os`: Directory traversal, path validation, and folder creation.
  * `shutil`: Secure file movement operations.

---

## 💻 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/MadhanBlastz/automated-file-organizer.git
cd automated-file-organizer
```

### 2. Run the script
```bash
python organizer.py
```

### 3. Enter your directory path
When prompted, type or paste the path to the directory you want to clean:
```text
Enter the folder path to organize: C:\Users\YourName\Downloads
```

---

## 🛡️ Edge Cases Handled

* **Files in Use:** If a file (e.g., `resume.docx`) is currently open in an application like Microsoft Word, the script catches `PermissionError`, prints a skip warning, and seamlessly continues with the remaining files.
* **Nested Folders:** Existing subdirectories and generated category folders are ignored to prevent recursive loops.
* **Input Quotes:** Windows paths wrapped in quotes (from drag-and-drop actions) are automatically sanitized.

---

## 👨‍💻 Author

**Madhankumar Onteddubandi**  
* GitHub: [@MadhanBlastz](https://github.com/MadhanBlastz)  
* LinkedIn: [madhankumaronteddubandi](https://www.linkedin.com/in/madhankumaronteddubandi)

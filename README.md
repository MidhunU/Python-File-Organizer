# 📂 File Sorter & Organizer

Tired of messy folders filled with a million random files? **File Sorter** is a simple, fast Python script that swoops in to rescue your digital workspace. 

With just a few prompts, you can effortlessly sift through cluttered directories and copy specific files (based on their extension or matching keywords) into a neat, organized output folder!

## ✨ Features
* **Extension Filtering**: Need all the `.jpg` and `.png` images? Just type them in.
* **Keyword Matching**: Want to gather every file that has a specific word (like "Vacation") in the name? This script grabs them too!
* **Safe Operations**: File Sorter copies your files over to the new destination. Your original messy folder stays exactly exactly the way it was, acting as a safe backup.

## 🚀 How to Use

1. Ensure you have Python installed on your computer.
2. Clone or download this project.
3. Open a terminal or command prompt in the project directory and run the script:
   ```sh
   python sorter.py
   ```
4. **Follow the interactive prompts:**
   - **Source dest**: Where's the mess? (e.g., `C:\...\Downloads`)
   - **Output dest**: Where do you want the organized files to go? (e.g., `C:\...\Organized`)
   - **Extensions**: Type a comma-separated list of extensions you want to target (e.g., `.jpg, .png`).
5. **Keyword Search**: You can either enter a keyword to search for (or leave it empty if you only want to sort by extension).
      Enter a keyword to search for (or leave empty): `my_fav_picture`
   

## 🛠 Prerequisites
- No external dependencies needed! File Sorter uses Python's standard `os` and `shutil` libraries. 

## 🤝 Contribution
Feel free to fork this project, add new filtering rules (like filtering by date or file size), and make it even more powerful!

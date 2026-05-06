# 📂 Image Sorter & Converter

Tired of messy folders filled with a million random files? **File Sorter** is a simple, fast Python tool that swoops in to rescue your digital workspace. 

With just a few prompts, you can effortlessly sift through cluttered directories, copy specific files (based on their extension or matching multiple keywords), and optionally **convert Apple HEIC/HEIF photos to JPG or PNG**!

## ✨ Features
* **Extension Filtering**: Need all the `.jpg` and `.png` images? Just type them in.
* **Multiple Keyword Matching**: Want to gather files containing words like "Vacation" or "Party" in their names? You can search for multiple comma-separated keywords simultaneously.
* **HEIC/HEIF Conversion**: Seamlessly converts high-efficiency Apple image formats (`.heic`, `.heif`) into standard formats (`.jpg`, `.png`) on the fly.
* **Continuous Processing**: The script loops automatically, allowing you to run multiple sorting and converting tasks back-to-back without restarting.
* **Safe Operations**: File Sorter copies your files over to the new destination. Your original messy folder stays exactly the way it was, acting as a safe backup.

## 🚀 How to Use

1. Ensure you have Python installed on your computer.
2. Clone or download this project.
3. Install the required dependencies using the provided requirements file:
   ```sh
   pip install -r requirements.txt
   ```
4. Open a terminal or command prompt in the project directory and run:
   ```sh
   python sorter.py
   ```

### 📦 Building a Standalone Executable
*(Note: Pre-built executables are not included in this repository.)*
If you want to create a standalone `.exe` file so you can run the tool without needing a Python environment, you can build it yourself:
1. Ensure your dependencies are installed (`pyinstaller` is included in `requirements.txt`).
2. Run the following command:
   ```sh
   python -m PyInstaller --onefile --console --name "Image_CO" --hidden-import PIL --hidden-import pillow_heif sorter.py
   ```
3. The newly compiled `Image_CO.exe` will be generated inside a `dist` folder!

## 🎮 Interactive Prompts Guide

When you run the tool, you will be guided through a series of prompts:
- **Source dest**: Where's the mess? (e.g., `C:\Users\Name\Downloads`) — Type `exit` here to quit the program.
- **Output dest**: Where do you want the organized files to go? (e.g., `C:\Users\Name\Organized`)
- **Extensions**: Type a comma-separated list of extensions you want to target (e.g., `.jpg, .png`).
- **Keyword Search**: Enter comma-separated keywords to search for in the file names (e.g., `IMG_, selfie`). Leave empty to skip.
- **Convert HEIC/HEIF**: If you want to convert Apple image formats, type `.jpg` or `.png`. Leave empty to simply copy them without conversion.

## 🛠 Prerequisites
File Sorter requires external libraries which are listed in `requirements.txt`. Key dependencies include:
- `pillow` (for image processing)
- `pillow-heif` (for HEIC/HEIF conversion)
- `pyinstaller` (optional, for building the executable)

## 🤝 Contribution
Feel free to fork this project, add new filtering rules (like filtering by date or file size), and make it even more powerful!

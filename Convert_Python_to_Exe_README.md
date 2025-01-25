# Convert Python Script to Executable Using PyInstaller

This guide explains how to convert a Python script into a standalone executable file using **PyInstaller**. Follow the steps below:

---

## **Prerequisites**
1. **Python Installed**  
   Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Install PyInstaller**  
   Use the following command to install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

3. **Check Python and PyInstaller Installation**  
   Confirm Python and PyInstaller are installed correctly:
   ```bash
   python --version
   pyinstaller --version
   ```
   If `pyinstaller` is not recognized, check the [troubleshooting section](#troubleshooting).

---

## **Steps to Convert a Script**

1. **Navigate to Your Script Directory**  
   Open a terminal or command prompt and navigate to the folder containing your Python script:
   ```bash
   cd "C:\Path\To\Your\Script"
   ```

2. **Run PyInstaller Command**  
   Use the following command to convert the Python script into a standalone executable:
   ```bash
   pyinstaller --onefile YourScriptName.py
   ```

   - `--onefile`: Combines all dependencies into a single executable.
   - Replace `YourScriptName.py` with the name of your Python script.

3. **Locate the Executable File**  
   After the command finishes, the executable file will be located in the `dist` folder inside your script directory:
   ```
   C:\Path\To\Your\Script\dist\YourScriptName.exe
   ```

4. **Run the Executable**  
   You can now run the standalone `.exe` file without requiring Python installed on the system:
   ```bash
   C:\Path\To\Your\Script\dist\YourScriptName.exe
   ```

---

## **Troubleshooting**

### **PyInstaller Not Recognized**
If you see an error like:
```
'pyinstaller' is not recognized as an internal or external command
```
It means the PyInstaller executable is not in your system's PATH.

1. Locate the PyInstaller script:
   ```
   C:\Users\<YourUsername>\AppData\Roaming\Python\<PythonVersion>\Scripts
   ```

2. Add this path to your system's PATH variable or use the full path to run PyInstaller:
   ```bash
   "C:\Users\<YourUsername>\AppData\Roaming\Python\<PythonVersion>\Scripts\pyinstaller" --onefile YourScriptName.py
   ```

---

## **Example**
### Convert a Script Named `DownloadAnyFileFromTorrent.py`:
1. **Install PyInstaller**:
   ```bash
   pip install pyinstaller
   ```

2. **Run PyInstaller**:
   ```bash
   pyinstaller --onefile DownloadAnyFileFromTorrent.py
   ```

3. **Locate the Executable**:
   Navigate to the `dist` folder:
   ```
   C:\Path\To\Script\dist\DownloadAnyFileFromTorrent.exe
   ```

4. **Run the Executable**:
   Double-click on the `.exe` file or run it from the command prompt:
   ```bash
   C:\Path\To\Script\dist\DownloadAnyFileFromTorrent.exe
   ```

---

## **Notes**
- The generated executable can be shared and run on other systems without needing Python installed.
- Ensure all required libraries are installed before running PyInstaller.
- If you face issues, consider running PyInstaller in a virtual environment.

---

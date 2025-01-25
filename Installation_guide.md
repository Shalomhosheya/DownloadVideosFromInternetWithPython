
# Installation Guide for aria2

This guide will help you install `aria2`, a lightweight multi-protocol & multi-source command-line download utility, and get it working for downloading torrents.

## Prerequisites

- **Operating System**: This guide supports Windows, Linux, and macOS.
- **Python**: If you're using Python scripts to interact with `aria2`, ensure you have Python installed.

## Installation Steps

### 1. **Installing aria2**

#### **On Windows**:

1. **Download the Windows binaries**:
   - Visit the [aria2 GitHub Releases Page](https://github.com/aria2/aria2/releases).
   - Download the latest `.zip` file for Windows (e.g., `aria2-1.36.0-win-64bit-build1.zip`).

2. **Extract the Files**:
   - Extract the contents of the `.zip` file to a folder, e.g., `C:\Program Files\aria2`.

3. **Add aria2 to the System PATH**:
   - Press `Win + R` to open the Run dialog, type `sysdm.cpl`, and hit Enter.
   - Under the **Advanced** tab, click **Environment Variables**.
   - In the **System Variables** section, find and select `Path`, then click **Edit**.
   - Add the path to the folder where you extracted `aria2` (e.g., `C:\Program Files\aria2`).
   - Click **OK** to save the changes.

4. **Verify Installation**:
   - Open a new Command Prompt (`cmd`) and type the following:
     ```bash
     aria2c --version
     ```
   - If the installation was successful, it will display the version of `aria2`.

#### **On Linux (Ubuntu/Debian)**:

1. Open a terminal and run the following command to install `aria2`:
   ```bash
   sudo apt update
   sudo apt install aria2
   ```

2. **Verify Installation**:
   - After installation completes, run:
     ```bash
     aria2c --version
     ```

#### **On macOS**:

1. **Using Homebrew**:
   - If you don't have Homebrew installed, first install it by running the following in the terminal:
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
   - Install `aria2` using Homebrew:
     ```bash
     brew install aria2
     ```

2. **Verify Installation**:
   - After installation completes, run:
     ```bash
     aria2c --version
     ```

---

### 2. **Using aria2 with Python**

If you're using `aria2` with Python (for example, in the provided script), follow these steps:

1. **Install the required Python packages**:
   Ensure that you have the `subprocess` and `shutil` modules available in Python, as they are used to run the `aria2c` command from the Python script.

   You may also need the `requests` library (if working with HTTP downloads):
   ```bash
   pip install requests
   ```

2. **Running the Python script**:
   - Make sure `aria2` is correctly installed and added to the system's PATH.
   - Run the script provided in the previous message to download torrents using `aria2c` via Python.

---

## Troubleshooting

- **aria2c not found**: If you get an error like `aria2c is not recognized as an internal or external command`, make sure you have added the `aria2c` folder to your system's PATH.
- **Error in Python script**: If your script doesn't work as expected, make sure you're capturing the correct output from `aria2c`. You might need to adjust the `stdout` reading logic based on the version of `aria2`.

---

## License

`aria2` is licensed under the [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

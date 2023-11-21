# Installing Python and Flask on Windows

This README will guide you through the process of installing Python and using the `pip` package manager to install Flask on a Windows operating system. This guide is intended for beginners who have no prior experience with Python.

## Table of Contents

1. [Installing Python](#installing-python)
2. [Verifying Python Installation](#verifying-python-installation)
3. [Installing Flask](#installing-flask)

## Installing Python

Python is a widely-used programming language and is essential for running Flask. Follow these steps to install Python on your Windows machine:

1. Visit the official Python website: [python.org](https://www.python.org/downloads/windows/).

2. Scroll down to the "Python Releases for Windows" section and click on the "Download Python x.y.z" button (x.y.z represents the current Python version).

3. On the download page, scroll down again and choose the "Windows installer (64-bit)" or "Windows installer (32-bit)" based on your system architecture. Most modern Windows systems are 64-bit.

4. Once the download is complete, run the installer by double-clicking on the downloaded file.

5. In the Python installer, check the box that says "Add Python x.y.z to PATH" during installation. This is crucial for easily running Python from the command prompt.

6. Click "Install Now" and follow the on-screen instructions to complete the installation.

## Verifying Python Installation

After successfully installing Python, it's essential to verify the installation:

1. Open the Windows Command Prompt by searching for "cmd" or "Command Prompt" in the Start menu.

2. In the Command Prompt, type the following command and press Enter:
   ```
   python --version
   ```

   You should see the Python version you installed displayed in the Command Prompt.

## Installing Flask

Now that Python is installed, you can use `pip` (Python's package manager) to install Flask:

1. Open the Windows Command Prompt.

2. To install Flask, simply run the following command:
   ```
   pip install flask
   ```

   This command will download and install Flask and its dependencies.



Congratulations! You have successfully installed Python and Flask on your Windows machine. You are now ready to start building web applications using Flask. 

## Running programs

Now that all dependencies for this project are installed. To run a file do the following
```
python <filename.py>
```
For calculator with HTML program alone output will in the browser and for rest of them you can see the output locally.
# Install Python on Windows


1. **Download Python 3.10 installer** : Visit the official Python website at python.org/downloads/. Look for the latest version, which should be Python 3.10 (at least at the time of this writing). Click on the download link for the Windows installer (either 32-bit or 64-bit, depending on your system architecture).
2. **Run the installer** : Once the installer is downloaded, locate the file (usually in your Downloads folder) and double-click to run it. You may need administrator privileges to install software on your system.
3. **Configure the installation** : In the installer window, you will see various options. Make sure to check the box that says "Add Python 3.10 to PATH". This will allow you to run Python from the command line without specifying the full path.
4. **Install Python** : Click on the "Install Now" button to start the installation process. The installer will copy files to your computer and set up Python. This process may take a few minutes.
5. **Verify installation** : Once the installation is complete, you can verify that Python has been installed correctly by opening a command prompt and typing `python --version`. You should see something like `Python 3.10.x`, indicating that Python 3.10 has been installed successfully.


# Install Python on MacOS


1. **Download Python 3.10 installer** : Visit the official Python website at python.org/downloads/. Look for the latest version, which should be Python 3.10 (at least at the time of this writing). Click on the download link for macOS.
2. **Run the installer** : Once the installer is downloaded, locate the file (usually in your Downloads folder) and double-click to open it. This will start the installation process.
3. **Configure the installation** : In the installer window, you may see some options. Make sure to check the box that says "Install Python 3.10" or similar. You may also have an option to customize the installation, but for most users, the default options are sufficient.
4. **Install Python** : Click on the "Install" button to start the installation process. You may need to enter your password to authorize the installation.
5. **Verify installation** : Once the installation is complete, you can verify that Python has been installed correctly by opening a terminal and typing `python3 --version`. You should see something like `Python 3.10.x`, indicating that Python 3.10 has been installed successfully.


# Prerequisites

1. After Installing Python. Clone this repository using `git clone https://github.com/fsad-assignment-group57/LLP.git`
2. Then create a virtual env using command `python -m venv venv`
3. Activate virtual env using command `./venv/Scripts/Activate`. Now you are within virtual env.
4. Install requirements using command `pip install -r requirements.txt`
5. Update config.json with DB details.
6. Run `python server.py` to get server up and running on port 5000.

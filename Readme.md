# RocketDock Cleaner
RocketDockCleaner is a Python script designed to clean up and optimize the configuration file (Settings.ini) of RocketDock, a popular application launcher for Windows. The script performs the following tasks:

## Features

### Backup Creation:

Creates a backup of the original Settings.ini file with a new extension (.bk).
You can customize the new_extension variable according to your preference.

### Check and Remove Nonexistent Icons:

Checks for entries in the configuration file related to icons that no longer exist.
Removes the entries associated with nonexistent icons.

### Enumerate Lines:

Enumerates the lines in the configuration file to ensure proper ordering.
Updates the count parameter to reflect the total number of valid entries.

### Update RocketDock Configuration:

Calls the above functions in sequence to create a new RocketDock configuration file.

### Usage
Adjust the file_to_copy variable to match your actual Settings.ini file name.
Customize the new_extension variable if needed.
Run the script.

### ToDo 
Implement a GUI for the script

### Note
Make sure to understand the implications of modifying RocketDock's configuration before running the script.
Always have a backup of important files before making changes.
Disclaimer: Use this script responsibly and at your own risk.
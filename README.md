# Downloads-Organizer
Python program to organize your downloads folder automatically.

## How It Works
Files in the directory you specify will be moved to respective folders with that extension (automatic organization). If you have an existing directory with the name png (even if it does not just contain .png files), the .png files in the root directory of your specified folder will be saved there -- so be careful with how you use this!

## How To Use
Simply install Python3, install requirements using your favorite virtual environment, and add a bash script to run main.py at startup. If you provide the argument -p <absolute_path> or --path <absolute_path>, you will be able to specify target directory without a GUI popping up.

## Supported Systems
This script is tested and run on Ubuntu 18.04.3 LTS and up, but I have not tested on any other systems.

## Example bash script to run at startup as a user application
```
#!/bin/bash

rm -rf Downloads-Organizer
git clone https://github.com/brandongraylong/Downloads-Organizer.git
virtualenv Downloads-Organizer/venv
source Downloads-Organizer/venv/bin/activate
pip install -r Downloads-Organizer/requirements.txt
python Downloads-Organizer/main.py --path /path/to/your/Downloads/folder
deactivate
```

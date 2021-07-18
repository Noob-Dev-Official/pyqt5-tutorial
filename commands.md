# Instruction to setup pyqt on raspberry pi (without venv)
1. sudo apt-get update && sudo apt-get upgrade -y
2. sudo apt-get install qt-default
3. sudo apt-get install qtcreator
4. sudo apt install pyqt5-dev-tools

# Instruction to setup pyqt on raspberry pi (with venv)
Follow this: www.niladicpodcast.com/blog/2017/8/install-pyqt5-inside-a-virtual-environment/

# Command convert a GUI file to code
pyuic5 -x test.ui -o test.py (replace the name of the .ui with your saved .ui file and .py file with what you want name the python file after exporting it
(you need pyqt5-dev-tools to make this happen)

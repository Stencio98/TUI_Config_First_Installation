# TUI_Debian_Configuration
_use this guide if you are not using PyInstaller script `tui`_
* make sure you are root user or in a root shell
* update your system if it is not
```
apt-get clean && apt-get update
apt-get dist-upgrade -y
apt-get full-upgrade -y
apt-get autoremove -y
```
* copy and paste following commands to prepare environment and run tool:
```
# prepare environment and install questionary
sudo apt install -y python3-full &&
python3 -m venv myenv &&
source myenv/bin/activate &&
pip install questionary

# now run tool:
source myenv/bin/activate && python3 tui.py
# deactivate environment:
deactivate

# remove environment folder
rm -rf myenv"
```

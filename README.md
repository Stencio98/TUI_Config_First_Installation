# TUI_Debian_Configuration
* make sure you are root user or in a root shell
* update your system if it is not
* copy and paste following commands to prepare environment:
```
sudo apt install -y python3-full &&
 
python3 -m venv myenv &&

source myenv/bin/activate &&

pip install questionary
```

* now TUI Debian Configuration ready
* "to run tool:"
```
source myenv/bin/activate && python3 scripts/tui.py
```
* to end virtual ambient python:
```
deactivate
rm -rf myenv
```

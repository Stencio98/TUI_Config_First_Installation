# Use PyInstaller to don't use an environment and libraries
_it makes a script or exe... that contains all app need
it work also without installing python on a target computer_
* how to _make_ script for linux:
```
# do you have python full?
sudo apt install -y python3-full

# we must be in an environment
python3 -m venv myenv && source myenv/bin/activate

# pyinstaller need that library to "screenshot"
pip install questionary

# install PyInstaller
pip install pyinstaller

# make one executable file
pyinstaller --onefile tui.py

# the file (script) that we want is in:
dict/hello (Linux/Mac)
dict/hello.exe (windows)
```
* if you run into that error:
```
ERROR: On Linux, objdump is required. It is typically provided by the 'binutils' package installable via your Linux distribution's package manager.

```
* install binutils
```
sudo apt update
sudo apt install binutils
```

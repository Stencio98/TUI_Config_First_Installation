# Use PyInstaller to don't need an environment and libraries
_it makes a script or exe... that contains all app need
it work also without installing python on a target computer_
* how to _make_ script for linux:
```
# install PyInstaller
pip install pyinstaller

# make one executable file
pyinstaller --onefile hello.py

# the file (script) that we want is in:
dict/hello (Linux/Mac)
dict/hello.exe (windows)
```

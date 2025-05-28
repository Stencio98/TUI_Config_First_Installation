# (⚠️ Work in progress !stable ) Use PyInstaller to don't use an environment and libraries
_it makes a script or exe... that contains all app need
it work also without installing python on a target computer_
* how to _make_ script for linux:
```
# do you have python full?
sudo apt install -y python3-full

# we must be in an environment
python3 -m venv myenv 
source myenv/bin/activate

# pyinstaller need that library to "screenshot"
pip install questionary

# install PyInstaller
pip install pyinstaller

# make one executable file
pyinstaller --onefile tui.py
```

* the file (script) that we want is in:
```
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

# errors (needed analysis)
* fedora (**maybe** script must be done on fedora and run on it... if you make it on debian and run fedora could not work):
```
🔧 ⚙️  🛠️  0ad
flatpak: /tmp/_MEIQU7g02/libssl.so.3: version `OPENSSL_3.2.0' not found (required by /lib64/libcurl.so.4)

```

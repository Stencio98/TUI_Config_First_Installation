*You can use script made with Pyinstaller instead of following commands.. but this commands sequence maybe work better*
# TUI -- Debian / Ubuntu based
* make sure you are root user or in a root shell
* update your system if it is not (use `su` / `sudo su` before)
```
apt-get clean && apt-get update
apt-get dist-upgrade -y
apt-get full-upgrade -y
apt-get autoremove -y
```
* copy and paste following commands to prepare environment and run tool:
```
sudo apt install -y python3-full python3-venv python3-pip python3-dev build-essential &&

python3 -m venv myenv &&
source myenv/bin/activate &&

python3 -m pip install --upgrade pip &&

pip install questionary &&

python3 tui.py &&

deactivate &&

rm -rf myenv
```

# TUI -- Fedora
* make sure you are root user or in a root shell
* update your system if it is not (use `sudo su` before)
```
dnf clean all && dnf update -y
dnf upgrade --refresh -y
dnf autoremove -y
```
* copy and paste following commands to prepare environment and run tool:
```
sudo dnf install -y python3 python3-virtualenv python3-pip gcc python3-devel &&

python3 -m venv myenv &&
source myenv/bin/activate &&

python3 -m pip install --upgrade pip &&

pip install questionary &&

python3 tui.py &&

deactivate &&

rm -rf myenv
```

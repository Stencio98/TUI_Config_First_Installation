import questionary
import subprocess
import sys
import os
from questionary import Choice

# Add folder config to search path
current_dir = os.path.dirname(__file__)                  # current directory
config_dir = os.path.abspath(os.path.join(current_dir, '..', 'config'))  # absolute path ../config
sys.path.insert(0, config_dir)                           # insert 'config' at top of module research list

from packages import programs

choices = [Choice(prog, value=prog) for prog in programs.keys()]

print("\n")
print("\033[1m* apt packages -->\033[0m ⚪")
print("\033[1m* flatpak packages -->\033[0m 🔵")
print("\033[1m* snap packages --> \033[0m 🔴")
print("\033[5m* Make sure that snapd or flatpak are installed (first 3 rows) before select a snap or flatpak package\033[0m")
selected = questionary.checkbox(
    "",
    choices=choices
).ask()

if not selected:
    print("❌ No package selected")
else:
    for prog in selected:
        print(f"\n\t🔧 ⚙️  🛠️  {prog}")
        subprocess.run(programs[prog], shell=True)
        
    print("\n✅  Maybe you have to Restart Session.\n\n")


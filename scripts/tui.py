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

selected = questionary.checkbox(
    "\n\n\nSelect packages that will be installed:\n    apt packages --> ⚪\n    flatpak packages --> 🔵\n    snap packages --> 🔴\n\nBefore install snap or/and flatpak package\nmake sure that snapd or/and flatpak are installed ⚠️\n\n",
    choices=choices
).ask()

if not selected:
    print("❌ No package selected")
else:
    for prog in selected:
        print(f"\n\t...⚙️ {prog}...")
        subprocess.run(programs[prog], shell=True)

    print("\n✅  Installation Finished.")
    print("\n⚠️  Maybe you have to Restart Session.\n\n")


import questionary
import subprocess
import sys
import os
from questionary import Choice
import packages

from packages import programs

choices = [
    Choice(prog, value=prog) for prog in programs.keys()
]

selected = questionary.checkbox(
    "Make sure that snapd or flatpak are installed (first 3 rows) before select a snap or flatpak",
    choices=choices
).ask()

if not selected:
    print("❌ No package selected")
else:
    for prog in selected:
        print(f"\n\t🔧 ⚙️  🛠️  {prog}")
        subprocess.run(programs[prog], shell=True)
        
    print("\n✅  \033[5mMaybe you have to Restart Session.\033[0m\n\n")


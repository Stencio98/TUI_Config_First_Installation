import questionary
import subprocess
import sys
import os
from questionary import Choice
from questionary import Style

import packages

from packages import programs

choices = [
    Choice(prog, value=prog) for prog in programs.keys()
]


orange_heat = Style([
    ("qmark", "fg:#FFA500 bold"),
    ("question", "fg:#FF8C00 bold"),
    ("selected", "fg:#FFD700"),
    ("pointer", "fg:#FF4500 bold"),
    ("instruction", "fg:#FF6347"),
])


selected = questionary.checkbox(
    "Make sure that snapd or flatpak are installed (first 3 rows) before select a snap or flatpak",
    choices=choices,
    style=orange_heat
).ask()

if not selected:
    print("❌ No package selected")
else:
    for prog in selected:
        print(f"\n\t🔧 ⚙️  🛠️  {prog}")
        subprocess.run(programs[prog], shell=True)
        
    print("\n✅  \033[1mMaybe you have to Restart Session.\033[0m\n\n")


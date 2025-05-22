import questionary
import subprocess
import sys
import os
from questionary import Choice
from questionary import Separator
from questionary import Style

import packages

from packages import programs

#choices = [
#    Choice(prog, value=prog) for prog in programs.keys()
#]

choices = []
for category, progs in programs.items():
    choices.append(Separator(f"\n{category}"))
    for prog in progs.keys():
        choices.append(Choice(prog, value=prog))



orange_heat = Style([
    ("qmark", "fg:#FFA500 bold"),
    ("question", "fg:#FF8C00 bold"),
    ("selected", "fg:#FFD700"),
    ("pointer", "fg:#FF4500 bold"),
    ("instruction", "fg:#FF6347"),
])


selected = questionary.checkbox(
    "Make sure that snapd or flatpak are installed before select a snap or flatpak (first 2 rows)\n--> The flatpak and snapd installation command will also update apt\n",
    choices=choices,
    style=orange_heat
).ask()

if not selected:
    print("❌ No package selected")
else:
    for prog in selected:
    	found = False
    	for category, progs in programs.items():
    	    if prog in progs:
    	        print(f"\n\t🔧 ⚙️  🛠️  {prog}")
    	        subprocess.run(progs[prog], shell=True)
    	        found = True
    	        break
    	if not found:
    	    print(f"❌ Program {prog} not found!")

    print("\n✅  \033[1mMaybe you have to Restart Session.\033[0m\n\n")


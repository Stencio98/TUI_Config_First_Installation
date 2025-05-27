import questionary
import subprocess
import sys
import os
from questionary import Choice
from questionary import Separator
from questionary import Style
import importlib

orange_heat = Style([
    ("qmark", "fg:#FFA500 bold"),
    ("question", "fg:#FF8C00 bold"),
    ("selected", "fg:#FFD700"),
    ("pointer", "fg:#FF4500 bold"),
    ("instruction", "fg:#FF6347"),
])

package_managers = questionary.checkbox(
    "What packages do you can/want manage?",
    choices=[
        Choice("APT", value="apt"),
        Choice("Flatpak", value="flatpak"),
        Choice("DNF", value="dnf"),
    ],
    style=orange_heat
).ask()

if not package_managers:
    print("❌ No manager selected.")
    exit(0)


program_sources = {}

for manager in package_managers:
    try:
        module = importlib.import_module(f"{manager}_packages")
        program_sources[manager] = module.programs
    except ModuleNotFoundError:
        print(f"❌ module {manager}_packages nont found.")

choices = []
for manager, programs in program_sources.items():
    #choices.append(Separator(f"\n🎛️  {manager.upper()}"))
    for category, progs in programs.items():
        choices.append(Separator(f"\n{category}"))
        for prog in progs.keys():
            choices.append(Choice(f"{prog} ({manager})", value=(prog, manager)))

selected = questionary.checkbox(
    "Select programs that will be installed, or just update existing programs:",
    choices=choices,
    style=orange_heat
).ask()

if not selected:
    print("❌ No program selected.")
    exit(0)

for prog, manager in selected:
    programs = program_sources[manager]
    found = False
    for category, progs in programs.items():
        if prog in progs:
            print(f"\n\t🔧 ⚙️  🛠️  {prog} ({manager.upper()})")
            subprocess.run(progs[prog], shell=True)
            found = True
            break
    if not found:
        print(f"❌ Program {prog} not founded in module {manager}_packages.")

print("\n✅  \033[1mMaybe you have to restart session.\033[0m\n\n")


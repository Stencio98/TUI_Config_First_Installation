
import questionary
import subprocess
import sys
import os

# Add folder config to search path
current_dir = os.path.dirname(__file__)                  # current directory
config_dir = os.path.abspath(os.path.join(current_dir, '..', 'config'))  # absolute path ../config
sys.path.insert(0, config_dir)                           # insert 'config' at top of module research list


from packages import programs

selected = questionary.checkbox("Select packages that will be installed:",
    choices=list(programs.keys())
).ask()

if not selected:
    print("❌ No package selected")
else:
    for prog in selected:
        print(f"\n➡️ {prog}...")
        subprocess.run(programs[prog], shell=True)

    print("\n✅ Installation Finished.")

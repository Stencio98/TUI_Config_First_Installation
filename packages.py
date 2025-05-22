#apt-get clean && apt-get update && apt-get dist-upgrade -y && apt-get full-upgrade -y && apt-get autoremove -y &&
programs = {
	"🔄 📦 Installation flatpak and snap:": {
    	"install flatpak with flathub repo": "apt-get clean && apt-get update && apt-get dist-upgrade -y && apt-get full-upgrade -y && apt-get autoremove -y && sudo apt install -y flatpak && flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo",
    	"snapd and snap store gui": "apt-get clean && apt-get update && apt-get dist-upgrade -y && apt-get full-upgrade -y && apt-get autoremove -y && sudo apt install -y snapd && sudo snap install snapd && sudo snap install snap-store"
	},
	"🔄 update packages:": {
		"🔄 update apt -- update debian packages": "apt-get clean && apt-get update && apt-get dist-upgrade -y && apt-get full-upgrade -y && apt-get autoremove -y",
    	"🔄 update flatpak -- update flatpak packages ": "sudo flatpak update -y",
    	"🔄 update snap -- update snap packages:": "sudo snap refresh"
    },
    "📦 apt packages:": {
    	"gedit and gedit's plugins": "apt install -y gedit && apt install -y gedit-plugins",
    	"neofetch": "apt install -y neofetch",
    	"lm-sensors": "apt install -y lm-sensors",
    	"psensor (gui)": "apt install -y psensor",
    	"acpi (battery percentage laptop (terminal command))": "apt install -y acpi",
    	"openbox": "apt install -y openbox",
    	"tree": "apt install -y tree",
    	"fish": "apt install -y fish",
    	"flatpak-plugin-gnome": "sudo apt install -y gnome-software-plugin-flatpak",
    	"flatpak-plugin-KDE_Plasma": "sudo apt install -y plasma-discover-backend-flatpak",
    	"VirtualBox": " sudo apt install -y virtualbox && sudo apt install -y virtualbox-ext-pack",
		"KVM \"Kernel Virtual Machine\" Desktop use 💻": "sudo apt install -y qemu-system libvirt-daemon-system",
    	"KVM \"Kernel Virtual Machine\" Server use 💾": "sudo apt install -y --no-install-recommends qemu-system libvirt-clients libvirt-daemon-system"
	},    
	"📦 flatpak packages:": {
    	"discord": "flatpak install -y flathub com.discordapp.Discord",
    	"chromium": "flatpak install -y flathub org.chromium.Chromium",
    	"Intellij Community": "flatpak install -y com.jetbrains.IntelliJ-IDEA-Community",
    	"Android Studio": "flatpak install -y com.google.AndroidStudio",
    	"Visual Studio Code": "flatpak install -y com.visualstudio.code",
    	"Microsoft Teams": "flatpak install flathub com.github.IsmaelMartinez.teams_for_linux",
    	"spotify": "flatpak install -y flathub com.spotify.Client",
    	"steam": "flatpak install -y flathub com.valvesoftware.Steam",
    	"telegram": "flatpak install -y flathub org.telegram.desktop",
    	"0ad": "flatpak install -y com.play0ad.zeroad"
	}
}


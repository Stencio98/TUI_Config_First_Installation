#apt-get clean && apt-get update && apt-get dist-upgrade -y && apt-get full-upgrade -y && apt-get autoremove -y &&
programs = {
	"📦 flatpak packages:": {
		"🔄 update flatpak -- update flatpak packages ": "sudo flatpak update -y",
    	"discord": "flatpak install -y flathub com.discordapp.Discord",
    	"chromium": "flatpak install -y flathub org.chromium.Chromium",
    	"Intellij Community": "flatpak install -y com.jetbrains.IntelliJ-IDEA-Community",
    	"Android Studio": "flatpak install -y com.google.AndroidStudio",
    	"Visual Studio Code": "flatpak install -y com.visualstudio.code",
    	"Microsoft Teams": "flatpak install -y flathub com.github.IsmaelMartinez.teams_for_linux",
    	"spotify": "flatpak install -y flathub com.spotify.Client",
    	"steam": "flatpak install -y flathub com.valvesoftware.Steam",
    	"telegram": "flatpak install -y flathub org.telegram.desktop",
    	"0ad": "flatpak install -y com.play0ad.zeroad"
	}
}


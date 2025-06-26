#include <stdio.h>
#include <stdlib.h>

int esegui_comando(const char *comando) {
    int status = system(comando);
    if (status == -1) {
        perror("Errore nell'esecuzione del comando");
        return 1;
    }
    return 0;
}

int main() {
    printf("Aggiornamento della lista dei pacchetti...\n");
    if (esegui_comando("sudo apt-get update") != 0) return 1;

    printf("Aggiornamento dei pacchetti installati...\n");
    if (esegui_comando("sudo apt-get upgrade -y") != 0) return 1;

    printf("Rimozione dei pacchetti non necessari...\n");
    if (esegui_comando("sudo apt-get autoremove -y") != 0) return 1;

    printf("Pulizia dei pacchetti obsoleti...\n");
    if (esegui_comando("sudo apt-get autoclean -y") != 0) return 1;

    printf("Per fare l'avanzamento di versione occorre eseguire:\nsudo do-release-upgrade\n");

    printf("Aggiornamento completato.\n");
    return 0;
}


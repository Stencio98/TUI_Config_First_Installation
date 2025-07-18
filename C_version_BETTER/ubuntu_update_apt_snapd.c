#include <stdio.h>
#include <stdlib.h>
#define INSTALLATION

int exec_command(const char *command) {
    int status = system(command);
    if (status == -1) {
        perror("\033[1merror exec_command:\033[0m\n");
        fprintf(stdout, "%s", command);
        return 1;
    }
    return 0;
}

int main() {
    printf("\033[1mUpdating package list...\033[0m\n");
    if (exec_command("sudo apt-get update") != 0) return 1;

    printf("\033[1mUpdating installed packages...\033[0m\n");
    if (exec_command("sudo apt-get upgrade -y") != 0) return 1;

    printf("\033[1mRemoving unused packages...\033[0m\n");
    if (exec_command("sudo apt-get autoremove -y") != 0) return 1;

    printf("\033[1mCleaning old packages...\033[0m\n");
    if (exec_command("sudo apt-get autoclean -y") != 0) return 1;

    printf("\033[1mto upgrade version of operative system (for example from ubuntu 22 to ubuntu 24):\nsudo do-release-upgrade\033[0m\n");

    printf("\033[1mUpdating snap packages...\033[0m\n");
    if (exec_command("sudo snap refresh") != 0) return 1;
    printf("\033[1mUpdate completed.\033[0m\n");    
    
    printf("\033[1mDo you want to check/install driver nvidia? \npress y to continue\033[0m\n");
    
    char ch;
    ch = getchar();
    if (ch == 'y' || ch == 'Y') {} else {return 0;}
    
    if (exec_command("ubuntu-drivers devices") != 0) return 1;
    
    if (exec_command("sudo ubuntu-drivers autoinstall") != 0) return 1;
    
    printf("\033[1mConsider to reboot system\033[0m\n");
    
}


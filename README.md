# toshiba_encore2

Aqui subire informacion y archivos utiles para la tablet toshiba encore 2 wt8-b32cn aunque puede funcionar para la dos versiones  (WT8-B/WT10-A)

IMPORTANTE
El sistema de la tablet es BIOS EFI 32B con procesador de 64B asi que todo sistema operativo que quieras probar debe tener BOOT EFI de 32B, puedes saltar este problema usando "VENTOY" el cual permite iniciar cualquier sistema operativo en formato "ISO" o imagen boot.

INSTALAR ANDROID
para instalar android se debe usar la version https://androidfilehost.com/?fid=10763459528675589621

INSTALAR LINUXMINT
debes primero instalar la version android(para que cree la particion EFI al inicio), despues reparticionar el disco y crear una nueva particion con 20GB donde estara linuxmint, asi puedes tener doble boot o tambien puedes usar todo para linuxmint, solo debes evitar eliminar la particion EFI que es de 32 bits la cual debes modificar para lograr entrar a linuxmint(en mis archivos esta la configuracion de GRUB2 que uso para doble boot android+linuxmint)

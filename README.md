# toshiba_encore2

Aqui subire informacion y archivos utiles para la tablet toshiba encore 2 wt8-b32cn aunque puede funcionar para la dos versiones  (WT8-B/WT10-A)

IMPORTANTE
El sistema de la tablet es BIOS EFI 32B con procesador de 64B asi que todo sistema operativo que quieras probar debe tener BOOT EFI de 32B, puedes saltar este problema usando "VENTOY" el cual permite iniciar cualquier sistema operativo en formato "ISO" o imagen boot.

RECOMENDACIONES
- Usar linuxmint-20.3-cinnamon-64bit
- Usar teclado onboard, el mejor y permite dar segundo click.
- Usar Cinnamon o LXQt  como interfaz grafica.
- Instalar kernel 5.8.0.63-generic para mas velocidad y que funcione el brillo y mas cosas que antes no funcionaba con el kernel que trae linuxmint, recuerda que debes cambiar el archivo /BOOT/EFI/EFI/BOOT/ANDROID.cfg para que use el nuevo kernel.
- No usar gnome ya que es dificil por el tamaño de todo, usar Cinnamon o LXQt.
- Usar los script de rotacion o el de rotacion automatica que estan aqui publicados, tambien puedes usar la aplicacion tencore2 escrita por mi en python con ella puedes rotar panalla o cambiar brillo en una interfaz grafica.
- Se puede instalar metasploit y ettercap con wireshark, aun no hay modo monitor en wifi por la targeta que no lo soporta.
- Si tu tablet toshiba encore 2 no tiene sonido, instala un firmware de bios bajo ya que los ultimos dan problemas, realiza un downgrade.
- Si dañas algo del grub2 entra con linuxmint version live para repararlo, aqui dejo un grub configurado por mi dualboot (android linux)
- Tanto android 8.1 como linuxmint 20.3 cinnamon 64bits funcionan perfectos.
- Desabilitar el xscrensaver ya que pide contraseña aveces y no tiene teclado virtual.
- Desabilitar el apagado al presionar el boton de power y cambiarlo a suspender.

INSTALAR ANDROID
para instalar android se debe usar la version https://androidfilehost.com/?fid=10763459528675589621
ocupa todo el disco en la instalacion el creara las particiones EFI y la de android despues redimensionar para dejarle 20GB al linux al final del disco.

INSTALAR LINUXMINT
debes primero instalar la version android(para que cree la particion EFI al inicio), despues entra en el live de linux mint reparticionar el disco y crear una nueva particion con 20GB donde estara linuxmint, asi puedes tener doble boot o tambien puedes usar todo para linuxmint, solo debes evitar eliminar la particion EFI que es de 32 bits la cual debes modificar para lograr entrar a linuxmint(en mis archivos esta la configuracion de GRUB2 que uso para doble boot android+linuxmint)
IMPORTANTE: una vez culminada la instalacion saldra errer del grub debes modificar el archivo manualmente que se encuentra un la particion EFI mantala y modifica el archivo /BOOT/EFI/EFI/BOOT/ANDROID.cfg aqui hay una guia de como configure la entrada de linuxmint debes cambiar el UUID y colocar el de la particion donde esta linuxmint, ademas de cambiar el kernel y el initrd al que al que esta en /BOOT/ la version que viene cuando instalas es 5.4.0-63 recuerda que si actualisas el kernel debes modificar manualmente el archivo de nuevo.

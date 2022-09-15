# toshiba_encore2

Aqui subire informacion y archivos utiles para la tablet toshiba encore 2 wt8-b32cn aunque puede funcionar para la dos versiones  (WT8-B/WT10-A)

IMPORTANTE
El sistema de la tablet es BIOS EFI 32B con procesador de 64B asi que todo sistema operativo que quieras probar debe tener BOOT EFI de 32B, puedes saltar este problema usando "VENTOY" el cual permite iniciar cualquier sistema operativo en formato "ISO" o imagen boot.

RECOMENDACIONES
- Usar teclado onboard, el mejor y permite dar segundo click.
- Usar LXQt como interfaz grafica.
- Instalar kernel 5.15.0.46-generic para mas velocidad y que funcione el brillo y mas cosas que antes no funcionaba con el kernel que trae linuxmint.
- No usar gnome ni cinnamon ya que es dificil por el tamaño de todo, usar LXQt.
- Usar los script de rotacion o el de rotacion automatica que estan aqui publicados.
- Se puede instalar metasploit y ettercap con wireshark, aun no hay modo monitor en wifi.
- Si tu tablet toshiba encore 2 no tiene sonido, instala un firmware bajo ya que los ultimos dan problemas, realiza un downgrade.
- Si dañas algo del grub2 entra con linuxmint verdion live para repararlo.
- Tanto android 8.1 como linuxmint 20.3 cinnamon 64bits funcionan perfectos.
- Desabilitar el xscrensaver ya que pide contraseña aveces y no tiene teclado virtual.
- Desabilitar el apagado al presionar el boton de power y cambiarlo a suspender.l           

INSTALAR ANDROID
para instalar android se debe usar la version https://androidfilehost.com/?fid=10763459528675589621

INSTALAR LINUXMINT
debes primero instalar la version android(para que cree la particion EFI al inicio), despues reparticionar el disco y crear una nueva particion con 20GB donde estara linuxmint, asi puedes tener doble boot o tambien puedes usar todo para linuxmint, solo debes evitar eliminar la particion EFI que es de 32 bits la cual debes modificar para lograr entrar a linuxmint(en mis archivos esta la configuracion de GRUB2 que uso para doble boot android+linuxmint)

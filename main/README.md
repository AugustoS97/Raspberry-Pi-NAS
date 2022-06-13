# OLED STATISTIC

Servicio del sistema que lanza un script en python para mostar en un display OLED LCD los siguientes datos:
- Direccion IP
- Ocupacion del disco principal
- Consumo de RAM
- Temperatura
- Ocupacion del disco externo (en caso de emplearse como NAS).

## Requerimientos para el uso del Display OLED I2C

- Python3:
	sudo apt-get install python3-pip
	sudo pip3 install --upgrade setuptools
- Raspi blinka:
	wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
	sudo python3 raspi-blinka.py
- Adafruit python shell:
	sudo pip3 install --upgrade adafruit-python-shell
- Adafruit SSD1306: 
	pip3 install adafruit-circuitpython-ssd1306
- Python PIL:
	sudo apt-get install python3-pil

## Requerimientos para el compilado

Para la compilación del paquete .deb requiere:

  - dh-make
  - debmake
  - debhelper
  - devscripts
  - dpkg-dev
  - make
  - python3
  - build-essential
  - sudo apt-get install debhelper dh-virtualenv

## Empaquetado

Para hacer el paquete con el servicio del sistema, se debe ejecutar:

    $ debuild -us -uc

Se debe estar en la carpeta 'oled-statistic'.

Mas información [aquí](https://blog.packagecloud.io/eng/2016/12/15/howto-build-debian-package-containing-simple-shell-scripts/ "Documentación dh-make").

## Localización de la instalación

Una vez instalado el .deb se genera un directorio en /usr/share llamado 'oled-statistic'
que contiene 'src' donde se aloja el script.
Los ficheros del servicio de superusuario se alojan en '/lib/systemd/system'

    $ sudo dpkg -i oled-statistic_1.0_all.deb

## Desinstalación

Para proceder a desinstalar el paquete, debe ejecutarse:

    $ sudo dpkg -r oled-statistic

Se eliminan todos los ficheros.

## Revisión del estado del timer y el servicio

    $ systemctl status oled-statistic.service
    $ systemctl status oled-statistic.timer
    $ systemctl start oled-statistic.service
    $ systemctl stop oled-statistic.service
    $ systemctl daemon-reload

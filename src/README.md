# Raspberry Pi NAS Software

## Instalar Open Media Vault
    $ sudo wget -O - https://github.com/OpenMediaVault-Plugin-Developers/installScript/raw/master/install | sudo bash $

## OLED STATISTIC
Servicio del sistema que lanza un script en python para mostar en un display OLED LCD los siguientes datos:
- Direccion IP
- Ocupacion del disco principal
- Consumo de RAM
- Temperatura
- Ocupacion del disco externo (en caso de emplearse como NAS).

## Requerimientos para el uso del Display OLED I2C

- Python3:
  
    $ sudo apt-get install python3-pip

	$ sudo pip3 install --upgrade setuptools

- Raspi blinka:
  
	$ wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py

	$ sudo python3 raspi-blinka.py

- Adafruit python shell:
  
	$ sudo pip3 install --upgrade adafruit-python-shell

- Adafruit SSD1306: 
  
	$ pip3 install adafruit-circuitpython-ssd1306

- Python PIL:
  
	$ sudo apt-get install python3-pil


## Carpeta con el contenido a copiar dentro de /home/pi
- Debe copiarse la carpeta shutdwon-monitor para permitir apagar meidante el boton conectado al GPIO-17 (pin BCM número 11).
- Debe copiarse la carpeta oled-statistic para ejecutar el script que muestra de forma continua la info en pantalla.

## Configuracion con Cron
- Abrir el configurador de cron con $ crontab -e $
- Escribir la configuracion con encendido retardado y volcado a un fichero de log: 


    $ @reboot sleep 2; /usr/bin/python3 /home/pi/oled-statistic/oled-statistic.py >> /home/pi/oled-statistic/oled-statistic.log

    $ @reboot sleep 10; /usr/bin/python3 /home/pi/shutdown-monitor/shutdown-monitor.py >> /home/pi/shutdown-monitor/shutdown-monitor.log
- Asegurarse de dar permiso de ejecucion a ambos scripts con 
    $ chmod 777 nombre.py

## Pines ocupados 
- Ventilador: GPIO 12 (PWM 3.3V). Se configura en el /boot/config.txt como 
  
    $ dtoverlay=gpio-fan,gpiopin=12,temp=60000
- LED Amarillo (Estatus LED): GPIO26. Se configura en el /boot/config.txt como 
  
    $ dtparam=act_led_gpio=26
- LED Rojo (Encendido LED): GPIO19
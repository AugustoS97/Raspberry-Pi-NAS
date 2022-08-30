# Raspberry Pi NAS Software

NAS (Network Attached Storage) basado en Rapsberry Pi con Open Media Vault impreso en 3D con HDD de 3,5" de Toshiba alimentado a 12V.
Este diseño pretende reaprovechar los Discos Duros Externos de 3,5" USB para ser usados como NAS en una carcasa que integra todo lo necesario.
Incorpora LEDs indicador de estado (LED verde) y de encendido (LED rojo), así como OLED para identificar la dirección IP, el espacio libre y los datos de consumo de RAM y CPU.

![NAS_exterior](/Photos/NAS_exterior.jpg)

![NAS exterior 2](/Photos/NAS_exterior_1.jpg)

![NAS frontal](/Photos/NAS_frente.jpg)

## Lista de Materiales (BOM)

Para montar este sistema se precisa de lo siguiente:

### Elementos mecánicos

- 4 tornillos M3x15
- 12 tuercas M3.
- 10 tornillos M3x6 (para interior)
- 4 tornillos M2.5x6 (para RPi)
- 8 tornillos M3x10
- 2 tornillos M4x15
- 2 insertos M4
- Piezas impresas en PLA. Puedes localizarse en la carpeta 3D Model o en [Thingiverse](https://www.thingiverse.com/thing:5462342)
- Metacrilato de 3mm cortado para "cristal" de OLED.

### Electrónica

- Raspberry 3B+.
- Ventilador para Rapsberry Pi.
- Disco Duro 3,5" Toshiba o similar con placa de alimentación a 12V
- 2 Interruptores 8x15mm
- LED rojo
- LED amarillo
- 2 Resistencias 220 Ohm
- Regulador DC/DC StepDown MP2307 o LM2596
- Fusible 2A (Opcional para proteger alimentación de Raspberry)
- Placa para control del ventilador [PWM](https://github.com/AugustoS97/RPi-accessories/tree/main/PWM-TRANSISTOR-PCB) de diseño propio (opcional). En caso de querer controlar mediante PWM es necesario un transistor 2N2222, un diodo 1N4007 y una Resistencia de 1KOhm.
- Puede sustituirse la integración de los LEDs de estado, el fusible, el DC/DC y la placa para control PWM, empleando una [placa de expansión para RPi de diseño propio](https://github.com/AugustoS97/RPi-accessories/tree/main/LED-RPi-PCB).

### Esquema para el control PWM del ventilador

![Esquema de control PWM](/Photos/Esquema%20PWM%20control.png)

### Esquema para la Placa de expansión para RPi

![Esquema placa RPi](/Photos/Esquema%20PCB%20main%20NAS.png)

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

from machine import Pin,ADC, I2C
from utime   import sleep_ms
import time
from ssd1306 import SSD1306_I2C
import framebuf
import button
import fb
import servi

ejey=ADC(Pin(4))
ejex=ADC(Pin(2))
ejey.atten(ADC.ATTN_11DB)   # para calibrar de 0 a 3.3v
ejey.width(ADC.WIDTH_12BIT) # establecer resolución
ejex.atten(ADC.ATTN_11DB)   # para calibrar de 0 a 3.3v
ejex.width(ADC.WIDTH_12BIT) # establecer resolución
boton=Pin(18,Pin.IN, Pin.PULL_UP)
#led=Pin(2,Pin.OUT)

ancho = 128
alto = 64
i2c = I2C(0, scl=Pin(22), sda=Pin(23))
oled = SSD1306_I2C(ancho, alto, i2c)

m_lis = ['sum.pbm', 'res.pbm','mul.pbm', 'div.pbm']
cont = 0
se = 1

while True:
  cont = int(cont)
  x=ejex.read()
  y=ejey.read()
  #print (f"valor en el eje y: {ejey.read()}")
  #print (f"valor en el eje x: {ejex.read()}")
  #led.value(boton.value())
  if x==0:
    # print ("derecha")
    cont += 1
  elif x==4095:
    # print ("izquierda")
    cont -= 1
  elif y == 4095:
      print("press")
      se = 0
  if cont < 0:
      cont = 3
  elif cont > 3:
      cont = 0
  if se == 1:
      oled.blit(fb.op_da(m_lis[cont]),0,0)
      oled.show()
      sleep_ms(100)
      oled.fill(0)
  elif se == 0 :
      cont = str(cont)
      print(cont)
      print("entrada al menu")
      oled.fill(0)
      oled.text(servi.seleccion(cont), 0, 16)
      oled.text("return in 10 second(s)", 0, 56)
      oled.show()
      time.sleep(10)
      se = 1
      

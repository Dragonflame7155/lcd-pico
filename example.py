import lcd
from utime import sleep

while True:
    lcd.clear()
    lcd.write('Lcd pico demo')
    sleep(2)
    lcd.clear()
    lcd.write('Made by')
    sleep(1)
    lcd.clear()
    lcd.write('Dragonflame7155')
    sleep(2)
    lcd.clear()
    lcd.write("azAZ09=.?([{}])")
    sleep(2)
    lcd.clear()
    lcd.write("dispchar()")
    sleep(2)
    lcd.clear()
    lcd.dispchar(lcd.htg)
    lcd.dispchar(lcd.dlr)
    lcd.dispchar(lcd.prc)
    lcd.dispchar(lcd.aps)
    lcd.dispchar(lcd.fsh)
    lcd.dispchar(lcd.bsh)
    sleep(2)

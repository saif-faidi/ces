from sender import  Sender
from color import ColorEFI , ColorStrip
from conf import lumi_socket
from network.udp_client import Client
import time

'''
led_strip id 1 => gpio 18,
led_strip id 2 => gpio 19
'''

def setcolors(colors: list):
    for color in colors :
        sender.send(color)
        time.sleep(1)


if __name__ == "__main__":

    client = Client(*lumi_socket)
    sender = Sender(client)

    ####################################### test EFI colors  #####################################
    color1 = ColorEFI(1,255,0,0,255)
    color2 = ColorEFI(2, 0, 255, 0, 255)
    color3 = ColorEFI(3, 0, 0, 255, 255)
    color4 = ColorEFI(4, 255, 10, 60, 255)
    colors = [color1, color2, color3, color4]
    setcolors(colors)

    time.sleep(1)

    color1 = ColorEFI(1,0,0,0,0)
    color2 = ColorEFI(2, 0, 0, 0, 0)
    color3 = ColorEFI(3, 0, 0, 0, 0)
    color4 = ColorEFI(4, 0, 0, 0, 0)
    colors = [color1, color2, color3, color4]
    setcolors(colors)

    ####################################### test Strip colors  #####################################
    c1 = ColorStrip(2,255,0,0,100)  #pwm0
    c2 = ColorStrip(1, 255, 0, 0, 100) #pwm1


    colors = [c1,c2]
    setcolors(colors)
    time.sleep(2)

    c1 = ColorStrip(2,0,0,0,0)  #pwm0
    c2 = ColorStrip(1, 0, 0, 0, 0) #pwm1

    colors = [c1, c2]
    setcolors(colors)
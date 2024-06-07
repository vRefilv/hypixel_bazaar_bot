#proces
#idzie kupić 256 melon/ 228 gold
#przerabia w craftingu złoto na nugget
#daje nuggety dookoła melona
#powstaje glistering melon
#potem daje po 32 glistering melony dookoła
#powstaje enchanted glistering melon
#idzie go sprzedać


#imports
from time import sleep
from locate import *
import keyboard,mouse

#variables
crafting='bin/crafting.png'
farming='bin/farming.png'
farming_selected='bin/farming_selected.png'
mining='bin/mining.png'
mining_selected='bin/mining_selected.png'
gold='bin/gold.png'
gold2='bin/gold2.png'
gold64='bin/gold64.png'
melon='bin/melon.png'
melon2='bin/melon2.png'
melon64='bin/melon64.png'
glistering='bin/glistering.png'
glistering64='bin/glistering64.png'
nugget='bin/nugget.png'
nuggetcraft='bin/nuggetcraft.png'
buyinstant='bin/buyinstant.png'
custom='bin/custom.png'
done='bin/done.png'
final='bin/final.png'
sell1='bin/sell.png'
sell2='bin/sell2.png'
ttw=0.5  #time to wait before actions #0.4 #0.3

#functions
def open_bazaar():
    keyboard.press_and_release('1')
    mouse.click()

def buy_melons():
    clickonimage(melon)
    sleep(ttw)
    clickonimage(melon2)
    sleep(ttw)
    clickonimage(buyinstant)
    sleep(ttw)
    clickonimage(custom)
    sleep(ttw)
    keyboard.write('256')
    sleep(ttw)
    clickonimage(done)
    sleep(ttw)
    clickonimage(melon2)
    sleep(ttw)
    keyboard.press_and_release('esc')

def buy_gold():
    clickonimage(mining)
    sleep(ttw)
    clickonimage(gold)
    sleep(ttw)
    clickonimage(gold2)
    sleep(ttw)
    clickonimage(buyinstant)
    sleep(ttw)
    clickonimage(custom)
    sleep(ttw)
    keyboard.write('228')
    sleep(ttw)
    clickonimage(done)
    sleep(ttw)
    clickonimage(gold2)
    sleep(ttw)
    keyboard.press_and_release('esc')

def open_crafting():
    mouse.move(300, 0, absolute=False)
    keyboard.press_and_release('9')
    sleep(ttw)
    mouse.click()
    sleep(ttw)
    clickonimage(crafting)

def craft():
    locatecraft(gold64,click_multiple=True,holdshift=True,max_clicks=3,craft=True,craftimg=nuggetcraft)
    for i in range(0,2):
        locatecraft(nugget,click_multiple=True,holdshift=True,max_clicks=4)
        locatecraft(melon64,click_once=True,holdshift=True,craft=False)
        locatecraft(nugget,click_multiple=True,holdshift=True,max_clicks=4,craft=True,craftimg=glistering)
    locatecraft(gold64,click_once=True,holdshift=True,craft=True,craftimg=nuggetcraft)
    for i in range(0,2):
        locatecraft(nugget,click_multiple=True,holdshift=True,max_clicks=4)
        locatecraft(melon64,click_once=True,holdshift=True,craft=False)
        locatecraft(nugget,click_multiple=True,holdshift=True,max_clicks=4,craft=True,craftimg=glistering)
    locatecraft(glistering64,click_multiple=True,holdshift=True,max_clicks=4,craft=False)
    locatesplit(glistering64,max_clicks=4)
    craftingoutput(final,middlemove=True)
    keyboard.press_and_release('esc')

def sell():
    sleep(ttw)
    mouse.move(-300, 0, absolute=False)
    sleep(ttw)
    keyboard.press_and_release('1')
    sleep(ttw)
    mouse.click()
    sleep(ttw)
    clickonimage(farming)
    sleep(ttw)
    clickonimage(sell1)
    sleep(ttw)
    clickonimage(sell2)
    sleep(ttw)
    keyboard.press_and_release('esc')

# Main execution function
def main():
    while True:
            print("Starting process...")
            open_bazaar()
            sleep(ttw)
            buy_melons()
            sleep(ttw)
            open_bazaar()
            sleep(ttw)
            buy_gold()
            sleep(ttw)
            open_crafting()
            craft()
            sell()
            sleep(1)

sleep(5)
main()
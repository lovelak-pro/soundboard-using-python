from keyboard import add_hotkey
from keyboard import wait
from pygame import mixer
from sounds import *
import webbrowser as wb
import os



mixer.init()

os.system('cls')
print('\nHello There!')
print('\nYour Soundboard is Ready to use.')



def aaaaa():
    mixer.music.load(aaaaa_path)
    mixer.music.play()
def anime_ahh():
    mixer.music.load(anime_ahh_path)
    mixer.music.play()
def anime_wow():
    mixer.music.load(anime_wow_path)
    mixer.music.play()
def ara_ara():
    mixer.music.load(ara_ara_path)
    mixer.music.play()
def emotional_damage():
    mixer.music.load(emotional_damage_path)
    mixer.music.play()
def ew_brother_ew():
    mixer.music.load(ew_brother_ew_path)
    mixer.music.play()
def yes_omg_remix():
    mixer.music.load(yes_omg_remix_path)
    mixer.music.play()
def yes_mommy():
    mixer.music.load(yes_mommy_path)
    mixer.music.play()
def yes_daddy():
    mixer.music.load(yes_daddy_path)
    mixer.music.play()
def yesyes_nono():
    mixer.music.load(yesyes_nono_path)
    mixer.music.play()
def yamate_kudasai():
    mixer.music.load(yamate_kudasai_path)
    mixer.music.play()
def weeeee():
    mixer.music.load(weeeee_path)
    mixer.music.play()
def noob_():
    mixer.music.load(noob_path)
    mixer.music.play()
def byebye():
    mixer.music.load(byebye_path)
    mixer.music.play()
def the_rizz():
    mixer.music.load(the_rizz_path)
    mixer.music.play()
def hub_into():
    mixer.music.load(hub_intro_path)
    mixer.music.play()
def im_sponge_bob():
    mixer.music.load(im_sponge_bob_path)
    mixer.music.play()
def limit_on_talking():
    mixer.music.load(limit_on_talking_path)
    mixer.music.play()
def sorry_indian():
    mixer.music.load(sorry_indian_path)
    mixer.music.play()
def spiderman_meme():
    mixer.music.load(spiderman_meme_path)
    mixer.music.play()


add_hotkey('1',aaaaa)
add_hotkey('2',anime_ahh)
add_hotkey('3',anime_wow)
add_hotkey('4',ara_ara)
add_hotkey('5',emotional_damage)
add_hotkey('6',ew_brother_ew)
add_hotkey('7',yes_omg_remix)
add_hotkey('8',yes_mommy)
add_hotkey('9',yes_daddy)
add_hotkey('1+2',yesyes_nono)
add_hotkey('2+3',yamate_kudasai)
add_hotkey('4+5',weeeee)
add_hotkey('5+6',noob_)
add_hotkey('7+8',byebye)
add_hotkey('8+9',the_rizz)
add_hotkey('/',hub_into)
add_hotkey('*',im_sponge_bob)
add_hotkey('/+*',limit_on_talking)
add_hotkey('enter',sorry_indian)
add_hotkey('.',spiderman_meme)



def help_sound():
    wb.open('help.html')
add_hotkey('h+e+l+p',help_sound)












while 1:
    wait()
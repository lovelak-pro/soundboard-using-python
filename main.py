from keyboard import add_hotkey
from keyboard import wait
from tkinter import *
from pygame import mixer
import webbrowser as wb

root = Tk()
root.title('Soundboard using python')
mixer.init()

root.resizable(0,0)
def disable_event():
   pass
root.protocol("WM_DELETE_WINDOW", disable_event)


fbi_path = 'sfx\\fbi-open-up-sfx.mp3'
anime_ahh_path = 'sfx\\anime-ahh.mp3'
anime_wow_path = 'sfx\\anime-wow-sound-effect.mp3'
ara_ara_path = 'sfx\\ara-ara.mp3'
emotional_damage_path = 'sfx\\emotional-damage-meme.mp3'
ew_brother_ew_path = 'sfx\\eww-brother-eww.mp3'
yes_omg_remix_path = 'sfx\\yes-omg-remix.mp3'
yes_mommy_path = 'sfx\\yes-mommy.mp3'
yes_daddy_path = 'sfx\\yes-daddy.mp3'
yesyes_nono_path = 'sfx\\yes-yes-yes-yes-no-no-no-no.mp3'
yamate_kudasai_path = 'sfx\\yamate-kudasai.mp3'
weeeee_path = 'sfx\\weeeee_original_1193597514938524841.mp3'
noob_path = 'sfx\\noob sound.mp3'
byebye_path = 'sfx\\byebye-indian.mp3'
the_rizz_path = 'sfx\\the-weekend-rizz-extended.mp3'
hub_intro_path = 'sfx\\hub-intro-sound.mp3'
im_sponge_bob_path = 'sfx\\im-spongebob.mp3'
limit_on_talking_path = 'sfx\\limit-on-talking.mp3'
sorry_indian_path = 'sfx\\sorry-indian.mp3'
spiderman_meme_path = 'sfx\\spiderman-meme-song.mp3'
dog_laughing_path = 'sfx\\laughing-dog-meme.mp3'
sad_violin_path = 'sfx\\worlds-smallest-violin.mp3'
what_the_dog_doin_path = 'sfx\\what-the-dog-doin.mp3'
snore_mimimi_path = 'sfx\\snore-mimimimimimi.mp3'
meme_ending_path = 'sfx\\meme-de-creditos-finales.mp3'
run_meme_path = 'sfx\\run-vine-sound-effect.mp3'
gay_echo_path = 'sfx\\gay-echo.mp3'
thankyou_anime_path = 'sfx\\thankyou_anime.mp3'
thankyou_myfriend_path = 'sfx\\thank_you_my_friend.mp3'


def exit():
    quit()

def fbi():
    mixer.music.load(fbi_path)
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
def dog_laughing():
    mixer.music.load(dog_laughing_path)
    mixer.music.play()
def sad_violin():
    mixer.music.load(sad_violin_path)
    mixer.music.play()
def what_the_dog_doin():
    mixer.music.load(what_the_dog_doin_path)
    mixer.music.play()
def snore_mimimi():
    mixer.music.load(snore_mimimi_path)
    mixer.music.play()
def meme_ending():
    mixer.music.load(meme_ending_path)
    mixer.music.play()
def run_meme():
    mixer.music.load(run_meme_path)
    mixer.music.play()
def gay_echo():
    mixer.music.load(gay_echo_path)
    mixer.music.play()
def thankyou_anime():
    mixer.music.load(thankyou_anime_path)
    mixer.music.play()
def thankyou_myfriend():
    mixer.music.load(thankyou_myfriend_path)
    mixer.music.play()


btn1 = Button(root,text='1\nFBI Open UP',width=15,height=7,font=5,command=lambda:fbi())
btn2 = Button(root,text='2\nAnime Ahh',width=15,height=7,font=5,command=lambda:anime_ahh())
btn3 = Button(root,text='3\nAnime WOW',width=15,height=7,font=5,command=lambda:anime_wow())
btn4 = Button(root,text='4\nAra Ara',width=15,height=7,font=5,command=lambda:ara_ara())
btn5 = Button(root,text='5\nEmotional Damage',width=15,height=7,font=5,command=lambda:emotional_damage())
btn6 = Button(root,text='6\nEw Brother Ew',width=15,height=7,font=5,command=lambda:ew_brother_ew())
btn7 = Button(root,text='7\nYes OMG Remix',width=15,height=7,font=5,command=lambda:yes_omg_remix())
btn8 = Button(root,text='8\nYes Mommy',width=15,height=7,font=5,command=lambda:yes_mommy())
btn9 = Button(root,text='9\nYes Daddy',width=15,height=7,font=5,command=lambda:yes_daddy())
btn10 = Button(root,text='0\nThank you Anime',width=15,height=7,font=5,command=lambda:thankyou_anime())
btn11 = Button(root,text='1+2\nYes Yes No No KSI',width=15,height=7,font=5,command=lambda:yesyes_nono())
btn12 = Button(root,text='2+3\nYamate Kudasai',width=15,height=7,font=5,command=lambda:yamate_kudasai())
btn13 = Button(root,text='4+5\nWee Wee Wee',width=15,height=7,font=5,command=lambda:weeeee())
btn14 = Button(root,text='5+6\nnoob_',width=15,height=7,font=5,command=lambda:noob_())
btn15 = Button(root,text='7+8\nTa Ta Bye Bye',width=15,height=7,font=5,command=lambda:byebye())
btn16 = Button(root,text='8+9\nThe Rizz Sound',width=15,height=7,font=5,command=lambda:the_rizz())
btn17 = Button(root,text='1+4\nDog Laughing',width=15,height=7,font=5,command=lambda:dog_laughing())
btn18 = Button(root,text='2+5\nSad Violin',width=15,height=7,font=5,command=lambda:sad_violin())
btn19 = Button(root,text='3+6\nWhat The Dog Doin',width=15,height=7,font=5,command=lambda:what_the_dog_doin())
btn20 = Button(root,text='4+7\nSnore Mimimi',width=15,height=7,font=5,command=lambda:snore_mimimi())
btn21 = Button(root,text='5+8\nMeme Ending',width=15,height=7,font=5,command=lambda:meme_ending())
btn22 = Button(root,text='6+9\nThank you my friend',width=15,height=7,font=5,command=lambda:thankyou_myfriend())
btn23 = Button(root,text='/\nHub Intro',width=15,height=7,font=5,command=lambda:hub_into())
btn24 = Button(root,text='*\nIm Sponge Bob',width=15,height=7,font=5,command=lambda:im_sponge_bob())
btn25 = Button(root,text='/+*\nLimit On Talking',width=15,height=7,font=5,command=lambda:limit_on_talking())
btn26 = Button(root,text='Enter\nSorry Indian',width=15,height=7,font=5,command=lambda:sorry_indian())
btn27 = Button(root,text='.\nSpiderman Meme',width=15,height=7,font=5,command=lambda:spiderman_meme())
btn28 = Button(root,text='-\nRun Meme',width=15,height=7,font=5,command=lambda:run_meme())
btn29 = Button(root,text='-+*\nGay Echo',width=15,height=7,font=5,command=lambda:gay_echo())


quitbtn = Button(root,text='Quit Soundboard',width=47,height=7,font=15,command=lambda:exit())





btn1.grid(column=0,row=0)
btn2.grid(column=1,row=0)
btn3.grid(column=2,row=0)
btn4.grid(column=3,row=0)
btn5.grid(column=4,row=0)
btn6.grid(column=5,row=0)
btn7.grid(column=6,row=0)
btn8.grid(column=7,row=0)

btn9.grid(column=0,row=1)
btn10.grid(column=1,row=1)
btn11.grid(column=2,row=1)
btn12.grid(column=3,row=1)
btn13.grid(column=4,row=1)
btn14.grid(column=5,row=1)
btn15.grid(column=6,row=1)
btn16.grid(column=7,row=1)

btn17.grid(column=0,row=2)
btn18.grid(column=1,row=2)
btn19.grid(column=2,row=2)
btn20.grid(column=3,row=2)
btn21.grid(column=4,row=2)
btn22.grid(column=5,row=2)
btn23.grid(column=6,row=2)
btn24.grid(column=7,row=2)

btn25.grid(column=0,row=3)
btn26.grid(column=1,row=3)
btn27.grid(column=2,row=3)
btn28.grid(column=3,row=3)
btn29.grid(column=4,row=3)


quitbtn.grid(column=5,row=3,columnspan=3)




add_hotkey('1',fbi)
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
add_hotkey('1+4',dog_laughing)
add_hotkey('2+5',sad_violin)
add_hotkey('3+6',what_the_dog_doin)
add_hotkey('4+7',snore_mimimi)
add_hotkey('5+8',meme_ending)
add_hotkey('-',run_meme)
add_hotkey('-+*',gay_echo)
add_hotkey('0',thankyou_anime)
add_hotkey('6+9',thankyou_myfriend)


root.mainloop()



while 1:
    wait()

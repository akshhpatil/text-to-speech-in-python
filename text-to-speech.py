

from gtts import gTTS                                     #import modules from gtts
import os

Myvariable ="Hello Good evening this is demo program of text-to-speech in python." 

language = 'en'                                            #Select language              

output = gTTS(text= Myvariable,lang=language,slow=False)   

output.save("output.mp3")                                   

os.system("start output.mp3")                             #save your file in directory & play when it save

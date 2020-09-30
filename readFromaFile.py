from gtts import gTTS
import os

fname='Simple_text_editor.py.txt'
fhand=open(fname)
text=''
for line in fhand:
    text=text+' '+line

print(text)
language='en'

output_File=gTTS(text=text,lang=language,slow=False)
output_File.save("code.mp3")
os.system("start code.mp3")


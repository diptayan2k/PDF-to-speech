"""
Created on Thu Dec 26 20:46:01 2019

@author: DIPTAYAN BISWAS
"""

# Import the Gtts module for text  
# to speech conversion 
from gtts import gTTS 
import PyPDF2

# pdf file object
pdfFileObj = open('sample.pdf', 'rb')
 
# pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#Extracting the pdf into a string
text=""
for i in range (pdfReader.numPages):
    pageObj = pdfReader.getPage(i) 
    text+=pageObj.extractText()
    

    # import Os module to start the audio file
import os
text = text.replace("\n"," ")
text = text.lower()

punctuations = '''!()-[]{};:'"\<>/?@#$%^&*_~123456789'''
# remove punctuation from the string
no_punct = ""
for char in text:
   if char not in punctuations:
       no_punct = no_punct + char

myText = no_punct
# Language we want to use 
language = 'en'

output = gTTS(text=myText, lang=language, slow=False)

output.save("output.mp3")


# Play the converted file 
os.system("start output.mp3")
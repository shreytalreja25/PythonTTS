#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pyttsx3
import PyPDF2

book = open('queen.pdf','rb')
pdfReader = PyPDF2.pdfReader(book)
pdfPages = pdfReader.numPages
print(pdfPages)
engine = pyttsx3.init()
x = input("Read From Which Page?")
page = pdfReader.getPaage(x)
text = page.extractText()

engine.say(text)
engine.runAndWait()


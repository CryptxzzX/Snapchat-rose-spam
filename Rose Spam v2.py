from selenium import webdriver
import tkinter as tk
from tkinter import filedialog, Text
import os
from os import system, name 
import time
import random
root = tk.Tk()

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
            

def startSpam():
    messages = ["your a fuckin loser", "go fuck yourself bud", "quit ur shit you fucking junkie", "mirrors can't talk. Lucky for you, they cant laugh either.", "if I had a face like yours, I'd sue my parents.", "If I said anything to offend you it was purely intentional.", "If I throw a stick, will you go away? fucking dog", "You started at the bottom and it's been downhill ever since"]
    url = 'URL HERE'
    driver = webdriver.Chrome("PATH TO DRIVER HERE")
    clear()
    for y in range(0, 183):  
        driver.get(url)    
        time.sleep(2)
        driver.find_element_by_id('message-textarea').send_keys(random.choice(messages))
        time.sleep(1)
        driver.find_element_by_id('message-submit').click()
        print("Sent successfully on time %d" % (y))
    driver.close()

start = tk.Button(root, text="Start Spam", padx=10, pady=5, fg="black", command=startSpam)
start.pack()
root.mainloop()

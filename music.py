from tkinter import*
import webbrowser
from random import choice

sarki = ['https://www.youtube.com/watch?v=M1vBPvektSE&ab_channel=Randomn00b2',
         'https://www.youtube.com/watch?v=I6NU3kWqnDE&ab_channel=LinkinPark-Topic',
         'https://www.youtube.com/watch?v=4512AYi9Pn8&ab_channel=TheGathering-Topic',
         'https://www.youtube.com/watch?v=LpC0SKU6O00&ab_channel=LinkinPark',
         'https://www.youtube.com/watch?v=IpwHB2U3J1s&ab_channel=PearlJam-Topic']
 
root =Tk()

root.title('music')
root.geometry('250x150')
root.config(bg='purple')

btn = Button(root,
             text ='çal',
             bd = '5',
             bg='violet',
             fg='white',
             command = root.destroy)
btn.pack(pady=30)

def kapat():
    quit()

kapatma_tusu = Button(text = "Kapat", bg = "red", fg='white',bd='5',command = kapat)
kapatma_tusu.pack()

root.mainloop()


webbrowser.open(choice(sarki),new=2)



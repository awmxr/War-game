# Amir Marvasti Nejad
# All Right Reserved
# 1399.2.27
# T05 with tkinter
from random import shuffle
from colorama import Fore, Back, Style 
from os import system
import tkinter as tk
import tkinter.messagebox as tm
class Deck:
    def __init__(self,list):
        self.carts = list
    def bor(self):
        shuffle(self.carts)
        cart1 = carts[0:26]
        cart2 = carts[26:53]
        return cart1,cart2
      
class Hand:
    def __init__(self,cart1):
        self.cart1 = cart1
    def Add(self,new_cart):
        self.cart1 = self.cart1 + new_cart
        return self.cart1
    def Remove(self,old_cart):
        del self.cart1[0:old_cart]
        return self.cart1
class Player:
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand
    def play_card(self,b = 0):
        a = self.hand.cart1[b]
        return a
    def remove_war(self):
        a = self.hand.cart1[0:3]
        return a
    def remaining(self):
        if len(self.hand.cart1) <= 0:
            return False
        return True


#########################################################
            
#########################################################
class Application(tk.Frame):
    def __init__(self,hand1,hand2, master=None):
        super().__init__(master)
        self.master = master
        # self.master.configure(bg = "red")
        self.hand1 = hand1
        self.hand2 = hand2
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # self.master.configure(bg = "lightblue")
        self.play = tk.Button(self)
        self.play["text"] = "WAR"
        self.play["command"] = self.play2
        self.play["font"] = ("Helvetica", 50)
        self.play["fg"] = "Blue"
        self.play["bg"] = "orange"
        
        self.play.pack()
        self.quit = tk.Button(self, text="QUIT", fg="red",command=self.master.destroy)
        self.quit.pack(side="bottom")
        

    def play2(self):
        # self.master.configure(bg = "lightblue")
        self.quit.destroy()
        self.play.destroy()
        self.quit.destroy()
        self.label0 = tk.Label(text = "Name",font=("Helvetica", 30))
        self.entry0 = tk.Entry(font=("Helvetica", 30))
        self.i = self.entry0.get()
        self.karbar = Player(self.i,self.hand2)
        self.computer = Player("computer",self.hand1)
        self.start = tk.Button()
        self.start["text"] = "Lets Play"
        self.start["command"] = self.start2
        self.start["font"] = font=("Helvetica", 40)
        self.start["bg"] = "green"
        self.label0.pack()
        self.entry0.pack()
        self.start.pack()
        self.quit = tk.Button(text="QUIT", fg="red",command=self.master.destroy)
        self.quit.pack(side="bottom")
    
    def start2(self):
        # self.master.configure(bg = "lightblue")
        self.karbar_name = self.entry0.get()
        self.label0.destroy()
        self.entry0.destroy()
        self.start.destroy()
        self.quit.destroy()
        self.vasat = []
        
        self.label1 = tk.Label(text = f"number of computer card : {len(hand1.cart1) - len(self.vasat)//2}",fg = "Red",font=("Helvetica", 18))#number of computer card
        self.label2 = tk.Label(text = f"number of {self.karbar_name} card : {len(hand2.cart1) - len(self.vasat)//2}",fg = "Green",font=("Helvetica", 18))#number of your card
        self.start2 = tk.Button()
        self.start2["text"] = "Start"
        self.start2["command"] = self.play3
        self.start2["font"] = font=("Helvetica", 40)
        self.start2["bg"] = "gray"
        self.label1.pack()
        self.label2.pack()
        self.start2.pack()
        self.quit = tk.Button(text="QUIT", fg="red",command=self.master.destroy)
        self.quit.pack(side="bottom") 
        self.round = 0
       
        self.war = 0
        self.g = 0
        self.t = 0
        self.warff = 0
    def play3(self):
        # self.master.configure(bg = "lightblue")
        if self.t == 0:
            self.player1 = self.computer.play_card()
            self.player2 = self.karbar.play_card()
            self.vasat.append(self.player1)
            self.vasat.append(self.player2)
        if self.t != 0:
            self.warff += 1
            self.player1 = self.computer.play_card(self.warff)
            self.player2 = self.karbar.play_card(self.warff)
            self.vasat.append(self.player1)
            self.vasat.append(self.player2)
            self.t = 0

        if self.g == 0:
            
            self.label1.destroy()
            self.label2.destroy()
            self.start2.destroy()
            self.quit.destroy()
            self.g += 1
            self.label1 = tk.Label(text = f"number of computer card : {len(hand1.cart1) - len(self.vasat) // 2}",fg = "Red",font=("Helvetica", 18))#change
            self.label2 = tk.Label(text = f"number of {self.karbar_name} card : {len(hand2.cart1) - len(self.vasat) // 2}",fg = "Green",font=("Helvetica", 18))
            self.round_label = tk.Label(text = f"round : {self.round}")#numbe of round
            self.war_label = tk.Label(text = f"War : {self.war}")
            self.label_karbar = tk.Label(text = f"{self.player1}",font=("Helvetica", 40),bg = "Red")#karbar kart
            self.label_computer = tk.Label(text = f"{self.player2}",font=("Helvetica", 40),bg = "green")#computer card
            self.start2 = tk.Button()
            self.start2["text"] = "Next Round"
            self.start2["font"] = ("Helvetica", 40)
            self.start2["bg"] = "yellow"
            self.start2["command"] = self.play_change
            self.start2.pack()
            self.label1.pack()
            self.label2.pack()
            self.round_label.pack()
            self.war_label.pack()
            self.label_karbar.pack(side = "right")
            self.label_computer.pack(side ="left")
            self.quit = tk.Button(text="QUIT", fg="red",command=self.master.destroy)
            self.quit.pack(side="bottom")
        else:
            
            self.quit.destroy()
            self.start2.destroy()
            self.label1.destroy()
            self.label2.destroy()
            self.round_label.destroy()
            self.war_label.destroy()
            self.label_karbar.destroy()
            self.label_computer.destroy()
            self.label1 = tk.Label(text = f"number of computer card : {len(hand1.cart1) - len(self.vasat)//2}",fg = "Red",font=("Helvetica", 18))#change
            self.label2 = tk.Label(text = f"number of {self.karbar_name} card : {len(hand2.cart1) - len(self.vasat)//2}",fg = "Green",font=("Helvetica", 18))
            self.round_label = tk.Label(text = f"round : {self.round}")#numbe of round
            self.war_label = tk.Label(text = f"War : {self.war}")
            self.label_karbar = tk.Label(text = f"{self.player1}",font=("Helvetica", 40),bg = "Red")#karbar kart
            self.label_computer = tk.Label(text = f"{self.player2}",font=("Helvetica", 40),bg = "Green")#computer card
            self.start2 = tk.Button()
            self.start2["text"] = "Next Round"
            self.start2["font"] = ("Helvetica", 40)
            self.start2["bg"] = "yellow"
            self.start2["command"] = self.play_change
            self.quit = tk.Button(text="QUIT", fg="red",command=self.master.destroy)
            self.start2.pack()
            self.label1.pack()
            self.label2.pack()
            self.round_label.pack()
            self.war_label.pack()
            self.label_karbar.pack(side ="right")
            self.label_computer.pack(side = "left")
            self.quit = tk.Button(text="QUIT", fg="red",command=self.master.destroy)
            self.quit.pack(side="bottom")
        self.round += 1
        

    def play_change(self):
        
        self.x1 = self.player1.replace("S","") 
        self.x1 = self.x1.replace("H","") 
        self.x1 = self.x1.replace("O","") 
        self.x1 = self.x1.replace("D","") 
        self.x2 = self.player2.replace("S","") 
        self.x2 = self.x2.replace("H","") 
        self.x2 = self.x2.replace("O","") 
        self.x2 = self.x2.replace("D","") 
        self.x1 = int(self.x1)
        self.x2 = int(self.x2)
        self.check2()
        self.play3()

    def check2(self):
        if self.x2 > self.x1:
            self.warff = 0
            # self.t = 0
            self.karbar.hand.Remove(len(self.vasat) // 2)
            # self.barg = self.vasat2
            self.vasat.reverse()
            self.karbar.hand.Add(self.vasat)
            # self.karbar.hand.Add(self.vasat1)
            # del self.vasat1
            self.computer.hand.Remove(len(self.vasat) // 2)
            del self.vasat
            self.vasat = []
            # self.vasat2 = []
            
        if self.x1 > self.x2:
            self.warff = 0
            # self.t = 0
            self.computer.hand.Remove(len(self.vasat) // 2)
            # self.barg = self.vasat1
            self.vasat.reverse()
            self.computer.hand.Add(self.vasat)
            # self.computer.hand.Add(self.vasat2)
            # del self.vasat2
            self.karbar.hand.Remove(len(self.vasat) // 2)
            del self.vasat
            self.vasat = []
            # self.vasat2 = []
        # self.a = 1
        if self.x1 == self.x2:
            self.t += 1
            tm.showinfo( f"WooooW", "WAAAAAAAAAAAAAAR")
            self.war += 1
            self.player11 = self.computer.remove_war()
            self.player22 = self.karbar.remove_war()
            self.vasat += self.player11
            self.vasat += self.player22
            self.x1 = self.player1.replace("S","") 
            self.x1 = self.x1.replace("H","") 
            self.x1 = self.x1.replace("O","") 
            self.x1 = self.x1.replace("D","") 
            self.x2 = self.player2.replace("S","") 
            self.x2 = self.x2.replace("H","") 
            self.x2 = self.x2.replace("O","") 
            self.x2 = self.x2.replace("D","") 
            self.x1 = int(self.x1)
            self.x2 = int(self.x2)
            
        if self.computer.remaining() == False:
            tm.showinfo( f"WooooooW", "Tabrik\nShoma bordid")
            self.master.destroy()
        if self.karbar.remaining() == False:
            tm.showinfo( f"Next Time", "Shoma bakhtid")
            self.master.destroy()




        

carts1 = list(range(1,14))
carts2 = list(range(1,14))
carts3 = list(range(1,14))
carts4 = list(range(1,14))
for i in range(13):
    carts1[i] = str(carts1[i]) + " D"
    carts2[i] = str(carts2[i]) + " S"
    carts3[i] = str(carts3[i]) + " H"
    carts4[i] = str(carts4[i]) + " O"
    
carts = carts1 + carts2 + carts3 + carts4
# print(len(carts))
cards = Deck(carts)
cart1 , cart2 = cards.bor()
hand1 = Hand(cart1)
hand2 = Hand(cart2)


        


win = tk.Tk()
# win.configure(bg = "lightblue")
win.title("Centering windows")
win.resizable(False, False)  # This code helps to disable windows from resizing

window_height = 500
window_width = 500

screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
app = Application(hand1,hand2,master=win)
app.mainloop()
#########################################################################################################

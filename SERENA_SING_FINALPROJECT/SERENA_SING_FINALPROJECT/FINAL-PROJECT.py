from tkinter import *
from tkinter.messagebox import *
import random
import RPi.GPIO as GPIO   
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)#REDpin
GPIO.setup(16,GPIO.OUT)#GREENpin
GPIO.setup(22,GPIO.OUT)#1st
GPIO.setup(19,GPIO.IN)#2nd
GPIO.setup(25,GPIO.IN)#PUSH BUTTON 1
GPIO.setup(18,GPIO.OUT)#1st


button1 = GPIO.input(25)


GPIO.output(4, True)
GPIO.output(16, False)
    

class MainGui:
    
    def __init__(self):
        self.mainWin = Tk()
        self.mainWin.geometry("800x550+100+100")
        self.mainWin.title("Rock Paper Scissors")
        
        self.distance = 100000.00
        self.score = 0
        self.score2 = 0
        self.rounds = 0
#         self.count = 0
        
        self.frame1 = Frame(self.mainWin, width = 350, height = 400, bg = "#B0E0E6")
        self.frame1.place(x = 50, y = 100)
        self.frame2 = Frame(self.mainWin, width = 350, height = 400, bg = "#FFF0F5")
        self.frame2.place(x = 400, y = 100)
        self.frame3 = Frame(self.mainWin, width = 800, height = 100, bg = "white")
        self.frame3.place(x = 0, y = 0)
        self.frame4 = Frame(self.mainWin, width = 50, height = 400, bg = "black")
        self.frame4.place(x = 0, y = 100)
        self.frame5 = Frame(self.mainWin, width = 50, height = 400, bg = "black")
        self.frame5.place(x = 750, y = 100)
        self.frame6 = Frame(self.mainWin, width = 800, height = 50, bg = "white")
        self.frame6.place(x = 0, y = 500)
        
        self.my_menu = Menubutton(self.frame3, text = "Options", bg = 'white', fg = 'black',activebackground = 'red')
        self.my_menu.place(x = 732, y = 0)
        self.my_menu.menu = Menu(self.my_menu, tearoff = 0)
        self.my_menu["menu"] = self.my_menu.menu
        self.my_menu.menu.add_command(label = "Help", command = self.do_help)
        self.my_menu.menu.add_command(label = "Info", command = self.do_info)
        self.my_menu.menu.add_separator()
        self.my_menu.menu.add_command(label = "Exit", command = self.mainWin.destroy)
        
        self.img4 = PhotoImage(file = "rps2.png")
        self.img4Label = Label(image = self.img4, border = 0)
        self.img4Label.place(x = 300, y = 0)
        
        self.comp = PhotoImage(file = "computer1.png")
        self.compLabel = Label(image = self.comp, border = 0)
        self.compLabel.place(x = 507, y = 148)
    
        self.player1 = PhotoImage(file = "player 2.png")
        self.player1Label = Label(image = self.player1, border = 0)
        self.player1Label.place(x = 148, y = 148)
        
        self.VSL = Label(self.mainWin, text = "VS", font = ("lithograph", 20, "bold"), bg = "black", fg = "white")
        self.VSL.place(x = 375, y = 270)
        self.roundsL = Label(self.frame3, text = "NUMBER OF ROUNDS:", font = ("lithograph", 11, "bold"), bg = "white", fg = "black")
        self.roundsL.place(x = 0, y = 0)
        
        self.choiceR = StringVar() 
        self.r1 = Radiobutton(self.frame3, text = "I", font = ("Times new roman",8, "bold"),bg = "white", fg = "black", variable = self.choiceR, value = "I", command = self.score1) 
        self.r2 = Radiobutton(self.frame3, text = "II", font = ("Times new roman",8, "bold"), bg = "white", fg = "black", variable = self.choiceR, value = "II", command = self.score1)
        self.r3 = Radiobutton(self.frame3, text = "III", font = ("Times new roman",8, "bold"), bg = "white", fg = "black",variable = self.choiceR, value = "III", command = self.score1) 
        self.r1.place(x = 0, y = 20)
        self.r2.place(x = 0, y = 40)
        self.r3.place(x = 0, y = 60)
        
#         self.RPS = StringVar()
#         self.rockImg = PhotoImage(file = "rock.png")
#         self.rockLabel = Label(image = self.rockImg, border = 0)
#         self.rockLabel.place(x = 55, y = 320)
#         self.paperImg = PhotoImage(file = "paper.png")
#         self.paperLabel = Label(image = self.paperImg, border = 0)
#         self.paperLabel.place(x = 170, y = 345)
#         self.scissorsImg = PhotoImage(file = "scissor.png")
#         self.scissorsLabel = Label(image = self.scissorsImg, border = 0)
#         self.scissorsLabel.place(x = 280, y = 330)
#         self.rock = Radiobutton(self.frame1, text = "Rock", font = ("Times new roman",8, "bold"),bg = "#B0E0E6", fg = "black", variable = self.RPS, value = '1', command = self.RPS1) 
#         self.paper = Radiobutton(self.frame1, text = "Paper", font = ("Times new roman",8, "bold"), bg = "#B0E0E6", fg = "black", variable = self.RPS, value = '2', command = self.RPS1)
#         self.scissors = Radiobutton(self.frame1, text = "Scissors", font = ("Times new roman",8, "bold"), bg = "#B0E0E6", fg = "black", variable = self.RPS, value = '3', command = self.RPS1) 
#         self.rock.place(x = 5, y = 280)
#         self.paper.place(x = 125, y = 335)
#         self.scissors.place(x = 240, y = 320)
        
        mainloop()
        
    def do_info(self):
        info = "Details: A rock, paper, scissors game\nCreator: Serena Sing\nDate of Creation: 2022/04/06"
        showinfo("Info", info)
        
    def do_help(self):
        help = "1.Choose the number of rounds you would like to play\n2.choose rock, paper, or scissors"
        showinfo("HELP", help)
    
    def compRand(self):
        ans = random.randint(1, 3)
        random.time(0)
        
        return ans
    
    def score1(self):
        if self.choiceR.get() == 'I':
            self.rounds = 1
        elif self.choiceR.get() == 'II':
            self.rounds = 2
        else:
            self.rounds = 3
            
        self.RPS = StringVar()
        self.rockImg = PhotoImage(file = "rock.png")
        self.rockLabel = Label(image = self.rockImg, border = 0)
        self.rockLabel.place(x = 55, y = 320)
        self.paperImg = PhotoImage(file = "paper.png")
        self.paperLabel = Label(image = self.paperImg, border = 0)
        self.paperLabel.place(x = 170, y = 345)
        self.scissorsImg = PhotoImage(file = "scissor.png")
        self.scissorsLabel = Label(image = self.scissorsImg, border = 0)
        self.scissorsLabel.place(x = 280, y = 330)
        self.rock = Radiobutton(self.frame1, text = "Rock", font = ("Times new roman",8, "bold"),bg = "#B0E0E6", fg = "black", variable = self.RPS, value = '1', command = self.RPS1) 
        self.paper = Radiobutton(self.frame1, text = "Paper", font = ("Times new roman",8, "bold"), bg = "#B0E0E6", fg = "black", variable = self.RPS, value = '2', command = self.RPS1)
        self.scissors = Radiobutton(self.frame1, text = "Scissors", font = ("Times new roman",8, "bold"), bg = "#B0E0E6", fg = "black", variable = self.RPS, value = '3', command = self.RPS1) 
        self.rock.place(x = 5, y = 280)
        self.paper.place(x = 125, y = 335)
        self.scissors.place(x = 240, y = 320)
        
    def RPS1(self):
        self.Distance_front(22, 19)
        if (self.distance) > 10.00:
            print('reccursion')
            self.mainWin.after(1, self.RPS1)
        else:
            self.RPS1_Loop()
    
    
    def RPS1_Loop(self):
        ans = self.compRand()
        
    
        if self.distance < 10:
                
            if self.RPS.get() == '1':
                if ans == 1:
                    self.equal9 = PhotoImage(file = "equall.png")
                    self.equal9Label = Label(image = self.equal9, border = 0)
                    self.equal9Label.place(x = 350, y = 100)
                    self.x = PhotoImage(file = "rock.png")
                    self.xLabel = Label(image = self.x, border = 0)
                    self.xLabel.place(x = 500, y = 350)
                elif ans == 2:
                    self.lost = PhotoImage(file = "lost.png")
                    self.lostLabel = Label(image = self.lost, border = 0)
                    self.lostLabel.place(x = 350, y = 100)
                    self.x = PhotoImage(file = "paper.png")
                    self.xLabel = Label(image = self.x, border = 0)
                    self.xLabel.place(x = 500, y = 350)
                    self.score2 += 1
                    self.player2s = Label(self.frame6, text = str(self.score2), font = ("lithograph", 16, "bold"), bg = "white", fg = "black")
                    self.player2s.place(x = 750, y = 0)
                    if self.score == self.rounds:
                        self.done = Label(self.frame6, text = 'WIN', font = ("lithograph", 16, "bold"), bg = "white", fg = "black")
                        self.done.place(x = 300, y = 0)
                        self.w = PhotoImage(file = "winner.png")
                        self.wLabel = Label(image = self.w, border = 0)
                        self.wLabel.place(x = 300, y = 200)
                    if self.score2 == self.rounds:
                        self.done = Label(self.frame6, text = 'LOSE', font = ("lithograph", 16, "bold"), bg = "white", fg = "black")
                        self.done.place(x = 300, y = 0)
                        self.l = PhotoImage(file = "loser.png")
                        self.lLabel = Label(image = self.l, border = 0)
                        self.lLabel.place(x = 300, y = 200)
                    self.beep()
                else:
                    self.winner2 = PhotoImage(file = "confetti.png")
                    self.winner2Label = Label(image = self.winner2, border = 0)
                    self.winner2Label.place(x = 350, y = 100)
                    self.x = PhotoImage(file = "scissor.png")
                    self.xLabel = Label(image = self.x, border = 0)
                    self.xLabel.place(x = 500, y = 350)
                    for i in range(6):
                        GPIO.output(4, True)
                        time.sleep(0.1)
                        GPIO.output(4, False)
                        time.sleep(0.1)
                        GPIO.output(16, True)
                        time.sleep(0.1)
                        GPIO.output(16, False)
                        time.sleep(0.1)
                    self.score += 1
                    self.player1s = Label(self.frame6, text = str(self.score), font = ("lithograph", 16, "bold"), bg = "white", fg = "black")
                    self.player1s.place(x = 0, y = 0)
                    if self.score == self.rounds:
                        self.done = Label(self.frame6, text = 'WIN', font = ("lithograph", 16, "bold"), bg = "white", fg = "black")
                        self.done.place(x = 300, y = 0)
                        self.w = PhotoImage(file = "winner.png")
                        self.wLabel = Label(image = self.w, border = 0)
                        self.wLabel.place(x = 300, y = 200)
                    if self.score2 == self.rounds:
                        self.done = Label(self.frame6, text = 'LOSE', font = ("lithograph", 16, "bold"), bg = "white", fg = "black")
                        self.done.place(x = 300, y = 0)
                        self.l = PhotoImage(file = "loser.png")
                        self.lLabel = Label(image = self.l, border = 0)
                        self.lLabel.place(x = 300, y = 200)
                        
                
            if self.RPS.get() == '2':
                if ans == 1:
                    self.winner3 = PhotoImage(file = "confetti.png")
                    self.winner3Label = Label(image = self.winner3, border = 0)
                    self.winner3Label.place(x = 350, y = 100)
                    self.x = PhotoImage(file = "rock.png")
                    self.xLabel = Label(image = self.x, border = 0)
                    self.xLabel.place(x = 500, y = 350)
                    for j in range(10):
                        GPIO.output(4, True)
                        time.sleep(0.1)
                        GPIO.output(4, False)
                        time.sleep(0.1)
                        GPIO.output(16, True)
                        time.sleep(0.1)
                        GPIO.output(16, False)
                        time.sleep(0.1)
                    self.score += 1
                    self.player1s = Label(self.frame6, text = str(self.score), font = ("lithograph", 16, "bold"), bg = "white", fg = "black")
                    self.player1s.place(x = 0, y = 0)
                    if self.score == self.rounds:
                        self.done = Label(self.frame6, text = 'WIN', font = ("lithograph", 16, "bold"), bg = "white", fg = "black")
                        self.done.place(x = 300, y = 0)
                        self.w = PhotoImage(file = "winner.png")
                        self.wLabel = Label(image = self.w, border = 0)
                        self.wLabel.place(x = 300, y = 200)
                    if self.score2 == self.rounds:
                        self.done = Label(self.frame6, text = 'LOSE', font = ("lithograph", 16, "bold"), bg = "white", fg = "black")
                        self.done.place(x = 300, y = 0)
                        self.l = PhotoImage(file = "loser.png")
                        self.lLabel = Label(image = self.l, border = 0)
                        self.lLabel.place(x = 300, y = 200)
                elif ans == 2:
                    self.equal6 = PhotoImage(file = "equall.png")
                    self.equal6Label = Label(image = self.equal6, border = 0)
                    self.equal6Label.place(x = 350, y = 100)
                    self.x = PhotoImage(file = "paper.png")
                    self.xLabel = Label(image = self.x, border = 0)
                    self.xLabel.place(x = 500, y = 350)
                else:
                    self.lost4 = PhotoImage(file = "lost.png")
                    self.lost4Label = Label(image = self.lost4, border = 0)
                    self.lost4Label.place(x = 350, y = 100)
                    self.x = PhotoImage(file = "scissor.png")
                    self.xLabel = Label(image = self.x, border = 0)
                    self.xLabel.place(x = 500, y = 35)
                    self.score2 += 1
                    self.player2s = Label(self.frame6, text = str(self.score2), font = ("lithograph", 16, "bold"), bg = "white", fg = "black")
                    self.player2s.place(x = 750, y = 0)
                    if self.score == self.rounds:
                        self.done = Label(self.frame6, text = 'WIN', font = ("lithograph", 16, "bold"), bg = "white", fg = "black")
                        self.done.place(x = 300, y = 0)
                        self.w = PhotoImage(file = "winner.png")
                        self.wLabel = Label(image = self.w, border = 0)
                        self.wLabel.place(x = 300, y = 200)
                    if self.score2 == self.rounds:
                        self.done = Label(self.frame6, text = 'LOSE', font = ("lithograph", 16, "bold"), bg = "white", fg = "black")
                        self.done.place(x = 300, y = 0)
                        self.l = PhotoImage(file = "loser.png")
                        self.lLabel = Label(image = self.l, border = 0)
                        self.lLabel.place(x = 300, y = 200)
                    self.beep()
                
            if self.RPS.get() == '3':
                if ans == 1:
                    self.lost5 = PhotoImage(file = "lost.png")
                    self.lost5Label = Label(image = self.lost5, border = 0)
                    self.lost5Label.place(x = 350, y = 100)
                    self.x = PhotoImage(file = "rock.png")
                    self.xLabel = Label(image = self.x, border = 0)
                    self.xLabel.place(x = 500, y = 350)
                    self.score2 += 1
                    self.player2s = Label(self.frame6, text = str(self.score2), font = ("lithograph", 16, "bold"), bg = "white", fg = "black")
                    self.player2s.place(x = 750, y = 0)
                    if self.score == self.rounds:
                        self.done = Label(self.frame6, text = 'WIN', font = ("lithograph", 16, "bold"), bg = "white", fg = "black")
                        self.done.place(x = 300, y = 0)
                    if self.score2 == self.rounds:
                        self.done = Label(self.frame6, text = 'LOSE', font = ("lithograph", 16, "bold"), bg = "white", fg = "black")
                        self.done.place(x = 300, y = 0)
                        self.l = PhotoImage(file = "loser.png")
                        self.lLabel = Label(image = self.l, border = 0)
                        self.lLabel.place(x = 300, y = 200)
                    self.beep()
                elif ans == 2:
                    self.winner7 = PhotoImage(file = "confetti.png")
                    self.winner7Label = Label(image = self.winner7, border = 0)
                    self.winner7Label.place(x = 350, y = 100)
                    self.x = PhotoImage(file = "paper.png")
                    self.xLabel = Label(image = self.x, border = 0)
                    self.xLabel.place(x = 500, y = 350)
                    for k in range(10):
                        GPIO.output(4, True)
                        time.sleep(0.1)
                        GPIO.output(4, False)
                        time.sleep(0.1)
                        GPIO.output(16, True)
                        time.sleep(0.1)
                        GPIO.output(16, False)
                        time.sleep(0.1)
                    if self.score == self.rounds:
                        self.done = Label(self.frame6, text = 'WIN', font = ("lithograph", 16, "bold"), bg = "white", fg = "black")
                        self.done.place(x = 300, y = 0)
                    if self.score2 == self.rounds:
                        self.done = Label(self.frame6, text = 'LOSE', font = ("lithograph", 16, "bold"), bg = "white", fg = "black")
                        self.done.place(x = 300, y = 0)
                        self.l = PhotoImage(file = "loser.png")
                        self.lLabel = Label(image = self.l, border = 0)
                        self.lLabel.place(x = 300, y = 200)
                    self.score += 1
                    self.player1s = Label(self.frame6, text = str(self.score), font = ("lithograph", 16, "bold"), bg = "white", fg = "black")
                    self.player1s.place(x = 0, y = 0)
                else:
                    self.equal3 = PhotoImage(file = "equall.png")
                    self.equal3Label = Label(image = self.equal3, border = 0)
                    self.equal3Label.place(x = 350, y = 100)
                    self.x = PhotoImage(file = "scissor.png")
                    self.xLabel = Label(image = self.x, border = 0)
                    self.xLabel.place(x = 500, y = 350)
                self.distance = 1000000
                    
    def beep(self):
        i = 0
        while i < 1000:
            GPIO.output(18,True)
            time.sleep(0.001)
            GPIO.output(18   , False)
            time.sleep(0.001)
            i += 1
        
        
    
    def Distance_front(self, pin1, pin2):
#         print("Distance Measurement in Progress")
        GPIO.output(pin1, True)
        time.sleep(0.00001)
        GPIO.output(pin1, False)
        startTime = time.time()
        stopTime = time.time()
        while GPIO.input(pin2) == False:
            startTime = time.time()
        while GPIO.input(pin2) == True:
            stopTime = time.time()
        during = stopTime - startTime
        self.distance = (during * 34300) / 2
        print('loop')


while button1 == True:
    button1 = GPIO.input(25)
GPIO.output(4, False)
GPIO.output(16, True)
myGui = MainGui()

from tkinter import *
from tkinter.messagebox import *

class MyGui:
    def __init__(self):
        self.mainWin = Tk()
        self.mainWin.geometry("793x496+100+100")
        self.mainWin.title("Food Picker: What should I eat?")
        
        self.frame1 = Frame(self.mainWin, width = 793, height = 50, bg = "white")
        self.frame1.place(x = 0, y = 0)
        self.frame2 = Frame(self.mainWin, width = 793, height = 146)
        self.frame2.place(x = 0, y = 350)
        self.frame3 = Frame(self.mainWin, width = 793, height = 300)
        self.frame3.place(x = 0, y = 50)
        
        
        self.bg1 = PhotoImage(file = 'pic3.png')
        self.canvasBg1 = Canvas(self.frame3, width = 793, height = 300)
        self.canvasBg1.pack(fill = "both", expand = True)
        self.canvasBg1.create_image( 0, 0, image = self.bg1, anchor = "nw")
        self.bg2 = PhotoImage(file = 'pic32.png')
        self.canvasBg2 = Canvas(self.frame2, width = 793, height = 496)
        self.canvasBg2.pack(fill = "both", expand = True)
        self.canvasBg2.create_image( 0, 0, image = self.bg2, anchor = "nw")
        
        
        self.titleL = Label(self.frame1, text = "Your 24/7 Food Picker", font = ("engravers mt", 20, "bold"), bg = "white", fg = "black")
        self.titleL.place(x = 20, y = 0)
        self.ingredients = Label(self.frame3, text = "2) Ingredients:", font = ("engravers mt", 6), bg = "white", fg = "black")
        self.ingredients.place(x = 640, y = 5)
        self.num1 = Label(self.frame3, text = "1)", font = ("engravers mt", 10), bg = "white", fg = "black")
        self.num1.place(x = 65, y = 135)
        
        self.choice13 = StringVar()
        self.choice13.set("BF")  
        self.r1 = Radiobutton(self.frame3, text = "Breakfast", font = ("Times new roman",10),bg = "white", variable = self.choice13, value = "BF") 
        self.r2 = Radiobutton(self.frame3, text = "Lunch", font = ("Times new roman",10), bg = "white", variable = self.choice13, value = "L")
        self.r3 = Radiobutton(self.frame3, text = "Dinner", font = ("Times new roman",10), bg = "white", variable = self.choice13, value = "D") 
        self.r1.place(x = 97, y = 150)
        self.r2.place(x = 240, y = 150)
        self.r3.place(x = 355, y = 150)
        
        self.choice2 = IntVar()
        self.choice3 = IntVar()
        self.choice1 = IntVar()
        self.choice4 = IntVar()
        self.choice5 = IntVar()
        self.choice6 = IntVar()
        self.choice7 = IntVar()
        self.choice8 = IntVar()
        self.choice9 = IntVar()
        self.choice10 = IntVar()
        self.choice11 = IntVar()
        self.choice12 = IntVar()
        self.choice1.set(0) 
        self.choice2.set(0)
        self.choice3.set(0)
        self.choice4.set(0) 
        self.choice5.set(0)
        self.choice6.set(0)
        self.choice7.set(0) 
        self.choice8.set(0)
        self.choice9.set(0)
        self.choice10.set(0) 
        self.choice11.set(0)
        self.choice12.set(0)
        self.ch1 = Checkbutton(self.frame3, text = "Tomatoes", font = ("Times new roman",6), bg = "#C2FBA6", variable = self.choice1) 
        self.ch2 = Checkbutton(self.frame3, text = "Eggs", font = ("Times new roman",6), bg = "#C2FBA6", variable = self.choice2)
        self.ch3 = Checkbutton(self.frame3, text = "Pasta", font = ("Times new roman",6), bg = "#F1C676", variable = self.choice3) 
        self.ch4 = Checkbutton(self.frame3, text = "Bacon", font = ("Times new roman",6), bg = "#E4C3C3", variable = self.choice4) 
        self.ch5 = Checkbutton(self.frame3, text = "Rice", font = ("Times new roman",6), bg = "#F1C676", variable = self.choice5)
        self.ch6 = Checkbutton(self.frame3, text = "Bread", font = ("Times new roman",6), bg = "#F1C676", variable = self.choice6) 
        self.ch7 = Checkbutton(self.frame3, text = "Bell peppers", font = ("Times new roman",6), bg = "#C2FBA6", variable = self.choice7)
        self.ch8 = Checkbutton(self.frame3, text = "Chicken", font = ("Times new roman",6), bg = "#E4C3C3", variable = self.choice8)
        self.ch9 = Checkbutton(self.frame3, text = "Cheese", font = ("Times new roman",6), bg = "#C2FBA6", variable = self.choice9) 
        self.ch10 = Checkbutton(self.frame3, text = "Sausages", font = ("Times new roman",6), bg = "#E4C3C3", variable = self.choice10)
        self.ch11 = Checkbutton(self.frame3, text = "Veggies", font = ("Times new roman",6), bg = "#C2FBA6", variable = self.choice11)
        self.ch12 = Checkbutton(self.frame3, text = "Broccoli", font = ("Times new roman",6), bg = "#C2FBA6", variable = self.choice12) 
        self.ch1.place(x = 620, y = 25)
        self.ch2.place(x = 620, y = 50)
        self.ch3.place(x = 620, y = 100)
        self.ch4.place(x = 620, y = 150)
        self.ch5.place(x = 620, y = 125)
        self.ch6.place(x = 690, y = 100)
        self.ch7.place(x = 620, y = 75)
        self.ch8.place(x = 690, y = 150)
        self.ch9.place(x = 700, y = 75)
        self.ch10.place(x = 620, y = 175)
        self.ch11.place(x = 690, y = 25)
        self.ch12.place(x = 700, y = 50)
        
        self.buttonOK = Button(self.frame3, text = "OK", font = ("Times new roman", 8, "bold"), bg = "#BB3131",fg = 'white', activebackground = '#EE9A4D',command = self.do_OK)
        self.buttonOK.place(x = 677, y = 250)
        
        self.entry = Entry(self.mainWin, width = 40, font = ("calibri", 6))
        self.entry.place(x = 360, y = 450)
        self.recL = Label(self.mainWin, text = "Suggestions for missing options:", font = ("calibri", 7), bg = "white", fg = "black")
        self.recL.place(x = 170, y = 450)
        self.buttonOK2 = Button(self.mainWin, text = "Send", font = ("calibri", 6, "bold"), bg = "white", command = self.do_OK2)
        self.buttonOK2.place(x = 570, y = 450)
        self.buttonOK2add = Button(self.mainWin, text = "add", font = ("calibri", 6, "bold"), bg = "white", command = self.do_OK2add)
        self.buttonOK2add.place(x = 600, y = 450)
        
        self.my_menu = Menubutton(self.frame1, text = "Options",relief = RAISED, bg = '#BB3131', fg = 'white',activebackground = '#EE9A4D')
        self.my_menu.place(x = 700, y = 10)
        self.my_menu.menu = Menu(self.my_menu, tearoff = 0)
        self.my_menu["menu"] = self.my_menu.menu
        self.my_menu.menu.add_command(label = "Help", command = self.do_help)
        self.my_menu.menu.add_command(label = "Info", command = self.do_info)
        self.my_menu.menu.add_separator()
        self.my_menu.menu.add_command(label = "Exit", command = self.mainWin.destroy)
        self.my_menu.place(x = 663, y = 10)
        
        mainloop()
    
    def do_help(self):
        help = "Don't know what to eat?\nYour 24/7 Food picker has got you covered!\n1. Pick whether this meal is for breakfast, lunch or dinner\n2. Checkmark which ingredients you have (optional)\n3. Click OK and a list of food options will be be shown\n4. Click a food option to see the recipe\n5. Enjoy!"
        showinfo("HELP", help)
    def do_info(self):
        info = "Details: An application to help choose what to eat\nCreator: Serena Sing\nDate of Creation: 2022/01/31"
        showinfo("Info", info)
    def do_OK(self):
        self.ingredients = Label(self.frame3, text = "3) Click image for Recipe:", font = ("engravers mt", 8), bg = "white", fg = "black")
        self.ingredients.place(x = 50, y = 220)
        if self.choice13.get() == "BF" and self.choice1.get() == 0 and self.choice2.get() == 0 and self.choice3.get() == 0 and self.choice4.get() == 0 and self.choice5.get() == 0 and self.choice5.get() == 0 and self.choice6.get() == 0 and self.choice7.get() == 0 and self.choice8.get() == 0 and self.choice9.get() == 0:
            if self.choice10.get() == 0 and self.choice11.get() == 0 and self.choice12.get() == 0:
                self.img1 = PhotoImage(file = "img1.png")
                self.img1Label = Label(image = self.img1)
                self.img1Button = Button(self.mainWin, image = self.img1, command = self.do_img1_1)
                self.img1Button.place(x = 95, y = 300 )
                
                self.img4 = PhotoImage(file = "EgginaHole.png")
                self.img4Label = Label(image = self.img4)
                self.img4Button = Button(self.mainWin, image = self.img4, command = self.do_img1_2)
                self.img4Button.place(x = 220, y = 300 )
                
                self.img6 = PhotoImage(file = "FEABS.png")
                self.img6Label = Label(image = self.img6)
                self.img6Button = Button(self.mainWin, image = self.img6, command = self.do_img1_3)
                self.img6Button.place(x = 370, y = 300 )
                
                
        elif self.choice13.get() == "L" and self.choice1.get() == 0 and self.choice2.get() == 0 and self.choice3.get() == 0 and self.choice4.get() == 0 and self.choice5.get() == 0 and self.choice5.get() == 0 and self.choice6.get() == 0 and self.choice7.get() == 0 and self.choice8.get() == 0 and self.choice9.get() == 0:
            if self.choice10.get() == 0 and self.choice11.get() == 0 and self.choice12.get() == 0:
                self.img2 = PhotoImage(file = "GCS.png")
                self.img2Label = Label(image = self.img2)
                self.img2Button = Button(self.mainWin, image = self.img2, command = self.do_img2_1)
                self.img2Button.place(x = 95, y = 300 )
                
                self.img5 = PhotoImage(file = "FriedRice.png")
                self.img5Label = Label(image = self.img5)
                self.img5Button = Button(self.mainWin, image = self.img5, command = self.do_img2_2)
                self.img5Button.place(x = 220, y = 300 )
                self.img5L = Label(self.mainWin, text = "Fried Rice", font = ("engravers mt", 6), fg = "white", bg = "black")
                
                self.img7 = PhotoImage(file = "STB.png")
                self.img7Label = Label(image = self.img7)
                self.img7Button = Button(self.mainWin, image = self.img7, command = self.do_img2_3)
                self.img7Button.place(x = 370, y = 300 )
                
        elif self.choice13.get() == "D" and self.choice1.get() == 0 and self.choice2.get() == 0 and self.choice3.get() == 0 and self.choice4.get() == 0 and self.choice5.get() == 0 and self.choice5.get() == 0 and self.choice6.get() == 0 and self.choice7.get() == 0 and self.choice8.get() == 0 and self.choice9.get() == 0:
            if self.choice10.get() == 0 and self.choice11.get() == 0 and self.choice12.get() == 0:
                self.img3 = PhotoImage(file = "Spaghetti.png")
                self.img3Label = Label(image = self.img3)
                self.img3Button = Button(self.mainWin, image = self.img3, command = self.do_img3_1)
                self.img3Button.place(x = 95, y = 300 )
                
                self.img8 = PhotoImage(file = "CC.png")
                self.img8Label = Label(image = self.img8)
                self.img8Button = Button(self.mainWin, image = self.img8, command = self.do_img3_2)
                self.img8Button.place(x = 220, y = 300 )
                
                self.img9 = PhotoImage(file = "sau.png")
                self.img9Label = Label(image = self.img9)
                self.img9Button = Button(self.mainWin, image = self.img9, command = self.do_img3_3)
                self.img9Button.place(x = 370, y = 300 )
        
        elif self.choice13.get() == "BF" and self.choice2.get() == 1:
            self.img1 = PhotoImage(file = "img1.png")
            self.img1Label = Label(image = self.img1)
            self.img1Button = Button(self.mainWin, image = self.img1, command = self.do_img1_1)
            self.img1Button.place(x = 95, y = 300 )
            self.img4 = PhotoImage(file = "EgginaHole.png")
            self.img4Label = Label(image = self.img4)
            self.img4Button = Button(self.mainWin, image = self.img4, command = self.do_img1_2)
            self.img4Button.place(x = 220, y = 300 )
            self.img6 = PhotoImage(file = "FEABS.png")
            self.img6Label = Label(image = self.img6)
            self.img6Button = Button(self.mainWin, image = self.img6, command = self.do_img1_3)
            self.img6Button.place(x = 370, y = 300 )
                
        elif self.choice13.get() == "BF" and self.choice9.get() == 1:
            self.img1 = PhotoImage(file = "img1.png")
            self.img1Label = Label(image = self.img1)
            self.img1Button = Button(self.mainWin, image = self.img1, command = self.do_img1_1)
            self.img1Button.place(x = 95, y = 300 )
            self.imgCS1 = PhotoImage(file = "cross3.png")
            self.imgCS1Label = Label(image = self.imgCS1)
            self.imgCS1Button = Button(self.mainWin, image = self.imgCS1)
            self.imgCS1Button.place(x = 220, y = 300 )
            self.imgCS2 = PhotoImage(file = "cross2.png")
            self.imgCS2Label = Label(image = self.imgCS2)
            self.imgCS2Button = Button(self.mainWin, image = self.imgCS2)
            self.imgCS2Button.place(x = 373, y = 300 )
                
        elif self.choice13.get() == "BF" and self.choice1.get() == 1:
            self.img1 = PhotoImage(file = "img1.png")
            self.img1Label = Label(image = self.img1)
            self.img1Button = Button(self.mainWin, image = self.img1, command = self.do_img1_1)
            self.img1Button.place(x = 95, y = 300 )
            self.imgCS1 = PhotoImage(file = "cross3.png")
            self.imgCS1Label = Label(image = self.imgCS1)
            self.imgCS1Button = Button(self.mainWin, image = self.imgCS1)
            self.imgCS1Button.place(x = 220, y = 300 )
            self.imgCS2 = PhotoImage(file = "cross2.png")
            self.imgCS2Label = Label(image = self.imgCS2)
            self.imgCS2Button = Button(self.mainWin, image = self.imgCS2)
            self.imgCS2Button.place(x = 373, y = 300 )
                
        elif self.choice13.get() == "BF" and self.choice6.get() == 1:
            self.img4 = PhotoImage(file = "EgginaHole.png")
            self.img4Label = Label(image = self.img4)
            self.img4Button = Button(self.mainWin, image = self.img4, command = self.do_img1_2)
            self.img4Button.place(x = 220, y = 300 )
            self.img6 = PhotoImage(file = "FEABS.png")
            self.img6Label = Label(image = self.img6)
            self.img6Button = Button(self.mainWin, image = self.img6, command = self.do_img1_3)
            self.img6Button.place(x = 370, y = 300 )
            self.imgCS3 = PhotoImage(file = "cross.png")
            self.imgCS3Label = Label(image = self.imgCS3)
            self.imgCS3Button = Button(self.mainWin, image = self.imgCS3)
            self.imgCS3Button.place(x = 95, y = 300 )
                
        elif self.choice13.get() == "BF" and self.choice4.get() == 1:
            self.img6 = PhotoImage(file = "FEABS.png")
            self.img6Label = Label(image = self.img6)
            self.img6Button = Button(self.mainWin, image = self.img6, command = self.do_img1_3)
            self.img6Button.place(x = 370, y = 300 )
            self.imgCS3 = PhotoImage(file = "cross.png")
            self.imgCS3Label = Label(image = self.imgCS3)
            self.imgCS3Button = Button(self.mainWin, image = self.imgCS3)
            self.imgCS3Button.place(x = 95, y = 300 )
            self.imgCS1 = PhotoImage(file = "cross3.png")
            self.imgCS1Label = Label(image = self.imgCS1)
            self.imgCS1Button = Button(self.mainWin, image = self.imgCS1)
            self.imgCS1Button.place(x = 220, y = 300 )
        
        elif self.choice13.get() == "L" and self.choice6.get() == 1:
            self.img2 = PhotoImage(file = "GCS.png")
            self.img2Label = Label(image = self.img2)
            self.img2Button = Button(self.mainWin, image = self.img2, command = self.do_img2_1)
            self.img2Button.place(x = 95, y = 300 )
            self.imgCS1 = PhotoImage(file = "cross3.png")
            self.imgCS1Label = Label(image = self.imgCS1)
            self.imgCS1Button = Button(self.mainWin, image = self.imgCS1)
            self.imgCS1Button.place(x = 220, y = 300 )
            self.imgCS2 = PhotoImage(file = "cross2.png")
            self.imgCS2Label = Label(image = self.imgCS2)
            self.imgCS2Button = Button(self.mainWin, image = self.imgCS2)
            self.imgCS2Button.place(x = 373, y = 300 )
                
        elif self.choice13.get() == "L" and self.choice9.get() == 1:
            self.img2 = PhotoImage(file = "GCS.png")
            self.img2Label = Label(image = self.img2)
            self.img2Button = Button(self.mainWin, image = self.img2, command = self.do_img2_1)
            self.img2Button.place(x = 95, y = 300 )
            self.img7 = PhotoImage(file = "STB.png")
            self.img7Label = Label(image = self.img7)
            self.img7Button = Button(self.mainWin, image = self.img7, command = self.do_img2_3)
            self.img7Button.place(x = 370, y = 300 )
            self.imgCS1 = PhotoImage(file = "cross3.png")
            self.imgCS1Label = Label(image = self.imgCS1)
            self.imgCS1Button = Button(self.mainWin, image = self.imgCS1)
            self.imgCS1Button.place(x = 220, y = 300 )
                
        elif self.choice13.get() == "L" and self.choice11.get() == 1:
            self.img5 = PhotoImage(file = "FriedRice.png")
            self.img5Label = Label(image = self.img5)
            self.img5Button = Button(self.mainWin, image = self.img5, command = self.do_img2_2)
            self.img5Button.place(x = 220, y = 300 )
            self.imgCS2 = PhotoImage(file = "cross2.png")
            self.imgCS2Label = Label(image = self.imgCS2)
            self.imgCS2Button = Button(self.mainWin, image = self.imgCS2)
            self.imgCS2Button.place(x = 373, y = 300 )
            self.imgCS3 = PhotoImage(file = "cross.png")
            self.imgCS3Label = Label(image = self.imgCS3)
            self.imgCS3Button = Button(self.mainWin, image = self.imgCS3)
            self.imgCS3Button.place(x = 95, y = 300 )
                
        elif self.choice13.get() == "L" and self.choice2.get() == 1:
            self.img5 = PhotoImage(file = "FriedRice.png")
            self.img5Label = Label(image = self.img5)
            self.img5Button = Button(self.mainWin, image = self.img5, command = self.do_img2_2)
            self.img5Button.place(x = 220, y = 300 )
            self.img5L = Label(self.mainWin, text = "Fried Rice", font = ("engravers mt", 6), fg = "white", bg = "black")
            self.img5L = Label(self.mainWin, text = "Fried Rice", font = ("engravers mt", 6), fg = "white", bg = "black")
            self.imgCS2 = PhotoImage(file = "cross2.png")
            self.imgCS2Label = Label(image = self.imgCS2)
            self.imgCS2Button = Button(self.mainWin, image = self.imgCS2)
            self.imgCS2Button.place(x = 373, y = 300 )
            self.imgCS3 = PhotoImage(file = "cross.png")
            self.imgCS3Label = Label(image = self.imgCS3)
            self.imgCS3Button = Button(self.mainWin, image = self.imgCS3)
            self.imgCS3Button.place(x = 95, y = 300 )
                
        elif self.choice13.get() == "L" and self.choice5.get() == 1:
            self.img5 = PhotoImage(file = "FriedRice.png")
            self.img5Label = Label(image = self.img5)
            self.img5Button = Button(self.mainWin, image = self.img5, command = self.do_img2_2)
            self.img5Button.place(x = 220, y = 300 )
            self.img5L = Label(self.mainWin, text = "Fried Rice", font = ("engravers mt", 6), fg = "white", bg = "black")
            self.img7 = PhotoImage(file = "STB.png")
            self.img7Label = Label(image = self.img7)
            self.img7Button = Button(self.mainWin, image = self.img7, command = self.do_img2_3)
            self.img7Button.place(x = 370, y = 300 )
            self.imgCS3 = PhotoImage(file = "cross.png")
            self.imgCS3Label = Label(image = self.imgCS3)
            self.imgCS3Button = Button(self.mainWin, image = self.imgCS3)
            self.imgCS3Button.place(x = 95, y = 300 )
                
        elif self.choice13.get() == "L" and self.choice7.get() == 1:
            self.img7 = PhotoImage(file = "STB.png")
            self.img7Label = Label(image = self.img7)
            self.img7Button = Button(self.mainWin, image = self.img7, command = self.do_img2_3)
            self.img7Button.place(x = 370, y = 300 )
            self.imgCS3 = PhotoImage(file = "cross.png")
            self.imgCS3Label = Label(image = self.imgCS3)
            self.imgCS3Button = Button(self.mainWin, image = self.imgCS3)
            self.imgCS3Button.place(x = 95, y = 300 )
            self.imgCS1 = PhotoImage(file = "cross3.png")
            self.imgCS1Label = Label(image = self.imgCS1)
            self.imgCS1Button = Button(self.mainWin, image = self.imgCS1)
            self.imgCS1Button.place(x = 220, y = 300 )
                
        elif self.choice13.get() == "L" and self.choice8.get() == 1:
            self.img7 = PhotoImage(file = "STB.png")
            self.img7Label = Label(image = self.img7)
            self.img7Button = Button(self.mainWin, image = self.img7, command = self.do_img2_3)
            self.img7Button.place(x = 370, y = 300 )
            self.imgCS3 = PhotoImage(file = "cross.png")
            self.imgCS3Label = Label(image = self.imgCS3)
            self.imgCS3Button = Button(self.mainWin, image = self.imgCS3)
            self.imgCS3Button.place(x = 95, y = 300 )
            self.imgCS1 = PhotoImage(file = "cross3.png")
            self.imgCS1Label = Label(image = self.imgCS1)
            self.imgCS1Button = Button(self.mainWin, image = self.imgCS1)
            self.imgCS1Button.place(x = 220, y = 300 )
                
        elif self.choice13.get() == "L" and self.choice1.get() == 1:
            self.img7 = PhotoImage(file = "STB.png")
            self.img7Label = Label(image = self.img7)
            self.img7Button = Button(self.mainWin, image = self.img7, command = self.do_img2_3)
            self.img7Button.place(x = 370, y = 300 )
            self.imgCS3 = PhotoImage(file = "cross.png")
            self.imgCS3Label = Label(image = self.imgCS3)
            self.imgCS3Button = Button(self.mainWin, image = self.imgCS3)
            self.imgCS3Button.place(x = 95, y = 300 )
            self.imgCS1 = PhotoImage(file = "cross3.png")
            self.imgCS1Label = Label(image = self.imgCS1)
            self.imgCS1Button = Button(self.mainWin, image = self.imgCS1)
            self.imgCS1Button.place(x = 220, y = 300 )
                
        elif self.choice13.get() == "D" and self.choice8.get() == 1:
            self.img3 = PhotoImage(file = "Spaghetti.png")
            self.img3Label = Label(image = self.img3)
            self.img3Button = Button(self.mainWin, image = self.img3, command = self.do_img3_1)
            self.img3Button.place(x = 95, y = 300 )
            self.img8 = PhotoImage(file = "CC.png")
            self.img8Label = Label(image = self.img8)
            self.img8Button = Button(self.mainWin, image = self.img8, command = self.do_img3_2)
            self.img8Button.place(x = 220, y = 300 )
            self.imgCS2 = PhotoImage(file = "cross2.png")
            self.imgCS2Label = Label(image = self.imgCS2)
            self.imgCS2Button = Button(self.mainWin, image = self.imgCS2)
            self.imgCS2Button.place(x = 373, y = 300 )
                
        elif self.choice13.get() == "D" and self.choice1.get() == 1:
            self.img3 = PhotoImage(file = "Spaghetti.png")
            self.img3Label = Label(image = self.img3)
            self.img3Button = Button(self.mainWin, image = self.img3, command = self.do_img3_1)
            self.img3Button.place(x = 95, y = 300 )
            self.img9 = PhotoImage(file = "sau.png")
            self.img9Label = Label(image = self.img9)
            self.img9Button = Button(self.mainWin, image = self.img9, command = self.do_img3_3)
            self.img9Button.place(x = 370, y = 300 )
            self.imgCS1 = PhotoImage(file = "cross3.png")
            self.imgCS1Label = Label(image = self.imgCS1)
            self.imgCS1Button = Button(self.mainWin, image = self.imgCS1)
            self.imgCS1Button.place(x = 220, y = 300 )
        
        elif self.choice13.get() == "D" and self.choice3.get() == 1:
            self.img3 = PhotoImage(file = "Spaghetti.png")
            self.img3Label = Label(image = self.img3)
            self.img3Button = Button(self.mainWin, image = self.img3, command = self.do_img3_1)
            self.img3Button.place(x = 95, y = 300 )
            self.imgCS1 = PhotoImage(file = "cross3.png")
            self.imgCS1Label = Label(image = self.imgCS1)
            self.imgCS1Button = Button(self.mainWin, image = self.imgCS1)
            self.imgCS1Button.place(x = 220, y = 300 )
            self.imgCS2 = PhotoImage(file = "cross2.png")
            self.imgCS2Label = Label(image = self.imgCS2)
            self.imgCS2Button = Button(self.mainWin, image = self.imgCS2)
            self.imgCS2Button.place(x = 373, y = 300 )
                
        elif self.choice13.get() == "D" and self.choice9.get() == 1:
            self.img3 = PhotoImage(file = "Spaghetti.png")
            self.img3Label = Label(image = self.img3)
            self.img3Button = Button(self.mainWin, image = self.img3, command = self.do_img3_1)
            self.img3Button.place(x = 95, y = 300 )
            self.img8 = PhotoImage(file = "CC.png")
            self.img8Label = Label(image = self.img8)
            self.img8Button = Button(self.mainWin, image = self.img8, command = self.do_img3_2)
            self.img8Button.place(x = 220, y = 300 )
            self.imgCS2 = PhotoImage(file = "cross2.png")
            self.imgCS2Label = Label(image = self.imgCS2)
            self.imgCS2Button = Button(self.mainWin, image = self.imgCS2)
            self.imgCS2Button.place(x = 373, y = 300 )
        
        elif self.choice13.get() == "D" and self.choice5.get() == 1:
            self.img8 = PhotoImage(file = "CC.png")
            self.img8Label = Label(image = self.img8)
            self.img8Button = Button(self.mainWin, image = self.img8, command = self.do_img3_2)
            self.img8Button.place(x = 220, y = 300 )
            self.img9 = PhotoImage(file = "sau.png")
            self.img9Label = Label(image = self.img9)
            self.img9Button = Button(self.mainWin, image = self.img9, command = self.do_img3_3)
            self.img9Button.place(x = 370, y = 300 )
            self.imgCS3 = PhotoImage(file = "cross.png")
            self.imgCS3Label = Label(image = self.imgCS3)
            self.imgCS3Button = Button(self.mainWin, image = self.imgCS3)
            self.imgCS3Button.place(x = 95, y = 300 )
            
        elif self.choice13.get() == "D" and self.choice12.get() == 1:
            self.img8 = PhotoImage(file = "CC.png")
            self.img8Label = Label(image = self.img8)
            self.img8Button = Button(self.mainWin, image = self.img8, command = self.do_img3_2)
            self.img8Button.place(x = 220, y = 300 )
            self.imgCS3 = PhotoImage(file = "cross.png")
            self.imgCS3Label = Label(image = self.imgCS3)
            self.imgCS3Button = Button(self.mainWin, image = self.imgCS3)
            self.imgCS3Button.place(x = 95, y = 300 )
            self.imgCS2 = PhotoImage(file = "cross2.png")
            self.imgCS2Label = Label(image = self.imgCS2)
            self.imgCS2Button = Button(self.mainWin, image = self.imgCS2)
            self.imgCS2Button.place(x = 373, y = 300 )
        
        elif self.choice13.get() == "D" and self.choice10.get() == 1:
            self.img9 = PhotoImage(file = "sau.png")
            self.img9Label = Label(image = self.img9)
            self.img9Button = Button(self.mainWin, image = self.img9, command = self.do_img3_3)
            self.img9Button.place(x = 370, y = 300 )
            self.imgCS3 = PhotoImage(file = "cross.png")
            self.imgCS3Label = Label(image = self.imgCS3)
            self.imgCS3Button = Button(self.mainWin, image = self.imgCS3)
            self.imgCS3Button.place(x = 95, y = 300 )
            self.imgCS1 = PhotoImage(file = "cross3.png")
            self.imgCS1Label = Label(image = self.imgCS1)
            self.imgCS1Button = Button(self.mainWin, image = self.imgCS1)
            self.imgCS1Button.place(x = 220, y = 300 )
            
        elif self.choice13.get() == "D" and self.choice7.get() == 1:
            self.img9 = PhotoImage(file = "sau.png")
            self.img9Label = Label(image = self.img9)
            self.img9Button = Button(self.mainWin, image = self.img9, command = self.do_img3_3)
            self.img9Button.place(x = 370, y = 300 )
            self.imgCS3 = PhotoImage(file = "cross.png")
            self.imgCS3Label = Label(image = self.imgCS3)
            self.imgCS3Button = Button(self.mainWin, image = self.imgCS3)
            self.imgCS3Button.place(x = 95, y = 300 )
            self.imgCS1 = PhotoImage(file = "cross3.png")
            self.imgCS1Label = Label(image = self.imgCS1)
            self.imgCS1Button = Button(self.mainWin, image = self.imgCS1)
            self.imgCS1Button.place(x = 220, y = 300 )
            
        else:
            self.imgCS3 = PhotoImage(file = "cross.png")
            self.imgCS3Label = Label(image = self.imgCS3)
            self.imgCS3Button = Button(self.mainWin, image = self.imgCS3)
            self.imgCS3Button.place(x = 95, y = 300 )
            self.imgCS1 = PhotoImage(file = "cross3.png")
            self.imgCS1Label = Label(image = self.imgCS1)
            self.imgCS1Button = Button(self.mainWin, image = self.imgCS1)
            self.imgCS1Button.place(x = 220, y = 300 )
            self.imgCS2 = PhotoImage(file = "cross2.png")
            self.imgCS2Label = Label(image = self.imgCS2)
            self.imgCS2Button = Button(self.mainWin, image = self.imgCS2)
            self.imgCS2Button.place(x = 373, y = 300 )
            
                
    def do_img1_1(self):
        omelette1 = "Ingredients: \n- 2 eggs\n- 2tbsp (20mL) water\n- pinch of salt and pepper\n- Filling ingredients (cheese, tomatoes)\n\n<<STEP 1>>\nWhisk eggs, water, salt and pepper\n\n<<STEP 2>>\nHeat pan over medium heat.Pour in egg mixture. As eggs set around edge of skillet, with spatula, gently push cooked portions toward centre of skillet. Tilt and rotate skillet to allow uncooked egg to flow into empty spaces.\n\n<<STEP 3>>"
        omelette2 = "\nWhen eggs are almost set on surface but still look moist, cover half of omelette with filling. Slip spatula under unfilled side; fold over onto filled half.\n\n<<STEP 4>>\nCook for a minute then slide onto plate."
        showinfo("Omelette", omelette1 + omelette2)
    def do_img2_1(self):
        GCS = "Ingredients:\n- 4 Slices white bread\n- 3 Tabespoons of butter\n- 2 slices chedder cheese\n\n<<STEP 1>>\nPreheat skillet over medium heat.\n\n<STEP 2>>\nApply butter to one sie of a slice of bread and place it butter side down onto the skillet and add 1 slice of cheese.\n\n<<STEP 3>>\n Butter the 2nd slice and place it butter side up on top of the sandwich and grill until light brown then flip over and continue grilling till the chesse is melted."
        showinfo("Grilled Cheese Sandwich", GCS)       
    def do_img3_1(self):
        Spaghetti = "Ingredients:\n- 1lb ground Chicken\n- 3 tablesoons olive oil\n- 2 tablespoons tomato paste\n- crushed tomatoes\n- ground black pepper\n- 12 ounces spaghetti or pasta\n- half cup parmesian cheese\n\n<<STEP 1>>\nMake Sauce - Heat the oil in a large pot over medium heat. Add meat and cook till brown, then ad tomato paste and stir. Pour in water, stir in tomatoes and add black pepper and salt. Bring sauce to low simmer and cook for 25 minutes\n\n<<STEP 2>>\nCook Spaghetti - 15 minutes before the sauce finishes cooking, cook the pasta according to the package directions\n\n<<STEP 3>>\nMix sauce and pasta and leave for a minute to allow pasta to soak in sauce. Add parmesian and then Bon Appetit!"
        showinfo("Spaghetti", Spaghetti) 
    def do_img1_2(self):
        egg = "Ingredients:\n- 1 slice of bread\n- 1 egg\n- salt and black pepper\n\n<<STEP 1>>\nPut a little bit of buter on the pan\n\n<<STEP 2>>\nCut 1 and a half to 2-inch hole in the middle of the bread slice and lay it on the pan\n\n<<STEP 3>>\nWhen side facing down is lightly toasted (about 2 minutes), flip and crack the egg into the hole. Season it with salt and pepper\n\n<<STEP 4>>\nContinue to cook until the egg is cooked and mostly firm. Flip again and cook for 1 minute to assure both sides are cooked."
        showinfo("Egg in a Hole", egg)
    def do_img2_2(self):
        rice = "Ingredients:\n- Cold rice\n- Butter\n- Veggies\n- eggs\n- Soy Sauce\n\n<<STEP 1>>\nScramble your eggs - A little bit of butter on the pan, scramble your eggs and set aside\n\n<<STEP 2>>\nCook Veggies and the turn burner to high heat and stir in rice with soy sauce. Mix everything and stir every 15-20 seconds for 3 minutes until rice and veggies start to brown slightly.\n\n<<STEP 3>>\nRemove from heat and add scrambled eggs and dish up."
        showinfo("Fried Rice", rice)
    def do_img1_3(self):
        french = "Ingredients:\n- 1 eggs beaten\n- 2 slices of bread\n- 2 slices of bacon\n- 1 egg\n\n<<STEP 1>>\nDip bread slices in beaten eggs.Heat a lightly oiled griddle or frying pan over medium high heat. Cook until browned on both sides. Set aside but keep warm.\n\n<<STEP 2>>\nPlace bacon in a large, deep skillet. Cook over medium high heat until evenly brown. Drain and set aside and fry remaining two eggs\n\n<<STEP 3>>\nPlace one piece of French toast on a plate. Place the fried eggs on top of the bread, top the eggs with strips of bacon. Cover with the remaining piece of French toast."
        showinfo("French Egg and Bacon Sandwich", french)
    def do_img2_3(self):
        STB = "Ingredients:\n- 6 Bell Peppers\n- 4 Tablespoons olive oil\n- 8 ounces ground chicken\n- Salt and black pepper\n- 4 finely diced Tomatoes\n- 1 cup Rice\n- 1 and a half cups Grated cheese\n\n<<STEP 1>>\nPreheat the oven to 350 degrees F\n\n<<STEP 2>>\nCut the tops off the peppers. Remove and discard the stems, then finely chop the tops; set aside. Scoop out the seeds. Place the peppers cut-side up in a baking dish just large enough to hold them upright.\n\n<<STEP 3>>\nHeat 2 tablespoons of the olive oil in a large skillet over medium-high heat. Add the chicken, season with salt and pepper and cook, breaking up the lumps, until the meat is cooked through and just beginning to brown, 8 to 10 minutes. Remove to a paper towel-lined plate to get rid of the fat.\n\n<<STEP 4>>\nAdd the remaining 2 Tablespoons of olive oil. Add the tomatoes and season with salt. Cook until everything is heated and then stir in the chicken, rice and 1 cup cheese\n\n<<STEP 5>>\nFill in the peppers with the mixture and top each with the remaining half cup of cheese. Pour small amount of water into baking dish and drizzle peppers with olive oil. Cover with foil and bake for 30 minutes. Uncover and bake until peppers are soft and cheese is melted and lightly brown for another 15-20 minutes."
        showinfo("Stuffed Bell Peppers", STB)
    def do_img3_2(self):
        CC = "Ingredients:\n- Half cup cheese\n- Chicken breast\n- cooked rice\n- broccoli\n\n<<STEP 1>>\nAdd seasoned chicken breast to olive oiled pan\n\n<<STEP 2>>\nSaute rice with olive oil and then add chicken broth when rice is toasting\n\n<<STEP 3>>\nAfter rice has been cooking for a while, add broccoli and let steam\n\n<<STEP 4>>\nWhen all the liquid has been absorbed by the rice, stir in the cheese and sprinkle some on top."
        showinfo("One-pan cheesy chicken, broccoli, and rice", CC)
    def do_img3_3(self):
        sau = "Ingredients:\n- Sausages\n- Bell peppers\n- salt and black pepper\n- Brown rice\n- Tomatoes\n\n<<STEP 1>>\nBrown the sausage slices in a large nonstick skillet, then remove to a plate. Sauté the peppers.\n\n<<STEP 2>>\nAdd the rice, salt and clack pepper. Cook until fragrant, then pour in the broth and tomatoes. Bring to a boil and stir, then cover and let simmer.\n\n<<STEP 3>>\nAdd the cooked sausage and remove from the heat. Let stand with the lid on for a few minutes, until the rice is tender. ENJOY!"
        showinfo("Sausage and rice casserole", sau)
    def do_OK2(self):
        self.recL = Label(self.mainWin, text = "Thank you! We will try to include it in our next update!", font = ("calibri", 6), bg = "white", fg = "black")
        self.recL.place(x = 350, y = 473)
    def do_OK2add(self):
        self.entry.delete(0, 'end')
        
my_gui = MyGui()



























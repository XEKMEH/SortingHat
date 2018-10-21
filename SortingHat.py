import tkinter as tk  # import Tkinter for GUI and ttk for nicer button layout
from tkinter import *
from tkinter import ttk
import  sys
import os

LARGE_FONT = ("Verdana", 16) # constant of our large font, constant size and font family
HEADER_FONT = ("Courier New", 24)

# -------------------------------------------Main Class-----------------------------------------------------------------

class HPQ(tk.Tk):  # Create class that inherits tk which allows for use of methods like tkraise()
    gryffindorCounter = 0
    ravenclawCounter = 0
    hufflepuffCounter = 0
    slytherinCounter = 0

    def __init__(self, *args, **kwargs):  # Create method __init__ that run when you call the class, self is a parameter, args allows passing of any variables, kwargs are keyword arguments
        tk.Tk.__init__(self, *args, **kwargs)  # Initialize Tkinter, args and kwargs - can pass different variables

        tk.Tk.wm_title(self,"Harry Potter Sorting Hat")  # changes title at top of window

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        # create container for all of the frames

        self.frames = {}

        for F in (MainMenu, History, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, EndPage):  # for loop to bring frames to top
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainMenu) #This starts up the MainMenu

    def show_frameHIS(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def show_frameG(self, cont):  # methods used to increment and also raise frame
        HPQ.gryffindorCounter += 1 #Gryffindor counter
        frame = self.frames[cont]
        frame.tkraise()  #raises frame to next one

    def show_frameR(self, cont):  # Ravenclaw counter
        HPQ.ravenclawCounter += 1
        frame = self.frames[cont]
        frame.tkraise()

    def show_frameH(self, cont):  # Hufflepuff counter
        HPQ.hufflepuffCounter += 1
        frame = self.frames[cont]
        frame.tkraise()

    def show_frameS(self, cont):  # Slytherin counter
        HPQ.slytherinCounter += 1
        frame = self.frames[cont]
        frame.tkraise()

    def show_frame(self, cont):  # this raises the frame to the front by passing self and controller
        frame = self.frames[cont]
        frame.tkraise()

    def show_frameEND(self, cont):  # Resets all values for house counters to 0
        HPQ.gryffindorCounter = 0
        HPQ.slytherinCounter = 0
        HPQ.hufflePuffCounter = 0
        HPQ.ravenClawCounter = 0
        frame = self.frames[cont]
        frame.tkraise()

# ----------------------------------------------Main Menu---------------------------------------------------------------

class MainMenu(tk.Frame): # inherit from frame
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Harry Potter Sorting Hat Quiz", font=HEADER_FONT) # taken class tk.Label and created object "label"
        label.pack(pady=20, padx=5) # leaves padding on outside edges to window

        ttk.Style().configure("MM.TButton", width=15)
        ttk.Style().configure("LG.TButton", width=20)


        startButton = ttk.Button(self, text="Start Quiz", style="MM.TButton", command= lambda: controller.show_frame(Q1)) # start button sending to questions 1
        startButton.pack()                                                                            #Lambda only way I could get correct command

        histButton = ttk.Button(self, text='History', style="MM.TButton", command=lambda: controller.show_frame(History)) # history button that shows sorting hat history
        histButton.pack()

        exitButton = ttk.Button(self, text="Exit", command=controller.quit) # exit button ends code
        exitButton.pack(pady=25)

        self.title_photo = PhotoImage(file="pottertitle.gif")
        self.Artwork = Label(self, image=self.title_photo)
        self.Artwork.title_photo = self.title_photo
        self.Artwork.pack()


class History(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.hat_photo = PhotoImage(file="harry_hat.gif")
        self.Artwork = Label(self, image=self.hat_photo)
        self.Artwork.hat_photo = self.hat_photo
        self.Artwork.pack()
        label = tk.Label(self, text='Legend has it that the Sorting Hat was sewn roughly one thousand years ago and began as a normal hat belonging to\n '
                                         'Godric Gryffindor. When Gryffindor, along with Salazar Slytherin, Rowena Ravenclaw and Helga Hufflepuff, wondered how\n'
                                         'they would continue to sort the students when the four were dead, Gryffindor pulled his hat from his head and, along\n '
                                         'with the other founders, enchanted it with their combined intelligence. All four founders wanted to ensure that students\n'
                                         'would be sorted into their eponymous houses, which would be selected according to each founders particular preferences\n '
                                         'in students.', font=LARGE_FONT)
        label.pack(pady=10, padx=5)

        homeButton = ttk.Button(self, text="Back to Home", style="MM.TButton", command=lambda: controller.show_frameEND(MainMenu))
        homeButton.pack(pady=10)

# -----------------------------------------Twelve Questions-------------------------------------------------------------


class Q1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='You will now take a seat in front of all the other wizards at Hogwarts School of Witchcraft and Wizardry and answer 12 simple questions about\n'
                                    'yourself to find out where you will be placed. Good Luck Young Wizard!\n'
                                    'Choose your favorite color: ', font=LARGE_FONT)
        label.pack(pady=10, padx=5)

        button1 = ttk.Button(self, text='Red', style="LG.TButton", command=lambda: controller.show_frameG(Q2)) # lambda is a throwaway function but can't get to work without
        button1.pack()                                                                     # if the user clicks on red then it goes to the gryffindor frame and adds 1

        button2 = ttk.Button(self, text='Blue', style="LG.TButton", command=lambda: controller.show_frameR(Q2))# if the user clicks on red then it goes to the ravenclaw frame and adds 1
        button2.pack()

        button3 = ttk.Button(self, text='Yellow', style="LG.TButton", command=lambda: controller.show_frameH(Q2))# if the user clicks on red then it goes to the hufflepuff frame and adds 1
        button3.pack()

        button4 = ttk.Button(self, text='Green', style="LG.TButton", command=lambda: controller.show_frameS(Q2))# if the user clicks on red then it goes to the slytherin frame and adds 1
        button4.pack()

        homeButton = ttk.Button(self, text="Back to Home", style="MM.TButton", command=lambda: controller.show_frameEND(MainMenu)) # sends  to main menu
        homeButton.pack(pady=10)

        #each class questions 1-12 is basically the same except the questions and answers so I will not comment each one

class Q2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Which Spiritual animal most relates to you? ', font=LARGE_FONT)
        label.pack(pady=10, padx=5)

        button1 = ttk.Button(self, text='Snake', style="LG.TButton", command= lambda: controller.show_frameS(Q3))
        button1.pack()

        button2 = ttk.Button(self, text='Lion', style="LG.TButton", command=lambda: controller.show_frameG(Q3))
        button2.pack()

        button3 = ttk.Button(self, text='Eagle', style="LG.TButton", command=lambda: controller.show_frameR(Q3))
        button3.pack()

        button4 = ttk.Button(self, text='Badger', style="LG.TButton", command=lambda: controller.show_frameH(Q3))
        button4.pack()

        homeButton = ttk.Button(self, text="Back to Home", style="MM.TButton", command=lambda: controller.show_frameEND(MainMenu))
        homeButton.pack(pady=10)

class Q3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='What characteristic best describes you? ', font=LARGE_FONT)
        label.pack(pady=10, padx=5)

        button1 = ttk.Button(self, text='Cunning', style="LG.TButton", command= lambda: controller.show_frameS(Q4))
        button1.pack()

        button2 = ttk.Button(self, text='Brave', style="LG.TButton", command=lambda: controller.show_frameG(Q4))
        button2.pack()

        button3 = ttk.Button(self, text='Wise', style="LG.TButton", command=lambda: controller.show_frameR(Q4))
        button3.pack()

        button4 = ttk.Button(self, text='Loyal', style="LG.TButton", command=lambda: controller.show_frameH(Q4))
        button4.pack()

        homeButton = ttk.Button(self, text="Back to Home", style="MM.TButton", command=lambda: controller.show_frameEND(MainMenu))
        homeButton.pack(pady=10)

class Q4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Which of these 4 states of matter do you find most interesting? ', font=LARGE_FONT)
        label.pack(pady=10, padx=5)

        button1 = ttk.Button(self, text='Gas', style="LG.TButton", command= lambda: controller.show_frameR(Q5))
        button1.pack()

        button2 = ttk.Button(self, text='Solid', style="LG.TButton", command=lambda: controller.show_frameH(Q5))
        button2.pack()

        button3 = ttk.Button(self, text='Liquid', style="LG.TButton", command=lambda: controller.show_frameS(Q5))
        button3.pack()

        button4 = ttk.Button(self, text='Plasma', style="LG.TButton", command=lambda: controller.show_frameG(Q5))
        button4.pack()

        homeButton = ttk.Button(self, text="Back to Home", style="MM.TButton", command=lambda: controller.show_frameEND(MainMenu))
        homeButton.pack(pady=10)

class Q5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Of the classic elements which appeals to you the most? ', font=LARGE_FONT)
        label.pack(pady=10, padx=5)

        button1 = ttk.Button(self, text='Fire', style="LG.TButton", command= lambda: controller.show_frameG(Q6))
        button1.pack()

        button2 = ttk.Button(self, text='Earth', style="LG.TButton", command=lambda: controller.show_frameH(Q6))
        button2.pack()

        button3 = ttk.Button(self, text='Air', style="LG.TButton", command=lambda: controller.show_frameR(Q6))
        button3.pack()

        button4 = ttk.Button(self, text='Water', style="LG.TButton", command=lambda: controller.show_frameS(Q6))
        button4.pack()

        homeButton = ttk.Button(self, text="Back to Home", style="MM.TButton", command=lambda: controller.show_frameEND(MainMenu))
        homeButton.pack(pady=10)

class Q6(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Out of these, what would your patronus be? ', font=LARGE_FONT)
        label.pack(pady=10, padx=5)

        button1 = ttk.Button(self, text='Phoenix', style="LG.TButton", command= lambda: controller.show_frameG(Q7))
        button1.pack()

        button2 = ttk.Button(self, text='Swan', style="LG.TButton", command=lambda: controller.show_frameR(Q7))
        button2.pack()

        button3 = ttk.Button(self, text='Rattlesnake', style="LG.TButton", command=lambda: controller.show_frameS(Q7))
        button3.pack()

        button4 = ttk.Button(self, text='Owl', style="LG.TButton", command=lambda: controller.show_frameH(Q7))
        button4.pack()

        homeButton = ttk.Button(self, text="Back to Home", style="MM.TButton", command=lambda: controller.show_frameEND(MainMenu))
        homeButton.pack(pady=10)

class Q7(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Where would you most likely be found daily in a castle? ', font=LARGE_FONT)
        label.pack(pady=10, padx=5)

        button1 = ttk.Button(self, text='The Forbidden Forest', style="LG.TButton", command= lambda: controller.show_frameS(Q8))
        button1.pack()

        button2 = ttk.Button(self, text='The Great Hall', style="LG.TButton", command=lambda: controller.show_frameH(Q8))
        button2.pack()

        button3 = ttk.Button(self, text='The Library', style="LG.TButton", command=lambda: controller.show_frameR(Q8))
        button3.pack()

        button4 = ttk.Button(self, text='Hagrids Hut', style="LG.TButton", command=lambda: controller.show_frameG(Q8))
        button4.pack()

        homeButton = ttk.Button(self, text="Back to Home", style="MM.TButton", command=lambda: controller.show_frameEND(MainMenu))
        homeButton.pack(pady=10)

class Q8(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='What is your favorite Diagon Alley store? ', font=LARGE_FONT)
        label.pack(pady=10, padx=5)

        button1 = ttk.Button(self, text='The Leaky Cauldon', style="LG.TButton", command= lambda: controller.show_frameH(Q9))
        button1.pack()

        button2 = ttk.Button(self, text='Florish and Blotts Bookstore', style="LG.TButton", command=lambda: controller.show_frameR(Q9))
        button2.pack()

        button3 = ttk.Button(self, text='Borgin and Burkes', style="LG.TButton", command=lambda: controller.show_frameS(Q9))
        button3.pack()

        button4 = ttk.Button(self, text='Quality Quidditch Supplies', style="LG.TButton", command=lambda: controller.show_frameG(Q9))
        button4.pack()

        homeButton = ttk.Button(self, text="Back to Home", style="MM.TButton", command=lambda: controller.show_frameEND(MainMenu))
        homeButton.pack(pady=10)

class Q9(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='What is your choice of Transportation? ', font=LARGE_FONT)
        label.pack(pady=10, padx=5)

        button1 = ttk.Button(self, text='Broomstick', style="LG.TButton", command= lambda: controller.show_frameG(Q10))
        button1.pack()

        button2 = ttk.Button(self, text='The Hogwarts Express', style="LG.TButton", command=lambda: controller.show_frameR(Q10))
        button2.pack()

        button3 = ttk.Button(self, text='Apparition', style="LG.TButton", command=lambda: controller.show_frameH(Q10))
        button3.pack()

        button4 = ttk.Button(self, text='The Hogwarts Boats', style="LG.TButton", command=lambda: controller.show_frameS(Q10))
        button4.pack()

        homeButton = ttk.Button(self, text="Back to Home", style="MM.TButton", command=lambda: controller.show_frameEND(MainMenu))
        homeButton.pack(pady=10)

class Q10(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='How do you deal with difficult situations? ', font=LARGE_FONT)
        label.pack(pady=10, padx=5)

        button1 = ttk.Button(self, text='Face it without hesitation', style="LG.TButton", command= lambda: controller.show_frameG(Q11))
        button1.pack()

        button2 = ttk.Button(self, text='Beat the system', style="LG.TButton", command=lambda: controller.show_frameS(Q11))
        button2.pack()

        button3 = ttk.Button(self, text='Study & analyze all aspects', style="LG.TButton", command=lambda: controller.show_frameR(Q11))
        button3.pack()

        button4 = ttk.Button(self, text='Just wing it dude', style="LG.TButton", command=lambda: controller.show_frameH(Q11))
        button4.pack()

        homeButton = ttk.Button(self, text="Back to Home", style="MM.TButton", command=lambda: controller.show_frameEND(MainMenu))
        homeButton.pack(pady=10)

class Q11(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Who is your favorite house ghost? ', font=LARGE_FONT)
        label.pack(pady=10, padx=5)

        button1 = ttk.Button(self, text='Nearly headless Nick', style="LG.TButton", command= lambda: controller.show_frameG(Q12))
        button1.pack()

        button2 = ttk.Button(self, text='Fat Friar', style="LG.TButton", command=lambda: controller.show_frameH(Q12))
        button2.pack()

        button3 = ttk.Button(self, text='Grey Lady', style="LG.TButton", command=lambda: controller.show_frameR(Q12))
        button3.pack()

        button4 = ttk.Button(self, text='Bloody Baron', style="LG.TButton", command=lambda: controller.show_frameS(Q12))
        button4.pack()

        homeButton = ttk.Button(self, text="Back to Home", style="MM.TButton", command=lambda: controller.show_frameEND(MainMenu))
        homeButton.pack(pady=10)

class Q12(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Which famous witch or wizard relates to you most? ', font=LARGE_FONT)
        label.pack(pady=10, padx=5)

        button1 = ttk.Button(self, text='Minerva McGonagall', style="LG.TButton", command= lambda: controller.show_frameG(EndPage))
        button1.pack()

        button2 = ttk.Button(self, text='Gilderoy Lockheart', style="LG.TButton", command=lambda: controller.show_frameR(EndPage))
        button2.pack()

        button3 = ttk.Button(self, text='Horace Slughorn', style="LG.TButton", command=lambda: controller.show_frameS(EndPage))
        button3.pack()

        button4 = ttk.Button(self, text='Pomona Sprout', style="LG.TButton", command=lambda: controller.show_frameH(EndPage))
        button4.pack()

        homeButton = ttk.Button(self, text="Back to Home", style="MM.TButton", command=lambda: controller.show_frameEND(MainMenu))
        homeButton.pack(pady=10)

class EndPage(tk.Frame): #Results Page
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Hmmmmmm....I think you would do best in......', font=LARGE_FONT)
        label.pack(pady=10, padx=5)

        houseLabel= tk.Label(self, text="", font=LARGE_FONT) #Spacing for suspenseful effect
        houseLabel.pack()

        resultsButton = ttk.Button(self, text="Results", style="MM.TButton", command=self.countWinner)
        resultsButton.pack()

        homeButton = ttk.Button(self, text="Back to Home", style="MM.TButton", command=lambda: controller.show_frameEND(MainMenu))
        homeButton.pack()

        exitButton = ttk.Button(self, text="Exit", command=controller.quit)
        exitButton.pack(pady=10)

    def countWinner(self):
        # if the gryffindor counter is greater than all of the others, it prints gryffindor
        if HPQ.gryffindorCounter > HPQ.slytherinCounter and HPQ.gryffindorCounter > HPQ.hufflepuffCounter and HPQ.gryffindorCounter > HPQ.ravenclawCounter:
            self.gryffindor_photo = PhotoImage(file="gryffindor.gif")
            self.Artwork = Label(self, image=self.gryffindor_photo)
            self.Artwork.gryffindor_photo = self.gryffindor_photo
            self.Artwork.pack()
            winner = tk.Label(self, text= 'GRYFFINDOR!!!\n'
                                    'You might belong in Gryffindor,\n'
                                    'Where dwell the brave at heart,\n'
                                    'Their daring, nerve, and chivalry\n'
                                    'Set Gryffindors apart', font=HEADER_FONT, fg = 'red')
            winner.pack(pady=0, padx=0)

        # if the ravenclaw counter is greater than all of the others, it prints ravenclaw
        elif HPQ.ravenclawCounter > HPQ.gryffindorCounter and HPQ.ravenclawCounter > HPQ.slytherinCounter and HPQ.ravenclawCounter > HPQ.hufflepuffCounter:
            self.ravenclaw_photo = PhotoImage(file="ravenclaw.gif")
            self.Artwork = Label(self, image=self.ravenclaw_photo)
            self.Artwork.ravenclaw_photo = self.ravenclaw_photo
            self.Artwork.pack()
            winner = tk.Label(self, text='RAVENCLAW!!!\n'
                                   'Or yet in wise old Ravenclaw,\n'
                                   'If you have ve a ready mind,\n'
                                   'Where those of wit and learning,\n'
                                   'Will always find their kind', font=HEADER_FONT, fg = 'purple')
            winner.pack(pady=0, padx=0)

        # if the hufflepuff counter is greater than all of the others, it prints hufflepuff
        elif HPQ.hufflepuffCounter > HPQ.gryffindorCounter and HPQ.hufflepuffCounter > HPQ.ravenclawCounter and HPQ.hufflepuffCounter > HPQ.slytherinCounter:
            self.hufflepuff_photo = PhotoImage(file="hufflepuff.gif")
            self.Artwork = Label(self, image=self.hufflepuff_photo)
            self.Artwork.hufflepuff_photo = self.hufflepuff_photo
            self.Artwork.pack()
            winner = tk.Label(self, text='HUFFLEPUFF!!!\n'
                                   'You might belong in Hufflepuff,\n'
                                   'Where they are just and loyal,\n'
                                   'Those patient Hufflepuffs are true,\n'
                                   'And unafraid of toil', font=HEADER_FONT, fg = '#255255000')
            winner.pack(pady=0, padx=0)
            winner.pack()

        # if the slytherin counter is greater than all of the others, it prints slytherin
        elif HPQ.slytherinCounter > HPQ.gryffindorCounter and HPQ.slytherinCounter > HPQ.hufflepuffCounter and HPQ.slytherinCounter > HPQ.ravenclawCounter:
            self.slytherin_photo = PhotoImage(file="slytherin.gif")
            self.Artwork = Label(self, image=self.slytherin_photo)
            self.Artwork.slytherin_photo = self.slytherin_photo
            self.Artwork.pack()
            winner = tk.Label(self, text='SLYTHERIN!!!\n'
                                   'Or perhaps in Slytherin,\n'
                                   'You will make your real friends,\n'
                                   'Those cunning folk use any means,\n'
                                   'To achieve their ends', font=HEADER_FONT, fg = 'green')
            winner.pack(pady=0, padx=0)

        elif HPQ.gryffindorCounter == HPQ.slytherinCounter or HPQ.gryffindorCounter == HPQ.hufflepuffCounter or HPQ.gryffindorCounter == HPQ.ravenclawCounter:
            self.ron_photo = PhotoImage(file="ronweasley.gif")
            self.Artwork = Label(self, image=self.ron_photo)
            self.Artwork.ron_photo = self.ron_photo
            self.Artwork.pack()
            winner = tk.Label(self, text='Sorry but you must have been lying\n' 
                                    'when answering because you are too\n'
                                    'similar between different houses. TRY AGAIN!', font = HEADER_FONT)

            winner.pack(pady=0, padx=0)

        elif HPQ.slytherinCounter == HPQ.hufflepuffCounter or HPQ.slytherinCounter == HPQ.ravenclawCounter:
            self.ron_photo = PhotoImage(file="ronweasley.gif")
            self.Artwork = Label(self, image=self.ron_photo)
            self.Artwork.ron_photo = self.ron_photo
            self.Artwork.pack()
            winner = tk.Label(self, text='Sorry but you must have been lying\n'
                                   'when answering because you are too\n'
                                   'similar between different houses. TRY AGAIN!', font=HEADER_FONT)

            winner.pack(pady=0, padx=0)

        elif HPQ.hufflepuffCounter == HPQ.ravenclawCounter:
            self.ron_photo = PhotoImage(file="ronweasley.gif")
            self.Artwork = Label(self, image=self.ron_photo)
            self.Artwork.ron_photo = self.ron_photo
            self.Artwork.pack()
            winner = tk.Label(self, text='You are too similar between houses.\n'
                                   'The sorting hat could not decide where to place you\n'
                                   'TRY AGAIN!', font=HEADER_FONT)

            winner.pack(pady=0, padx=0)

app = HPQ() # assigning the class to app
app.geometry('1500x1000')
app.title('Sorting Hat Game')
app.mainloop() #run code
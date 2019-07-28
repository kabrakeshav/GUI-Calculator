'''
 @author : Keshav Kabra
'''
from tkinter import *
from math import *
import re

# --------------------------------- Class Calculator --------------------------------------- #
class Calculator():
    def __init__(self, root): # constructor function
        self.total = 0
        self.answ = 0   #variable for ANS BUTTON
        self.scr_text = ""
        # --------------------------- Entry Widget ----------------------------------------- #
        f1 = Frame(root)
        self.screen = Entry(f1, bg="peach puff", font="Times 30 bold", bd=13,
                       justify=RIGHT, width=41)
        self.screen.grid(row=0, column=0, pady=(16,16), columnspan=500)

        # -------------------------------- Buttons : Standard ------------------------------ #
        number = "789456123"
        i = 0
        b = []
        for j in range(1, 4):
            for k in range(3):
                b.append(Button(f1, bg="light coral", fg="black", text=number[i],
                                font="Times 24 bold", width=4, bd=5))
                b[i].grid(row=j, column=k, pady=1)
                b[i]["command"] = lambda x=number[i]: self.action(x)
                i += 1

        btn_Zero = Button(f1, bg="light coral", fg="black", text="0", font="Times 24 bold", width=4,
                          bd=5,command=lambda : self.action(0)).grid(row=4, column=0)
        btn_Dot = Button(f1, bg="light coral", fg="black", text=".", font="Times 24 bold", width=4,
                         bd=5, command=lambda : self.action(".")).grid(row=4, column=1)
        btn_Ans = Button(f1, bg="royal blue", fg="black", text="ANS", font="Times 24 bold",
                         width=4, bd=5, command=self.ans).grid(row=5, column=1)
        btn_Equal = Button(f1, bg="red3", fg="black", text="=", font="Times 24 bold",
                           width=4, bd=5, command=self.equal).grid(row=5, column=3)

        btn_AC = Button(f1, bg="yellow", fg="black", text="AC", font="Times 24 bold",
                        width=4, bd=5, command=self.all_clear).grid(row=5, column=0)
        btn_backspace = Button(f1, bg="royal blue", fg="black", text="⌫", font="Times 24 bold",
                               width=4, bd=5, command=self.back_space).grid(row=5, column=2)
        btn_Add = Button(f1, bg="powder blue", fg="brown", text="+", font="Times 24 bold", width=4,
                         bd=5, command=lambda : self.action("+")).grid(row=1, column=3)
        btn_Sub = Button(f1, bg="powder blue", fg="brown", text="-", font="Times 24 bold", width=4,
                         bd=5, command=lambda : self.action("-")).grid(row=2, column=3)
        btn_Mul = Button(f1, bg="powder blue", fg="brown", text="*", font="Times 24 bold", width=4,
                         bd=5, command=lambda : self.action("*")).grid(row=3, column=3)
        btn_Div = Button(f1, bg="powder blue", fg="brown", text="/", font="Times 24 bold", width=4,
                         bd=5, command=lambda : self.action("/")).grid(row=4, column=3)
        btn_mod = Button(f1, bg="powder blue", fg="brown", text="%", font="Times 24 bold", width=4,
                         bd=5, command=lambda: self.action("%")).grid(row=4, column=2)

        f1.pack()
        # ------------------------------------------------------------------------------------- #
        # ------------------------------------- Gap ------------------------------------------- #
        can = Canvas(f1, width=20, height=-100)
        can.grid(row=0, column=5)
        # ------------------------------------------------------------------------------------- #
        # --------------------------------- Scientific Buttons -------------------------------- #

        btn_square = Button(f1, bg="burlywood1", fg="black", text="SQR", font="Times 24 bold",
                            width=4, bd=5, command=self.square).grid(row=1, column=12)
        btn_cube = Button(f1, bg="burlywood1", fg="black", text="CUBE", font="Times 24 bold",
                          width=4, bd=5, command=self.cube).grid(row=2, column=12)
        btn_inverse = Button(f1, bg="burlywood1", fg="black", text="INV", font="Times 24 bold",
                             width=4, bd=5, command=self.inverse).grid(row=3, column=12)
        btn_Root = Button(f1, bg="burlywood1", fg="black", text="√", font="Times 24 bold",
                          width=4, bd=5, command=self.sqr_root).grid(row=4, column=12)
        btn_brac_open = Button(f1, bg="dark seagreen3", fg="black", text="(", font="Times 24 bold",
                               width=4, bd=5, command=lambda: self.action("(")).grid(row=5, column=12)

        btn_pow = Button(f1, bg="burlywood1", fg="black", text="pow", font="Times 24 bold",
                         width=4, bd=5, command=lambda: self.action("pow(")).grid(row=1, column=13)
        btn_ln = Button(f1, bg="lavender", fg="black", text="ln", font="Times 24 bold",
                        width=4, bd=5, command=lambda: self.action("log(")).grid(row=2, column=13)
        btn_log2 = Button(f1, bg="lavender", fg="black", text="log2", font="Times 24 bold",
                          width=4, bd=5, command=lambda: self.action("log2(")).grid(row=3, column=13)
        btn_log10 = Button(f1, bg="lavender", fg="black", text="log10", font="Times 24 bold",
                           width=4, bd=5, command=lambda: self.action("log10(")).grid(row=4, column=13)
        btn_brac_close = Button(f1, bg="dark seagreen3", fg="black", text=")", font="Times 24 bold",
                                width=4, bd=5, command=lambda: self.action(")")).grid(row=5, column=13)

        btn_sin = Button(f1, bg="ivory3", fg="black", text="sin", font="Times 24 bold",
                         width=4, bd=5, command=lambda: self.action("sin(")).grid(row=1, column=14)
        btn_cos = Button(f1, bg="ivory3", fg="black", text="cos", font="Times 24 bold",
                         width=4, bd=5, command=lambda: self.action("cos(")).grid(row=2, column=14)
        btn_tan = Button(f1, bg="ivory3", fg="black", text="tan", font="Times 24 bold",
                         width=4, bd=5, command=lambda: self.action("tan(")).grid(row=3, column=14)
        btn_pi = Button(f1, bg="firebrick1", fg="black", text="π", font="Times 24 bold",
                        width=4, bd=5, command=lambda: self.action("pi")).grid(row=4, column=14)
        btn_degree = Button(f1, bg="plum", fg="black", text="deg", font="Times 24 bold",
                            width=4, bd=5, command=lambda: self.action("degrees(")).grid(row=5, column=14)

        btn_sininv = Button(f1, bg="ivory3", fg="black", text="sinI", font="Times 24 bold",
                            width=4, bd=5, command=lambda: self.action("asin(")).grid(row=1, column=15)
        btn_cosinv = Button(f1, bg="ivory3", fg="black", text="cosI", font="Times 24 bold",
                            width=4, bd=5, command=lambda: self.action("acos(")).grid(row=2, column=15)
        btn_taninv = Button(f1, bg="ivory3", fg="black", text="tanI", font="Times 24 bold",
                            width=4, bd=5, command=lambda: self.action("atan(")).grid(row=3, column=15)
        btn_E = Button(f1, bg="firebrick1", fg="black", text="e", font="Times 24 bold",
                       width=4, bd=5, command=lambda: self.action("e")).grid(row=4, column=15)
        btn_radian = Button(f1, bg="plum", fg="black", text="rad", font="Times 24 bold",
                            width=4, bd=5, command=lambda: self.action("radians(")).grid(row=5, column=15)

        btn_facto = Button(f1, bg="khaki3", fg="black", text="!", font="Times 24 bold",
                           width=4, bd=5, command=self.facto).grid(row=1, column=16)
        btn_comma = Button(f1, bg="navajowhite2", fg="black", text=",", font="Times 24 bold",
                            width=4, bd=5, command=lambda : self.action(",")).grid(row=2, column=16)
        btn_permute = Button(f1, bg="orange2", fg="black", text="P(", font="Times 24 bold",
                            width=4, bd=5, command=lambda: self.action("P(")).grid(row=3, column=16)
        btn_combi = Button(f1, bg="orange2", fg="black", text="C(", font="Times 24 bold",
                       width=4, bd=5, command=lambda: self.action("C(")).grid(row=4, column=16)
        btn_res4 = Button(f1, bg="pink1", fg="black", text="res", font="Times 24 bold",
                            width=4, bd=5).grid(row=5, column=16)

        # --------------------------------------------------------------------------------------- #

    # ------------------------------------ Driver Functions ------------------------------------- #

    def action(self, arg):
        self.screen.insert(END, arg)

    def ans(self):
        self.answ = self.total
        #self.screen.delete(0, END)
        self.screen.insert(END, "ANS")

    def all_clear(self):
        self.screen.delete(0, END)

    def equal(self):
        try:
            self.scr_text = self.screen.get()
            self.scr_text = self.scr_text.replace("ANS", str(self.answ))

            # for permutation
            if self.scr_text[0] =='P':
                self.permute()
                return
            # for combination
            if self.scr_text[0] =='C':
                self.combi()
                return

            self.total = float(eval(self.scr_text))
            self.screen.delete(0, END)
            self.screen.insert(END, self.total)
        except:
            self.screen.delete(0, END)
            self.total = "Invalid Operation"
            self.screen.insert(0, "Invalid Operation")
        with open("Output.txt", "a+") as f:
            f.write(self.scr_text + " = " + str(self.total) + "\n")

    def back_space(self):
        self.scr_text = self.screen.get()[:-1]
        self.screen.delete(0, END)
        self.action(self.scr_text)

    def sqr_root(self):
        try:
            self.total = sqrt(float(self.screen.get()))
            self.screen.delete(0, END)
            self.screen.insert(END, self.total)
        except:
            self.screen.delete(0, END)
            self.total = "Invalid Operation"
            self.screen.insert(0, "Invalid Operation")
        with open("Output.txt", "a+") as f:
            f.write("√" + self.scr_text + " = " + str(self.total) + "\n")

    def square(self):
        self.scr_text = self.screen.get()
        self.scr_text = self.scr_text.replace("ANS", str(self.answ))
        self.total = pow(float(self.scr_text), 2)
        self.screen.delete(0, END)
        self.screen.insert(END, self.total)
        with open("Output.txt", "a+") as f:
            f.write(self.scr_text + "^2 = " + str(self.total) + "\n")

    def cube(self):
        self.scr_text = self.screen.get()
        self.scr_text = self.scr_text.replace("ANS", str(self.answ))
        self.total = pow(float(self.scr_text), 3)
        self.screen.delete(0, END)
        self.screen.insert(END, self.total)
        with open("Output.txt", "a+") as f:
            f.write(self.scr_text + "^3 = " + str(self.total) + "\n")

    def inverse(self):
        try:
            self.scr_text = self.screen.get()
            self.scr_text = self.scr_text.replace("ANS", str(self.answ))
            self.total = 1/float(self.scr_text)
            self.screen.delete(0, END)
            self.screen.insert(END, self.total)
        except:
            self.screen.delete(0, END)
            self.total = "Invalid Operation"
            self.screen.insert(0, "Invalid Operation")
        with open("Output.txt", "a+") as f:
            f.write("1/" + self.scr_text + " = " + str(self.total) + "\n")

    def facto(self):
        try:
            self.scr_text = self.screen.get()
            self.scr_text = self.scr_text.replace("ANS", str(self.answ))
            self.total = factorial(float(self.scr_text))
            self.screen.delete(0, END)
            self.screen.insert(END, self.total)
        except:
            self.screen.delete(0, END)
            self.total = "Invalid Operation"
            self.screen.insert(0, "Invalid Operation")
        with open("Output.txt", "a+") as f:
            f.write(self.scr_text + "! = " + str(self.total) + "\n")

    def permute(self):
        n,r = re.findall(r'\d+', self.screen.get())
        print(type(n))
        try:
            self.total = factorial(float(n))/factorial(float(n)-float(r))
            self.screen.delete(0, END)
            self.screen.insert(END, self.total)
        except:
            self.screen.delete(0, END)
            self.total = "Invalid Operation"
            self.screen.insert(0, "Invalid Operation")
        with open("Output.txt", "a+") as f:
            f.write(n + "P" + r + " = " + str(self.total) + "\n")

    def combi(self):
        n,r = re.findall(r'\d+', self.screen.get())
        print(type(n))
        try:
            self.total = factorial(float(n))/factorial(float(r))/factorial(float(n)-float(r))
            self.screen.delete(0, END)
            self.screen.insert(END, self.total)
        except:
            self.screen.delete(0, END)
            self.total = "Invalid Operation"
            self.screen.insert(0, "Invalid Operation")
        with open("Output.txt", "a+") as f:
            f.write(n + "C" + r + " = " + str(self.total) + "\n")



# ---------------------------------------------------------------------------------- #


'''
 @author : Keshav Kabra
'''
# -----------------------------Importing Modules ---------------------------------------- #
from tkinter import *
import Help
import calculator_class
# --------------------------------------------------------------------------------------- #

# ------------------------ Making Basic Window ------------------------------------------ #
root = Tk()
root.title("Calculator")
root.geometry("910x495")
root.resizable(width=False, height=False)
root.wm_iconbitmap("1.ico")
# ---------------------------------------------------------------------------------------- #


# ------------------------------------- Menu Bar ----------------------------------------- #
main_menu = Menu(root)

m1 = Menu(main_menu, tearoff=0)
m1.add_command(label="About Us", command=Help.about)
m1.add_separator()
m1.add_command(label="Exit", command= lambda : Help.exit(root))
root.config(menu=main_menu)
main_menu.add_cascade(label="Help", menu=m1)

main_menu.add_command(label="Action", command=Help.Actions)
root.config(menu=main_menu)
# ------------------------------------------------------------------------------------------ #

# -------------------------------------- Driver Code --------------------------------------- #
calculator_class.Calculator(root)
root.mainloop()
# ------------------------------------------------------------------------------------------ #
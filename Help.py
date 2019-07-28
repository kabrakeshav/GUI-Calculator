'''
 @author : Keshav Kabra
'''
import tkinter.messagebox as tmsg

def about():
    tmsg.showinfo(
        "About",
        "This Software is made with by KESHAV KABRA.\n\n"
        "Contact Info :\n"
        "      Phone No. : +91-7014722936\n"
        "      Email Info  : keshavkabra118@gmail.com\n"
        "                        keshavkabra.official@gmail.com\n"                            
        "      INDIA \n\n"
        " If you have any Issues, please tell your Feedback."
    )

def Actions():
    tmsg.showinfo(
        "About Software",
        "- This is a Scientific Calculator\n"
        "- Contains Arithmetic and Algebraic Functions\n"
        "- Use the Mathematical Buttons as per requirement\n"
        "- Your calculations will be stored in an extenal Output file\n"
    )

def exit(root):
    val = tmsg.askyesno("Calculator", "Do you want to Exit ?")
    if val>0:
        tmsg.showinfo("Calculator", " Thank You! Hope you liked the Service !!")
        root.destroy()

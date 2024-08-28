#Importing libraries, I select tkinter for Graphic User Interface(GUI).
#At first, I wanted to use AES base64, however, there are some issues in importing AES.
#So I imported ordinary base64 library for encryption and decryption.
from tkinter import *
from tkinter import messagebox
import base64
import os


#Defining encryption algorithm by using base64 and ASCII table.
#And also creating messagebox to pop up encrypted message.
def encrypt():
    secret_key=code.get()

    if secret_key =="Howgwart1850!":
        screen1=Toplevel(screen)
        screen1.title("ENCRYPTION")
        screen1.geometry("390x200")
        screen1.configure(background="red")

        message=text1.get(1.0,END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")

        Label(screen1,text="Encrypted Message",font="arial",foreground="white",background="red").place(x=15,y=0)
        text2=Text(screen1,font="arial 22", bg="white", relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=15,y=40,width=355,height=140)

        text2.insert(END,encrypt)

    elif secret_key=="":
        messagebox.showerror("ERROR!", "Please Input Your Secret Key")

    elif secret_key !="Howgwart1850!":
        messagebox.showerror("ERROR!", "Key Incorrect")


#Defining decryption algorithm by using base64 and ASCII table. 
#And also creating messagebox to pop up decrypted message.
def decrypt():
    secret_key =code.get()

    if secret_key =="Howgwart1850!":
        screen2=Toplevel(screen)
        screen2.title("DECRYPTION")
        screen2.geometry("390x200")
        screen2.configure(background="green")

        message=text1.get(1.0,END)
        decode_message=message.encode("ascii")
        base64_bytes=base64.b64decode(decode_message)
        decrypt=base64_bytes.decode("ascii")

        Label(screen2,text="Decrypted Message",font="arial",foreground="white",background="green").place(x=15,y=0)
        text2=Text(screen2,font="arial 22", bg="white", relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=15,y=40,width=355,height=140)

        text2.insert(END,decrypt)

    elif secret_key=="":
        messagebox.showerror("ERROR!", "Please Input Your Secret Key")

    elif secret_key !="Howgwart1850!":
        messagebox.showerror("ERROR!", "Key Incorrect")


def main_screen():

    global screen
    global code
    global text1

    screen=Tk()
    screen.geometry("450x450")

#Adding Icon for GUI
    image_icon = PhotoImage(file="key_image.png")
    screen.iconphoto(FALSE, image_icon)

    screen.title("Email Encryption & Decryption")
    screen.configure(background="grey")
    def reset():
        code.set("")
        text1.delete(1.0,END)
#Editing Lable
    Label(text="Text box for encryption and decryption", foreground="black", font=("arial",15), background="grey").place(x=
    15,y=15)
    text1=Text(font="arial 22",background="white",relief=GROOVE,wrap=WORD,border=0)
    text1.place(x=15, y=60, width=420, height=120)

    Label(text="Enter secret key here: ", foreground="black", font=("ariel",15), background="grey").place(x=15,y=245)

    code=StringVar()
    Entry(textvariable=code,width=10,bd=0,font=("ariel",25),show="*").place(x=250,y=245)
#Adding Buttons for Encrytion and Decryption.
#if users are willing to encrypt another messages or decrypt the encrypted message, I added the reset button.
    Button(text="ENCRYPT",height="2",width=25,bg="red",fg="white",bd=0,command=encrypt).place(x=15,y=320)
    Button(text="DECRYPT",height="2",width=25,bg="green",fg="white",bd=0,command=decrypt).place(x=250,y=320)
    Button(text="RESET",height="2",width=25,bg="purple",fg="white",bd=0,command=reset).place(x=133,y=380)


    screen.mainloop()

main_screen()







#I imported these necessary libraries for the coding.
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from base64 import b64encode, b64decode
import tkinter as tk
from tkinter import messagebox


#Define functions for key generation encryption and decryption.
#I used 2048 bits to generate the private and public keys.
#Then I added messagebox to show whether the task is successful or not.
def generate_key():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    with open('private.pem', 'wb') as f:
        f.write(private_key)
    with open('public.pem', 'wb') as f:
        f.write(public_key)
    messagebox.showinfo("Key Generation", "Key files generated successfully!")

#Define functions for encryption and decryption.
#And I used PKCS1 along with optimal asymmetric encryption padding.
def encrypt():
    with open('public.pem', 'rb') as f:
        public_key = RSA.import_key(f.read())
    message = plaintext.get("1.0", "end-1c").encode()
    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = b64encode(cipher.encrypt(message))
    ciphertext_text.delete("1.0", "end")
    ciphertext_text.insert(tk.END, ciphertext.decode())
    messagebox.showinfo("Encryption", "Message encrypted successfully!")


def decrypt():
    with open('private.pem', 'rb') as f:
        private_key = RSA.import_key(f.read())
    ciphertext = b64decode(ciphertext_text.get("1.0", "end-1c"))
    cipher = PKCS1_OAEP.new(private_key)
    try:
        plaintext_message = cipher.decrypt(ciphertext).decode()
        plaintext.delete("1.0", "end")
        plaintext.insert(tk.END, plaintext_message)
        messagebox.showinfo("Decryption", "Message decrypted successfully!")
    except ValueError:
        messagebox.showerror("Decryption Error", "Unable to decrypt message. Invalid ciphertext.")


#Define functions for digital signatures and verification.
#And I added SHA-256 as a hashing algorithm.
def sign():
    with open('private.pem', 'rb') as f:
        private_key = RSA.import_key(f.read())
    message = plaintext.get("1.0", "end-1c").encode()
    hash = SHA256.new(message)
    signature = pkcs1_15.new(private_key).sign(hash)
    signature_text.delete("1.0", "end")
    signature_text.insert(tk.END, b64encode(signature).decode())
    messagebox.showinfo("Digital Signature", "Message signed successfully!")


def verify():
    with open('public.pem', 'rb') as f:
        public_key = RSA.import_key(f.read())
    message = plaintext.get("1.0", "end-1c").encode()
    hash = SHA256.new(message)
    signature = b64decode(signature_text.get("1.0", "end-1c"))
    try:
        pkcs1_15.new(public_key).verify(hash, signature)
        messagebox.showinfo("Digital Signature Verification", "Signature is valid!")
    except (ValueError, TypeError):
        messagebox.showerror("Digital Signature Verification", "Signature is not valid.")

#Define functions for reset buttons.
def reset():
    plaintext.delete('1.0', tk.END)
    ciphertext_text.delete('1.0', tk.END)
    signature_text.delete('1.0', tk.END)
    

#Define functions for GUI.
screen = tk.Tk()
screen.title("RSA Encryption, Decryption and Digital Signature")
screen.geometry("700x700")
screen.configure(background="grey")

#Add labels and text boxes.
tk.Label(screen, text="Plaintext: ", foreground="black", font=("arial",13), background="grey").place(x=15,y=75)
plaintext = tk.Text(screen, font="arial 22",background="white",relief="groove",wrap="word",border=0)
plaintext.place(x=160,y=15, width=500, height=120)

tk.Label(screen, text="Ciphertext: ", foreground="black", font=("arial",13), background="grey").place(x=15,y=250)
ciphertext_text = tk.Text(screen, font="arial 12",background="white",relief="groove",wrap="word",border=0)
ciphertext_text.place(x=160,y=200, width=500, height=120)

tk.Label(screen, text="Digital Signature: ", foreground="black", font=("arial",13), background="grey").place(x=15,y=430)
signature_text = tk.Text(screen, font="arial 12",background="white",relief="groove",wrap="word",border=0)
signature_text.place(x=160,y=385, width=500, height=120)

#Add buttons which would run the commands.
tk.Button(text="GENERATE KEY",height="2",width=15,bg="blue",fg="white",bd=0,command=generate_key).place(x=15,y=520)
tk.Button(text="ENCRYPT",height="2",width=15,bg="red",fg="white",bd=0,command=encrypt).place(x=270,y=520)
tk.Button(text="DECRYPT",height="2",width=15,bg="green",fg="white",bd=0,command=decrypt).place(x=520,y=520)
tk.Button(text="SIGN",height="2",width=15,bg="purple",fg="white",bd=0,command=sign).place(x=270,y=600)
tk.Button(text="VERIFY",height="2",width=15,bg="orange",fg="white",bd=0,command=verify).place(x=520,y=600)
tk.Button(text="RESET",height="2",width=15,bg="black",fg="white",bd=0,command=reset).place(x=15,y=600)


#Run the GUI
screen.mainloop()
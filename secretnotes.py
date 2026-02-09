## hata mesajı tkinter mesage box
## görsel koyma
# tkinter kriptogrofi
from base64 import decode
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from cryptography.fernet import Fernet
from tkinter import messagebox
import hashlib
import base64

window = Tk()
window.title("Secret Notes")
window.minsize(400,650)

## add image
#img = Image.open(r"C:\Users\GKCE\Downloads\secret2.png" = Label(window, image=photo))
#photo = ImageTk.PhotoImage(img)

#lab1
#lab1.place(x=130,y=50)
#lab1.image = photo

## ENTRY
entry_label = Label(text="Enter your title",font=("Arial",8,"bold"))
entry_label.place(x=155,y=180)
entry= Entry(width=30)
entry.place(x=100,y=200)

# TEXT
text_label=Label(text="Enter your secret",font=("Arial",8,"bold"))
text_label.place(x=145,y=220)
mytext=Text(width=30,height=15)
mytext.place(x=70,y=240)

# MASTER KEY
matserkey_label = Label(text="Enter master key",font=("Arial",8,"bold"))
matserkey_label.place(x=140,y=490)
masterkeyentry = Entry(width=32)
masterkeyentry.place(x=95,y=510)
savepass = masterkeyentry.get()

def get_fernet_key(master_key):
    key_hash = hashlib.sha256(master_key.encode()).digest()
    fernet_key = base64.urlsafe_b64encode(key_hash)
    return fernet_key

## make a key and save
def encrypter():
    if len(mytext.get("1.0",END))==0 or len(entry.get())==0 or len(masterkeyentry.get())==0:
        messagebox.showerror("Error","Please enter your secret and master key")

    message = mytext.get("1.0",END)
    x = message.encode()
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    encrypted = cipher_suite.encrypt(x)

    ## save key for text
    saveenter = entry.get()
    txt_file = open(r"C:\Users\GKCE\Documents\PhytonSecretNotes\secret.txt", "w")
    txt_file.write(saveenter)
    txt_file.write("\n")
    txt_file.write(encrypted.decode())
    mytext.delete("1.0",END)
    entry.delete(0, END)
    masterkeyentry.delete(0, END)

# secret meseage show
def showmsg():
     encrypted = mytext.get("1.0",END)
     master_secret = masterkeyentry.get()
     if len(encrypted)==0 or len(master_secret)==0:
         messagebox.showerror("Error","Please enter your secret and master key")

pass


def showmsg():
    master_key = masterkeyentry.get().strip()
    title = entry.get().strip()
    if not title or not master_key:
        messagebox.showerror("Hata", "Lütfen Başlık ve Ana Anahtarı girin.")
        return
    else:
        try:
            key = get_fernet_key(master_key)
            cipher_suite = Fernet(key)
            encrypted_data = mytext.get("1.0", END).strip().encode()
            decrypted_bytes = cipher_suite.decrypt(encrypted_data)
            decrypted = decrypted_bytes.decode()
            mytext.delete("1.0", END)
            mytext.insert("1.0", decrypted)

        except FileNotFoundError:
            messagebox.showerror("Hata", "Kayıt dosyası bulunamadı.")
        except Exception:
            messagebox.showerror("Hata", "Şifre Çözülemedi! Anahtarınızı veya şifreli metni kontrol edin.")



## button
button1=Button(text="Save & Encrypt",font=("Arial",8,"bold"),command=encrypter)
button1.place(x=140,y=540)
button2=Button(text="Decrypt",font=("Arial",8,"bold"),command=showmsg)
button2.place(x=155,y=575)



window.mainloop()

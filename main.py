from tkinter import *
from tkinter import filedialog
import os
import requests
from dna_get import main as encrypt
from dna_gdt import main as decrypt
import requests
import json
from tkinter import messagebox 

root = Tk()
root.geometry("500x500")
root.title("DNA Based Encryption and decryption of confidential data in cloud storage ! ")


class encryptor:
    def __init__(self):
        self.path=None
        self.folder=None

    def browsefile(self):
        filename = filedialog.askopenfilename()
        return filename
        
    def getfilepath(self):
        self.path=self.browsefile()
        return self.path

def send_data_to_cloud(text):
    x= requests.get('http://localhost/phpfiles/store.php?text='+text)
    if x.text=="Success":
        messagebox.showinfo("Success","The data has been sent to the cloud successfully !")
        
    else :
        messagebox.showerror("Error","Pls check weather the host is up !")

def download_from_cloud():
    y= requests.get('http://localhost/phpfiles/retrieve.php')
    x=json.loads(y.text)
    return x['data']


def upload_and_encrypt():
    q=encryptor()
    textdata=q.browsefile()
    encrypted_string= encrypt(textdata)
    send_data_to_cloud(encrypted_string)
    messagebox.showinfo("Encrypted text",encrypted_string)
    messagebox.showwarning("KEY","Pls keep key.txt file safe, since key is needed in decryption time ! ")



def download_and_decrypt():
 
    encrypted_text=download_from_cloud()
    decrypted_string=decrypt(encrypted_text)
    messagebox.showinfo("Decrypted data",decrypted_string)
    messagebox.showinfo("Decrypted data","Pls check the decrypted.txt for the decrypted data")


l1=Label(root,text="Pls select any text file to encrypt and upload to the cloud ! ",fg="green")

uploadbtn=Button(text="Encrypt and Upload a File",height=3,width=50,command=upload_and_encrypt,fg="white",bg="green")

downloadbtn=Button(text="Download and decrypt the file",height=3,width=50,command=download_and_decrypt,fg="white",bg="black")
l1.pack()
uploadbtn.pack()
downloadbtn.pack()
l1.place(relx=0.5, rely=0.3, anchor=CENTER)
uploadbtn.place(relx=0.5, rely=0.4, anchor=CENTER)
downloadbtn.place(relx=0.5,rely=0.5, anchor=CENTER)



root.mainloop()
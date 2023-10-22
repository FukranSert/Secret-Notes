import cryptocode
import tkinter as tk
import os
dosya_adi = "Secret.txt"
klasor_yolu = "C:\\Users\\sertf\\OneDrive\\Masaüstü\\SECRET NOTES"
dosya_yolu = os.path.join(klasor_yolu, dosya_adi)





#functions
def encryption_():
    if entry_key.get()=="" or entry_title.get()=="" or text_message.get(1.0,tk.END)=="":
        message_box=tk.Toplevel(windows_1)

        message_box.geometry("200x200")
        message_box.configure(bg="red")
        canvas = tk.Canvas(message_box, width=300, height=200,bg="black")
        canvas.pack()

        canvas.create_image(36, 0, anchor=tk.NW, image=image_messagebox)

        message_label = tk.Label(message_box, text="Enter all information!!",font=('Helvetica bold', 12))
        message_label.place(x=30,y=140)


        custom_button = tk.Button(message_box, text="Okey", command=message_box.destroy,bg="blue")
        custom_button.place(x=80,y=170)
    else:
        encoded_text=cryptocode.encrypt(message=text_message.get(1.0,tk.END),password=entry_key.get())
        with open(dosya_yolu, 'a') as dosya:

            dosya.write(f"{entry_title.get()}\n")
            dosya.write(f"{encoded_text}\n")
        entry_title.delete(0,tk.END)
        entry_key.delete(0,tk.END)
        text_message.delete(1.0,tk.END)
def dencryption_():
    if entry_key.get() == "" or text_message.get(1.0,tk.END) == "":
        message_box = tk.Toplevel(windows_1)

        message_box.geometry("200x200")
        message_box.configure(bg="red")
        canvas = tk.Canvas(message_box, width=300, height=200, bg="black")
        canvas.pack()

        canvas.create_image(36, 0, anchor=tk.NW, image=image_messagebox)

        message_label = tk.Label(message_box, text="Enter all information!!", font=('Helvetica bold', 12))
        message_label.place(x=30, y=140)

        custom_button = tk.Button(message_box, text="Okey", command=message_box.destroy, bg="blue")
        custom_button.place(x=80, y=170)
    else:
        decoded_text=cryptocode.decrypt(text_message.get(1.0,tk.END),password=entry_key.get())
        if decoded_text==False:
            message_box = tk.Toplevel(windows_1)

            message_box.geometry("200x200")
            message_box.configure(bg="red")
            canvas = tk.Canvas(message_box, width=300, height=200, bg="black")
            canvas.pack()

            canvas.create_image(36, 0, anchor=tk.NW, image=image_messagebox)

            message_label = tk.Label(message_box, text="Invalid text or password!!", font=('Helvetica bold', 12))
            message_label.place(x=25, y=140)

            custom_button = tk.Button(message_box, text="Okey", command=message_box.destroy, bg="blue")
            custom_button.place(x=80, y=170)
        else:
            text_message.delete(1.0,tk.END)
            entry_key.delete(0,tk.END)
            text_message.insert(1.0,decoded_text)




#window
windows_1=tk.Tk()
windows_1.configure(bg="grey")
windows_1.geometry("400x720")
windows_1.title("SECRET NOTES")
windows_1.resizable(False,False)
#title
frame_title=tk.Frame(bg="grey")
label_title=tk.Label(bg="grey",fg="black",text="Enter your title",width=15,font=('Helvetica bold', 15),master=frame_title)
entry_title=tk.Entry(bg="white",fg="black",width=30,master=frame_title)
label_title.pack()
entry_title.pack()
frame_title.place(x=110,y=120)
#message
frame_message=tk.Frame(bg="grey")
label_message=tk.Label(bg="grey",fg="black",text="Enter your text",width=15,font=('Helvetica bold', 13),master=frame_message)
text_message=tk.Text(bg="white",fg="black",width=40,master=frame_message,height=25)
label_message.pack()
text_message.pack()
frame_message.place(x=40,y=170)
#key
frame_key=tk.Frame(bg="grey")
label_key=tk.Label(bg="grey",fg="black",text="Enter your master key",width=20,font=('Helvetica bold', 14),master=frame_key)
entry_key=tk.Entry(bg="white",fg="black",width=30,master=frame_key)
label_key.pack()
entry_key.pack()
frame_key.place(x=90,y=600)
#button
frame_button=tk.Frame(bg="grey")
button_encrypt=tk.Button(text="Save and Encrypt",master=frame_button,command=encryption_)
button_decrypt=tk.Button(text="Decrypt",master=frame_button,command=dencryption_)
button_encrypt.pack()
button_decrypt.pack()

frame_button.place(x=150,y=655)
image_messagebox = tk.PhotoImage(file="C:/Users/sertf/PycharmProjects/Secret Notes/roket.gif")
windows_1.mainloop()


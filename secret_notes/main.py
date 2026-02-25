from tkinter import *

#window
pencere = Tk()
pencere.title("Gizli Notlarım")
pencere.minsize(width=400,height=550)

#label dosya başlığı
label = Label(text="Sırlarınızın başlığını giriniz",font=("Arial", 15, "bold"))
"""
label.config(bg="light blue")
label.config(fg="black")
"""
label.config(padx=20,pady=20)
label.pack()

text_baslik= Text(width=30,height=1)
text_baslik.insert("1.0", "Başlık giriniz?")
text_baslik.pack()
text_baslik.focus()

#label içerik
label1 = Label(text="Sırlarınızı yazınız....",font=("Arial", 15, "bold"))
"""
label.config(bg="Grey")
label.config(fg="black")
"""
label1.config(padx=20,pady=20)
label1.pack()

text_dosya= Text(width=30,height=15)
text_dosya.pack()

#label şifre
label2 = Label(text="Şifrenizi giriniz...",font=("Arial", 15, "bold"))
label2.pack()

text_sifre= Text(width=30,height=1)
text_sifre.pack()

#BUTTON
def kaydet_sakla():
    pass
button_save = Button(text="kaydet ve şifrele", command=kaydet_sakla)
button_save.pack()

#BUTTON şifre çöz
def notu_cikar():
    pass
button_save = Button(text="şifreyi çöz", command=notu_cikar)
button_save.config(pady=10)
button_save.pack()

#resim ekleme
resim = PhotoImage(file="resimm.pgm")
label_resim = Label(image=resim)
label_resim.pack(pady=20)











pencere.mainloop()
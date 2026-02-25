from tkinter import *
from PIL import Image, ImageTk

# Window
pencere = Tk()
pencere.title("Gizli Notlarım")
pencere.minsize(width=400, height=550)

# Label dosya başlığı
label = Label(text="Sırlarınızın başlığını giriniz", font=("Arial", 15, "bold"))
label.config(padx=20, pady=20)
label.pack()

text_baslik = Text(width=30, height=1)
text_baslik.insert("1.0", "Başlık giriniz?")
text_baslik.pack()
text_baslik.focus()

# Label içerik
label1 = Label(text="Sırlarınızı yazınız....", font=("Arial", 15, "bold"))
label1.config(padx=20, pady=20)
label1.pack()

text_dosya = Text(width=30, height=15)
text_dosya.pack()

# Label şifre
label2 = Label(text="Şifrenizi giriniz...", font=("Arial", 15, "bold"))
label2.pack()

text_sifre = Text(width=30, height=1)
text_sifre.pack()

# BUTTON kaydet ve şifrele
def kaydet_sakla():
    pass
button_save = Button(text="kaydet ve şifrele", command=kaydet_sakla)
button_save.pack()

# BUTTON şifre çöz
def notu_cikar():
    pass
button_decode = Button(text="şifreyi çöz", command=notu_cikar)
button_decode.config(pady=10)
button_decode.pack()

# Resim ekleme
image = Image.open("resim.png")  # Resmi Pillow kullanarak aç
photo = ImageTk.PhotoImage(image)
label_resim = Label(image=photo)
label_resim.image = photo  # PhotoImage referansını saklamak için
label_resim.pack(pady=20)

pencere.mainloop()


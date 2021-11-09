import random #bu çalışmamızda random modülünü kullanacağız
import tkinter as tk
from tkinter import messagebox #message box widgetını kullanacağız bu yüzden çağırdık
window = tk.Tk()
window.geometry("300x200")
count = 0 #bu sayıcı için bir sıfır değeri atadık.
#fonksiyonlar
def addtext(): #ekrana text ekleme fonksiyonu
    global count #count değerini global olarak tanıttık
    addtxt.config(text=" HELLO \n WORLD")
    """aşağıda tanımladığım labelın içeriğini değiştirdi"""
    count += 1
    """sayımıza 1 ekledik"""
    if count != 1 :
        """eğer sayımız 1e eşit değilse bir uyarı oluşturmasını istedik bunu
neden yaptık kullanıcının bir kez text butonuna basmasını istediğimiz için artık ikinci
kez bastığında aşağıdaki uyarı çıkacak """
        tk.messagebox.showwarning("WARNING","You can only click once")
        """message box widgetını
        tanımladık"""

def changecolor(): #yazımızın rengini değiştirmek için fonksiyon tanımladık
    selected=["red", "pink", "blue", "gray","#04B4AE","#8A4B08","#240B3B"]
    """ renklerimiz için bir liste tanımladık hem normal hem de renk kodu olarak ekledım"""
    select=random.choice(selected)
    """burada random olarak listeden bir renk seçmesini istedim"""
    addtxt.config(fg=select)#ve fg kısmına select değerini atadım"""
def changefont() :# font değiştirmek için fonksiyon"""
    selectedf=["Arial 12 italic", "Helvetica 18 underline","Times 12 overstrike",
                                                                                            "Constantia 13 bold","Calibri 16 "]
    selectf=random.choice(selectedf)
    addtxt.config(font=selectf) #aynı işlemler buna da uygulandı

addtxt=tk.Label(font = "Helvetica 12", fg= "black" )
"""bir adet label oluşturdum ve text
kısmını boş yaptım"""
addtxt.pack(side = tk.TOP)#yerleştirdim
button = tk.Button(window, text = "Text",font = "Helvetica 10", fg="black" ,
                                                                                                                                command =addtext)
button.pack(side = tk.LEFT, padx= 10 ,pady=20)
button2 = tk.Button(window, text = "Change Color",font = "Helvetica 10",fg="black",
                                                                                                                                command=changecolor)
button2.pack(side = tk.LEFT, padx= 10 ,pady=20)
button3 = tk.Button(window, text = "Change Font",font = "Helvetica 10",fg="black" ,
                                                                                                command= changefont)
button3.pack(side = tk.LEFT,  padx= 10 ,pady=20)
"""yukarıdaki butonlarda fg kısmına black yazmasam da default olarak siyah gelecekti 
ayrıyeten command kısmında gördüğünüz gibi fonksiyonları atayarak artık butonlarımı 
işlevli hale getirdim"""
window.mainloop()
import qrcode 
from tkinter import*
from pyzbar import*
#from pyzbar.pyzbar import decode
from PIL import Image

root = Tk()
root.title("qr code generator")
#root.geometry("400×400") #alt+0215 for multiply sign still not usable???
root.geometry("400x400")

def dec():
    
    img = Image.open("C:/Users/himansh/Documents/qr_code/qrcode.png")
    
    result = decode(img)
    print(result)

def gen():
    
#creating barcode
    data = entry.get()

    img = qrcode.make(data)

    qr = qrcode.QRCode(version=1, box_size=10, border=5)

    qr.add_data(data)

    qr.make(fit=True)
    img = qr.make_image(fill_colour="red", black_colour="white")
    img.save("C:/Users/himansh/Documents/qr_code/qrcode.png" )


#creating entry box for our input and button to perform generation of qrcode
label = Label(root, text="insert your data for qr code")
label.pack()
entry = Entry(root, width=30)
entry.pack()
b = Button(root, text="click to generate qr code", command=gen)
b.pack()
b1 = Button(root, text="decode your qr code", command=dec).pack()
root.mainloop()

#for error 13 permission not found uh can give it via adding "+w or R"
# already added https://github.com/kakashihatake81 my github link in qr code 
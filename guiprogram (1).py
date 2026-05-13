import tkinter as tk
from tkinter import messagebox
import qrcode
import barcode
from barcode.writer import ImageWriter

# QR Generator Function

def generate_qr():
    data = entry.get()

    if data == "":
        messagebox.showerror("Error", "Please Enter Data")
        return

    img = qrcode.make(data)
    img.save("generated_qr.png")

    messagebox.showinfo("Success", "QR Code Generated")  
# Barcode Generator Function

def generate_barcode():
    data = entry.get()

    if data == "":
        messagebox.showerror("Error", "Please Enter Data")
        return

    code128 = barcode.get_barcode_class('code128')

    my_barcode = code128(data, writer=ImageWriter())

    my_barcode.save("generated_barcode")

    messagebox.showinfo("Success", "Barcode Generated")

# Main Window
root = tk.Tk()
root.title("QR & Barcode Generator")
root.geometry("400x300")
# Heading
label = tk.Label(root,
                 text="QR & Barcode Generator",
                 font=("Arial", 16, "bold"))
label.pack(pady=20)

# Entry Box
entry = tk.Entry(root, width=35, font=("Arial", 12))
entry.pack(pady=10)

# Buttons
btn1 = tk.Button(root,
                 text="Generate QR",
                 command=generate_qr,
                 width=20,
                 bg="lightblue")
btn1.pack(pady=10)
btn2 = tk.Button(root,
                 text="Generate Barcode",
                 command=generate_barcode,
                 width=20,
                 bg="lightgreen")
btn2.pack(pady=10)

root.mainloop()
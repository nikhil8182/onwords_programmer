# Import Tkinter module
from tkinter import *
from tkinter.ttk import *
import esptool

# Create root window
root = Tk()
root.title("Code Uploader")
root.geometry("500x300")

# Disable the maximize window option
root.resizable(False, False)

# Create label for heading
heading_label = Label(root, text="Onwords Programmer", font=("calibri", 20, "bold"))
heading_label.grid(row=0, column=1, columnspan=2, pady=10)

# Create label for pid
pid_label = Label(root, text="pid:", font=("calibri", 19,))
pid_label.grid(row=1, column=1, sticky=E)

# Create label for pid value
pid_value = Label(root, text="3ch1fb", font=("calibri", 19,))
pid_value.grid(row=1, column=2, sticky=W)

# Create left frame for product name and upload button
left_frame = Frame(root, width=200, height=300)
left_frame.grid(row=2, column=0, padx=10, pady=5)

# Create label for product name
product_label = Label(left_frame, text="Product Name:")
product_label.grid(row=0, column=0, sticky=W)

# Create variable for product name
product_var = StringVar()
product_var.set("Select a product")

# Create dropdown menu for product name
product_options = ["Blink Led Program 3 sec", "Blink Led Program 1 sec", "Blink Led Program 5 sec"] # Add more products as needed
product_menu = OptionMenu(left_frame, product_var, *product_options)
product_menu.grid(row=0, column=1, padx=5)

# Define a function to print the product name and update the progressbar
def print_product():
    product_selected = product_var.get()
    print(f'Product Selected in dropdown = {product_selected}')
    if product_selected == "Blink Led Program 3 sec":
        print("uploading Blink Led Program 3 sec")
        esptool.main(["--chip","eps32","--port","/dev/cu.usbserial-0001","write_flash","0x10000","3sec.bin"])
        print("upload sucessfull")

style = Style()
style.configure("W.TButton", font=("calibri", 12, "bold"), foreground="green")

upload_button = Button(left_frame, text="Upload", style="W.TButton", command=print_product)
upload_button.grid(row=1, column=0, columnspan=2, padx=50)

root.mainloop()
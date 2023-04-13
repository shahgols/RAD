import tkinter as tk
import camera #--> uncomment
root = tk.Tk()
root.geometry("800x800")
root.title("Cash Safe")
# color info
light_blue = (97, 137, 183)
color_string = "#%02x%02x%02x" % light_blue

# Root background info
canvas = tk.Canvas(root, bg=color_string, width=800, height=500)
canvas.pack(expand=True)

# Text
text_frame = tk.Frame(root, width=221, height=70)
text_frame.place(x=230, y=180)

text_label = tk.Label(text_frame, text="SMRT BOX", font=("Bold", 70), bg=color_string, fg="white")
text_label.pack(fill=tk.BOTH, expand=True)

# Image
image_frame = tk.Frame(root, width=200, height=154.76)
image_frame.place(x=400, y=510, anchor="center")
image_label = tk.Label(image_frame, bg=color_string)
image_label.pack(fill=tk.BOTH, expand=True)

image = tk.PhotoImage(file="image.png")
image_label.config(image=image)
image_label.image = image

# Apply filter to the image
image_label.config(highlightthickness=0, bd=0)
image_label.bind("<Configure>", lambda e: image_label.config(width=e.width, height=e.height))


def display_input(money_input):

    label2_frame = tk.Frame(root, width=200, height=154.76)
    label2_frame.place(x=400, y=320, anchor="center")
    label2 = tk.Label(label2_frame, text=money_input, font=("Helvetica", 70), bg=color_string, fg="black")
    label2.pack(fill=tk.BOTH, expand=True)


#money input info
money_input = "camera()"#change this
display_input(money_input)
'''def hide_image():
    image_frame.pack_forget()
    image_label.pack_forget()

    root.after(3000, show_image)

# function to show the image
def show_image():
    image_frame.place(x=270, y=280)
    image_label.pack(fill=tk.BOTH, expand=True)
    image_label.config(highlightthickness=0, bd=0)
    image_label.bind("<Configure>", lambda e: image_label.config(width=e.width, height=e.height))'''

#money_input = None
#money_input = camera() --> uncomment
#money_input = "1234"#comment this out
'''if money_input:
    display_input(money_input)'''

root.mainloop()

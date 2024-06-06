import customtkinter as ctk
from PIL import Image, ImageTk, ImageFont, ImageDraw  # Ensure ImageDraw is imported
import tkinter as tk

# Initialize the main window
root = ctk.CTk()
root.geometry('600x440')
root.title('Sonic-AI')
root.iconbitmap('Bild.ico')

# Load the custom font using Pillow
font_path = "Minecraft.ttf"  # Specify the path to your font file
custom_font = ImageFont.truetype(font_path, 20)

# Use Pillow to render text if needed
def create_image_with_text(text, font, image_size=(300, 100)):
    image = Image.new("RGBA", image_size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    text_bbox = draw.textbbox((0, 0), text, font=font)  # Provide text as the first argument
    text_width, text_height = text_bbox[1] - text_bbox[0], text_bbox[3] - text_bbox[1]
    position = ((image_size[0] - text_width) // 2, (image_size[1] - text_height) // 2)
    draw.text(position, text, font=font, fill=(0, 0, 0, 255))
    return ImageTk.PhotoImage(image)

# Use the custom font in a Label
label_image = create_image_with_text("Sonic-AI", custom_font)
label = ctk.CTkLabel(root, image=label_image, text="")
label.pack(padx=20, pady=20)

# Saving image to variable
dark_image = Image.open("sonic-running-run.png")
# Using ctkimage element to add image to
bild = ctk.CTkImage(dark_image=dark_image, size=(80, 80))

# Putting the image inside a label
label_image = ctk.CTkLabel(root, image=bild, text="")
# Placing the label
label_image.place(x=1000, y=30)

# Create an ImageTk.PhotoImage for button icon
image_send = ImageTk.PhotoImage(Image.open('mingcute--send-fill (1).png'))

textbox = ctk.CTkTextbox(root, width=900, height=50, font=('Arial', 16), fg_color="white", text_color="black")
textbox.place(x=250, y=600)

button = ctk.CTkButton(root, width=100, height=50, text="", image=image_send, font=('Arial', 18))
button.place(x=1155, y=600)

def exit_app():
    root.quit()

exit_button = ctk.CTkButton(root, text="Quit", font=("Arial", 30), command=exit_app, width=150, height=50)
exit_button.place(x=1200, y=40)

login_button = ctk.CTkButton(root, text="Login", font=("Arial", 30), width=150, height=50)
login_button.place(x=1350, y=40)

scroll = ctk.CTkScrollableFrame(root, width=980, height=390, fg_color="white")
scroll.place(x=250, y=188)

def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)

combobox = ctk.CTkComboBox(root, values=["practice", "option2"], command=combobox_callback, width=200, height=50)
combobox.place(x=20, y=188)

root.mainloop()

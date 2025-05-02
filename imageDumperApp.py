import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class ImageDumperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ImageDumper")
        self.root.geometry("800x600")
        
        self.image = None
        self.tk_image = None
        
        # Label to show instructions
        self.label = tk.Label(root, text="Select an image file to start", font=("Arial", 14))
        self.label.pack(pady=10)
        
        # Button to select image
        self.select_button = tk.Button(root, text="Select Image", command=self.select_image)
        self.select_button.pack(pady=20)
        
        # Canvas to display the image
        self.canvas = tk.Canvas(root, width=500, height=300, bg="gray")
        self.canvas.pack(pady=20)
        
        # Label to show original image size
        self.info_label = tk.Label(root, text="No image selected", font=("Arial", 10))
        self.info_label.pack(pady=10)
        
    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.webp *.bmp")])
        if file_path:
            self.load_image(file_path)
        
    def load_image(self, file_path):
        try:
            # Open image using PIL
            self.image = Image.open(file_path)
            print(f"Image loaded: {self.image.size}")
            
            # Resize and display image on canvas
            self.display_image()
            
            # Show the image file name and original size
            self.label.config(text=f"Selected: {file_path.split('/')[-1]}")
            self.info_label.config(text=f"Original Size: {self.image.width} x {self.image.height}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open image: {e}")
    
    def display_image(self):
        # Resize image to fit the canvas size
        max_width, max_height = 500, 300
        img = self.image.copy()
        img.thumbnail((max_width, max_height))
        self.tk_image = ImageTk.PhotoImage(img)
        
        # Clear the canvas and display the image
        self.canvas.delete("all")
        self.canvas.create_image(max_width // 2, max_height // 2, image=self.tk_image)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageDumperApp(root)
    root.mainloop()
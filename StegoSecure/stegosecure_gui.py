import tkinter as tk
from tkinter import filedialog, messagebox
from utils.lsb_encoder import hide_data
from utils.lsb_decoder import extract_data
from utils.crypto import encrypt, decrypt
import os

class StegoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 StegoSecure")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        self.image_path = None

        # UI Elements
        tk.Label(root, text="Text to Hide / Extracted Message:").pack(pady=5)
        self.text_input = tk.Text(root, height=6, wrap="word")
        self.text_input.pack(padx=10, fill="x")

        tk.Label(root, text="Encryption Key (optional):").pack(pady=5)
        self.key_input = tk.Entry(root, show="*", width=50)
        self.key_input.pack(padx=10, fill="x")

        self.img_label = tk.Label(root, text="No image selected")
        self.img_label.pack(pady=10)

        tk.Button(root, text="📂 Choose Image", command=self.choose_image).pack()
        tk.Button(root, text="🔐 Hide Message", command=self.encode).pack(pady=5)
        tk.Button(root, text="🔍 Extract Message", command=self.decode).pack(pady=5)

    def choose_image(self):
        path = filedialog.askopenfilename(filetypes=[("Images", "*.png *.bmp")])
        if path:
            self.image_path = path
            self.img_label.config(text=f"Image: {os.path.basename(path)}")

    def encode(self):
        if not self.image_path:
            messagebox.showerror("Error", "Please choose an image.")
            return

        text = self.text_input.get("1.0", "end").strip()
        key = self.key_input.get().strip()

        if not text:
            messagebox.showerror("Error", "Please enter some text to hide.")
            return

        output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png"), ("BMP", "*.bmp")])
        if not output_path:
            return

        try:
            secret = encrypt(text, key) if key else text
            hide_data(self.image_path, secret, output_path)
            messagebox.showinfo("Success", f"Message hidden in:\n{output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Encoding failed:\n{e}")

    def decode(self):
        if not self.image_path:
            messagebox.showerror("Error", "Please choose an image.")
            return

        key = self.key_input.get().strip()

        try:
            hidden = extract_data(self.image_path)
            message = decrypt(hidden, key) if key else hidden
            self.text_input.delete("1.0", "end")
            self.text_input.insert("1.0", message)
            messagebox.showinfo("Success", "Message extracted successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Decoding failed:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = StegoApp(root)
    root.mainloop()

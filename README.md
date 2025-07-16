# 🛡️ StegoSecure – Secure Image-Based Data Hiding Tool

**StegoSecure** enhances traditional image steganography by combining it with **AES** encryption, ensuring that:
The hidden message is invisible to anyone viewing the image.
Even if extracted, the message remains unreadable without the correct password.
This dual-layer approach provides both secrecy (steganography) and security (encryption).

---

## ✨ Features

- 🔒 AES Encryption of hidden messages
- 🖼️ LSB (Least Significant Bit) image steganography
- 🧑‍💻 Command-line interface (CLI)
- 🪟 Easy-to-use GUI interface
- 🔓 Secure retrieval and decryption of embedded data
- 🧠 Modular structure for easy extension

---

## 📁 Project Structure

```

StegoSecure/
├── stegosecure.py            # CLI entry point
├── stegosecure\_gui.py        # GUI application
├── utils/
│   ├── crypto.py             # Encryption/decryption functions (AES)
│   ├── lsb\_encoder.py        # Data hiding logic
│   ├── lsb\_decoder.py        # Data retrieval logic

````

---

## 💻 How to Run

### ▶️ CLI Mode

```bash
python stegosecure.py
````

* Follow the terminal prompts to encode or decode data.
* Input the image path, message, and encryption password as requested.

### 🪟 GUI Mode

```bash
python stegosecure_gui.py
```

* A windowed interface will launch.
* Use the GUI to choose an image, type your secret message, and optionally apply encryption.

---

## 🔐 Encryption

* StegoSecure uses **AES encryption** (via the `cryptography` library).
* You can opt-in to encrypt your hidden message with a password.
* The same password must be used to decrypt during decoding.

---

## 📦 Requirements

Install the required dependencies:

```bash
pip install cryptography pillow
```

### Optional for GUI:

```bash
pip install tk
```

---

## 🧪 Example Usage

### Encode a message:

1. Choose a cover image (e.g., `cover.png`)
2. Provide the secret message or text file
3. Enter a password (optional)
4. Save the encoded image (e.g., `output.png`)

### Decode a message:

1. Open the encoded image (e.g., `output.png`)
2. Provide the same password (if encryption was used)
3. Retrieve and read the hidden message

---

## 🚀 Future Improvements

* 🖼️ Support for more image formats (JPEG, BMP)
* 🧠 Improve encryption options (e.g., RSA support)
* 📁 Drag & drop GUI functionality
* 🐳 Dockerized deployment

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## 👨‍💻 Author

**\[Behramm Umrigar]**
GitHub: [@Behramm10](https://github.com/Behramm10)

---


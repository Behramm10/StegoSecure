import argparse
from utils.lsb_encoder import hide_data
from utils.lsb_decoder import extract_data
from utils.crypto import encrypt, decrypt

def main():
    parser = argparse.ArgumentParser(description="StegoSecure: Hide text in images with optional AES encryption")
    subparsers = parser.add_subparsers(dest="command")

    enc = subparsers.add_parser("encode")
    enc.add_argument("--input", required=True, help="Input image")
    enc.add_argument("--output", required=True, help="Output image")
    enc.add_argument("--text", required=True, help="Text to hide")
    enc.add_argument("--key", help="Encryption key (optional)")

    dec = subparsers.add_parser("decode")
    dec.add_argument("--input", required=True, help="Stego image")
    dec.add_argument("--key", help="Decryption key (optional)")

    args = parser.parse_args()

    if args.command == "encode":
        secret_text = encrypt(args.text, args.key) if args.key else args.text
        hide_data(args.input, secret_text, args.output)
        print(f"Message hidden in '{args.output}'")

    elif args.command == "decode":
        hidden = extract_data(args.input)
        try:
            if args.key:
                hidden = decrypt(hidden, args.key)
            print(f"Hidden Message: {hidden}")
        except Exception:
            print("Failed to decrypt or decode.")

if __name__ == "__main__":
    main()

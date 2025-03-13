
import qrcode
from PIL import Image

def generate_qr_code(upi_id):
    qr_code = qrcode.make(upi_id)
    qr_code.save("qr_code.png")
    print("QR code generated successfully!")

def display_qr_code():
    qr_code_image = Image.open("qr_code.png")
    qr_code_image.show()

def main():
    upi_id = input("Enter text that you want to display in QR: ")
    generate_qr_code(upi_id)
    display_qr_code()

if __name__ == "__main__":
    main()
import qrcode
from qrcode.constants import (
    ERROR_CORRECT_L,
    ERROR_CORRECT_M,
    ERROR_CORRECT_Q,
    ERROR_CORRECT_H
)

print("===== QR CODE GENERATOR =====")

data = input("Enter text or website URL: ")

print("Choose QR Code Color:")
print("1. Black")
print("2. Blue")
print("3. Green")

color_choice = input("Enter choice: ")

colors = {
    "1": "black",
    "2": "blue",
    "3": "green"
}

fill_color = colors.get(color_choice, "black")

print("Choose Error Correction Level:")
print("1. Low")
print("2. Medium")
print("3. High")
print("4. Highest")

level_choice = input("Enter choice: ")

levels = {
    "1": ERROR_CORRECT_L,
    "2": ERROR_CORRECT_M,
    "3": ERROR_CORRECT_Q,
    "4": ERROR_CORRECT_H
}

error_level = levels.get(level_choice, ERROR_CORRECT_M)

border = int(input("Enter border thickness (1-10): "))

if data.strip():
    qr = qrcode.QRCode(
        version=None,
        error_correction=error_level,
        box_size=10,
        border=border
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(
        fill_color=fill_color,
        back_color="white"
    ).convert("RGB")

    img.save("my_qrcode.png")
    img.save("my_qrcode.jpeg", format="JPEG")

    print("QR Code generated successfully!")
    print("Saved as my_qrcode.png")
    print("Saved as my_qrcode.jpeg")
else:
    print("Please enter valid text or URL.")

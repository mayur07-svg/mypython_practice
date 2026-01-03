import qrcode as qr

data = input("Enter your text or link: ")
img = qr.make(data)
img.save("my_qr_code.png")

print("✅ QR Code generated successfully as my_qr_code.png")

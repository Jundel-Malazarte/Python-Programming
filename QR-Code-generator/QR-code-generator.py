import qrcode

img = qrcode.make("https://github.com/jundel-malazarte") # change this link for your qr code link
# Save the generated QR code as an image file

img.save("./images/qrcode.png") # path where the image will be saved
print("QR code generated and saved as ./images/qrcode.png")
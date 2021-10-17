pip install qrcode
#Import Library
import qrcode
#Generate QR Code
img=qrcode.make('Hello World')
img.save('hello.png')
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data("https://abhijithchandradas.medium.com/")
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="black")
img.save("medium.png")
pip install cv2
import cv2
img=cv2.imread("medium.png")
det=cv2.QRCodeDetector()
val, pts, st_code=det.detectAndDecode(img)
print(val)

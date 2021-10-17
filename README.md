# Create-and-Read-QR-code
QR codes are machine readable two dimensional pixelated barcodes which can be used to store a variety of information. QR in QR code stands for Quick Response.
QR code was invented by a Japanese engineer Masahiro Hara from automobile manufacturer Denso Wave in the year 1994 to track the movement of car parts.
QR Code has increased in popularity in the later 2010s with improvement in optical capabilities of mobile phones and their wide adoption.
Nowadays, QR codes are being used for wide variety of applications like, make online payments, check hotel menu, share wifi password, obtain price and other details of products etc. QR Codes have become so popular that now every new smartphone comes with in built QR code reader.
Install QR Code module
We will be using qrcode package for generating QR code.
The first step is installing the package using pip command.
Simple QR Code
A simple qr code can be generated by using the make function of qrcode and passing the data as argument.
The below code produces a QR code which reads ‘Hello World.’
Advanced QR Code
QR code can be customized using QRCode object which has the following parameters:
i. version:
There are 40 versions of QR code which controls the size of the code.
1 being the smallest and 40 being the largest.
Version 1 will create a 21X21 matrix QR Code.
ii. error_correction:
This parameter controls the Error Correction used for the QR code. This varies from 7% to 30% error correction as below.
ERROR_CORRECT_L: up to 7%
ERROR_CORRECT_M: up to 15%
ERROR_CORRECT_Q: up to 25%
ERROR_CORRECT_H: up to 30%
iii. box_size:
This parameter controls the number of pixels in each box of the QR code
iv. border:
This parameter controls the thickness of the border. The default border is 4 pixels thick.
The QRCode object has the following functions which can be used to create the QR Code.
i. add data
The content of the QR code can be passed as an argument to this function.
ii. make
If you are not sure about which version of QR code to use, the version can be set automatically by :
a. setting version parameter to None and
b. seting fit parameter of make to True.
iii. make image
This function generates the QR code. It can also be used to set the fill color and background color of the QR code using fill_color and back_color arguments.

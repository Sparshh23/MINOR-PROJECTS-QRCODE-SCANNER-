#QR CODE GENRATOR
import qrcode
import image
qr = qrcode.QRCode(
    version =  4 ,
    box_size = 3 , 
    border = 2
    
)
data = "https://www.linkedin.com/in/sparshhh23/"
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black",back_color ="white")
img.save("test.png")  
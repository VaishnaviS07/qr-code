import qrcode
import image
qr = qrcode.QRCode (
    version = 15,
    box_size = 10,
    border = 5,
)
data = "https://www.bing.com/search?q=python&form=ANNTH1&refig=60ccf48c02444e9291643d33e3682ddd"
qr.add_data(data)
qr.make(fit=True)
img= qr.make_image(fill="black",bg_color = "white")
img.save("test.png")

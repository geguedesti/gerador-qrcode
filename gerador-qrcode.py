import qrcode

url = "https://gspacefoco.vercel.app/"
img_file = "./qrcode.png"

# img = qrcode.make(url) 
# img.save(img_file)

qr = qrcode.QRCode()
qr.add_data(url)
img = qr.make_image(back_color= "pink", fill_color= "black")
img.save(img_file)

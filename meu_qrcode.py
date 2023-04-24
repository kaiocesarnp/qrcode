import qrcode

# Cria o objeto QR Code
qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 4,
)

# Adiciona o texto ao QR Code
qr.add_data('https://github.com/kaiocesarnp')  #Texto que você quer adicionar ao QR Code

# Gera o QR Code
qr.make(fit = True)

# Cria um objeto de imagem a partir de QR Code
img = qr.make_image(fill_color = "black", back_color = "white")

# Salva a imagem em um arquivo
img.save('qr_code.png')

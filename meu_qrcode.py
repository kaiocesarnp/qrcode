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


# Explicação de cada linha do código:

# import qrcode: importa a biblioteca "qrcode" que permite a criação de QR Codes em Python.

# qr = qrcode.QRCode(...): cria um objeto QRCode da biblioteca qrcode. A função recebe alguns argumentos como:
    # version = 1: define a versão do QR Code a ser gerado. Quanto maior o valor, mais informações podem ser armazenadas, mas também maior será o tamanho do código gerado.
    # error_correction = qrcode.constants.ERROR_CORRECT_L: define o nível de correção de erros que o QR Code deve ter.
        # O valor ERROR_CORRECT_L significa "Low" e indica um nível baixo de correção de erros. Outros valores possíveis são "Medium", "Quartile" e "High".
    # box_size = 10: define o tamanho de cada "caixa" do QR Code. Quanto maior o valor, maior será o tamanho do código gerado.
    # border = 4: define a largura da borda do QR Code.

# qr.add_data('https://github.com/kaiocesarnp'): adiciona os dados que devem ser armazenados no QR Code. Neste caso, é o link para o perfil do usuário "kaiocesarnp" no GitHub.

# qr.make(fit = True): gera o QR Code com base nos dados adicionados anteriormente. 
    # O argumento fit = True faz com que o código se ajuste automaticamente para caber no tamanho definido pelas configurações anteriores.

# img = qr.make_image(fill_color = "black", back_color = "white"): cria uma imagem a partir do QR Code gerado na etapa anterior. A cor de preenchimento do código é preta e a cor de fundo é branca.

# img.save('qr_code.png'): salva a imagem do QR Code em um arquivo chamado "qr_code.png".























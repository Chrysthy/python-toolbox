# pip install "qrcode[pil]" 
# Documentação para consulta: https://pypi.org/project/qrcode/

import qrcode
import time

print('=== QR Code Generator ===')

text = input('Digite um texto ou URL: ').strip()
print(f'Conteúdo informado: {text}')


if text == '':
    print('Por favor, digite um texto ou URL')
else:
    print('Gerando QRCode')
    time.sleep(1)

    qrcode_image = qrcode.make(text)
    # print(type(qrcode_image))

    file = 'qrcode.png'
    qrcode_image.save(file)


    print('QRCode gerado com sucesso!')
    print(f'Nome do arquivo: {file}')
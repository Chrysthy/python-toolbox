# pip install "qrcode[pil]"
# Documentação para consulta: https://pypi.org/project/qrcode/

import qrcode
import time

print('=== QR Code Generator ===')

text = input('Digite um texto ou URL: ').strip()
print(f'Conteúdo informado: {text}')

file_name = input('Digite o nome que deseja no arquivo ou enter para nome padrão: ').strip()


if text == '':
    print('Por favor, digite um texto ou URL')

else:
    print('Gerando QRCode')
    time.sleep(1)

    qrcode_image = qrcode.make(text)
    # print(type(qrcode_image))

    if file_name == '':
        file_name = 'document.png'

    elif not file_name.lower().endswith('.png'):
        file_name = f'{file_name}.png'


    qrcode_image.save(file_name)


    print('QRCode gerado com sucesso!')
    print(f'Nome do arquivo: {file_name}')
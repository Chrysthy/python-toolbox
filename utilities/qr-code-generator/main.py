# pip install "qrcode[pil]"
# Documentação para consulta: https://pypi.org/project/qrcode/

import qrcode
import time

print('=== QR Code Generator ===')

text = input('Digite um texto ou URL: ').strip()
print(f'Conteúdo informado: {text}')

file_name = input(
    'Digite o nome que deseja no arquivo ou enter para nome padrão: ').strip()


if text == '':
    print('Por favor, digite um texto ou URL')

else:
    qrcode_color = input('Digite a cor do QR Code: ').lower().strip()
    qrcode_back_color = input('Digite a cor do fundo do QR Code: ').lower().strip()
    print('Gerando QRCode')
    time.sleep(1)

    # qrcode_image = qrcode.make(text)
    # print(type(qrcode_image))

    if file_name == '':
        file_name = 'document.png'

    elif not file_name.lower().endswith('.png'):
        file_name = f'{file_name}.png'


    if qrcode_color == '':
        qrcode_color = 'black'


    if qrcode_back_color == '':
        qrcode_back_color = 'white'
      



    code = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )

    code.add_data(text)
    code.make(fit=True)
    qrcode_image = code.make_image(fill_color=qrcode_color, back_color=qrcode_back_color)
    qrcode_image.save(file_name)

    print('QRCode gerado com sucesso!')
    print(f'Nome do arquivo: {file_name}')

# Exemplo de QR Code para o Projeto

import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

def gerar_exemplo_qr():
    """Gera um QR code de exemplo para demonstração"""
    
    # URL de exemplo (você pode alterar para sua URL real)
    url_exemplo = "https://exemplo.com/namorados"
    
    # Configurações do QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    
    qr.add_data(url_exemplo)
    qr.make(fit=True)
    
    # Cria a imagem com cores românticas
    qr_img = qr.make_image(fill_color="#d63384", back_color="#fce4ec")
    
    if qr_img.mode != 'RGB':
        qr_img = qr_img.convert('RGB')
    
    # Cria imagem final decorada
    largura_final = qr_img.width + 200
    altura_final = qr_img.height + 300
    
    img_final = Image.new('RGB', (largura_final, altura_final), '#fce4ec')
    
    # Adiciona gradiente
    draw = ImageDraw.Draw(img_final)
    for i in range(altura_final):
        cor_r = int(252 - (i / altura_final) * 50)
        cor_g = int(228 - (i / altura_final) * 50)
        cor_b = int(236 - (i / altura_final) * 50)
        cor = (cor_r, cor_g, cor_b)
        draw.line([(0, i), (largura_final, i)], fill=cor)
      # Cola o QR code
    pos_x = (largura_final - qr_img.width) // 2
    pos_y = (altura_final - qr_img.height) // 2 + 50
    img_final.paste(qr_img, (pos_x, pos_y, pos_x + qr_img.width, pos_y + qr_img.height))
    
    # Adiciona texto
    try:
        fonte_titulo = ImageFont.truetype("arial.ttf", 36)
        fonte_subtitulo = ImageFont.truetype("arial.ttf", 20)
    except:
        fonte_titulo = ImageFont.load_default()
        fonte_subtitulo = ImageFont.load_default()
    
    # Título
    titulo = "❤️ Para Meu Amor ❤️"
    bbox = draw.textbbox((0, 0), titulo, font=fonte_titulo)
    largura_texto = bbox[2] - bbox[0]
    x_titulo = (largura_final - largura_texto) // 2
    draw.text((x_titulo, 30), titulo, fill="#d63384", font=fonte_titulo)
    
    # Subtítulo
    subtitulo = "Escaneie para ver sua surpresa 💕"
    bbox = draw.textbbox((0, 0), subtitulo, font=fonte_subtitulo)
    largura_texto = bbox[2] - bbox[0]
    x_subtitulo = (largura_final - largura_texto) // 2
    draw.text((x_subtitulo, 80), subtitulo, fill="#8e5572", font=fonte_subtitulo)
    
    # Texto inferior
    texto_inferior = "Dia dos Namorados 2025 💖"
    bbox = draw.textbbox((0, 0), texto_inferior, font=fonte_subtitulo)
    largura_texto = bbox[2] - bbox[0]
    x_inferior = (largura_final - largura_texto) // 2
    draw.text((x_inferior, altura_final - 50), texto_inferior, fill="#8e5572", font=fonte_subtitulo)
    
    # Salva
    nome_arquivo = "exemplo_qrcode_namorados.png"
    img_final.save(nome_arquivo, 'PNG', quality=95)
    print(f"QR code de exemplo gerado: {nome_arquivo}")
    return nome_arquivo

if __name__ == "__main__":
    gerar_exemplo_qr()

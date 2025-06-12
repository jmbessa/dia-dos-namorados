import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

def gerar_qr_code_romantico(url, nome_arquivo="qrcode_namorados.png"):
    """
    Gera um QR code personalizado para o Dia dos Namorados
    
    Args:
        url (str): URL da página web (pode ser local ou online)
        nome_arquivo (str): Nome do arquivo de saída
    """
    
    # Configurações do QR code
    qr = qrcode.QRCode(
        version=1,  # Controla o tamanho do QR code
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Alta correção de erro
        box_size=10,  # Tamanho de cada "caixa" do QR code
        border=4,  # Borda em "caixas"
    )
    
    # Adiciona os dados (URL)
    qr.add_data(url)
    qr.make(fit=True)
    
    # Cria a imagem do QR code com cores românticas
    qr_img = qr.make_image(
        fill_color="#d63384",  # Cor rosa/magenta
        back_color="#fce4ec"   # Fundo rosa claro
    )
    
    # Converte para RGB se necessário
    if qr_img.mode != 'RGB':
        qr_img = qr_img.convert('RGB')
    
    # Cria uma imagem maior para adicionar decorações
    largura_final = qr_img.width + 200
    altura_final = qr_img.height + 300
    
    # Cria imagem final com fundo gradiente
    img_final = Image.new('RGB', (largura_final, altura_final), '#fce4ec')
    
    # Cria um efeito de gradiente simples
    draw = ImageDraw.Draw(img_final)
    for i in range(altura_final):
        cor_r = int(252 - (i / altura_final) * 50)
        cor_g = int(228 - (i / altura_final) * 50)
        cor_b = int(236 - (i / altura_final) * 50)
        cor = f"#{cor_r:02x}{cor_g:02x}{cor_b:02x}"
        draw.line([(0, i), (largura_final, i)], fill=cor)
      # Cola o QR code no centro
    pos_x = (largura_final - qr_img.width) // 2
    pos_y = (altura_final - qr_img.height) // 2 + 50
    img_final.paste(qr_img, (pos_x, pos_y))
    
    # Adiciona texto decorativo
    draw = ImageDraw.Draw(img_final)
    
    try:
        # Tenta usar uma fonte maior (pode não funcionar em todos os sistemas)
        fonte_titulo = ImageFont.truetype("arial.ttf", 36)
        fonte_subtitulo = ImageFont.truetype("arial.ttf", 20)
    except:
        # Fonte padrão se não encontrar arial
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
    
    # Texto na parte inferior
    texto_inferior = "Dia dos Namorados 2025 💖"
    bbox = draw.textbbox((0, 0), texto_inferior, font=fonte_subtitulo)
    largura_texto = bbox[2] - bbox[0]
    x_inferior = (largura_final - largura_texto) // 2
    draw.text((x_inferior, altura_final - 50), texto_inferior, fill="#8e5572", font=fonte_subtitulo)
    
    # Salva a imagem
    img_final.save(nome_arquivo, 'PNG', quality=95)
    print(f"QR code gerado com sucesso: {nome_arquivo}")
    return nome_arquivo

def gerar_qr_local():
    """
    Gera QR code para uso local (arquivo HTML)
    """
    # Caminho para o arquivo HTML local
    caminho_html = os.path.abspath("index.html")
    url_local = f"file:///{caminho_html.replace(os.sep, '/')}"
    
    print("=== GERADOR DE QR CODE ROMÂNTICO ===")
    print("🌹 Para o Dia dos Namorados 🌹\n")
    
    print("Escolha uma opção:")
    print("1. Usar arquivo local (index.html)")
    print("2. Inserir URL personalizada (se você hospedar online)")
    
    escolha = input("\nDigite sua escolha (1 ou 2): ").strip()
    
    if escolha == "1":
        url = url_local
        print(f"\nUsando arquivo local: {url}")
    elif escolha == "2":
        url = input("Digite a URL da sua página (ex: https://meusite.com/namorados): ").strip()
        if not url.startswith(('http://', 'https://')):
            print("⚠️  Adicionando 'https://' à URL...")
            url = f"https://{url}"
    else:
        print("Opção inválida. Usando arquivo local por padrão.")
        url = url_local
    
    # Gera o QR code
    nome_arquivo = gerar_qr_code_romantico(url)
    
    print(f"\n✅ QR Code criado com sucesso!")
    print(f"📁 Arquivo salvo como: {nome_arquivo}")
    print(f"🔗 URL codificada: {url}")
    print(f"\n💕 Agora você pode imprimir o QR code e dar para sua namorada!")
    print(f"📱 Quando ela escanear, verá sua página romântica!")
    
    return nome_arquivo

if __name__ == "__main__":
    # Instala as dependências necessárias se não estiverem instaladas
    try:
        import qrcode
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        print("Instalando dependências necessárias...")
        os.system("pip install qrcode[pil] pillow")
        import qrcode
        from PIL import Image, ImageDraw, ImageFont
    
    # Gera o QR code
    gerar_qr_local()

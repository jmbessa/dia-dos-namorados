import qrcode
import os

def gerar_qr_simples(url, nome_arquivo="qrcode_namorados.png"):
    """
    Gera um QR code simples e funcional para o Dia dos Namorados
    """
    
    # Configurações do QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    
    # Adiciona os dados (URL)
    qr.add_data(url)
    qr.make(fit=True)
    
    # Cria a imagem do QR code com cores românticas
    qr_img = qr.make_image(
        fill_color="#d63384",  # Cor rosa/magenta
        back_color="white"     # Fundo branco
    )
    
    # Salva a imagem
    qr_img.save(nome_arquivo)
    print(f"✅ QR code gerado com sucesso: {nome_arquivo}")
    return nome_arquivo

def main():
    print("=== 💕 GERADOR DE QR CODE ROMÂNTICO 💕 ===")
    print("🌹 Para o Dia dos Namorados 🌹\n")
    
    print("Escolha uma opção:")
    print("1. Usar arquivo local (index.html na pasta atual)")
    print("2. Inserir URL personalizada (se você hospedar online)")
    print("3. Gerar exemplo de demonstração")
    
    escolha = input("\nDigite sua escolha (1, 2 ou 3): ").strip()
    
    if escolha == "1":
        # Caminho para o arquivo HTML local
        caminho_html = os.path.abspath("index.html")
        url = f"file:///{caminho_html.replace(os.sep, '/')}"
        print(f"\n📁 Usando arquivo local: {caminho_html}")
        
    elif escolha == "2":
        url = input("Digite a URL da sua página: ").strip()
        if not url.startswith(('http://', 'https://')):
            print("⚠️  Adicionando 'https://' à URL...")
            url = f"https://{url}"
            
    elif escolha == "3":
        url = "https://exemplo-namorados.com"
        print("📝 Gerando QR code de demonstração...")
        
    else:
        print("Opção inválida. Usando arquivo local por padrão.")
        caminho_html = os.path.abspath("index.html")
        url = f"file:///{caminho_html.replace(os.sep, '/')}"
    
    # Gera o QR code
    nome_arquivo = gerar_qr_simples(url)
    
    print(f"\n🎉 SUCESSO!")
    print(f"📄 Arquivo criado: {nome_arquivo}")
    print(f"🔗 URL codificada: {url}")
    print(f"\n💡 PRÓXIMOS PASSOS:")
    print(f"1. 🖨️  Imprima o arquivo {nome_arquivo}")
    print(f"2. 💝 Cole em um cartão bonito")
    print(f"3. 🎁 Dê para sua namorada!")
    print(f"4. 📱 Ela escaneia e vê a surpresa!")
    
    return nome_arquivo

if __name__ == "__main__":
    main()

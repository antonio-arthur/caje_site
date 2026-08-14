from pathlib import Path
from PIL import Image
import pillow_heif

pillow_heif.register_heif_opener()

# Local do projeto
pasta_projeto = Path(__file__).parent

# Pasta correta das fotos
pasta = pasta_projeto / "equipe"

print(f"Pasta: {pasta.resolve()}")

if not pasta.exists():
    print("ERRO: a pasta não existe!")
    exit()

arquivos = [
    arquivo
    for arquivo in pasta.iterdir()
    if arquivo.is_file()
    and arquivo.suffix.lower() in [".heic", ".heif"]
]

print(f"Arquivos encontrados: {len(arquivos)}")

for arquivo in arquivos:
    try:
        print(f"Convertendo: {arquivo.name}")

        imagem = Image.open(arquivo)

        saida = arquivo.with_suffix(".webp")

        imagem.convert("RGB").save(
            saida,
            "WEBP",
            quality=85,
            method=6
        )

        print(f"OK: {saida.name}")

    except Exception as e:
        print(f"ERRO em {arquivo.name}: {e}")

print("Conversão finalizada.")


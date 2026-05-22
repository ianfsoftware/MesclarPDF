from PyPDF2 import PdfMerger
import os

merger = PdfMerger()

pasta_pdfs = "pdfs"

arquivos = sorted(os.listdir(pasta_pdfs))

for arquivo in arquivos:

    if arquivo.endswith(".pdf"):

        caminho_arquivo = os.path.join(pasta_pdfs, arquivo)

        print(f"Adicionando: {arquivo}")

        merger.append(caminho_arquivo)

merger.write("arquivo_final.pdf")

merger.close()

print("PDF criado com sucesso!")
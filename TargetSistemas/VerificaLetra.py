texto = input('Digite algo: ').upper()
l = input('Digite uma letra para verificar se ela tem no texto: ').upper()

cont = 0

# Verificar se a letra está no texto e contar as ocorrências
if l in texto:
    cont = texto.count(l)
    print(f'Tem a letra {l}, {cont} vezes')
else:
    print('Não')

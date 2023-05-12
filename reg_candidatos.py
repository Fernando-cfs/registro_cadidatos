candidatos = []

while True:
    



    nome = str(input('\nDigite o nome do candidato: '))
    e = float(input('\nDigite uma nota para Entrevista: '))
    t = float(input('Digite uma nota para Teste teorico: '))
    p = float(input('Digite uma nota para Teste prático: '))
    s = float(input('Digite uma nota para Avaliação de soft skills: '))
    
        
    candidatos.append(f"Candidato {len(candidatos)}: {nome}, Notas: E:{e}_T:{t}_P:{p}_S:{s}")
    
    
    cadastra = str(input('\nCadastra mais candidatos: S/N '))
    if cadastra in 'Nn':
            break
    


for i in candidatos:
      print(i)

candidatos = []
while True:      
    nome = str(input('\nDigite o nome do candidato: '))
    e = float(input('\nDigite uma nota para Entrevista: '))
    t = float(input('Digite uma nota para Teste teorico: '))
    p = float(input('Digite uma nota para Teste prático: '))
    s = float(input('Digite uma nota para Avaliação de soft skills: '))
    candidatos.append(f"Candidato {len(candidatos)}: {nome}, Notas: E{e}_T{t}_P{p}_S{s}")

    cadastra = str(input('\nCadastrar mais candidatos: S/N '))
    if cadastra in 'Nn':
        break   
for i in candidatos:
    print(i)
    
nova_lista = []
while True:
    

    en = float(input('\nDigite uma nota mínima para a Entrevista: '))
    te = float(input('Digite uma nota mínima para o Teste teórico: '))
    pe = float(input('Digite uma nota mínima para o Teste prático: '))
    se = float(input('Digite uma nota mínima para a Avaliação de soft skills: '))
    for candidato in candidatos:
        notas = candidato.split(', Notas: ')[1].split('_')
        e_candidato = float(notas[0][1:])
        t_candidato = float(notas[1][1:])
        p_candidato = float(notas[2][1:])
        s_candidato = float(notas[3][1:])
        if e_candidato >= en and t_candidato >= te and p_candidato >= pe and s_candidato >= se:
            nova_lista.append(candidato)
    print('Candidatos selecionados: ')
    for i in nova_lista:
        print(i)
    print('Obrigado por utilizar o programa')
    exit()
        

def candidatos_menu(candidatos,en,te,pe,se):
    # cria uma nova lista para a busca de candidatos    
    nova_lista = []
    for candidato in candidatos:
        # separa a lista de notas e as e as notas dos processos
        notas = candidato.split(', Notas: ')[1].split('_')
        # armazena as notas do candidatos e converte para float
        e_candidato = float(notas[0][1:])
        t_candidato = float(notas[1][1:])
        p_candidato = float(notas[2][1:])
        s_candidato = float(notas[3][1:])
        # compara as notas dos candidatos com as notas de corte
        if e_candidato >= en and t_candidato >= te and p_candidato >= pe and s_candidato >= se:
            # Adiciona a nova lista de candidatos filtrados
            nova_lista.append(candidato)
    return nova_lista

candidatos = []
while True: 
    # Aqui digita o nome e as notas dos candidatos     
    nome = str(input('\nDigite o nome do candidato: '))
    e = float(input('\nDigite uma nota para Entrevista: '))
    t = float(input('Digite uma nota para Teste teorico: '))
    p = float(input('Digite uma nota para Teste prático: '))
    s = float(input('Digite uma nota para Avaliação de soft skills: '))
    # adiciona a lista de candidatos
    candidatos.append(f"Candidato {len(candidatos)}: {nome}, Notas: E{e}_T{t}_P{p}_S{s}")
    # e usado para para o cadastro dos candidatos
    cadastra = str(input('\nCadastrar mais candidatos: S/N '))
    print('-' * 30)
    if cadastra in 'Nn':
        break  

print('-' * 30)
# faz um print nos candidatos 
print('Candidatos cadastrados:\n')
for i in candidatos:
    print(i)
  

print('-' * 30)
# para colocar as notas minimas de busca dos candidatos
print('\nFiltra candidatos digite as notas minimas para cada etapa do processo')
en = float(input('\nDigite uma nota mínima para a Entrevista: '))
te = float(input('Digite uma nota mínima para o Teste teórico: '))
pe = float(input('Digite uma nota mínima para o Teste prático: '))
se = float(input('Digite uma nota mínima para a Avaliação de soft skills: '))

print('-' * 30)
print('\nCandidatos selecionados que foram bem no processo seletivo:\n')

# chamar funcao candidatos_mennu
nova_lista = candidatos_menu(candidatos,en,te,pe,se)  
# printa 
for i in nova_lista:
    print(i)
print('\nObrigado por utilizar o programa')

        

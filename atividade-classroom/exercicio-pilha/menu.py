from pilha import Pilha;
pilhas = 1;
while pilhas != 10:
    print('''
            (e) Empilhar
            (d) Desempilhar
            (t) Tamanho
            (o) Obter elemento do topo
            (v) Teste de pilha vazia
            (r) Criar nova Pilha
            (n) Inverter os elementos da pilha
            (z) Esvaziar a pilha
            (c) Concatenar duas pilhas
            (m) Escolher outra pilha
            (n) Conversão dec/bin
            (s) Sair
    ''')
    user_input = input('> ESCOLHA A OPÇÃO: ');
    match user_input:
        case 'e':
            Pilha.empilhar();
        case 'd':
            Pilha.desempilhar();
        case 't':
            Pilha.tamanho();
        case 'o':
            Pilha.obtemTopo();
        case 'v':
            Pilha.estahVazia();
        case 'r':
            Pilha.criarPilha();
        case 'n':
            Pilha.inverterPilha();
        case 'z':
            Pilha.esvaziar();
        case 'c':
            Pilha
        case 'm':
            pass
        case 'n':
            pass    
        case 's':
            pilhas = 10;






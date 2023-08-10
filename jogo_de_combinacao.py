import random

def gerar_sequencia():
    return random.choices('RGBYOP', k=5)

def comparar_sequencias(seq_gerada, seq_jogador):
    dicas = []
    for i in range(5):
        if seq_jogador[i] == seq_gerada[i]:
            dicas.append('C')
        elif seq_jogador[i] in seq_gerada:
            dicas.append('P')
        else:
            dicas.append('-')
    return ''.join(dicas)

def jogar_senha():
    print("Bem-vindo ao jogo Senha!")
    seq_gerada = gerar_sequencia()
    
    for _ in range(10):
        print(f"\nTentativa {_ + 1}/10")
        seq_jogador = input("Digite a sequência de pinos (RGBYOP): ").upper()
        
        if len(seq_jogador) != 5 or not all(cor in 'RGBYOP' for cor in seq_jogador):
            print("Sequência inválida.")
            continue
        
        dicas = comparar_sequencias(seq_gerada, seq_jogador)
        print(f"Dicas: {dicas}")
        
        if dicas == 'CCCCC':
            print("Parabéns! Você acertou!")
            break
        else:
            dica_option = input("Deseja pedir uma dica? (S/N): ").upper()
            if dica_option == 'S':
                print(f"Dica: {seq_gerada[random.randint(0, 4)]}")
    
    else:
        print(f"Fim do jogo. A sequência era: {''.join(seq_gerada)}")

def main():
    jogar_senha()
    while input("Deseja jogar novamente? (S/N): ").upper() == 'S':
        jogar_senha()
    print("Obrigado por jogar até a próxima!")
if __name__ == "__main__":
    main()
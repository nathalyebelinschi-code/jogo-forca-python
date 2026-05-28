# ==============================================================================
# Script: jogo_forca.py
# Propósito: Simular um jogo da forca simplificado com lógica iterativa
# Contexto: Experiência Prática 3 - Desenvolvimento de Jogo Educativo
# ==============================================================================

import random

def inicializar_jogo():
    """
    Prepara o ambiente inicial da partida, definindo o banco de dados de palavras,
    realizando o sorteio aleatório e gerando a máscara visual de lacunas.

    Retorna:
        tuple: Uma tupla contendo a palavra_secreta (str) sorteada e a lista de
               letras_descobertas (list) preenchida com sublinhados.
    """
    # Lista indexada ordenada que funciona como repositório de palavras
    vocabulario = ["PYTHON", "PROGRAMACAO", "ESTRUTURA", "DESENVOLVIMENTO", "LOGICA"]
    
    # Sorteio eficiente utilizando indexação interna em tempo constante O(1)
    palavra_secreta = random.choice(vocabulario)
    
    # Geração dinâmica da palavra mascarada com compreensão de lista
    letras_descobertas = ["_" for _ in palavra_secreta]
    
    return palavra_secreta, letras_descobertas


def processar_tentativa(letra, palavra_secreta, letras_descobertas):
    """
    Processa a letra fornecida pelo jogador, varrendo a palavra secreta para
    atualizar as lacunas descobertas em caso de acerto.

    Argumentos:
        letra (str): A letra palpite enviada pelo jogador.
        palavra_secreta (str): A string da palavra correta da partida.
        letras_descobertas (list): A lista contendo o status atual das lacunas.

    Retorna:
        bool: True se o palpite estiver correto e houver alteração na máscara,
              False caso contrário.
    """
    acertou = False
    
    # Varredura indexada usando enumerate para mapear a posição exata da letra
    for indice, caractere in enumerate(palavra_secreta):
        if caractere == letra:
            letras_descobertas[indice] = letra
            acertou = True
            
    return acertou


# --- FLUXO PRINCIPAL DE EXECUÇÃO ---

# Configuração e desempacotamento do estado inicial gerado pela função
palavra_secreta, letras_descobertas = inicializar_jogo()

# Inicialização do controle de vidas
tentativas_restantes = 6

# JUSTIFICATIVA TÉCNICA DO USO DE SETS:
# Escolhemos um conjunto (set) para armazenar o histórico de palpites por ser baseado 
# em tabelas de dispersão (hash tables). Isso garante uma busca em tempo constante O(1) 
# para checar se a letra já foi tentada, além de impedir duplicidade de forma nativa.
letras_tentadas = set()

print("="*45)
print("   BEM-VINDO AO JOGO DA FORCA EDUCATIVO   ")
print("="*45)

# Laço de repetição condicional que sustenta o ciclo ativo de jogo
while tentativas_restantes > 0 and "_" in letras_descobertas:
    print("\n" + "-"*40)
    print(f"Palavra:  {' '.join(letras_descobertas)}")
    print(f"Tentativas restantes: {tentativas_restantes}")
    # Conversão do set para lista ordenada apenas para exibição limpa ao usuário
    print(f"Letras já tentadas: {', '.join(sorted(letras_tentadas)) if letras_tentadas else 'Nenhuma'}")
    print("-"*40)
    
    # Coleta da entrada tratando espaços em branco e convertendo para caixa alta
    letra = input("Digite uma letra: ").strip().upper()
    
    # 1ª Camada de Validação: Verificação de preenchimento ou digitação múltipla
    if not letra or len(letra) != 1 or not letra.isalpha():
        print("⚠ Entrada inválida! Por favor, digite apenas uma letra válida.")
        continue
        
    # 2ª Camada de Validação: Busca instantânea O(1) no histórico do conjunto
    if letra in letras_tentadas:
        print(f"⚠ Atenção: Você já tentou a letra '{letra}'. Escolha outra!")
        continue
        
    # Adiciona a nova letra ao conjunto de histórico
    letras_tentadas.add(letra)
    
    # Execução da lógica modularizada de processamento
    if processar_tentativa(letra, palavra_secreta, letras_descobertas):
        print(f"🎉 Muito bem! A letra '{letra}' faz parte da palavra secreta.")
    else:
        print(f"❌ Letra incorreta! A letra '{letra}' não está na palavra secreta.")
        tentativas_restantes -= 1

# Encerramento controlado e validação das condições de parada fora do loop
print("\n" + "="*45)
if "_" not in letras_descobertas:
    print(f"🏆 PARABÉNS, VOCÊ VENCEU!")
    print(f"A palavra secreta era exatamente: {palavra_secreta}")
else:
    print(f"💀 GAME OVER! Suas tentativas esgotaram.")
    print(f"A palavra correta era: {palavra_secreta}")
print("="*45)

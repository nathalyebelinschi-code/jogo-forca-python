# 🎮 Jogo da Forca Educativo (Python)

Este projeto consiste em um **Jogo da Forca Simplificado** desenvolvido em Python. A aplicação roda diretamente no terminal de comandos e foi projetada focando em conceitos fundamentais de engenharia de software, como modularização, legibilidade e otimização de estruturas de dados.

O projeto foi desenvolvido como parte das atividades práticas de programação, simulando a criação de um software educativo interativo.

---

## 🛠️ Tecnologias e Conceitos Aplicados

* **Linguagem:** Python 3.14
* **Modularização:** Código estruturado em funções com responsabilidades isoladas (`inicializar_jogo` e `processar_tentativa`).
* **Documentação:** Uso rigoroso de `docstrings` para especificação de propósitos, argumentos e retornos, além de comentários seguindo a **PEP 8**.
* **Estruturas de Dados Estratégicas:**
    * **Listas (`list`):** Utilizadas para armazenar o vocabulário e gerenciar a máscara de lacunas (`_`), permitindo alteração direta via índices.
    * **Conjuntos (`set`):** Aplicados no histórico de letras tentadas. Por serem baseados em *hash tables*, impedem palpites duplicados nativamente e garantem buscas ultra-rápidas com complexidade de tempo constante **$O(1)$**.

---

## ⚙️ Demonstração de Execução

*(Dica: Se você rodar o jogo no VS Code, tire um print do terminal jogando e arraste a imagem para cá!)*

---

## 🚀 Como Executar o Projeto

1. Certifique-se de ter o Python instalado em sua máquina.
2. Baixe o arquivo `jogo_forca.py`.
3. Abra o terminal na pasta do arquivo e execute o comando:
   ```bash
   python jogo_forca.py

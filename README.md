# Em uma galáxia muito muito distante... 🌌🚀
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Há muito tempo, em uma galáxia muito muito distante, chamada CIn-UFPE, a resistência luta contra o Império Galáctico, escapando de asteróides e coletando droids para ajudar nas suas missões. ☄️👾

Engenharia da Computação, CIn - UFPE  
Membros:

- Ana Cecília Estelita Costa <acec>
- Edson Oliveira da Silva <eos>
- Gabriel Vitor Velozo Pereira da Silva <gvvps>
- Geovana Pereira de Santana Soares <gpss>
- Maria José Barbosa Mendes <mjbm>
- Vyvian Hiara Patricio de Freitas <vhpf>

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**Instruções de Instalação:**
1) Baixe o **Python 3.x** na sua máquina  
   [python.org](https://www.python.org/)
2) Abra o terminal e baixe a biblioteca do Pygame, seguindo o comando:
   ```bash
   pip install pygame
   ```
3) Baixe o repositório na Área de Trabalho e extraia toda a pasta
4) Rode o jogo, seguindo o comando:
   ```bash
   python Main.py
   ```
**Instruções do Jogo:**
1) Para mover a nave, pressione (⭠ e ⭢) ou (A e D)  
2) Para atirar, pressione ESPAÇO
3) O objetivo é fugir ou destruir os asteróides, enquanto coleta o máximo de estrelas e droids possível

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**Galeria de Fotos:**
<p align="center">
  <img src="https://github.com/user-attachments/assets/2c936a8e-1dac-4987-bdcd-9d2f3ee35707" width="100%" alt="Tela Inicial">
  <br><br>
  <img src="https://github.com/user-attachments/assets/b70580da-1edf-498c-8fda-7bb47f770530" width="100%" alt="Introdução">
  <br><br>
  <img src="https://github.com/user-attachments/assets/ce62c86c-f4fc-4cb8-96c6-c99f7d144fc6" width="100%" alt="Gameplay 1">
  <br><br>
  <img src="https://github.com/user-attachments/assets/a7523dad-2f4d-4058-a35c-7e86f79cf120" width="100%" alt="Gameplay 2">
  <br><br>
  <img src="https://github.com/user-attachments/assets/6c96f3b0-0d63-44e1-b10a-3c9e42bd84b4" width="100%" alt="Game Over">
</p>

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**Arquitetura do Projeto:**  

**Lógica e Funcionamento do Jogo**   
O fluxo principal inicia-se no arquivo Main.py, que invoca a função TelaInicial. Ao pressionar a tecla Enter, o menu é encerrado e a partida é inicializada. O cenário é gerenciado pela classe Fundo, responsável pela renderização das estrelas, do background e da trilha sonora.

Os objetos principais são carregados sequencialmente: a classe Nave (com controles via A/D ou setas e disparos pela barra de Espaço) e os obstáculos. Durante a execução, itens coletáveis (R2D2, C3PO e Estrelas) surgem com sons personalizados e alimentam um placar exibido no canto superior esquerdo. Caso a nave colida com um asteroide, a função gameover é ativada, exibindo a tela de encerramento e permitindo o reinício do ciclo.

**Mecânicas e Geração Aleatória**  
O jogo utiliza um sistema de intervalos para o surgimento (spawn) de elementos, baseado na biblioteca random:  
- Asteroides: Utilizam a função randint para definir uma posição aleatória no topo da tela. Existem três variações com atributos inversamente proporcionais:  
  - Pequeno (70% de chance): Alta velocidade e baixa durabilidade.  
  - Médio (20% de chance): Atributos equilibrados.  
  - Grande (10% de chance): Baixa velocidade e alta durabilidade.  

- Coletáveis: Possuem taxas de raridade distintas baseadas em tempo; a Estrela é o item mais frequente, enquanto o R2D2 é o mais raro.

**Diagrama da Arquitetura do Jogo**
```
Jogo-IP
|
|-- Main.py (Loop principal, Gerenciamento de Estados e Eventos)
|
|-- Objetos/ (Classes dos Objetos)
|   |-- Nave.py       (Movimentação e lógica de tiro)
|   |-- Asteroides.py (Obstáculos com sistema de vida)
|   |-- Estrela.py    (Item coletável - Pontuação)
|   |-- c3po.py       (Item coletável - Especial)
|   |-- r2d2.py       (Item coletável - Especial)
|
|-- Tela/ (Interfaces do Usuário)
|   |-- Telainicial.py  (Controle do Menu, Música de entrada e Start)
|   |-- TelaGameOver.py (Feedback de derrota e Pontuação final)
|
|-- Aspectos/ (Componentes Visuais de Fundo)
|   |-- FundoJogo.py (Background)
|
|-- Sons/ (Recursos de Áudio)
|   |-- Lyoda.mp3 (Voz inicial)
|   |-- Impacto.wav (Som das Colisões)
|   |-- happy world with mochi.mp3 (Música de Fundo)
|
|-- Sprites/ (Visuais - PNG)
    |-- nave.png 
    |-- estrela.png
    |-- asteroide.png
    |-- r2d2.png
    |-- c3po.png
```

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**Bibliotecas utilizadas:**
- "Random"
- "Pygame"

A biblioteca "Random" foi utilizada para definição dos tamanhos e das posições iniciais dos asteróides na tela (no eixo X).

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Divisão de Trabalho**  

| Membros | Responsabilidade | Atividades Principais |
| :--- | :--- | :--- |
| **Ana Cecília** | Coletáveis, Telas, Sons e Colisões | Desenvolvimento e implementação da lógica e sprites dos coletáveis, sprites das telas iniciais, implementação do áudio inicial e controle das colisões com coletáveis |
| **Edson** | Base do Jogo, Asteróides, Sons e Colisões | Polimento da base do jogo, desenvolvimento e implementação da lógica e sprites dos asteróides, implementação do áudio inicial e das colisões com asteróides|
| **Gabriel** | Design | Design visual da interface |  
| **Geovana** | Ajustes, Música e Sons | Ajustes de tela, implementação dos efeitos sonoros e música de fundo do jogo |    
| **Maria José** | Coletáveis e Testes | Configurações extras dos coletáveis, testes |    
| **Vyvian** | Ideação e Base do Jogo | Ideação do formato do jogo e prototipação do funcionamento |    


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**Conceitos aplicados da disciplina de introdução à programação:**  

| Conceito | Aplicação Prática no Projeto |
| :--- | :--- |
| **Variáveis** | Controle de pontuação, armazenamento da vida dos asteroides e configurações de velocidade. |
| **Laços de Repetição** | O loop `while` mantém o jogo rodando e o `for` percorre as listas de objetos para atualizar a tela. |
| **Listas** | Gerenciamento de sprites (tiros e asteroides) que aparecem simultaneamente. |
| **Condicionais (`if/else`)** | Verificação de comandos do teclado e lógica de probabilidades (70%, 20%, 10%) para os tipos de asteroides. |
| **POO (Classes)** | Organização do código em classes (`Nave`, `Asteroides`, `Coletáveis`), permitindo que cada objeto tenha seus próprios atributos. |
| **Tuplas** | Definição de cores em formato RGB e coordenadas de posição que não mudam durante o processamento. |
| **Funções** | Modularização de tarefas específicas, como a função `atirar()`, `TelaInicial()` e `gameover()`. |

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Erros:  
O maior erro foi o gerenciamento das telas.Tentamos fazer o jogo reiniciar liso após o Game Over, mas sem sucesso. Percebemos tarde que o problema era não ter estruturado a Main dentro de uma função ou classe específica, o que dificultou "limpar" o jogo para começar do zero

Desafios:  
O maior desafio foi a parte criativa e o tempo. Conciliar a complexidade do desenvolvimento com o prazo foi desafiador e precisamos desistir de algumas implementações para priorizar tarefas mais necessárias

Lições Aprendidas:  
A principal lição foi que criar um jogo é uma experiência construtiva e divertida, mas exige paciência e resiliência. Vimos que, com dedicação, é possível fazer um bom projeto e que tudo o que aprendemos na disciplina de IP serviu como uma base para a construção desse protótipo.


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

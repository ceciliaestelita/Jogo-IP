Relatório JogoIP - Uma galáxia muito distante.
Curso Engenharia da Computação - CIn
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Membros:

- Maria José Barbosa Mendes <mjbm>
- Vyvian Hiara Patricio de Freitas <vhpf>
- Ana Cecília Estelita Costa <acec>
- Gabriel Vitor Velozo Pereira da Silva <gvvps>
- Edson Oliveira da Silva <eos>
- Geovana Pereira de Santana Soares <gpss>

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Galeria de Fotos:
<img width="1920" height="1080" alt="{9F3732E3-EA11-4DAF-8CD5-9E36E723CEC0}" src="https://github.com/user-attachments/assets/2c936a8e-1dac-4987-bdcd-9d2f3ee35707" />
<img width="1920" height="1080" alt="{653647FC-CCB4-455B-BB9E-B24FECD8F22D}" src="https://github.com/user-attachments/assets/b70580da-1edf-498c-8fda-7bb47f770530" />
<img width="1920" height="1080" alt="{5DC58F67-BEF9-4533-95D2-CBA296AA1C3B}" src="https://github.com/user-attachments/assets/ce62c86c-f4fc-4cb8-96c6-c99f7d144fc6" />
<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/6c96f3b0-0d63-44e1-b10a-3c9e42bd84b4" />
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Bibliotecas usadas:
- ''Random''
- ''Pygame''

No geral, apenas a biblioteca ''Random'' foi utilizada para definir a posição de onde os asteróides apareceriam no topo da tela e fazer a escolha de seus respectivos tamanhos.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Estrutura do código:

- O código inicialmente começa na main, onde ele vai puxar a função ''TelaInicial'' que mostrará a tela inicial do jogo, na tela inicial, ao apertar enter, a tela inicial será fechada e a tela e o jogo será gerado. Na classe ''fundo'' chamada na Main é dado a tela do jogo, onde terá a formação das estrelas, a imagem de fundo e a música. Em seguida, os objetos principais serão carregados no código, sendo a classe ''Nave'' juntamente da definição ''atirar'' e os asteróides, no qual a nave poderá se mexer com A e D e as setas pros lados e atirar com a barra de espaço.
- Ao decorrer da main, os coletáveis serão feitos e seus respectivos sons serão atribuídos a cada, onde os coletáveis vão ser considerados num contador que dirá o placar no jogo no canto superior esquerdo, sendo R2D2, C3PO e estrelas.
- Quando a nave colidir com um asteróide, a definição de ''gameover'' será ativada, onde vai mostrar a tela de game over que reiniciará todo o código para o jogador tentar novamente do zero.

Pontos adicionais sobre o código:

- O código possui um sistema de ''intervalos'' para os coletáveis e para os asteróides, e no caso dos asteróides, cada asteróide tem 3 variações, o grande, médio e pequeno. Quanto maior, maior a vida, menor a velocidade. Quanto menor, menor a vida, maior a velocidade. O código escolherá o código aleatóriamente usando da função ''Randint'' da biblioteca Random, e o randint também juntamente fará o asteróide aparecer numa localização aleatória no topo da tela. Os asteróides possuem porcentagens de serem escolhidos, sendo respectivamente pro menor do maior: 70% pequeno, 20% médio, 10% grande
- No caso dos coletáveis, alguns coletáveis tem um tempo onde eles vão spawnar, sendo o menos raro a estrela e o mais raro o R2D2.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Funções do grupo:

==== Base do jogo ====

Feita por Vyvian Hiara e Edson Oliveira.
- Vyvian planejou o jogo, deu a ideia e fez os protótipos, enquanto Edson poliu a base do jogo.

==== Coletáveis ====
  
Feito majoritariamente por Ana Cecília com ajuda de Maria José na configuração dos coletáveis e fazer os testes necessários.

=== Ajustes e Design ===

Os sprites e o Design do jogo foi feito majoritariamente por Geovana e Gabriel.
- Além da música ter sido Geovana quem foi a responsável, enquanto na maioria da parte Gabriel fez o design.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Conceitos aplicados da disciplina de introdução à programação:

Uso de variáveis, laços de repetição, listas, condicionais, programação orientada a objetos(classes), tupla e funções.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Desafios e erros:

- Um dos maiores erros cometidos no projeto foi o manejo das telas. Tentamos fazer o jogo reiniciar quando dava game over, mas simplesmente não conseguimos reiniciar o jogo de forma lisa. Além disso, descobrimos que o maior problema foi não ter deixado a main do jogo numa classe ou função. O maior desafio foi a parte criativa, pensar como o jogo iria ser e desenvolve-lo. E, o manejo de tempo para colocar tudo em uma ideia durante um período curto de tempo foi um desafio. Por fim, as lições aprendidas é que criar um jogo é muito maneiro, se tiver paciência e vigor, dá para fazer algo bem legal, e no fim a cadeira de IP nos preparou bastante para fazer esse protótipo.

- ''Thats all, folks.''
- Edson Oliveira
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

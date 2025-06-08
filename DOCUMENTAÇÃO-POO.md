# **Documentação do Projeto: Racing game em Python com Pygame**

## **1.Visão Geral**

**Tecnología utilizada:** Python \+ Pygame  
**Descrição:** Implementação de um jogo de corrida utilizando a biblioteca Pygame para renderização gráfica e lógica do jogo.  
**Objetivo:** Criar uma versão funcional de um jogo de corrida, com obstáculos, prêmios a serem alcançados e uma linha de chegada.

## **2.Descrição detalhada do projeto**

**O que é um jogo de corrida?**  
Jogo de corrida ou racing game é um jogo onde o objetivo é correr atrás dos itens, coletá-los e desviar dos obstáculos, para que no final possa se obter uma quantidade determinada de elementos no qual determinará algo por exemplo uma vitória ou uma derrota.

**Curiosidade:** A prática de jogos de corrida pode melhorar a coordenação motora e os reflexos. 

**História do jogo**   
Tudo começou em um laboratório escondido no fim de uma pequena cidade esquecida...

O Dr. Victor era brilhante, mas também desesperado. Seu filho havia sido acometido por uma doença misteriosa e, tomado pelo medo, o pai recorreu a um experimento proibido uma substância que prometia salvar vidas, mas cujo efeito ainda era desconhecido.

Em vez de cura, o que veio foi a transformação: o filho do Dr. Victor perdeu sua humanidade e se tornou um zumbi e a partir daí o vírus se espalhou pela cidade e em seguida pelo mundo.

Muito tempo depois as ruas frias e silenciosas da cidade ainda escondem segredos que ninguém ousa contar, entre as sombras dos arranha-céus e os becos esquecidos, corre um zumbi... mas não um qualquer.

Este zumbi não devora por instinto ele corre com um propósito: reconquistar sua humanidade.  
Para isso, ele precisa coletar o que resta de cérebros pela cidade e acumular moedas perdidas no caos. Cada cérebro traz de volta uma parte de sua consciência, cada moeda, uma lembrança esquecida.

Mas o tempo corre... e você também deve correr.  
Será que ao final dessa corrida frenética pelas ruas pixeladas da cidade, o zumbi vai conseguir se tornar humano novamente?

Ou será apenas mais um corpo perdido na esteira da loucura?

> Referência: *The Walking Dead Agreste*, série de Dinah Moraes.

> **Introdução no jogo:**
Antes do jogador assumir o controle, será exibido uma sequência de imagens que apresenta um pouco dessa história. Essa introdução visual irá funcionar como uma espécie de "cena de abertura", ajudando a criar um clima do jogo e situar o jogador no universo narrativo do projeto, mas se caso ele não quiser ver essa parte, terá a opção de pular.

**2.1 Funcionalidades principais** 

* **Motor do jogo:**  
  * Geração de obstáculos.  
  * Movimentação (direita e para cima).  
  * Sistema de pontuação e próximo bloco.  
      
* **Interface gráfica:**  
  * Display de pontuação.  
  * Telas de início, pausa e game over.  
  * Botões para acelerar e pular  
* **Extras:**  
  * Efeitos sonoros (coleta dos itens, ao longo do jogo e game over)  
  * Comando de voz.  
  * Easter egg.

### 2.2 Arquitetura do Código**
``` 
corrida/  
├── main.py            \# Ponto de entrada (inicialização do jogo)  
├── game.py            \# Lógica principal (estado do jogo, loop principal)  
├── obstaculos.py          \# Definição dos obstáculos e direção  
├── ui/                \# Interface do usuário  
│   ├── render.py      \# Renderização gráfica (Pygame)  
│   └── sounds.py      \# Gerenciamento de áudio  
|    
├── config.py      \# Constantes (imagens, tamanhos)  
└── scores.py      \# Manipulação de high scores
``` 


**3\. Etapas de entrega (Cronograma detalhado)**  
**Etapa 1: Criação das artes ( Semana 1 a 4\)** 

* Configuração no ambiente (pixelart e libresprite).  
* Criação das artes principais (personagens, itens e cenário)  
* Criação da tela do menu inicial, de pausa e de game over.  
* Desenvolvimento dos sprites do personagem principal (zumbi) em diferentes poses (parado, andando, coletando itens).

**Etapa 2: Protótipo básico ( Semana 5 a 8 )**

* Estrutura inicial do projeto (módulos principais).  
* Organização de layout e imagem final.  
* Movimentação manual.


**Etapa 3: Lógica do jogo ( Semana 9 a 15 )**

* Menu inicial e demais telas (pausa/game over).  
* Efeitos sonoros e high score.  
* Detecção de colisões  
* Controle do jogador (teclado/mouse).

**Etapa 4: Testes e Entrega Final ( Semana 15 a 18 )**

* Testes de usabilidade;  
* Correção de erros e adição de elementos que faltarem;  
* Documentação final ( [README.md](http://README.md) e comentários no código ).


**4\. Requisitos técnicos**  
**4.1 requirements.txt**
``` 
  python==3.12  
  pygame==2.6.0
```



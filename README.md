# Caminho Hamiltoniano em Python

Este projeto implementa uma solução para encontrar Caminhos Hamiltonianos em grafos utilizando Python. A visualização do grafo e do caminho (quando encontrado) é feita com as bibliotecas NetworkX e Matplotlib.

---

## Descrição do Algoritmo

O algoritmo implementado é baseado em **busca backtracking**, onde tentamos construir um caminho passo a passo, retornando (backtrack) se não conseguirmos continuar a partir de um vértice.

### Lógica linha a linha:

1. `find_hamiltonian_path`: tenta iniciar o caminho a partir de cada vértice.
2. `hamiltonian_util`: verifica recursivamente se é possível continuar o caminho.
3. `is_hamiltonian_path`: valida um caminho completo.
4. Se um caminho válido for encontrado, ele é retornado.

---

## Como Executar o Projeto

1. Clone o repositório:
   git clone https://github.com/ClaudioJansen/CaminhoHamiltoniano

2. Entre na pasta do repositório:
   cd CaminhoHamiltoniano

3. Instale as dependências:
   pip install networkx matplotlib

4. Execute o algoritmo:
   python main.py

5. Visualize o grafo:
   python view.py

## Relatório Técnico

### Classes de Complexidade

O problema do Caminho Hamiltoniano pertence à classe **NP-Completo**, pois:

- **É NP**: Dado um caminho, podemos verificar em tempo polinomial se ele é Hamiltoniano.
- **É NP-completo**: Pode ser reduzido do Problema do Caixeiro Viajante, que é classicamente NP-completo.

---

### Complexidade Assintótica

- O algoritmo possui **complexidade de tempo exponencial**: `O(n!)` no **pior caso**, pois testa todas as permutações possíveis.
- Essa complexidade foi determinada por **contagem de operações recursivas**.

---

### Teorema Mestre

- **Não aplicável diretamente**, pois o Teorema Mestre se aplica a algoritmos do tipo **dividir-para-conquistar** com recorrência do tipo `T(n) = aT(n/b) + f(n)`.
- Como este algoritmo usa **backtracking puro**, o Teorema Mestre **não se aplica** aqui.

---

### Análise de Casos

- **Pior caso**: Nenhum caminho Hamiltoniano → complexidade `O(n!)`
- **Melhor caso**: Primeiro caminho tentado já é válido → aproximadamente `O(n^2)`
- **Caso médio**: Depende da **estrutura do grafo**

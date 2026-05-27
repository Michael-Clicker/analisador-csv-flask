# 📊 Analisador de Dados CSV

O Analisador de Dados CSV é uma aplicação web interativa desenvolvida para simplificar e automatizar a etapa inicial de análise exploratória de dados. O projeto consome arquivos CSV brutos carregados pelo usuário e renderiza de forma dinâmica um painel triplo de relatórios estatísticos e estruturais, eliminando a necessidade de abrir softwares pesados de planilhas ou digitar códigos em notebooks.

## 🚀 Funcionalidades e Painéis

O sistema processa o arquivo em segundo plano e constrói instantaneamente três visões analíticas na tela:
* **Prévia dos Dados (Head):** Exibe as primeiras 5 linhas do arquivo original em uma tabela limpa, permitindo a verificação rápida das colunas e do padrão de preenchimento, com a numeração de linhas corrigida para iniciar em 1.
* **Resumo Estatístico (Describe):** Gera automaticamente as métricas descritivas fundamentais para todas as colunas numéricas, com os termos técnicos totalmente traduzidos para o português (Média, Mínimo, Máximo, Desvio Padrão e Quartis).
* **Estrutura Geral (Qualidade dos Dados):** Consolida metadados cruciais sobre o arquivo, informando o volume total de linhas e colunas, a distribuição por tipos de dados (numéricos vs. texto) e levantando o total exato de células vazias/nulas existentes no arquivo completo.

## 🧮 Lógica de Manipulação de Dados

O motor da aplicação combina a robustez do Pandas no back-end com tratamento de dados estruturados para garantir relatórios precisos:
* 🔹 **Tradução de Matrizes:** O índice original do método `.describe()` do Pandas é mapeado e reconstruído via dicionário de tradução, convertendo os termos nativos em inglês para nomenclatura estatística padrão em português através da função `.rename(index=...)`.
* 🔹 **Mapeamento de Tipos de Dados:** A contagem de colunas por natureza é feita dinamicamente isolando os tipos primitivos com `.select_dtypes()`, separando dados puramente quantitativos (`number`) de dados qualitativos (`object`, `string`).


## 🎨 Destaques do Design e Código

* **Isolamento de Responsabilidades:** Arquitetura limpa com separação estrita de escopo, isolando a estilização das tabelas no `style.css` e as validações dinâmicas de comportamento no `script.js`.
* **Validação em Duas Camadas:** O JavaScript atua na primeira linha de defesa interceptando o evento `onsubmit` no front-end para barrar envios de formulários vazios ou extensões inválidas. O Flask complementa no back-end verificando o cabeçalho da requisição através de blocos `try-except`.
* **Uploader Responsivo e Visual:** Seletor de arquivos estilizado com bordas tracejadas e efeitos de hover, que manipula o DOM em tempo real via JavaScript para dar feedback visual instantâneo ao usuário.
* **Processamento Resiliente de Tabelas:** O CSS utiliza propriedades de `overflow-x: auto` e `border-collapse: collapse` combinadas com seletores `nth-child(even)` para garantir que tabelas gigantescas mantenham leitura confortável e rolagem suave sem quebrar o layout da página.

## 🛠️ Tecnologias Utilizadas

* **Python 3:** Linguagem base para o processamento lógico.
* **Flask:** Micro-framework para roteamento web e renderização de templates.
* **Pandas:** Biblioteca de alto desempenho para manipulação e análise de dados.
* **HTML5 & CSS3:** Estruturação semântica e estilização nativa
* **JavaScript (ES6):** Manipulação dinâmica do DOM e controle de eventos de validação.
* **Fontes e Ícones:** Integração com Google Fonts (Lato) e Font Awesome 6.

## 💻 Como Rodar o Projeto Localmente

### Pré-requisitos
Ter o Python instalado globalmente em sua máquina.

### 1. Clonar o repositório
```bash
git clone [https://github.com/Michael-Clicker/NOME_DO_REPOSITORIO.git](https://github.com/Michael-Clicker/NOME_DO_REPOSITORIO.git)
cd NOME_DO_REPOSITORIO
python app.py

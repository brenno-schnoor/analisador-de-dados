# Analisador de Dados Interativo com Streamlit

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.25%2B-red.svg)

Uma aplicação web gráfica e interativa desenvolvida em Python para análise rápida e visualização de dados a partir de arquivos no formato CSV.

## Demonstração

![Demonstração do App](assets/demo.gif)

## Instalação e Pré-requisitos

### Pré-requisitos
* **Python 3.9** ou superior instalado na máquina.
* Gerenciador de pacotes **pip**.

### Passo a Passo de Instalação

1. Clone o repositório para o seu ambiente local:
```bash
git clone [https://github.com/seu-usuario/analisador-de-dados.git](https://github.com/seu-usuario/analisador-de-dados.git)
```

2. Acesse a pasta do projeto:

```Bash
cd analisador-de-dados
```

3. Instale as dependências listadas no projeto:

```Bash
pip install -r requirements.txt
```

### Uso e Exemplos
Para iniciar o servidor web do Streamlit e carregar a interface gráfica, execute o comando abaixo:

```Bash
streamlit run src/app.py
```

### Como Usar a Aplicação
1. Clique no botão Browse files na tela inicial para fazer upload de qualquer arquivo .csv.
   
2. Visualize as primeiras linhas da tabela renderizada na tela.

3. Confira métricas rápidas de contagem de linhas e colunas.

4. Analise a tabela de estatísticas descritivas (média, desvio padrão, min, max, etc.).

5. Escolha uma coluna numérica no menu suspenso para gerar um histograma de frequência.

6. O navegador será aberto automaticamente no endereço local http://localhost:8501.

### Estrutura do Projeto
```Plaintext
analisador-de-dados/
├── assets/
│   └── demo.gif
├── src/
│   └── app.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

### Descrição dos Arquivos Principais
src/app.py: Código-fonte principal com a interface gráfica construída via Streamlit e lógica de análise com Pandas.

assets/demo.gif: Imagem/GIF demonstrando o uso da interface web.

requirements.txt: Lista de dependências e bibliotecas Python necessárias para rodar o projeto.

LICENSE: Termos da licença MIT sob a qual o projeto está distribuído.

README.md: Documentação oficial com instruções completas de configuração e uso.

### Licença
Este projeto está sob a licença MIT. Para mais informações, acesse o arquivo LICENSE.

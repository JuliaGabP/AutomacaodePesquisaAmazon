# Automação de Pesquisa de Produtos na Amazon

Este é um script em Python desenvolvido com o objetivo de automatizar pesquisas de produtos na Amazon Brasil utilizando Selenium.

O programa realiza uma busca a partir do termo informado pelo usuário no terminal, acessa a página de resultados da Amazon, coleta os links dos produtos encontrados e abre automaticamente os 5 primeiros resultados no navegador padrão do sistema.

## Objetivo do projeto

O principal objetivo deste projeto é praticar conceitos de:

- automação web com Python;
- navegação automatizada com Selenium;
- interação com elementos de páginas web;
- abertura automática de páginas no navegador.

Este projeto também permite compreender a diferença entre páginas simples que podem ser manipuladas com `requests` e `BeautifulSoup`, e páginas mais dinâmicas, que exigem ferramentas de automação de navegador, como o Selenium.

## Como o projeto funciona

O script executa automaticamente as seguintes etapas:

1. recebe o termo de pesquisa digitado pelo usuário no terminal;
2. abre o site da Amazon Brasil no navegador;
3. localiza a barra de pesquisa da página;
4. digita o termo pesquisado;
5. envia a busca;
6. coleta os links dos produtos exibidos;
7. filtra apenas os links válidos de produtos;
8. remove links duplicados;
9. abre automaticamente os 5 primeiros produtos encontrados.

## Tecnologias e bibliotecas utilizadas

Este projeto foi desenvolvido com as seguintes tecnologias:

- **Python 3**
- **Selenium** permite controlar o navegador automaticamente;
- **webbrowser** abre páginas no navegador padrão do sistema;
- **sys** lê os argumentos digitados na execução do script;
- **time** adiciona pausas para permitir o carregamento da página.

## Estrutura do projeto

```bash
searchamazon.py
README.md
```

## Executando o projeto

```bash
python searchamazon.py item_consultado

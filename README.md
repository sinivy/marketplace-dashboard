# Marketplace Analytics Dashboard

Dashboard interativo construído com **Streamlit + Pandas + Plotly** para análise de desempenho de um marketplace.

---

## Objetivo

O projeto tem como objetivo visualizar e monitorar indicadores importantes de um marketplace, como:

- Receita total
- Vendas concluídas
- Ticket médio
- Taxa de cancelamento
- Desempenho de vendedores
- Performance por categoria
- Evolução das vendas ao longo do tempo

---

## Tecnologias utilizadas

- Python 🐍
- Streamlit
- Pandas
- Plotly Express

---

## Estrutura esperada dos dados

O dashboard utiliza um arquivo CSV com a seguinte estrutura básica:

| coluna      | descrição                        |
|------------|----------------------------------|
| data       | Data da venda                   |
| categoria  | Categoria do produto            |
| vendedor   | Nome do vendedor               |
| status     | Status da venda (Concluído/Cancelado/Em andamento) |
| valor      | Valor da transação             |

---

## Funcionalidades

- Filtros dinâmicos
Filtragem por categoria
Filtragem por vendedor

- KPIs principais
Receita total
Número de pedidos concluídos
Ticket médio
Taxa de cancelamento

- Destaques
Melhor vendedor
Melhor categoria

- Visualizações
Receita por categoria (barra)
Distribuição de pedidos (pizza)
Receita mensal
Top 5 vendedores
Evolução de vendas no tempo (linha)

---

## Observações

Este projeto foi desenvolvido com foco em prática de análise de dados + visualização interativa, podendo ser expandido para aplicações reais de BI.

## Autor

Projeto desenvolvido para estudo de Data Analytics para Portfólio por Sinivy.
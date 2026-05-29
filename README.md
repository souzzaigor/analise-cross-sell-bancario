# 🎯 Análise de Propensão e Cross-Sell Bancário

## 📌 Contexto e Problema de Negócio
No setor bancário, conquistar novos clientes é mais caro do que vender novos produtos para a base atual. Este projeto visa otimizar uma campanha de **Cross-Sell (Venda Cruzada)** de Empréstimos Pessoais para clientes que já possuem conta no banco, mas que ainda não utilizam linhas de crédito.

O objetivo é evitar gastos desnecessários com marketing em massa e focar apenas nos clientes com maior probabilidade (propensão) de aceitar a oferta.

## ⚙️ Pipeline de Dados e Feature Engineering

### 1. Preparação e Enriquecimento (Python / Pandas)
**Arquivo:** `Tratamento_Dados.py`
Para gerar inteligência, o dado bruto precisava ser categorizado. Utilizei Python para criar regras de negócio (*Feature Engineering*) em cima do comportamento do cliente:
* **Segmentação de Renda:** Categorização dos clientes em faixas (Baixa, Média e Alta Renda).
* **Perfil de Gasto:** Classificação baseada no uso médio do cartão de crédito.
* **Score de Propensão:** Criação de um algoritmo simples que cruza o gasto médio no cartão com a renda anual para classificar o cliente em: `Alta Propensão`, `Média Propensão` ou `Baixa Propensão`.

### 2. Validação da Conversão (SQL)
**Arquivo:** `consultas_cross_sell.sql`
* Criação de consultas para validar a eficácia da regra de propensão no banco de dados.
* Cálculo da **Taxa de Conversão (%)** agrupando os clientes que efetivamente aceitaram o empréstimo dentro de cada faixa de propensão.

### 3. Visualização (Power BI)
* Consumo da base enriquecida para criação de um dashboard tático.
* O painel permite que a equipe comercial filtre os clientes de "Alta Propensão" por CEP e Escolaridade, direcionando as ligações do call center de forma assertiva.

## 🚀 Impacto do Projeto
Ao classificar os clientes, a equipe de marketing consegue reduzir o custo de aquisição (CAC) e aumentar o Retorno sobre o Investimento (ROI) da campanha, ligando apenas para quem tem o perfil financeiro adequado para o crédito.

<img width="1531" height="859" alt="Captura de tela 2026-04-24 220639" src="https://github.com/user-attachments/assets/b1360bb3-0d60-47ba-9a92-86daee4d7960" />


---
**Desenvolvido por:** Igor Carvalho de Souza
*Graduação em Análise e Desenvolvimento de Sistemas - Universidade São Francisco (USF)*

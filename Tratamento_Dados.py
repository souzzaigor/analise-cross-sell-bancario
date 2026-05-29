# %%
import pandas as pd
# %%
df = pd.read_csv("../Bank_Personal_loan_Modelling.csv")
df.head()
# %%
df.columns = ['ID_Cliente', 'Idade', 'Anos_Experiencia', 'Renda_Anual_Mil', 'CEP', 
    'Tamanho_Familia', 'Gasto_Medio_Cartao', 'Escolaridade', 'Valor_Hipoteca', 
    'Aceitou_Emprestimo', 'Conta_Investimento', 'Conta_CD', 
    'Usa_Internet_Banking', 'Tem_Cartao_Credito_Banco'
    ]
df.columns

# %%
# Segmentações Estratégicas para o Power BI
def classificar_renda(renda):
    if renda <= 40: return 'Baixa Renda (Até 40k)'
    elif renda <= 80: return 'Média Renda (41k - 80k)'
    else: return 'Alta Renda (Acima de 80k)'

df['Segmento_Renda'] = df['Renda_Anual_Mil'].apply(classificar_renda)
# %%
# Perfil de Gasto no Cartão
def classificar_gasto_cartao(gasto):
    if gasto < 1.0: return 'Gasto Baixo'
    elif gasto <= 2.5: return 'Gasto Médio'
    else: return 'Gasto Alto'

df['Perfil_Gasto'] = df['Gasto_Medio_Cartao'].apply(classificar_gasto_cartao)
#%%
# Classificando quem tem o perfil ideal para receber a oferta
def calcular_propensao(row):
    if row['Renda_Anual_Mil'] > 80 and row['Gasto_Medio_Cartao'] > 2.5:
        return 'Alta Propensão'
    elif row['Renda_Anual_Mil'] > 50 or row['Gasto_Medio_Cartao'] > 1.5:
        return 'Média Propensão'
    else:
        return 'Baixa Propensão'

df['Propensao_Emprestimo'] = df.apply(calcular_propensao, axis=1)
#%%
# 5. Exportando a Base Enriquecida e Limpa
nome_arquivo = 'Base_CrossSell_Bancario.csv'
df.to_csv(nome_arquivo, index=False)

print(f"Base tratada com sucesso! Arquivo salvo como: {nome_arquivo}")
print("\nUma prévia dos dados:")
display(df[['ID_Cliente', 'Renda_Anual_Mil', 'Gasto_Medio_Cartao', 'Segmento_Renda', 'Propensao_Emprestimo']].head())
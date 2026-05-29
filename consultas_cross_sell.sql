-- Validando a taxa de conversão da campanha de Empréstimo Pessoal
-- Agrupando pelos perfis de propensão gerados no Python

SELECT 
    Propensao_Emprestimo,
    COUNT(ID_Cliente) AS total_clientes_alvo,
    SUM(Aceitou_Emprestimo) AS clientes_que_converteram,
    ROUND((SUM(Aceitou_Emprestimo) * 100.0) / COUNT(ID_Cliente), 2) AS taxa_conversao_percentual
FROM 
    tb_base_cross_sell
GROUP BY 
    Propensao_Emprestimo
ORDER BY 
    taxa_conversao_percentual DESC;

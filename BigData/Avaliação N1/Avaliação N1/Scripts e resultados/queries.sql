--1. perfil de cliente que mais compra (por gênero, estado civil e faixa etária de idade)
SELECT 
    vls."Sexo",
    vls."Estado Civil",
    CASE 
        WHEN vls."Idade" BETWEEN 18 AND 25 THEN '18-25'
        WHEN vls."Idade" BETWEEN 26 AND 30 THEN '26-30'
        WHEN vls."Idade" BETWEEN 31 AND 40 THEN '31-40'
        WHEN vls."Idade" BETWEEN 41 AND 50 THEN '41-50'
        ELSE '50+'
    END AS faixa_etaria,
    ROUND(AVG(vls."Valor_venda")::numeric, 2) AS ticket_medio,
    COUNT(*) AS quantidade_vendas
FROM vendas_loja_seminovos vls
GROUP BY 
    vls."Sexo", 
    vls."Estado Civil",
    faixa_etaria
ORDER BY ticket_medio DESC;

--2. classificação dos veículos que os perfis dos clientes mais compram
SELECT
    vls."Sexo",
    vls."Estado Civil",
    CASE 
        WHEN vls."Idade" BETWEEN 18 AND 25 THEN '18-25'
        WHEN vls."Idade" BETWEEN 26 AND 30 THEN '26-30'
        WHEN vls."Idade" BETWEEN 31 AND 40 THEN '31-40'
        WHEN vls."Idade" BETWEEN 41 AND 50 THEN '41-50'
        ELSE '50+'
    END AS faixa_etaria,
    CASE 
        WHEN vls."Valor_venda" < 40000 THEN 'Econômico'
        WHEN vls."Valor_venda" BETWEEN 40000 AND 80000 THEN 'Intermediário'
        ELSE 'Premium'
    END AS categoria_preco,
    COUNT(*) AS total_vendas,
    ROUND(AVG(vls."Valor_venda")::numeric, 2) AS ticket_medio
FROM vendas_loja_seminovos vls
GROUP BY
    vls."Sexo",
    vls."Estado Civil",
    faixa_etaria,
    categoria_preco
ORDER BY total_vendas DESC;

--3. ticket médio de vendas por data
SELECT 
    TO_CHAR(vls."Data_venda"::date, 'YYYY-MM') AS ano_mes, --converte a data que é string e nomeia como mes
    ROUND(AVG(vls."Valor_venda")::numeric, 2) AS ticket_medio --trazendo a média (AVG) e apenas 2 casas decimais após a vírgula (ROUND e Numeric)
FROM vendas_loja_seminovos vls
GROUP BY ano_mes
ORDER BY ano_mes;

--4. Quantas vendas cada marca faz em suas categorias
SELECT 
    vls."Marca",
    COUNT(*) as volume_vendas,
    SUM(vls."Valor_venda") as receita_total,
    ROUND(AVG(vls."Valor_venda")::numeric, 2) AS ticket_medio,
    CASE 
        WHEN vls."Valor_venda" < 40000 THEN 'Econômico'
        WHEN vls."Valor_venda" BETWEEN 40000 AND 80000 THEN 'Intermediário'
        ELSE 'Premium'
    END AS categoria_preco
FROM vendas_loja_seminovos vls
GROUP BY vls."Marca", categoria_preco 
order by receita_total desc, ticket_medio DESC;

--5. distribuição por estado
SELECT 
    vls."Estado",
    COUNT(*) as total_vendas
FROM vendas_loja_seminovos vls
GROUP BY vls."Estado"
ORDER BY total_vendas DESC;  

--6. qual mês que mais vende
SELECT 
    to_char(vls."Data_venda"::date, 'MM') as mes,
    COUNT(*) as total_vendas
FROM vendas_loja_seminovos vls
GROUP BY to_char(vls."Data_venda"::date, 'MM')
ORDER BY mes desc;


--ticket médio de vendas por veículo
SELECT 
    vls."Marca" ,
    vls."Modelo",
    ROUND(AVG(vls."Valor_venda")::numeric, 2) AS ticket_medio
FROM vendas_loja_seminovos vls
GROUP BY vls."Marca", vls."Modelo" 
ORDER BY ticket_medio DESC; --mais vendido para o menos vendido


--ticket médio de vendas por perfil de cliente (tipo de cliente que mais compra)
SELECT 
    vls."Sexo",
    vls."Estado Civil",
    ROUND(AVG(vls."Valor_venda")::numeric, 2) AS ticket_medio
FROM vendas_loja_seminovos vls
GROUP BY vls."Sexo", vls."Estado Civil"
ORDER BY ticket_medio DESC;


--classificação por faixa de preço
SELECT *,
    CASE 
        WHEN vls."Valor_venda" < 40000 THEN 'Econômico'
        WHEN vls."Valor_venda" BETWEEN 40000 AND 80000 THEN 'Intermediário'
        ELSE 'Premium'
    END AS categoria_preco
FROM vendas_loja_seminovos vls 



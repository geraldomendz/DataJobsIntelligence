CREATE OR ALTER VIEW vw_total_vagas_empresa AS

SELECT
    c.nome AS empresa,
    COUNT(*) AS total_vagas
FROM jobs j
JOIN companies c
    ON j.company_id = c.id
GROUP BY c.nome;
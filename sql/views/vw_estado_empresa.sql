CREATE OR ALTER VIEW vw_estado_empresa AS

SELECT
    c.nome AS empresa,
    ISNULL(j.estado,'Não informado') AS estado,
    COUNT(*) AS vagas
FROM jobs j
JOIN companies c
    ON j.company_id = c.id
GROUP BY
    c.nome,
    ISNULL(j.estado,'Não informado');
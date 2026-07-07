CREATE OR ALTER VIEW vw_estados AS

SELECT
    ISNULL(estado,'Não informado') AS estado,
    COUNT(*) AS vagas
FROM jobs
GROUP BY
    ISNULL(estado,'Não informado');
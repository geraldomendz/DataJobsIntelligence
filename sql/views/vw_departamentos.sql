CREATE OR ALTER VIEW vw_departamentos AS

SELECT
    departamento,
    COUNT(*) AS vagas
FROM jobs
GROUP BY departamento;
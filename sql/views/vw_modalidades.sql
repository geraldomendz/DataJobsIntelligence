CREATE OR ALTER VIEW vw_modalidades AS

SELECT
    modalidade,
    COUNT(*) AS vagas
FROM jobs
GROUP BY modalidade;
SELECT
    departamento,
    COUNT(*) AS vagas
FROM jobs
GROUP BY departamento
ORDER BY vagas DESC;
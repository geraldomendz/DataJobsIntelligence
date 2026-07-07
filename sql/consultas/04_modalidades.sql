SELECT
    modalidade,
    COUNT(*) AS vagas
FROM jobs
GROUP BY modalidade
ORDER BY vagas DESC;
SELECT
    estado,
    COUNT(*) AS vagas
FROM jobs
GROUP BY estado
ORDER BY vagas DESC;
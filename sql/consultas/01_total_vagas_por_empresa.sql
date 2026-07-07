SELECT
    c.nome AS empresa,
    COUNT(*) AS total_vagas
FROM jobs j
INNER JOIN companies c
    ON j.company_id = c.id
GROUP BY c.nome
ORDER BY total_vagas DESC;
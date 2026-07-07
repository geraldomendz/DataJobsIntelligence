SELECT
    c.nome,
    j.estado,
    COUNT(*) AS vagas
FROM jobs j
INNER JOIN companies c
    ON j.company_id = c.id
GROUP BY
    c.nome,
    j.estado
ORDER BY
    c.nome,
    vagas DESC;
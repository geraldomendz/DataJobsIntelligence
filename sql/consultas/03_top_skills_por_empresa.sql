SELECT
    c.nome,
    js.skill,
    COUNT(*) AS quantidade
FROM job_skills js
INNER JOIN companies c
    ON js.company_id = c.id
GROUP BY
    c.nome,
    js.skill
ORDER BY
    c.nome,
    quantidade DESC;
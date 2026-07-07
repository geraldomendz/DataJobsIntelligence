SELECT
    c.nome,
    COUNT(*) AS vagas
FROM job_skills js
INNER JOIN companies c
    ON js.company_id = c.id
WHERE js.skill = 'Python'
GROUP BY c.nome
ORDER BY vagas DESC;
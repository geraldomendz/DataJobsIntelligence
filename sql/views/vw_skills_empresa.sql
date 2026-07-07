CREATE OR ALTER VIEW vw_skills_empresa AS

SELECT
    c.nome AS empresa,
    js.skill,
    COUNT(*) AS quantidade
FROM job_skills js
JOIN companies c
    ON js.company_id = c.id
GROUP BY
    c.nome,
    js.skill;
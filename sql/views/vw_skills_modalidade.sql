CREATE OR ALTER VIEW vw_skills_modalidade AS

SELECT
    j.modalidade,
    js.skill,
    COUNT(*) AS quantidade
FROM jobs j
JOIN job_skills js
    ON j.id = js.job_id
GROUP BY
    j.modalidade,
    js.skill;
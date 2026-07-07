SELECT
    j.modalidade,
    js.skill,
    COUNT(*) AS quantidade
FROM jobs j
INNER JOIN job_skills js
    ON j.id = js.job_id
GROUP BY
    j.modalidade,
    js.skill
ORDER BY
    j.modalidade,
    quantidade DESC;
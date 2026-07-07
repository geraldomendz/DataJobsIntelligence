SELECT
    skill,
    COUNT(*) AS quantidade
FROM job_skills
GROUP BY skill
ORDER BY quantidade DESC;
CREATE OR ALTER VIEW vw_top_skills AS

SELECT
    skill,
    COUNT(*) AS quantidade
FROM job_skills
GROUP BY skill;
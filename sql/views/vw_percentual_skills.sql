CREATE OR ALTER VIEW vw_percentual_skills AS

SELECT
    skill,
    COUNT(*) AS quantidade,

    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(DISTINCT id) FROM jobs),
        2
    ) AS percentual
FROM job_skills
GROUP BY skill;
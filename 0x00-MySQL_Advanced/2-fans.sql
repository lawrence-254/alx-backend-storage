-- SQL script that ranks country origins of bands,
--ordered by the number of (non-unique) fan
CREATE TEMPORARY TABLE tmp_fan_counts AS
SELECT origin, COUNT(*) AS nb_fans
FROM bands
GROUP BY origin;
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;

SELECT band_name, (2022 - formed) AS lifespan
FROM bands
WHERE split LIKE '%Glam rock%'
ORDER BY lifespan DESC;


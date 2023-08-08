-- Lists bands using Glam rock style, ranked by longevity
SELECT  band_name,
        IFNULL(split,2022) - IFNULL(formed,0) AS lifespan
FROM metal_bands
WHERE style like '%Glam rock%'
ORDER BY 2 DESC; 

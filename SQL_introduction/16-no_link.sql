-- lists score and name for records that have a name, best first
SELECT score, name FROM second_table WHERE name IS NOT NULL
    ORDER BY score DESC;

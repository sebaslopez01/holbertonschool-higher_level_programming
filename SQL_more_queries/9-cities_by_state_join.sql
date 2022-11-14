-- Cities by state
SELECT cities.id, cities.name, states.name FROM cities NATURAL JOIN states ORDER BY cities.id;

SELECT name, imdb_rating FROM movies;

SELECT DISTINCT FROM movies; --No duplication in cols.

SELECT * FROM movies
WHERE imdb_rating > 8; --Where clause filters querty

SELECT * FROM movies
WHERE name LIKE 'Se_en';

--name LIKE Se_en is a condition evaluating the name column for a specific pattern.
--The _ means you can substitute any individual character here.
-- Seven|Se7en

SELECT * FROM movies
WHERE name LIKE 'a%';

SELECT * FROM movies
WHERE name LIKE '%man%';

--a% matches all movies with names that begin with "A"
--%man% any movie that contains the word "man" in its name will be displayed

SELECT * FROM movies
WHERE year BETWEEN 1990 AND 2000 --range
AND genre = 'comedy'; --adding another condition

SELECT * FROM movies
ORDER BY imdb_rating DESC; --ORDERING!

SELECT * FROM movies
ORDER BY imdb_rating DESC
LIMIT 3; --let you specify the maximum number of rows the result set will have.


------------------------------------------------------------


SELECT COUNT(*) FROM fake_apps;
--calculate the number of rows in a table is to use the COUNT() function.


SELECT COUNT(*) FROM fake_apps
WHERE price = 0;
---add condition

SELECT price, COUNT(*) FROM fake_apps
GROUP BY price;
-- GROUP BY is a clause in SQL that is only used with aggregate functions.
-- It is used in collaboration with the SELECT statement to arrange
-- identical data into groups.

SELECT price, COUNT(*) FROM fake_apps
WHERE downloads > 20000
GROUP BY price;

SELECT SUM(downloads) FROM fake_apps;
--add all values in a particular column using SUM().

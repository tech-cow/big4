--**********************************
          -- Overview
-- CREATE TABLE creates a new table.
-- INSERT INTO adds a new row to a table.
-- SELECT queries data from a table.
-- UPDATE edits a row in a table.
-- ALTER TABLE changes an existing table.
-- DELETE FROM deletes rows from a table.

--**********************************



--**********************************
-- Create a Table
--**********************************
CREATE TABLE table_name(  --create a table in a database.
	column_1 data_type, -- name & its data type
  column_2 data_type,
  column_3 data_type
);


-- Example
CREATE TABLE celebs(  --create a table named celebs in a database.
  id INTERGER,      --set column name to id, and correspoding datatype to Int.
  name TEXT,
  age INTERGER
);

--**********************************
--Insert Values into a table
--**********************************
INSERT INTO celebs (id,name,age) --insert new records in a table
VALUES (1,'Justin Bieber',21);

--**********************************
-- Query data in celebs table
--**********************************
SELECT * FROM celebs;
-- The SELECT statement is used to select data from a database.
-- the result stores in celebs, which is a table/relation/result set

--**********************************
-- Update a row in celebs
--**********************************
UPDATE celebs
SET age = 22  --edit a selected column
WHERE id = 1; --indicates which row

--**********************************
-- Insert a new column and give its data_type
--**********************************
ALTER TABLE celebs  --make a change in a table
ADD COLUMN twitter_handle TEXT;  --twitter_handle that holds string data_type

--**********************************
-- Insert/clearing something into the new column
--**********************************
UPDATE celebs
SET twitter_handle = '@taylorswift13'
WHERE id = 4;
--**********************************
-- Delete all of the rows that have a NULL value in the twitter column.
--**********************************
DELETE FROM celebs  --statement allows to delete row in a table
WHERE twitter_handle IS NULL;

SELECT * FROM celebs;

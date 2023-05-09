# Write your MySQL query statement below
# SELECT DISTINCT email FROM Person
# WHERE COUNT(SELECT DISTINCT email FROM Person) > 1;

SELECT email FROM Person 
GROUP BY email 
HAVING COUNT(email)>1
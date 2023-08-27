# Write your MySQL query statement below
# SELECT A.name AS Employee FROM Employee A
# INNER JOIN Employee B
#     ON A.id = B.managerId
# WHERE A.


SELECT name AS Employee FROM Employee A
WHERE salary > (SELECT salary FROM Employee WHERE id = A.managerId)

/* Write your T-SQL query statement below */
SELECT unique_id, name FROM Employees EM
FULL OUTER JOIN EmployeeUNI EMU
    ON EM.id = EMU.id
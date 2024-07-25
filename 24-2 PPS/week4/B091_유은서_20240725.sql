-- SELECT name AS Employee
-- FROM Employee as E
-- WHERE E.salary > (
--     SELECT salary
--     FROM Employee
--     WHERE E.managerid = id
-- )
SELECT e2.name as Employee
FROM employee e1
INNER JOIN employee e2 ON e1.id = e2.managerID
WHERE
e1.salary < e2.salary
-- 코드를 작성해주세요
SELECT s.score, e.emp_no, emp_name, position, email
FROM hr_employees e JOIN
    (SELECT SUM(score) as score, emp_no
    FROM hr_grade
    GROUP BY emp_no) s 
ON e.emp_no = s.emp_no
ORDER BY score DESC
LIMIT 1;
-- a.  Student.objects.all()
SELECT * FROM STUDENT
-- b.  Student.objects.filter(first_name__iexact='Charlie')
SELECT * FROM STUDENT WHERE FIRST_NAME = 'CHARLIE'
-- c.  Student.objects.filter(first_name__istartswith='C')
SELECT * FROM STUDENT WHERE FIRST_NAME LIKE 'C%' OR FIRST_NAME LIKE 'c%'
-- d.  Student.objects.filter(first_name__startswith='C')
SELECT * FROM STUDENT WHERE FIRST_NAME LIKE 'C%'
-- e.  Student.objects.filter(first_name__contains='har')
SELECT * FROM STUDENT WHERE FIRST_NAME LIKE '%har%'
-- f.  Student.objects.filter(first_name__exact='Charlie').exclude(last_name__exact='Garrod')
SELECT * FROM STUDENT WHERE FIRST_NAME LIKE 'Charlie' AND LAST_NAME != 'GARROD'

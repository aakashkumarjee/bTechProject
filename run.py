from first import startSql, getSql_like
import sys
print("started")
#query = sys.argv[1]
#query = "get name, score, cityName of employee with score  equal to 5"
query = input("Enter Query\n")
db = input("Enter Path to SQL Dump\n")
a = startSql(str(query), str(db))
#a = startSql(str(query), "./emp.sql")
# a = getSql_like(str(query), "./emp.sql")
print(a)
print("done")

# get all names from emp

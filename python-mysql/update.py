import mysql.connector

dbcon = None
cursor = None

try:
    dbcon = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='9am'
    )
    cursor = dbcon.cursor()
    

    sql_st = "UPDATE* FROM employee"
    cursor.execute(sql_st)

    employees = cursor.fetchall()
    print(type(employees))
    print("Total employees:", len(employees))


    for emp in employees:
        print(emp[1])

except mysql.connector.Error as err:
    print("Error:", err)

finally:
    if cursor:
        cursor.close()
    if dbcon:
        dbcon.close()
        

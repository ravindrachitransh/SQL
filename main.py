from choice import *
import psycopg2
import psycopg2.extras
# from SQL_Project import connection
from functions import *

def main_():
    db_params = {
        'dbname':"Hospital",
        'user':"postgres",
        'password':"password",
        'host':"localhost",
        'port':"5432"
    }
    
    connection = psycopg2.connect(**db_params)
    cur= connection.cursor(cursor_factory=psycopg2.extras.DictCursor)


    while True:
        
        choice = show_menu()
        if choice == 0:
            clear_screen()
            print("Goodbye")
            break
        if choice == 1:
            
            cur.execute("""
        SELECT age,
            COUNT(CASE WHEN hospital_death = '1' THEN 1 END) as amount_that_died,
            COUNT(CASE WHEN hospital_death = '0' THEN 1 END) as amount_that_survived
        FROM patient
        GROUP BY age
        ORDER BY age ASC; """)
    # Fetch the results
            results = cur.fetchall()
            # print(results)
            age_death(results)

        if choice == 2:
            cur.execute("""
        SELECT ethnicity, COUNT(hospital_death) as total_hospital_deaths
        FROM patient 
        WHERE hospital_death = '1'
        GROUP BY ethnicity;  """)
            rows = cur.fetchall()
            print(rows)
            ethnicity_deaths(rows)
            
        if choice == 3:
            cur.execute("""SELECT
    ROUND(SUM(CASE WHEN aids = 1 THEN 1 ELSE 0 END) * 100 / COUNT(*),2) AS aids_percentage,
    ROUND(SUM(CASE WHEN cirrhosis = 1 THEN 1 ELSE 0 END) * 100 / COUNT(*),2) AS cirrhosis_percentage,
    ROUND(SUM(CASE WHEN diabetes_mellitus = 1 THEN 1 ELSE 0 END) * 100 / COUNT(*),2) AS diabetes_percentage,
    ROUND(SUM(CASE WHEN hepatic_failure = 1 THEN 1 ELSE 0 END) * 100 / COUNT(*),2) AS hepatic_failure_percentage,
    ROUND(SUM(CASE WHEN immunosuppression = 1 THEN 1 ELSE 0 END) * 100 / COUNT(*),2) AS immunosuppression_percentage,
    ROUND(SUM(CASE WHEN leukemia = 1 THEN 1 ELSE 0 END) * 100 / COUNT(*),2) AS leukemia_percentage,
    ROUND(SUM(CASE WHEN lymphoma = 1 THEN 1 ELSE 0 END) * 100 / COUNT(*),2) AS lymphoma_percentage,
    ROUND(SUM(CASE WHEN solid_tumor_with_metastasis = 1 THEN 1 ELSE 0 END) * 100 / COUNT(*),2) AS solid_tumor_percentage
FROM patient
WHERE hospital_death = 1;""")
            result = cur.fetchall()
            medical_condition_deaths(result)

            
main_()
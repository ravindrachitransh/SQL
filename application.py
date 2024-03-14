from choice import show_menu
from functions import *
from SQL_Project import age_deaths
# Exploratory Data Analysis

#Taking choice Input
choice = show_menu()

if choice==1:
    age_deaths()
elif choice==2:
    ethnicity_deaths()
elif choice==3:
    medical_condition_deaths()
elif choice==4:
    ICU_type_deaths()
elif choice==5:
    BMI_deaths()
else:
    print("wrong choice")
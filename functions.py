import numpy as np
import numpy as np
import matplotlib.patheffects as path_effects
import matplotlib.pyplot as plt

def age_death(result):
        # Separate the data for plotting
    ages = [record['age'] for record in result]
    deaths = [record['amount_that_died'] for record in result]
    survivals = [record['amount_that_survived'] for record in result]

    # Define the age intervals
    intervals = [(0, 10), (11, 20), (21, 30), (31, 40), (41, 50), (51, 60), (61, 70), (71, 80), (81, 90), (91, 100)]

    # Initialize lists for intervals
    interval_deaths = [0] * len(intervals)
    interval_survivals = [0] * len(intervals)

    # Assign each age to an interval
    for i, age in enumerate(ages):
        if age is not None:  # Skip None values
            for interval_index, (start, end) in enumerate(intervals):
                if start <= age <= end:
                    interval_deaths[interval_index] += deaths[i]
                    interval_survivals[interval_index] += survivals[i]
                    break

    # Plotting
    x_labels = [f"{start}-{end}" for start, end in intervals]
    x = np.arange(len(x_labels))

    plt.figure(figsize=(10, 6))
    plt.bar(x, interval_deaths, label='Died', color='red')
    plt.bar(x, interval_survivals, bottom=interval_deaths, label='Survived', color='green')
    plt.xlabel('Age Intervals')
    plt.ylabel('Number of Patients')
    plt.title('Hospital Mortality by Age Intervals')
    plt.xticks(x, x_labels)
    plt.legend()
    plt.show()


def ethnicity_deaths(rows):
    # Separate data for the pie chart
    labels = [row[0] for row in rows]
    values = [row[1] for row in rows]

    # Plotting the pie chart
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Distribution of Hospital Deaths by Ethnicity')
    plt.show()


def medical_condition_deaths(result):
    

    # Separate data for the pie chart
    labels = [
        'AIDS', 'Cirrhosis', 'Diabetes Mellitus', 'Hepatic Failure',
        'Immunosuppression', 'Leukemia', 'Lymphoma', 'Solid Tumor'
    ]
    values = result[0]

    # Plotting the pie chart
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Distribution of Patients who Died due to Different Medical Conditions')
    plt.show()


def ICU_type_deaths():
    pass


def BMI_deaths():
    pass
        







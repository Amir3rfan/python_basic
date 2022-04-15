import csv
# For the average
from statistics import mean 

def calculate_averages(input_file_name, output_file_name):
    with open(input_file_name) as f :
        reader = csv.reader(f)
        for row in reader:
            name = row[0]
            these_grades = list()
            for grade in row[1:]:
                these_grades.append(int(grade))
            final = list()
            final.append(name)
            final.append(mean(these_grades))
            print(final)

calculate_averages('input_file_name.csv', 'output_file_name.csv')

# def calculate_sorted_averages(input_file_name, output_file_name):
    


# def calculate_three_best(input_file_name, output_file_name):
    


# def calculate_three_worst(input_file_name, output_file_name):
    


# def calculate_average_of_averages(input_file_name, output_file_name):



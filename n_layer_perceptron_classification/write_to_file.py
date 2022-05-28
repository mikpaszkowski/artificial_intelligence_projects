import csv

header = ['layers', 'time', 'accuracy', 'cross-validation-accuracy', 'MSE', 'MAE', 'cross-entropy']

def write_to_file(rows):
    with open('result_data.csv', 'w', newline='') as f:
        #create the csv writer
        writer = csv.writer(f)

        #write header
        writer.writerow(header)

        writer.writerows(rows)

import csv
row_list = [["SN", "Name", "Experience"],
             [1, "sai", "1year"],
             [2, "akhil", "2year"],
             [3, "kolla", "3year"]]
with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)

with open('students.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
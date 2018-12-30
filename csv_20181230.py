import csv

example_file = open('example.csv')
example_reader = csv.reader(example_file)

for row in example_reader:
    print('Row #' + str(example_reader.line_num) + ' ' + str(row))
# example_date = list(example_reader)

output_file = open('output.csv', 'w', newline='')
output_writer = csv.writer(output_file)
output_writer.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
output_file.close

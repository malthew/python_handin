import csv
import platform

def print_file_content(file):
    with open(file) as file_object:
        content = file_object.readlines()
    for line in content[:20]:
        print(line.strip().split(','))

def write_list_to_file(output_file, lst):
    if platform.system() == 'Windows':
        newline=''
    else:
        newline=None

    with open(output_file, 'a+', newline=newline) as output_file:
        output_writer = csv.writer(output_file)

        output_writer.writerow(lst)

## def read_csv(input_file):

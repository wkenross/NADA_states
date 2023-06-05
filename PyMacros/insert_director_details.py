import argparse
import csv
import openpyxl

parser = argparse.ArgumentParser(description='Process CSV file and paste values into Excel sheet')
parser.add_argument('csv_file', metavar='csv_file', type=str, help='path to CSV file')
parser.add_argument('file_path', metavar='file_path', type=str, help='path to CSV file')
parser.add_argument('sheet_name', metavar='sheet_name', type=str, help='name of sheet to paste values into')
args = parser.parse_args()

wb = openpyxl.load_workbook(args.file_path)
sheet = wb[args.sheet_name]
wb.active = sheet

with open(args.csv_file, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        arg_name = row[0]
        value = row[1]
        header = row[2]
        if arg_name and value:
            cell = sheet[arg_name]
            cell.value = value
            if header:
                sheet.cell(row=5, column=cell.column).value = header

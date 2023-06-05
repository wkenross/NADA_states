# Script that activates the sheet named "Georgia" in the active workbook 
# and loops across the column cells in row 5 until it finds the label "email":

import argparse
import os
import xlwings as xw

import win32com.client as win32
import sys

with open(sys.argv[1], 'r') as f:
    args = f.read().split()

print(args)

# Create an argument parser to accept headline argument
parser = argparse.ArgumentParser()

parser.add_argument('file_path', nargs='?', default = '', help=r'C:\Projects\govt\NADA_states_marketing_list.xlsx')
parser.add_argument('State_Name', nargs='?', default = '', help='Entity Name Text')
parser.add_argument('Entity', nargs='?', default = '', help='Entity Name Text')
parser.add_argument('Website', nargs='?', default = '', help='Entity Website Text')
parser.add_argument('Address', nargs='?', default = '', help='Address Text')
parser.add_argument('City', nargs='?', default = '', help='City Text')
parser.add_argument('State', nargs='?', default = '', help='State Text')
parser.add_argument('Zip', nargs='?', default = '', help='Zip Text')
parser.add_argument('Key_Contact', nargs='?', default = '', help='Key Contact Text')
parser.add_argument('Title', nargs='?', default = '', help='Title Text')
parser.add_argument('Phone', nargs='?', default = '', help='Phone Text')
parser.add_argument('Email', nargs='?', default = '', help='Email Text')


# Parse the arguments
args = parser.parse_args()

# Access the optional arguments
arg1 = args.arg1 or ''
arg2 = args.arg2 or ''
arg3 = args.arg3 or ''
arg4 = args.arg4 or ''
arg5 = args.arg5 or '' 
arg6 = args.arg6 or ''
arg7 = args.arg7 or ''
arg8 = args.arg8 or ''
arg9 = args.arg9 or ''
arg10 = args.arg10 or ''
arg11 = args.arg11 or ''
arg12 = args.arg12 or ''

# Get the value of the Headline argument
if args.State_Name == '':
    ws_name = 'Georgia'
else:
    ws_name = args.State_Name

# Path to the Excel file
if args.file_path == '':
    file_path = r'C:\Projects\govt\NADA_states_marketing_list.xlsx'
else:
    file_path = args.file_path

# Verify that the file exists
if os.path.exists(file_path):
    # Open the file using xlwings and the 'Georgia' sheet
    wb = xw.Book(file_path)
    ws = wb.Sheets(ws_name)
    ws.Activate()
else:
    print(f'The file "{file_path}" does not exist.')   
    exit()

# Loop across the column cells in row 5 until it finds Entity Name column
row = 5
column = 1
while True:
    cell = ws.Cells(row, column)
    value = cell.Value
    if value == 'Entity Name':
        print(f'Found "{value}" at cell {cell.Address}')
        break
    elif value is None:
        print('End of column reached without finding "email"')
        break
    else:
        column += 1

# Find the last row with data in the "Entity Name" column
last_row = ws.Cells(ws.Rows.Count, 'B').End(-4162).Row

# Loop through the rows of the "Entity Name" column to find the first blank cell
for row in range(1, last_row+1):
    if not ws.Cells(row, 'B').Value:
        # Select the cell 3 rows down from the blank cell and set its row as the target row
        target_row = ws.Cells(row+3, 'B').Row
        entity_cell= ws.Cells(row+3, 'B').select()
        entity_cell.Value = args.Entity
        break

# Initialize the counter cell to the cell immediately to the right of Entity_cell
target_cell = entity_cell.offset(row=0, column=1)
url = input("Enter hyperlink for cell '{}': ".format(target_cell.coordinate))
# Set the current cell to a hyperlink with the Address text and the specified link
target_cell.formula = args.website
# '=HYPERLINK("{}","Address")'.format(url)


# Loop through row 5 starting from Entity cell
while ws.cell(row=5, column=target_cell.column).value is not None:
    # Check if current cell is the Address or City column
    if target_cell.offset(row=0, column=2).value == 'Address':
        target_cell.value = args.Address
        target_cell.offset(row=1, column=0).value= args.Address
    elif target_cell.offset(row=0, column=2).value == 'City':
        target_cell.value = 'Atlanta'
        target_cell.offset(row=1, column=0).value = 'Atlanta'
    elif target_cell.offset(row=0, column=2).value == 'State':
        target_cell.value = 'GA'
        target_cell.offset(row=1, column=0).value = 'GA'
    elif target_cell.offset(row=0, column=2).value == 'Zip Code':
        # Set the value for the next column over as 30349
        target_cell.value = 30349
        target_cell.number_format = 'General'
        target_cell.offset(row=1, column=0).value = args.zip
        target_cell.offset(row=1, column=0).format = 'General'

    elif target_cell.offset(row=0, column=2).value == 'Key Contact':
        # Set the value for the next column over as 'Joe Walter'
        target_cell.value = args.Key_Contact
        target_cell.offset(row=1, column=0).value = 'Michael Smith'
    elif target_cell.offset(row=0, column=2).value == 'Title':
        target_cell.value = args.Title
        target_cell.offset(row=1, column=0).value = 'Deputy Commissioner'

    elif target_cell.offset(row=0, column=2).value == 'Phone':
        # Set the value for the next column over as 'phone'
        target_cell.value = args.phone
        target_cell.offset(row=1, column=0).value = args.phone
    elif target_cell.offset(row=0, column=2).value == 'Email':
        # Set the value for the next column over as 'Email'
        target_cell.value = args.Email
        target_cell.offset(row=1, column=0).value = args.email
        break

    # Move to the next cell in the same row
    target_cell = target_cell.offset(row=0, column=1)

# Save the Excel file
# wb.save('my_excel_file.xlsx')

# Do something with the target row, such as printing its value
print(f"The target row is {target_row}")
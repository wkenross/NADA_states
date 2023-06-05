import argparse
import os
import xlwings as xw

# Create an argument parser to accept headline argument
parser = argparse.ArgumentParser()
# parser.add_argument('$headline', help='headline to insert in the new row')
parser.add_argument('Headline', type=str, help='a string for headline')
args = parser.parse_args()

# Get the value of the Headline argument
headline = args.Headline

# Path to the Excel file
file_path = r'C:\Projects\govt\NADA_states_marketing_list.xlsx'

# Verify that the file exists
if os.path.exists(file_path):
    # Open the file using xlwings and select the 'Target 28' sheet
    wb = xw.Book(file_path)
    sheet = wb.sheets['Target 28']
    sheet.activate()
    # Loop through the cells in column B to find the cell that contains 'Georgia'
    if headline == 'open':
        exit
    else:
        for cell in sheet.range('B1:B' + str(sheet.cells.last_cell.row)):
            if cell.value == 'Georgia':
                # Select the cell
                cell.select()
                # Insert a new row below the selected cell
                sheet.api.Rows(cell.row+1).Insert(Shift=xw.constants.InsertShiftDirection.xlShiftDown)
                # Paste headline string in the column to the right of the newly inserted row
                sheet.range(f'C{cell.row+2}').value = headline
                break  # exit the loop once the cell is found
        else:
            print('Could not find "Georgia" in column B.')
else:
    print(f'The file "{file_path}" does not exist.')


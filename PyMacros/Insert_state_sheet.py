
import argparse
import os
import xlwings as xw

# Create an argument parser to accept headline argument
parser = argparse.ArgumentParser()
# parser.add_argument('$headline', help='headline to insert in the new row')
parser.add_argument('State_Name', type=str, help='a string for headline')
args = parser.parse_args()

# Get the value of the Headline argument
sheet_name = args.State_Name
# headline = 'This is a test headline'

# Path to the Excel file
file_path = r'C:\Projects\govt\NADA_states_marketing_list.xlsx'

# Verify that the file exists
if os.path.exists(file_path):
    # Open the file using xlwings and select the 'Target 28' sheet
    wb = xw.Book(file_path)
    copy_sheet = wb.sheets['Minnesota']
    copy_sheet.api.Copy(Before=copy_sheet.api)

    # Get the new sheet, which is the new active sheet now
    new_sheet = wb.sheets.active

    # Rename the new sheet as 'Georgia'
    new_sheet.name = 'Georgia'

    # Clear the content of rows 6 through 12 of the new sheet
    new_sheet.range('6:12').clear_contents()

    # Activate the new sheet
    new_sheet.activate()

    sheet = wb.sheets['Target 28']
    sheet.activate()
    # Loop through the cells in column B to find the cell that contains 'Georgia'
    for cell in sheet.range('B1:B' + str(sheet.cells.last_cell.row)):
        if cell.value == 'Georgia':
            # Select the cell
            cell.select()
            # Get the selected cell and copy the row beneath it too
            selected_cell = xw.apps.active.selection
            selected_row = selected_cell.row
            row_range = str(selected_cell.row) + ':' + str(selected_cell.row + 1)
            row_data = xw.apps.active.range(row_range).value                
            break  # exit the loop once the cell is found
    else:
        print('Could not find "Georgia" in column B.')
    
    # Paste the row data on cell A6 of the new sheet
    new_sheet.range('A6').value = row_data
    new_sheet.activate()
    new_sheet['M10'].select()

else:
    print(f'The file "{file_path}" does not exist.')


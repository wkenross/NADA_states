import argparse
import win32com.client as win32


def run_excel_macro(macro_name, workbook_path):
    # Open Excel application
    excel = win32.gencache.EnsureDispatch('Excel.Application')

    # Open workbook and enable macros
    workbook = excel.Workbooks.Open(workbook_path, ReadOnly=False, Password='')
    workbook.EnableAutoRecover = False
    excel.DisplayAlerts = False

    # Run specified macro
    excel.Application.Run(macro_name)

    # Save and close workbook, and quit Excel application
    workbook.Save()

    # Show first sheet and keep workbook open
    workbook.Windows(1).Visible = True
    workbook.Windows(1).WindowState = win32.constants.xlMaximized
    excel.Visible = True
    excel.DisplayAlerts = True



if __name__ == '__main__':
    # Create argument parser
    parser = argparse.ArgumentParser(description='Run an Excel macro from a Python script')

    # Add arguments
    parser.add_argument('macro_name', help='name of the macro to run')
    parser.add_argument('workbook_path', help='path to the macro-enabled workbook')

    # Parse arguments
    args = parser.parse_args()

    # Call function with arguments

    run_excel_macro(args.macro_name, args.workbook_path)


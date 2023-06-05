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
    # workbook.Save()
    # workbook.Close()
    # excel.Quit()

    # return workbook

def GetMacroList():
    # Get a reference to the currently active workbook
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    
    # Get list of available macros
    macros = excel.Application.Run("'vba_macros.xlsm'!Module1.GetMacroList")

    # Loop through each module and sheet in the workbook
        # For each module, loop through each line of code and check if it is a procedure
        # If it is a procedure, add it to the list of available macros
        # Return the list of available macros
        # Need to add GetMacroList to vba_macros.xlsm
        # Also need to Enable All Macros in Excel Trust Center and Trust accss  to the VBA project object model in Macro Settings   

    # Display list of available macros
    print("Available macros:")

    for macro in macros:
        print("- " + macro)


# Save and close workbook, and quit Excel application
# workbook = run_excel_macro("hello_world", r"C:\projects\PyMacros\vba_macros.xlsm")
# workbook.Save()
# workbook.Close()
# excel.Quit()

# Open Excel application
# excel = win32.gencache.EnsureDispatch('Excel.Application')

# Open workbook and enable macros
# workbook = excel.Workbooks.Open(r'C:\projects\PyMacros\vba_macros.xlsm', ReadOnly=False, Password='')
# workbook.EnableAutoRecover = False
# excel.DisplayAlerts = False
# excel.Application.Run("'vba_macros.xlsm'!Module1.hello_world")


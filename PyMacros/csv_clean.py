import xlwings as xw

# Get handle to current active workbook and active sheet
wb = xw.books.active
sheet = wb.sheets.active
# Widen remaining columns
sheet.range('A:XFD').columns.autofit()

def clean_csv(input_file, output_file):
    # Read input CSV file into DataFrame
    df = pd.read_csv(input_file)

    # Remove columns with labels "apikey", "ip", and "id"
    if 'apiKey' in df.columns:
        df.drop('apiKey', axis=1, inplace=True)
    if 'ip' in df.columns:
        df.drop('ip', axis=1, inplace=True)
    if 'id' in df.columns:
        df.drop('id', axis=1, inplace=True)

    # Remove rows with missing data
    df.dropna(inplace=True)

    # Drop duplicate rows
    df.drop_duplicates(inplace=True)

    # Write cleaned DataFrame to output CSV file
    df.to_csv(output_file, index=False)


if __name__ == '__main__':
    input_file = 'input.csv'
    output_file = 'output.csv'
    clean_csv(input_file, output_file)

    # Save cleaned Excel workbook to specified file path and name
    output_file = 'c:/projects/metrics/api_metrics/Northbridge_logs_2023-04.xlsx'
    wb.save(output_file)

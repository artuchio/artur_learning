# # Import the necessary libraries
# import requests
# from bs4 import BeautifulSoup as BS
# import csv
# import pandas as PD
#
# # Step 1: Define the URL of the webpage with the table
# url = 'https://www.ilmateenistus.ee/ilm/ilmavaatlused/vaatlusandmed/oopaevaandmed/?lang=en'
#
# # Step 2: Send a GET request to the URL to fetch the webpage content
# response = requests.get(url)
#
# if response.ok:    # Step 3: Check if the request was successful (HTTP status code 200)
#     soup = BS(response.text, 'html.parser')  # Parse the HTML content of the page with Beautiful Soup
#     table = soup.find('table')
#     table_data = [] # Initialize a list to store the extracted data
#
#     if table:
#         # Find all table row tags
#         rows = table.find_all('tr') # If the table is found, iterate over its rows
#         start_collecting = False    # Flags to identify the start and end of the desired data segment
#
#         for row in rows:
#             # Check for the start of the desired data range
#             if 'Haapsalu' in row.text:
#                 start_collecting = True
#
#             # If within the desired range, extract the data
#             if start_collecting:
#                 row_data = [cell.text.strip() for cell in row.find_all('td')] # Extract text from each cell (column) in the row
#                 table_data.append(row_data)
#
#                 # Check for the end of the desired data range
#                 if 'Väike-Maarja' in row.text:
#                     break
#
#     # Write the data to a CSV file
#     csv_file_path = 'weather_data.csv'
#     with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerows(table_data)
#
#     print(f'Data written to {csv_file_path}')
# else:
#     # If the request failed, print an error message
#     print('Failed to retrieve the webpage. Status code:', response.status_code)
#
#
# # Step 9: Use pandas to read the CSV file and format it for display
# # Load the CSV data into a pandas DataFrame
# df = PD.read_csv(csv_file_path)
#
# # Display the DataFrame in a pretty-printed tabular format
# print(df.to_string(index=False))
#
# df = PD.read_csv('weather_data.csv') # Read your CSV file
#
# # Create a Pandas Excel writer using XlsxWriter as the engine
# excel_file_path = 'weather_data.xlsx'
# writer = PD.ExcelWriter(excel_file_path, engine='xlsxwriter')
#
# # Convert the dataframe to an XlsxWriter Excel object
# df.to_excel(writer, sheet_name='Sheet1', index=False)
#
# # Get the xlsxwriter workbook and worksheet objects
# workbook = writer.book
# worksheet = writer.sheets['Sheet1']
#
# # Set the column width and format
# for column in df:
#     column_length = max(df[column].astype(str).map(len).max(), len(column))
#     col_idx = df.columns.get_loc(column)
#     writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_length)
#
# writer._save() # Close the Pandas Excel writer and output the Excel file
#
#
import requests
from bs4 import BeautifulSoup as BS
import csv
url = 'https://www.ilmateenistus.ee/ilm/ilmavaatlused/vaatlusandmed/oopaevaandmed/?lang=en'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
response = requests.get(url, headers=headers)
soup = BS(response.text, 'html.parser')

table_data = soup.find('tbody').find_all('tr')
print(table_data)

with open('wearther.csv', 'w') as weather_file:
    csv_writer = csv.writer(weather_file, lineterminator='\n')
    for row in table_data:
        row_data = []
        for cell in row.find_all('td'):
            row_data.append(cell.text)
        print(row_data)



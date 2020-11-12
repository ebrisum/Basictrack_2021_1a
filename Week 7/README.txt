READ ME:

This python program is used to create invoices and store
information about the companies/individuals. 

First an overview of all files, secondly
an overview of the function(s) used and then an overview
of the overall program flow.


Basictrack.py:


*Files*
Invoice-Template.xlsx:	Template used to output new invoice
			excel file. (existing cells get replaced)
invoices.csv	:	history of generated invoices
			(ID, Date, time, Company, Total)
company_address.csv:	All companies and addresses
			(Company, Address)

Output file of the program:
company + '#' + (new_id) + 'xlsx'


*Function(s)*
def invoice_generator(): is used to create the invoice itself,
With the use of a format named: 'Invoice-Template.xlsx'.
Most of the things in this file could be changed, such as logo,
extra information, etc. However, in this functions we make
use of specific locations within the excel file (current_row and
current_column (16,2)). Therefore any changes that add/delete 
columns/rows could result in the needed change of the variables
current_row and/or current_columns. These variables decide from
where the data is added, always set these parameters to the cell
that represents the left upper corner in the table. 
With the use of openpyxl I load the format into python where 
I use a dictionary of lists to make pairs that replace certain
values in the excel file. 

Inputs: 
company, address, date, new_id

Output:
Excel file named: 
company + '#' + (new_id) + 'xlsx'


*Program flow*
1. Opening CSV files ('company_address.csv' and 'invoices.csv')
2. Creating pandas DataFrame.
3. Generating ID
4. Asking for the Company name for the invoice
5. Checking if company already exists
	yes: --> finding and storing address in variable
	no: --> creating new address variable and storing it
		in 'company_address.csv'
6. Asking for input and store these in lists
	(VAT-rates are asked to the user)
7. Store inputs in 'invoice.csv'


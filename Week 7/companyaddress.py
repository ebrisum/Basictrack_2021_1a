
company = input("company name: ")
companies = []
addresses = []

#check if it exists:
with open("file", 'r') as company_address:
    for line in company_address:
        company_name, address = line.split(",")
        companies.append(company_name)
        addresses.append(address)



address = input("address: ")
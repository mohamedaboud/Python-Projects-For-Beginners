email=input('Please enter your email in correct format xxxxx@yyyyy.zzzz : ')

# Getting user name and domain
(username, domain) = email.split('@')

# Getting company name from domain name 
companyname, domainsuffix= domain.split('.')

# Output User Name And Company Name
print('User Name Is: ', username)
print('Company Name Is: ', companyname)

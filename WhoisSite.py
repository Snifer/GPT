import whois

data = raw_input("Insert URL for the <Whois> site information: www.")
domain = whois.query(data)

print '\n'
print '*****************************************************'
print '*  Whois information'+ ' ' + str(data)+ ' ' + '*'
print '*****************************************************'
print 'Domain Name: ' + str(domain.domain_name)
print 'Creation date: ' + str(domain.creation_date)
print 'Expiration Date: ' + str(domain.expiration_date)
print 'Register: ' + str(domain.registrar)

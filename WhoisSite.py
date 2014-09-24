import whois

data = raw_input("Insert URL for the <Whois> site information: ")
whoisData = whois.whois(data)
whoisSite = data

print '\n'
print '********************************************'
print '*  Whois information'+ ' ' + str(whoisSite)+ '*'
print '********************************************'
#Brute data
print 'Domain Name: ' + str(whoisData.domain_name)
print 'Emails registered: ' + str(whoisData.emails)
print 'Creation date: ' + str(whoisData.creation_date)
print 'Expiration Date: ' + str(whoisData.expiration_date)
print 'Last Update: ' + str(whoisData.updated_date)


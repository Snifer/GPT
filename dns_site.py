import sys
import DNS

siteDNS = raw_input("Insert site retrieve DNS: ")

DNS.DiscoverNameServers()
request = DNS.Request()
for qt in DNS.Type.A, DNS.Type.AAAA, DNS.Type.CNAME, DNS.Type.MX, DNS.Type.NS:
    response = request.req(name = siteDNS, qtype = qt)
    for answer in response.answers:
        print answer['name'], answer['classstr'], answer['typename'], \
            repr(answer['data'])

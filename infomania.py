import sys
import whois
import dns.resolver
import shodan
import requests
import argparse
import socket
argparse = argparse.ArgumentParser(description="This is a basic information gathering tool", usage="python3 infomania.py -d DOMAIN")
argparse.add_argument("-d","--domain",help="Enter the domain name for footprinting.")
argparse.add_argument("-o","--output",help="Enter the file to write output to.")

args = argparse.parse_args()
domain = args.domain
output = args.output

# whois module
print("[+] Getting whois info.")
whois_result = ''
# using whois library, creating instance
try:
    py = whois.query(domain)
    print("[+] whois info found.")
    whois_result += "Name: {}"+format(py.name) + '\n'
    whois_result += "Registrar: {}".format(py.registrar) + '\n'
    whois_result += "Creation Date: {}".format(py.creation_date) + '\n'
    whois_result += "expiration date: {}".format(py.expiration_date) + '\n'
    whois_result += "Registrant: {}".format(py.registrar) + '\n'
    whois_result += "registrant Country: {}".format(py.registrant_country) + '\n'


except:
    pass
print(whois_result)

#DNS module

print("[+] Getting DNS indo..")
dns_result = ''
#implementing dns.resolver from dnspython
try:
    for a in dns.resolver.resolve(domain, 'A'):
        dns_result += "[+] A Record: {}".format(a.to_text()) + '\n'

    for ns in dns.resolver.resolve(domain, 'NS'):
        dns_result += "[+] NS Record: {}".format(ns.to_text()) + '\n'
    for mx in dns.resolver.resolve(domain,'MX'):
        dns_result += "[+] MX Record: {}".format(mx.to_text()) + '\n'
    for txt in dns.resolver.resolve(domain, 'TXT'):
        dns_result += "[+] TXT Record: {}".format(txt.to_text()) + '\n'
except:
    pass
print(dns_result)

#Geolocation module
print("[+] Getting geolocation info..")
geo_result = ''

#implementing requests for web request
try:
    response = requests.request('GET',"https://geolocation-db.com/json/" + socket.gethostbyname(domain)).json()
    geo_result += "[+] Country: {}".format(response['country_name']) + '\n'
    geo_result += "[+] Latitude: {}".format(response['latitude']) + '\n'
    geo_result += "[+] Longitude: {}".format(response['longitude']) + '\n'
    geo_result += "[+] City: {}".format(response['city']) + '\n'
    geo_result += "[+] State: {}".format(response['state']) + '\n'

except:
    pass
print(geo_result)

if (output):

    with open(output, 'w') as file:

        file.write(whois_result + '\n\n')
        file.write(dns_result + '\n\n')
        file.write(geo_result + '\n\n')

import sys
import whois
import dns.resolver
import shodan
import requests
import argparse
import socket
argparse = argparse.ArgumentParser(description="This is a basic information gathering tool", usage="python3 infomania.py -d DOMAIN")
argparse.add_argument("-d","--domain",help="Enter the domain name for footprinting.")

args = argparse.parse_args()
domain = args.domain

# whois module
print("[+] Getting whois info.")
# using whois library, creating instance
try:
    py = whois.query(domain)
    print("[+] whois info found.")
    print("Name: {}"+format(py.name))
    print("Registrar: {}".format(py.registrar))
    print("Creation Date: {}".format(py.creation_date))
    print("expiration date: {}".format(py.expiration_date))
    print("Registrant: {}".format(py.registrar))
    print("registrant Country: {}".format(py.registrant_country))

except:
    pass
#DNS module
print("[+] Getting DNS indo..")
#implementing dns.resolver from dnspython
try:
    for a in dns.resolver.resolve(domain, 'A'):
        print("[+] A Record: {}".format(a.to_text()))
    for ns in dns.resolver.resolve(domain, 'NS'):
        print("[+] NS Record: {}".format(ns.to_text()))
    for mx in dns.resolver.resolve(domain,'MX'):
        print("[+] MX Record: {}".format(mx.to_text()))
    for txt in dns.resolver.resolve(domain, 'TXT'):
        print("[+] TXT Record: {}".format(txt.to_text()))
except:
    pass
#Geolocation module
print("[+] Getting geolocation info..")

#implementing requests for web request
try:
    response = requests.request('GET',"https://geolocation-db.com/json/" + socket.gethostbyname(domain)).json()
    print("[+] Country: {}".format(response['country_name']))
    print("[+] Latitude: {}".format(response['latitude']))
    print("[+] Longitude: {}".format(response['longitude']))

    print("[+] City: {}".format(response['city']))

    print("[+] State: {}".format(response['state']))

except:
    pass
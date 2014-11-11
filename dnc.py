#!/usr/bin/env python

from __future__ import print_function
import xmlrpclib

k = os.getenv("GANDI_APIKEY")
if not k:
    print("Please set the GANDI_APIKEY environment variable. Exiting.")
    exit()

endpoint = os.getenv("GANDI_APIURL", "https://rpc.gandi.net/xmlrpc/")
if endpoint == "OTE":
    print("Using OTE endpoint.")
    endpoint = "https://rpc.ote.gandi.net/xmlrpc/"
api = xmlrpclib.ServerProxy(endpoint)

def add(fqdn, target):
    # Accept a subdomain or domain, point it at a target 
    # If a CNAME record exists already, raise an error/prompt
    # If an A record exists, add another and warn the user
    # If -f option is specified, just do it
    # Figure out if target is IPv4 or IPv6
    pass

def rm(fqdn):
    # Remove all records for a given FQDN or wildcard
    # Prompt, unless -f is given
    pass

def dig(fqdn, rr):
    # Return all records of a given type for a given FQDN

def dig_any(fqdn):
    # Return all records of any type for a given FQDN

def list_zone(domain):
    # Show full zone file--all subdomains--for a given domain

def guess_type(resource_record):
    rr=resource_record

def is_ipv4(input):
    # Determine if input is a valid IPv4 address
    pass

def is_ipv6(input):
    # Determine if input is a valid IPv6 address
    pass

if __name__ == "__main__"



    # Parse input

    # If action is "add", test if it's compatible with existing records, if any

    # If action is "remove", do it

    # If action is "dig", return existing values

    # TODO: TTL



"So i was tied to the bed in a telletubby costume and then she breaks out the cheese grater and i was like "holy shit, it's Christmas!" William, at the White Horse in Seattle



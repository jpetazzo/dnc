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





#!/usr/bin/env python3
# Check hostname against expected value

## Collect input from user
hostname = input("What value should we set for hostname?")

if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("hostname matches expected config")

print("Exiting the script")

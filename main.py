#!/usr/bin/python3
import requests
import argparse

def dirScan(url, words):
    response = requests.get(url)
    print(f'{response.status_code}: {url}')
    i = 1
    while i < len(words):
        response = requests.get(url+'/'+words[(i-1)])
        print(response.status_code)
        if(response.status_code == 200):
            print(f'{response.status_code}: {url}')
        if(response.status_code == 301 or response.status_code == 302):
            print(f'{response.status_code}: {url}')
        #else:
        #    print(f'{response.status_code}: {url}')
        print(i, url+'/'+words[(i-1)])
        i += 1

# Set default wordlist file if user does not supply one
wordlist_file = 'path/to/wordlist/file'

# Start argument parser
parser = argparse.ArgumentParser(
        prog='',
        description='Simple directory brute forcer',
        add_help=True
        )

parser.add_argument("-u", type=str, required=False, help="Provide the URL")
parser.add_argument("-w", type=str, required=False, help="Wordlist file to use")
options = parser.parse_args()

# Set url and wordlist file based on user input
if options.u:
    url = options.u
if options.w:
    wordlist_file = options.w

# Open wordlist file 
file = open(wordlist_file, 'r')
words = file.readlines()
file.close()


# If no options were selected, error and stop program.
if not any(vars(options).values()):
            parser.error("No arguments provided. Must use at least `-u [URL_TO_SCAN]`")


dirScan(url, words)


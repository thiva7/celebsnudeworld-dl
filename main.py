import argparse
from bs4 import BeautifulSoup
import requests



def get_links(url):
    # create a requests to url.com get the html
    r = requests.get(url, verify=False)
    # create a BeautifulSoup object
    soup = BeautifulSoup(r.text, 'html.parser')
    # find all the links in the page
    links = soup.find_all('a')
    # create a list to store the links
    celebs = []
    # loop through the links
    for link in links:
        # get the link
        link = link.get('href')
        # check if the link is not empty and if it is not a link to the homepage

            # append the link to the list
        celebs.append(link)
    # loop through the list
    for celeb in celebs:
        filename = url.replace('https://', '')
        if filename.endswith('/'):
            filename = filename.replace('/', '')
        # create a requests to the link and get the html
        with open(f'{filename}.txt', 'a') as f:
            f.write(celeb + '\n' )



# create a argument parser object
parser = argparse.ArgumentParser(description='Process some Website.')

# add long and short argument
parser.add_argument("--url", "-u", help="The URL to scrape" , required=True)


# read arguments from the command line
args = parser.parse_args()

# check for --url and get links
get_links(args.url)



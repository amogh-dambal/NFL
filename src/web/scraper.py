# python 3.6
# script to scrape through provided
# urls and obtain data on NFLML
# passers from seasons

from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
import requests
import csv

# with a pre loaded list of urls
# get all the data from them as csv files
# write them to .csv files


# extract table data from a url
# to a CSV file
# TODO: implement for advanced statistics
def get_pff_data(url):
	try:
		r = requests.get(url)
		r.raise_for_status()

		bs = BeautifulSoup(r.text, 'html.parser')
		table = bs.find('table', {'id': 'passing'})

		raw_header = table.find_all('th')
		header = []
		for th in raw_header[:31]:
			header.append(th.text)

		rows = []
		for tr in table.find_all('tr'):
			cols = tr.find_all('td')
			row = []
			for col in cols:
				row.append(col.text)
			rows.append(row)

		filename = get_filename(url)
		with open(filename, "w") as f:
			wr = csv.writer(f)
			wr.writerow(header)
			wr.writerows(rows)

	except HTTPError as http_err:
		print(f"HTTP error! {http_err}")
		print(f"Could not complete url request for url:{url}")


def get_fo_data(url):
	try:
		r = requests.get(url)
		r.raise_for_status()

		bs = BeautifulSoup(r.text, 'html.parser')
		table = bs.find('table')

		header = [h.text for h in table.find_all('th')]

		rows = []
		for tr in table.find_all('tr'):
			cols = tr.find_all('td')
			row = []
			for col in cols:
				row.append(col.text)
			rows.append(row)

		filename = get_filename(url)
		with open(filename, "w") as f:
			wr = csv.writer(f)
			wr.writerow(header)
			wr.writerows(rows)

	except HTTPError as http_err:
		print(f"HTTP error! {http_err}")
		print(f"Could not complete url request for url:{url}")


def get_filename(url):
	path = "../../data/"
	extension = ".csv"
	prefix = "years/"

	if prefix in url:
		index = url.find(prefix) + 6
		fmt = url[index:index+4]
	else:
		fmt = url
	return path + fmt + extension


def generate_urls(start=2010, end=2018, utype="passing", adv=False):
	'''Specific function to generate urls to
	PFF basic quarterback statistic tables
	:param start: the season to start looking for data
	:param end: the season to end looking for data
	:param utype: the type of table to look for ('passing', 'rushing', 'receiving')
	:param adv: boolean flag that fetches advanced data
	:return:
	'''
	if start < 2000 or end > 2018 or end < start:
		raise RuntimeError("Invalid parameters")

	urls = []
	dest = "http://pro-football-reference.com/years/"
	if adv:
		suffix = "/" + utype.lower() + "_advanced.htm"
	else:
		suffix = "/" + utype.lower() + ".htm"

	for year in range(start, end + 1):
		urls.append(dest + str(year) + suffix)

	return urls


def scrape(urls, source):
	for url in urls:
		if source is 'PFF':
			get_pff_data(url)
		elif source is 'FO':
			get_fo_data(url)


# PFF Reference
# all_urls = generate_urls()
# scrape(all_urls)

# Football Outsiders
fo_url = "https://www.footballoutsiders.com/stats/qb/2018"

# Recipe scraper | Practing web scraping

## What this app does

This is a script to collect recipes from the Dutch recipes site Smulweb.nl.

## Used technologies and concepts

- BeautifulSoup, Requests, Regex to fetch and parse HTML
- Django as ORM for postgres DB
- Amazon RDS as 'receiving postgres DB'
- Amazon EC2 as Ubuntu virtual machine to run the script

## Goal of this project

The goal of this project is entirely educatinonal/practice. I learned these tools independently by following online courses and tutorials and consulting forums like StackExchange. Specific goals were:

- [learn how to scrape sites](https://github.com/tdijkmans/recipefree-django/blob/master/recipefree/Smulwebscraper.py)
- learn how to parse HTML data to JSON/csv
- learn how to run this from 'the cloud' using Amazon EC2
- [learn how to store data in 'the cloud' using Amazon RDS/Django ORM](https://github.com/tdijkmans/recipefree-django/blob/master/recipefree/collector/models.py)

NB Although not evident from the code, I was able to scrape recipes from using an AWS EC2 Ubuntu instance, storing the data in an AWS RDS db.

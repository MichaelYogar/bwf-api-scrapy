## BWF API WEB SCRAPER

## Motivation

Since a public badminton player API does not exist, I decided to build one for a future project I want to create.

## Features

Languges: Python, Typescript \
Technologies: Scrapy, Node.js, Express.js, MySQL

-   scrapes data based on player rankings from [BWF](https://bwfbadminton.com/rankings/) using the Scrapy framework
-   created a pipeline to store up to 5000 rows of data into a MySQL database daily
-   developed REST API with Express.js to display scraped data

## Requirements

Requires node, npm, python3, virutalenv, and scrapy installed

## Running Web Scraper

1. `git clone https://github.com/MichaelYogar/bwf-api-scrapy.git`
2. `virtualenv ./`
3. `pip install -r requirements.txt`
4. Add environment variables for your MySQL database
    - E.g. add environment variables to your `config.fish`
    - Refer to `/bwf-api-scrapy/bwf_crawler/pipelines.py`

```
DB_NAME=
DB_User=
DB_PASS=
```

In same folder as scrapy.cfg, run `scrapy crawl api`

## Running Server

1. Run `npm install`
2. Create `.env` file in same folder as `db.ts` and add:

```
DB_NAME=
DB_USER=
DB_PASS
```

3. Run `npm run dev`

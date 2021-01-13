## BWF API WEB SCRAPER


## Features

Languges: Python, Typescript \
Technologies: Scrapy, Node.js, Express.js, MySQL


## Prereqs

You'll need node, npm, python3, virutalenv, and scrapy installed

## Running Web Scraper

1. `git clone https://github.com/MichaelYogar/bwf-api-scrapy.git`
2. `virtualenv ./`
3. `pip install -r requirements.txt`
4. Add environment variables for your MySQL database 
    - E.g. add environment variables to your `config.fish`
    - Refer to `/bwf-api-scrapy/bwf_crawler/pipelines.py`
```
DB_User=
DB_PASS=
DB_NAME=
```


In same folder as scrapy.cfg, run `scrapy crawl api`

## Running Server

1. Run `npm install`
2. Create `.env` file in same folder as `db.ts` and add:

```
MYSQL_HOST=
DB_NAME=
DB_USER=
DB_PASS
```

3. Run `npm run dev`




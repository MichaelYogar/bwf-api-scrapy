# bwf-api-scrapy

## Install

1. `git clone https://github.com/MichaelYogar/bwf-api-scrapy.git`
2. `virtualenv ./`
3. `pip install -r requirements.txt`
4. Add environment variables for your MySQL database 
    - E.g. add environment variables to your `config.fish`
    - Refer to `/bwf-api-scrapy/bwf_crawler`
```
DB_User=
DB_PASS=
DB_NAME=
```

## Scraping

In same folder as scrapy.cfg, run `scrapy crawl api`

## Running Server

1. Run `npm install`
2. Run `npm run dev`

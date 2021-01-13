import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
from bwf_crawler.items import ApiItem
from scrapy.loader import ItemLoader
import json



class ApiSpider(CrawlSpider):
    name = 'api'

    # An optional list of strings containing domains that this spider is allowed to crawl.
    allowed_domains = ['bwfbadminton.com']
    base_url = 'http://bwfbadminton.com/rankings'


    def find_nth(self, haystack, needle, n):
        start = haystack.find(needle)
        while start >= 0 and n > 1:
            start = haystack.find(needle, start+len(needle))
            n -= 1
        return start

    def addOne(self, s):
        val = int(s.group(1))
        return str(val+1)
    

    def start_requests(self):
        yield scrapy.Request(url='https://bwfbadminton.com/rankings/')

    # rules contain at least one rule tuple
    rules = (
        Rule(LinkExtractor(allow=('rankings/2/bwf-world-rankings/'),), callback='parse_item', follow=True),
    )


    def parse_item(self, response):

        items = ApiItem()

        rows = response.xpath('//tr[not(@class="tr-ranking-detail")]') # returns a list of selector objects, each selector object represents a full <a /> element
        category = response.xpath('normalize-space(//li[@class="active"]/a/text())').get()

        url = response.url
        page_index = self.find_nth(url, '=', 2) + 1
        current_page= int(url[page_index:]) + 1
        next_page = str(current_page)
        parsed_url = url[:page_index] + next_page 

        # since its an selector object, can use xpath against it
        for row in rows:
            rank = row.xpath('.//td[1]/text()').get()
            country = row.xpath('normalize-space(.//td[2]/div/span/text())').get()

            player_selector = row.xpath('.//td[3]/div/span/a')
            player = player_selector.xpath('.//@title').getall()

            rank_change = row.xpath('.//td[4]/span/text()').get()
            win_loss = row.xpath('normalize-space(.//td[5]/text())').get()
            prize = row.xpath('.//td[6]/text()').get()
            points = row.xpath('.//td[7]/strong/text()').get()

            # name_link = link.xpath('.//@href').get()

            items['rank'] = rank
            items['country'] = country
            items['player'] = json.dumps(player)
            items['rank_change'] = rank_change
            items['win_loss'] = win_loss
            items['prize'] = prize
            items['points'] = points
            items['category'] = category 
            items['parsed_url'] = parsed_url

            yield items

        is_div_present = response.xpath('//div[@class="player"]')
        if is_div_present:
            yield response.follow(parsed_url, self.parse_item)
                


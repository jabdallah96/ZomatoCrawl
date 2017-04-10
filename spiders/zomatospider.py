import scrapy
from scrapy.spiders import Spider
from re import findall
from ZomatoTest.items import Restaurant
from ZomatoTest.items import RestItemLoader

class ZomatoSpider(Spider):
    name = 'zomatospider'
    allowed_domains = ['zomato.com']
    start_urls = [
        'https://www.zomato.com/beirut/restaurants?page=1',
        'https://www.zomato.com/beirut/restaurants?page=2',
        'https://www.zomato.com/beirut/restaurants?page=3',
        'https://www.zomato.com/beirut/restaurants?page=4',
        'https://www.zomato.com/beirut/restaurants?page=5',
        'https://www.zomato.com/beirut/restaurants?page=6',
        'https://www.zomato.com/beirut/restaurants?page=7',
        'https://www.zomato.com/beirut/restaurants?page=8',
        'https://www.zomato.com/beirut/metn-restaurants?page=2',
        'https://www.zomato.com/beirut/metn-restaurants?page=3',
        'https://www.zomato.com/beirut/metn-restaurants?page=4',
        'https://www.zomato.com/beirut/metn-restaurants?page=5',
        'https://www.zomato.com/beirut/metn-restaurants?page=6',
        'https://www.zomato.com/beirut/metn-restaurants?page=7',
        'https://www.zomato.com/beirut/metn-restaurants?page=8',
        'https://www.zomato.com/beirut/metn-restaurants?page=9',
        'https://www.zomato.com/beirut/metn-restaurants?page=10',
        'https://www.zomato.com/beirut/harissa-restaurants?all=1',
        'https://www.zomato.com/beirut/harissa-restaurants?all=2',
        'https://www.zomato.com/beirut/harissa-restaurants?all=3',
        'https://www.zomato.com/beirut/jounieh-restaurants?all=1',
        'https://www.zomato.com/beirut/jounieh-restaurants?all=2',
        'https://www.zomato.com/beirut/jounieh-restaurants?all=3',
        'https://www.zomato.com/beirut/badaro-restaurants?all=1',
        'https://www.zomato.com/beirut/badaro-restaurants?all=2',
        'https://www.zomato.com/beirut/badaro-restaurants?all=3',
        'https://www.zomato.com/beirut/jbeil-restaurants?all=1',
        'https://www.zomato.com/beirut/jbeil-restaurants?all=2',
        'https://www.zomato.com/beirut/jbeil-restaurants?all=3'
    ]


    def parse(self, response):
        for rest in response.css('a.result-title'):
            url = rest.xpath('@href').extract()[0]
            yield scrapy.Request(url, callback=self.parse_rest)

        next_link = response.css('li.current + li.active a').xpath('@href').extract()
        print ("NEXT LINK:", next_link)
        if next_link:
            yield scrapy.Request(response.urljoin(next_link[0]), callback=self.parse)

    def parse_rest(self, response):
        
        rest = RestItemLoader(item=Restaurant(), response=response)

        rest.add_css('r_name', "h1.res-name a::attr(title)") #
        rest.add_xpath('r_id', '//*/@data-res-id') #
        rest.add_css('r_type', "span.res-info-estabs a::text") #
        rest.add_value('link', response.url) #
        rest.add_value('city',  findall('\\.com\/([a-z]+)\/', response.url)) #
        rest.add_css('cost', "div.res-info-detail span::attr(aria-label)") #
        rest.add_css('area', "div.res-main-address span span::text") #
        rest.add_xpath('rating', "//meta[@property='zomatocom:average_rating']/@content") #
        rest.add_css('rating_votes', "span[itemprop='ratingCount']::text") #
        rest.add_css('cuisines', "div.res-info-cuisines a.zred::text") #
        rest.add_css('collections', "span.res_collection_span a::text") #
        address = response.css("div.res-main-address span::text").extract_first()
        rest.add_value('r_address', address) #
        rest.add_xpath('r_latitude', "//meta[@property='place:location:latitude']/@content") #
        rest.add_xpath('r_longitude', "//meta[@property='place:location:longitude']/@content") #
        rest.add_css('r_image', "div.progressive_img::attr(data-url)") #
        tel = response.css("span.res-tel span.tel::text").extract_first()
        rest.add_value('r_tel', tel)
        rest.add_css('r_timing',"div.res-info-timings div.medium::text")

        yield rest.load_item()





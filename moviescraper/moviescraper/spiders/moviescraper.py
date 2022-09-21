import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from moviescraper.moviescraper.items import MoviescraperItem

class MovieScraper(scrapy.Spider):
    name = "moviescraper"
    start_urls = ["https://rezka.ag/series/comedy/2040-kremnievaya-dolina-2014.html"]


    def parse_movie(self, response):
        movie_item = MoviescraperItem()

        movie_item["title"] = response.xpath("/html/body/div[1]/div/div[4]/div/div[2]/div[1]/div[1]/h1").extract()
        movie_item["original_title"] = response.xpath('/html/body/div[1]/div/div[4]/div/div[2]/div[1]/div[2]').extract()
        movie_item["imdb"] = response.xpath("/html/body/div[1]/div/div[4]/div/div[2]/div[1]/div[4]/div[2]/div/table/tbody/tr[1]/td[2]/span[1]/span").extract()
        movie_item["country"] = response.xpath("/html/body/div[1]/div/div[4]/div/div[2]/div[1]/div[4]/div[2]/div/table/tbody/tr[5]/td[2]/a").extract()
        movie_item["duration"] = response.xpath('/html/body/div[1]/div/div[4]/div/div[2]/div[1]/div[4]/div[2]/div/table/tbody/tr[10]/td[2]').extract()
        movie_item["description"] = response.xpath('/html/body/div[1]/div/div[4]/div/div[2]/div[1]/div[5]/div[2]').extract()
        return movie_item


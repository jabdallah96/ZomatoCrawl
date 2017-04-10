SPIDER_MODULES = ['ZomatoTest.spiders']
NEWSPIDER_MODULE = 'ZomatoTest.spiders'
DEFAULT_ITEM_CLASS = 'ZomatoTest.items.Restaurant'
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'
ITEM_PIPELINES = {
    'ZomatoTest.pipelines.CSVPipeline': 300,
}

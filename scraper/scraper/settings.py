# Scrapy settings for scraper project
BOT_NAME = 'scraper'

SPIDER_MODULES = ['scraper.spiders']
NEWSPIDER_MODULE = 'scraper.spiders'

# 適切なヘッダーの設定
USER_AGENT = 'scraper (+http://www.yourdomain.com)'

# 遵守すべきルールの設定
ROBOTSTXT_OBEY = True

# ダウンロード間隔
DOWNLOAD_DELAY = 2

# パイプラインの設定
ITEM_PIPELINES = {
    'scraper.pipelines.DjangoDBPipeline': 300,
}

# Djangoの設定をインポート
import sys
import os
import django
sys.path.append('/app/django_app')
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_app.settings'
django.setup()

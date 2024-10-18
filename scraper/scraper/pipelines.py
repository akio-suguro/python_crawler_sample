import sys
import os
from scrapy.exceptions import NotConfigured

# Djangoの設定を読み込む
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # django_appの親ディレクトリをパスに追加
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_app.settings')  # Djangoの設定モジュールを指定

import django
django.setup()  # Djangoのセットアップを行う

from django_app.api.models import ScrapedData  # Djangoモデルのインポート

class DjangoDBPipeline:
    def process_item(self, item, spider):
        ScrapedData.objects.create(
            title=item['title'],
            url=item['url'],
            content=item['content']
        )
        return item

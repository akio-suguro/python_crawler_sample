from django_app.api.models import ScrapedData

class DjangoDBPipeline:
    def process_item(self, item, spider):
        ScrapedData.objects.create(
            title=item['title'],
            url=item['url'],
            content=item['content']
        )
        return item

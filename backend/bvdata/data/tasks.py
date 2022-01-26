from bvdata.celery import app
from bvdata.data.review_sync import import_reviews_from_wordpress


@app.task(name="import_wordpress_reviews")
def import_wordpress_reviews():
    import_reviews_from_wordpress()

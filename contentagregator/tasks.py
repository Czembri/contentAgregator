from contentagregator import celery
import os

@celery.task
def run_scraper():
    os.system("python contentagregator/modules/api/scrap.py")
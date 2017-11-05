from django.core.management.base import BaseCommand
import csv

from accident.models import AccidentData
from config import settings


class Command(BaseCommand):
    help = 'Sync accidents open data'

    def handle(self, *args, **options):
        AccidentData.objects.all().delete()
        f = open("{}/opendata/nezgode.csv".format(settings.STATIC_ROOT), 'rt')
        try:
            counter = 0
            reader = csv.reader(f)
            for row in reader:
                counter = counter + 1
                accident = AccidentData()
                accident.lat = row[3]
                accident.lng = row[2]
                accident.damage = row[4]
                accident.desc = row[5]
                accident.save()


        finally:
            f.close()
        self.stdout.write(self.style.SUCCESS('Successfully saved "%s"' % counter))
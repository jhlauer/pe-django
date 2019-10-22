import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Site, States, Iso, Category, Region

def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)

    Site.objects.all().delete() #Membership
    States.objects.all().delete()
    Iso.objects.all().delete()
    Category.objects.all().delete()
    Region.objects.all().delete()

    # Format
    # name, description, justification, year, longitude, latitude, area_hectares, category, states, region, iso

    for row in reader:
        print(row)

        c, created = Category.objects.get_or_create(name=row[7])
        st, created = States.objects.get_or_create(name=row[8])
        rg, created = Region.objects.get_or_create(name=row[9])
        i, created = Iso.objects.get_or_create(name=row[10])

        try:
            y = int(row[3])
        except:
            y = None
        try:
            lg = float(row[4])
        except:
            lg = None
        try:
            lt = float(row[5])
        except:
            lt = None
        try:
            ah = float(row[6])
        except:
            ah = None

        site = Site(name=row[0], description=row[1], justification=row[2], year=y, longitude=lg, latitude=lt, area_hectares=ah, category=c, states=st, region=rg, iso=i)
        site.save()
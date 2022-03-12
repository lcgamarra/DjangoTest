import csv
import os
from djangoProject.models import MusicalWork
from djangoProject.models import Contributor
from django.core.exceptions import ObjectDoesNotExist


def run():
    file = open("./ExternalData/works_metadata.csv")
    read_file = csv.reader(file)

    # option
    MusicalWork.objects.all().delete()
    Contributor.objects.all().delete()

    count = 1

    for record in read_file:
        if count == 1:
            pass
        else:
            print(record)
            if record[2] != "":
                try:
                    MusicalWork.objects.filter(title=record[0]).get()
                    print("queried")
                    musical_work, result = MusicalWork.objects.update_or_create(title=record[0], defaults={'iswc': record[2]})

                except ObjectDoesNotExist:
                    musical_work, result = MusicalWork.objects.get_or_create(title=record[0], iswc=record[2])

                    for contributor in record[1].split("|"):
                        Contributor.objects.get_or_create(musical_works=musical_work, contributor=contributor)
                    count += 1
                    continue

            else:
                print("empty")
                musical_work, result = MusicalWork.objects.get_or_create(title=record[0])

            for contributor in record[1].split("|"):
                Contributor.objects.get_or_create(musical_works=musical_work, contributor=contributor)

        count += 1

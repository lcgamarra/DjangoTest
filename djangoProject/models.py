from django.db import models
from django.contrib import admin


class MusicalWork(models.Model):
    title = models.CharField(max_length=60)
    iswc = models.CharField(max_length=60)


class Contributor(models.Model):
    musical_works = models.ForeignKey(MusicalWork, related_name='contributors', on_delete=models.CASCADE)
    contributor = models.TextField(max_length=120)


class ContributorInLine(admin.StackedInline):
    model = Contributor


class MusicalWorkAdmin(admin.ModelAdmin):
    inlines = [
        ContributorInLine,
    ]
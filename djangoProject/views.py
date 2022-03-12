from django.views.generic import ListView
from rest_framework.response import Response

from .models import MusicalWork
from .models import Contributor
from .serializers import MWMetaSerializer
from rest_framework import viewsets


class MusicalWorkListView(ListView):
    template_name = 'index.html'

    _queryset = []
    for mw in MusicalWork.objects.all():
        contributors = ','.join([c.contributor for c in Contributor.objects.filter(musical_works=mw.id)])
        str_set = mw.iswc + " | " + mw.title + " | " + contributors
        _queryset.append(str_set)

    queryset = _queryset


class MWMetaViewSet(viewsets.ModelViewSet):
    serializer_class = MWMetaSerializer

    def list(self, request, *args, **kwargs):
        self.queryset = MusicalWork.objects.all().filter(iswc=kwargs['iswc'])
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

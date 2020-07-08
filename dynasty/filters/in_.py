from django_filters.rest_framework import filterset
from django_filters.rest_framework import filters

from ..models import Dynasty


class NumberInFilter(filters.BaseInFilter, filters.NumberFilter):
    pass


class InFilterSet(filterset.FilterSet):
    begin_year = NumberInFilter(field_name='begin_year', lookup_expr='in')

    class Meta:
        model = Dynasty
        fields = ['begin_year']

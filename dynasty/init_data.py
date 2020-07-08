from .models import Dynasty

create = Dynasty.objects.create

create(name='夏', begin_year=-2070, end_year=-1600)
create(name='商', begin_year=-1600, end_year=--1046)
create(name='西周', begin_year=-1046, end_year=-770)

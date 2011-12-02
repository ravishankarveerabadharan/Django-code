>>> Entry.contacts.filter(
...     contactdetail__startswith='NOKIA'
... ).exclude(
...     cs_date__gte=datetime.now()
... ).filter(
...     cs_date__gte=datetime(2010, 1, 1)
... )


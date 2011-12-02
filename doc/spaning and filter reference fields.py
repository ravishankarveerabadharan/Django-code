>>> from django.db.models import F
>>> Entry.objects.filter(n_comments__gt=F('model_no'))
>>> Detail.contacts.filter(mobile__name__exact='Give Me Five')
>>> Mobile.contacts.filter(detail__contacts__contains='NOKIA')
>>> from datetime import timedelta

    Mobile.contacts.filter(detail__company__name='NOKIA')
    Mobile.contacts.filter(detail__company__name__isnull=True)
    Mobile.contacts.filter(detail__company__isnull=False,
        detail__company__name__isnull=True)
    Mobile.contacts.filter(detail__contactdetails__contains='NOKIA',
        detail__cs_date__year=2010.3.1)
    Mobile.contacts.filter(detail__contactdetails__contains='NOKIA').filter(
        detail__cs_date__year=2010.3.1)

>>> Detail.contacts.filter(n_comments__gt=F('model_no'))
>>> Detail.contacts.filter(n_comments__gt=F('model_no') * 2)
>>> Detail.contacts.filter(rating__lt=F('n_comments') + F('model_no'))
>>> Detail.contacts.filter(company__name=F('mobile__name'))
>>> Detail.contacts.filter(mod_date__gt=F('cs_date') + timedelta(days=3))









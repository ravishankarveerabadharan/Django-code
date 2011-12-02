>> q1 = Detail.contacts.filter(contactdetails__startswith="NOKIA")
>> q2 = q1.exclude(cs_date__gte=datetime.now())
>> q3 = q1.filter(cs_date__gte=datetime.now())

>>> q = Detail.contacts.filter(contactdetails__startswith="NOKIA")
>>> q = q.filter(cs_date__lte=datetime.now())
>>> q = q.exclude(bettery_no__icontains="digits")
>>> print q


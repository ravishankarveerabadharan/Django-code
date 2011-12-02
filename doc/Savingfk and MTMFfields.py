>>> from mobile.models import Detail
>>> detail = Detail.contacts.get(pk=1)
>>> china_mobile = Mobile.contacts.get(name="Give Me Five")
>>> detail.mobile = china_mobile
>>> detail.save()


>>> from mobile.models import Company
>>> nokia = Company.contacts.create(name="NOKIA")
>>> entry.companys.add(nokia)


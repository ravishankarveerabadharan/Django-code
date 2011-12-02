>>> Modile.contacts.get(serial_no__exact=14) # Explicit form
>>> Mobile.contacts.get(serial_no=14) # __exact is implied
>>> Mobile.contacts.get(pk=14) # pk implies id__exact
# Get mobile details with id 1, 4 and 7
>>> Mobile.contacts.filter(pk__in=[1,4,7])

# Get all mobile details with id > 14
>>> Mobile.contacts.filter(pk__gt=14)
>>> Mobile.contacts.filter(mobile__serial_no__exact=3) # Explicit form
>>> Mobile.contacts.filter(mobile__serial_no=3)        # __exact is implied
>>> Mobile.contacts.filter(mobile__pk=3)        # __pk implies __serial_no__exact


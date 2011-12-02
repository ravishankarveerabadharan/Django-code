>>> Mobile.contacts
<django.db.models.manager.Manager contacts at ...>
>>> m = Mobile(name='Foo', tagline='Bar')
>>> m.contacts
Traceback:
    ...
AttributeError: "Manager contact can't accessible via Mobile instances."

>>> all_details = Detail.contacts.all()



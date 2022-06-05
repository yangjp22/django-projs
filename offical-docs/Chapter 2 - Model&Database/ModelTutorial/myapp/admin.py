from django.contrib import admin

from .models import Person, Musician, Album, Runner, Group, Membership, Team


# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "shirt_size"]
admin.site.register(Person, PersonAdmin)

admin.site.register(Runner)
admin.site.register(Album)
admin.site.register(Musician)
admin.site.register(Group)
admin.site.register(Membership)
admin.site.register(Team)


from django.contrib import admin
from .models import Invite

class InvitesAdmin(admin.ModelAdmin):
      exclude = ('is_used',)

admin.site.register(Invite,InvitesAdmin)

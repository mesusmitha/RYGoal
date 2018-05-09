# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from UserDatabase.models import student_details, scholorship, notify_me, spons_details, guide_details, guide_inbox, \
    student_inbox, sponsor_inbox

# Register your models here.
admin.site.register(student_details)
admin.site.register(notify_me)
admin.site.register(scholorship)
admin.site.register(spons_details)
admin.site.register(guide_details)
admin.site.register(guide_inbox)
admin.site.register(student_inbox)
admin.site.register(sponsor_inbox)






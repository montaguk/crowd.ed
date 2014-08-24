from django.contrib import admin
from crowded.models import *

"""Register models to the admin interface
"""


class ReviewAdmin(admin.ModelAdmin):
    class FlagInline(admin.TabularInline):
        model = ReviewFlag

    inlines = [ FlagInline ]

admin.site.register(UserContent)
admin.site.register(ReviewFlag)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Reviewable)

admin.site.register(Bill)

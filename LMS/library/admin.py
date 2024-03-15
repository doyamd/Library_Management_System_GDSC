from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Book)
admin.site.register(models.Author)
admin.site.register(models.Fine)
admin.site.register(models.Genre)
admin.site.register(models.Likes)
admin.site.register(models.Publisher)
admin.site.register(models.Loan)
admin.site.register(models.Review)
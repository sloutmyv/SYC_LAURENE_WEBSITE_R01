from django.contrib import admin

from .models import Praticien, Formation, Experience

### Admin model "Praticien"
class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1
class FormationInline(admin.TabularInline):
    model = Formation
    extra = 1
class PraticienAdmin(admin.ModelAdmin):
    inlines = [ FormationInline, ExperienceInline]

admin.site.register(Praticien,PraticienAdmin)

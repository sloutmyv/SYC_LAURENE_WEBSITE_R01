from django.contrib import admin

from .models import (
                        Praticien,
                        Formation,
                        Experience,
                        Cabinet,
                        Cabinetphoto,
                        Profession,
                        CategorieActe,
                        Acte,
                    )

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

### Admin model "Cabinet"
class CabinetphotoInline(admin.TabularInline):
    model = Cabinetphoto
    extra = 1
class CabinetAdmin(admin.ModelAdmin):
    inlines = [CabinetphotoInline,]
admin.site.register(Cabinet, CabinetAdmin)

### Admin model "Profession"
admin.site.register(Profession)

### Admin model "Catégorie d'acte"
admin.site.register(CategorieActe)

### Admin model "Acte"
admin.site.register(Acte)

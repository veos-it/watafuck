from django.contrib import admin
from django.utils.safestring import mark_safe
# Register your models here.

from .models import Partner, Advantage, Application


class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'logo', 'is_published', 'get_logo')
    list_display_links = ('name',)
    search_fields = ('name', 'desc')
    list_editable = ('is_published',)

    def get_logo(self, obj):
        if obj.logo:
            return mark_safe(f'<img src="{ obj.logo.url }" width="75">')
        else:
            return 'Фото не установлено'

    get_logo.short_description = 'Миниатюра'


class AdvantageAdmin(admin.ModelAdmin):
    list_display = ('img', 'text', 'get_img')
    list_display_links = ('text',)

    def get_img(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{ obj.img.url }" width="75">')
        else:
            return 'Уствновите иконку'

    get_img.short_description = 'Иконка'


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'comment')
    list_display_links = ('email',)


admin.site.register(Application, ApplicationAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Advantage, AdvantageAdmin)
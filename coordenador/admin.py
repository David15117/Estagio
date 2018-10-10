from django.contrib import admin

# Register your models here.
from .models import Coordenador
from .models import Orientador
from .models import Orientando
from .models import Calendario

class OrientandoInline(admin.TabularInline):
    model = Orientando
    extra = 0

admin.site.register(Coordenador)

@admin.register(Orientador)
class OrientadorAdmin(admin.ModelAdmin):
    list_display =('nome','cgu',)
    search_fields = ('nome',)
    inlines = [OrientandoInline]

admin.site.register(Orientando)


class OrientadorInline(admin.TabularInline):
    model = Orientador
    extra = 0


admin.site.register(Calendario)

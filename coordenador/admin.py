from django.contrib import admin

# Register your models here.
from .models import Coordenador
from .models import Orientador
from .models import Orientando
from .models import Acompanhamento
from .models import Calendario


admin.site.register(Coordenador)
admin.site.register(Orientador)
admin.site.register(Orientando)
admin.site.register(Acompanhamento)
admin.site.register(Calendario)
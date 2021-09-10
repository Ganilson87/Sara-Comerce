from django.contrib import admin
from .models import produto
#Definicões do admin
admin.site.site_header = "E-SARA"
admin.site.site_title = "Gerenciador"
admin.site.index_title = "E-SARA"

#Meus models
admin.site.register(produto)
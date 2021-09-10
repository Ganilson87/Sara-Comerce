from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class produto(models.Model):
    img = models.ImageField(verbose_name="Imagem Prévia", upload_to='static', max_length=None, null=True)
    nome_prod = models.CharField(verbose_name="Nome do Produto", max_length=100)
    descr = models.TextField(verbose_name="Descrição", max_length=2000)
    tipo_prod_choices = [
        ('Produtos Alimentares','Produtos Alimentares'),
        ('Bebidas','Bebidas'),
        ('Produtos de Limpeza','Produtos de Limpeza'),
        ('Cosméticos','Cosméticos'),
            ]
    tipo_prod = models.CharField(verbose_name="Tipo de Produto", choices=tipo_prod_choices, max_length=100)
    prec_prod = models.FloatField(verbose_name="Preço")
    promovido = models.BooleanField(verbose_name="Promovido", default=False)
    data = models.DateTimeField( auto_now=False, auto_now_add=True)
    disponibilidade = models.BooleanField(verbose_name="disponivel", default=False)
    

    usuario = models.ForeignKey(User, null=False, blank=False, on_delete=models.PROTECT)
    def __str__(self):
        return ("{}: {} ".format(self.nome_prod, 
        
        self.prec_prod,
        
        ))

    

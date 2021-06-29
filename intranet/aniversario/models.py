from django.db import models

class AtivoManager(models.Manager):
    def get_queryset(self):
        return super(AtivoManager,
                     self).get_queryset().filter(status='ativo')

class Aniversariante(models.Model):
    STATUS_CHOICES = (
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
    )
    LOCAL_CHOICES = (
        ('bh', 'Belo Horizonte'),
        ('op', 'Ouro Preto'),
        ('ip', 'Ipatinga'),
        ('mc', 'Montes Claros'),
        ('jf', 'Juiz de Fora'),
        ('vg', 'Varginha'),
    )
    nome = models.CharField(max_length=255, null=True)
    setor = models.CharField(max_length=20, null=True)
    datanascimento = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=7,
                              choices=STATUS_CHOICES,
                              default='ativo')
    foto = models.ImageField(upload_to='nome/%d/%m/%Y/', blank=True)
    local = models.CharField(max_length=2,
                             choices=LOCAL_CHOICES,
                             default='bh')
    objects = models.Manager()
    ativo = AtivoManager()


    class Meta:
        ordering = ('datanascimento',)

    def __str__(self):
        return self.nome
import uuid
from django.db import models
from stdimage.models import StdImageField
from django.utils.translation import gettext_lazy as _

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Evento(models.Model):
    nome = models.CharField(('Nome'), blank=True, max_length=100)
    descricao = models.TextField(('Descrição'), max_length=500)
    imagem = StdImageField(('Imagem'), null=True, blank=True, upload_to=get_file_path, variations={'thumb':{'width':420, 'height':260, 'crop':True}})

    class Meta:
        verbose_name = ('Evento')
        verbose_name_plural = ('Eventos')

class Usuario(models.Model):
    nome = models.CharField(_('Nome'), max_length=100)
    cpf = models.CharField(_('CPF'), max_length=100)
    senha = models.CharField(_('Senha'), blank=True, max_length=50)
    email = models.EmailField(_('E-mail'), blank=True, max_length=100)

    class Meta:
        abstract = True
        verbose_name = _('Usuario')
        verbose_name_plural = _('Usuarios')
        ordering = ['id']

    def __str__(self):
        return self.nome


class Administrador(Usuario):
    cargo = models.CharField(_('Cargo'), blank=True, max_length=100)
    telefone = models.CharField(_('Telefone'), blank=True, max_length=15)
    data_nascimento = models.DateField(_('Data de Nascimento'), blank=True, null=True, help_text=_('Formato DD/MM/AAAA'))

    class Meta:
        verbose_name = _('Administrador')
        verbose_name_plural = _('Administradores')




class Atividade(models.Model):
    evento = models.ForeignKey(Evento, related_name='Evento', blank=True, null=True, on_delete=models.CASCADE)
    nome = models.CharField(_('Nome'), blank=True, max_length=100)
    descricao = models.TextField(_('Descrição'), max_length=500)
    data_inicio = models.DateField(_('Data de Início'), blank=True, null=True, help_text=_('Formato DD/MM/AAAA'))
    hora_inicio = models.TimeField(_('Hora Início'), blank=True, null=True, help_text=_('Formato HH:MM'))
    local = models.CharField(_('Local'), blank=True, max_length=100)
    capacidade = models.IntegerField(_('Capacidade'), blank=True, null=True)
    imagem = StdImageField(_('Imagem'), null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 420, 'height': 260, 'crop': True}})

    class Meta:
        verbose_name = _('Atividade')
        verbose_name_plural = _('Atividades')

    def __str__(self):
        return self.nome
class Usuario(models.Model):
    nome = models.CharField(('Nome'), max_length=100)
    cpf = models.CharField(('CPF'), max_length=100)
    senha = models.CharField(('Senha'), blank=True, max_length=50)
    email = models.EmailField(('E-mail'), blank=True, max_length=100)

    class Meta:
        abstract = True
        verbose_name = ('Usuario')
        verbose_name_plural = ('Usuarios')
        ordering = ['id']

    def __str__(self):
        return self.nome


class residente(models.Model):
    data_nascimento = models.DateField()
    foto = models.ImageField(upload_to='resident_photos/', blank=True, null=True)
    def __str__(self):
        return self.nome
class responsavel(models.Model):
    telefone = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)
    telefone_comercial = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = ('Responsável')
        verbose_name_plural = ('Responsáveis')

class endereco(models.Model):
    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    class Meta:
        verbose_name = ('Endereço')
        verbose_name_plural = ('Endereços')

class inscricao(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
    ]


    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')

    def __str__(self):
        return f"Inscrição de {self.usuario} - {self.status}"
    class Meta:
            verbose_name = ('Incrição')
            verbose_name_plural = ('Incrições')
class categoria(models.Model):
    nome_categoria = models.CharField(max_length=255)

    def __str__(self):
        return self.nome_categoria

class feedback(models.Model):
    inscricao = models.OneToOneField(inscricao, on_delete=models.CASCADE)
    comentario = models.TextField()
    nota = models.IntegerField()

    def __str__(self):
        return f"Feedback para Inscrição {self.inscricao} - Nota: {self.nota}"


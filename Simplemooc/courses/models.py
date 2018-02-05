from django.db import models

class CoursesManager(models.Model):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | models.Q(description__icontains=query)
        )

class Courses(models.Model):
    name = models.CharField('Nome',max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição',blank=True)
    about = models.TextField('Sobre o Curso',blank=True)
    start_date = models.DateField('Data Ínicio', null=True, blank=True)
    image = models.ImageField(upload_to='courses/images', verbose_name='Imagem',null=True,blank=True)
    created_at = models.DateTimeField('Criado em',auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em',auto_now=True)


    object = CoursesManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return (self.slug)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['name']

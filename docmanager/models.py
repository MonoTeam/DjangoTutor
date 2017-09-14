from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return "{} {}".format(self.first_name,self.last_name)

class Document(models.Model):
    choice = [(0,"Book"),(1,"Thesis")]
    title = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=14)
    release_date = models.DateField()
    author = models.ForeignKey(Author)
    doc_type = models.IntegerField(choices=choice)

#admin
#qwer1234
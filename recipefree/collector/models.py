from django.contrib.postgres.fields import JSONField
from django.db import models

# Create your models here.
class SmulWebPage(models.Model):
    page_url = models.CharField(max_length=50, unique=True)
    page_nr = models.IntegerField(default="0")

    def __str__(self):
        return "Smulwebpage " + str(self.page_nr)

class SmulWebRecipe(models.Model):
    page_url = models.ForeignKey(SmulWebPage, db_column="page_url", on_delete=models.CASCADE)
    recipe_url = models.CharField(max_length=2000)
    recipe_JSON = JSONField()

    def __str__(self):
        return self.recipe_JSON["name"]


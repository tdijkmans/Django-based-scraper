from django.db import models

# Create your models here.
class SmulWebPage(models.Model):
    page_url = models.CharField(max_length=50)
    page_nr = models.IntegerField(default="0")

    def __str__(self):
        return "Smulwebpage:" + self.page_nr

class SmulWebRecipe(models.Model):
    listing_url = models.ForeignKey(SmulWebPage, db_column="page_url", on_delete=models.CASCADE)
    raw_text = models.CharField(max_length=2000)
    titel_gerecht = models.CharField(max_length=2000)
    url = models.CharField(max_length=2000)
    keuken = models.CharField(max_length=2000)
    gang = models.CharField(max_length=2000)
    tijdsduur = models.CharField(max_length=2000)
    datum = models.CharField(max_length=2000)
    intro = models.CharField(max_length=2000)
    recepttekst = models.CharField(max_length=2000)
    plaatser_naam = models.CharField(max_length=2000)
    plaatser_url = models.CharField(max_length=2000)
    plaatser_volgers = models.IntegerField(blank=True, null=True)
    plaatser_recepten = models.IntegerField(blank=True, null=True)
    plaatser_kookboeken = models.IntegerField(blank=True, null=True)
    ingredienten = models.CharField(max_length=2000)
    tags = models.CharField(max_length=2000)
    bekeken = models.IntegerField(blank=True, null=True)
    bewaard = models.IntegerField(blank=True, null=True)
    kookgroepen = models.IntegerField(blank=True, null=True)
    kookboeken = models.IntegerField(blank=True, null=True)
    beoordeling_avg = models.IntegerField(blank=True, null=True)
    beoordeling_aantal = models.IntegerField(blank=True, null=True)
    reactie_aantal = models.IntegerField(blank=True, null=True)
    reacties = models.CharField(max_length=2000)
from django.db import models
from django.db.models.signals import pre_save                            # pour la création des signaux
from .utils import unique_slug_generator, upload_location                # pour la création des signaux, l'enregistrement des photos

### Modèles
class Praticien(models.Model):
    praticien_prenom                  = models.CharField(max_length=120, verbose_name="Prénom du praticien")
    praticien_nom                     = models.CharField(max_length=120, verbose_name="Nom du praticien")
    slug                              = models.SlugField(null=True, blank=True, editable=False, verbose_name="Photo")
    praticien_image                   = models.ImageField(upload_to=upload_location, null=True,blank=True)
    praticien_presentation_titre      = models.CharField(max_length=120,null=True, blank=True, verbose_name="Titre de la section 'Mon Parcours'")
    praticien_presentation_texte      = models.TextField(null=True,blank=True, verbose_name="Texte de la section 'Mon Parcours'")

    class Meta:
        """ Le titre du modèle qui d'affiche dans l'interface d'administration"""
        verbose_name_plural = 'Praticien'

    def __str__(self):
        """ Pour l'affichage d'un titre modèle dans l'admin"""
        return self.praticien_prenom + ' ' + self.praticien_nom

    @property
    def title(self):
        """ Nécéssaire à l'appel du signal de création de slug"""
        return self.praticien_prenom + ' ' + self.praticien_nom

class Formation(models.Model):
    formation_praticien         = models.ForeignKey(Praticien, related_name='formation',verbose_name="Praticien")
    formation_date              = models.DateField(verbose_name="Date de la formation")
    formation_titre             = models.CharField(max_length=300,verbose_name="Titre de la formation et organisme")
    formation_commentaire       = models.TextField(null=True, blank=True ,verbose_name="Commentaire(s)")

    class Meta:
        """ Le titre du modèle qui d'affiche dans l'interface d'administration"""
        verbose_name_plural = 'Diplôme(s) et formation(s)'

    def __str__(self):
        """ Pour l'affichage d'un titre modèle dans l'admin"""
        return self.formation_titre

class Experience(models.Model):
    experience_praticien         = models.ForeignKey(Praticien, related_name='experience',verbose_name="Praticien")
    experience_date_debut        = models.CharField(max_length=300, verbose_name="Début de l'experience")
    experience_date_fin          = models.CharField(blank=True,max_length=300, verbose_name="Fin de l'experience")
    experience_titre             = models.CharField(max_length=300,verbose_name="Titre de l'experience et entreprise")
    experience_commentaire       = models.TextField(null=True, blank=True ,verbose_name="Commentaire(s)")

    class Meta:
        """ Le titre du modèle qui d'affiche dans l'interface d'administration"""
        verbose_name_plural = 'Expérience professionnelle(s)'

    def __str__(self):
        """ Pour l'affichage d'un titre modèle dans l'admin"""
        return self.experience_titre


### Signals de création des slugs
def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=Praticien)

from django.db import models
from django.db.models.signals import pre_save                            # pour la création des signaux
from .utils import unique_slug_generator, upload_location                # pour la création des signaux, l'enregistrement des photos

### Modèles
class Praticien(models.Model):
    praticien_prenom                  = models.CharField(max_length=120, verbose_name="Prénom du praticien")
    praticien_nom                     = models.CharField(max_length=120, verbose_name="Nom du praticien")
    slug                              = models.SlugField(null=True, blank=True, editable=False, verbose_name="slug")
    praticien_image                   = models.ImageField(upload_to=upload_location, null=True,blank=True, verbose_name="photo")
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

class Cabinet(models.Model):
    cabinet_titre           = models.CharField(max_length=120, verbose_name="Cabinet titre")
    slug                    = models.SlugField(null=True, blank=True, editable=False, verbose_name="slug")
    cabinet_adresse         = models.CharField(max_length=200, verbose_name="Adresse postale")
    cabinet_telephone       = models.CharField(max_length=10, verbose_name="Téléphone")
    cabinet_email           = models.EmailField(max_length=254, verbose_name="Email")
    cabinet_rdvenligne      = models.URLField(max_length=300, null=True, blank=True, verbose_name="Url rdv en ligne")
    cabinet_description     = models.TextField(null=True, blank=True, verbose_name="Texte accueil cabinet")
    cabinet_acces           = models.TextField(null=True, blank=True, verbose_name="Cabinet accès")
    cabinet_lat             = models.DecimalField(null=True, blank=True, max_digits=9, decimal_places=6, verbose_name="Cabinet latitude")
    cabinet_lng             = models.DecimalField(null=True, blank=True, max_digits=9, decimal_places=6, verbose_name="Cabinet longitude")

    class Meta:
        """ Le titre du modèle qui d'affiche dans l'interface d'administration"""
        verbose_name_plural = 'Cabinet'

    def __str__(self):
        """ Pour l'affichage d'un titre modèle dans l'admin"""
        return self.cabinet_titre

    @property
    def title(self):
        """ Nécéssaire à l'appel du signal de création de slug"""
        return self.cabinet_titre

    def showable_number(self):
        number = self.cabinet_telephone
        txt=""
        for i in range(len(number)):
            txt += number[i]
            if i%2 == 1 and i < len(number)-1:
                txt += '.'
        return txt

    def callable_number(self):
            number = self.cabinet_telephone
            return ''.join(number[1:])

class Cabinetphoto(models.Model):
    cabinetphoto_cabinet             = models.ForeignKey(Cabinet, related_name='cabinetphoto',verbose_name="Cabinet")
    cabinetphoto_titre              = models.CharField(max_length=120, verbose_name="Titre de la photo")
    slug                            = models.SlugField(null=True, blank=True, editable=False, verbose_name="slug")
    cabinetphoto_photo              = models.ImageField(upload_to=upload_location, null=True,blank=True, verbose_name="photo du cabinet")

    class Meta:
        """ Le titre du modèle qui d'affiche dans l'interface d'administration"""
        verbose_name_plural = 'Photos du cabinet'

    def __str__(self):
        """ Pour l'affichage d'un titre modèle dans l'admin"""
        return self.cabinetphoto_titre

    @property
    def title(self):
        """ Nécéssaire à l'appel du signal de création de slug"""
        return self.cabinetphoto_titre

class Profession(models.Model):
    profession_titre             = models.CharField(max_length=120, verbose_name="Profession titre")
    slug                         = models.SlugField(null=True, blank=True, editable=False, verbose_name="Slug")
    profession_description_titre = models.CharField(max_length=120, verbose_name="Titre description profession")
    profession_description_texte = models.TextField(null=True, blank=True, verbose_name="Texte description profession")
    profession_img               = models.ImageField(upload_to=upload_location, null=True,blank=True, verbose_name="Image description profession")

    class Meta:
        """ Le titre du modèle qui d'affiche dans l'interface d'administration"""
        verbose_name_plural = 'Profession'

    def __str__(self):
        """ Pour l'affichage d'un titre modèle dans l'admin"""
        return self.profession_titre

    @property
    def title(self):
        """ Nécéssaire à l'appel du signal de création de slug"""
        return self.profession_titre

class CategorieActe(models.Model):
    categorieacte_titre             = models.CharField(max_length=120, verbose_name="Categorie d'acte")
    slug                            = models.SlugField(null=True, blank=True, editable=False, verbose_name="Slug")
    categorieacte_description_card  = models.CharField(null=True, blank=True, max_length=200, verbose_name="Description card deck")
    categorieacte_description       = models.TextField(null=True, blank=True, verbose_name="Texte description catégorie acte")
    categorieacte_cardimage         = models.ImageField(upload_to=upload_location, null=True,blank=True, verbose_name="Image card deck")
    categorieacte_mainimage         = models.ImageField(upload_to=upload_location, null=True,blank=True, verbose_name="Image principale")

    class Meta:
        """ Le titre du modèle qui d'affiche dans l'interface d'administration"""
        verbose_name_plural = "Catégorie d'acte"

    def __str__(self):
        """ Pour l'affichage d'un titre modèle dans l'admin"""
        return self.categorieacte_titre

    @property
    def title(self):
        """ Nécéssaire à l'appel du signal de création de slug"""
        return self.categorieacte_titre

class Acte(models.Model):
    acte_categorie                  = models.ForeignKey(CategorieActe, related_name='categorieacte',verbose_name="Catégorie de l'acte")
    acte_titre                      = models.CharField(max_length=120, verbose_name="Acte")
    slug                            = models.SlugField(null=True, blank=True, editable=False, verbose_name="Slug")
    acte_description                = models.TextField(null=True, blank=True, verbose_name="Texte description acte")
    acte_image                      = models.ImageField(upload_to=upload_location, null=True,blank=True, verbose_name="Image principale")

    class Meta:
        """ Le titre du modèle qui d'affiche dans l'interface d'administration"""
        verbose_name_plural = "Acte"

    def __str__(self):
        """ Pour l'affichage d'un titre modèle dans l'admin"""
        return self.acte_titre

    @property
    def title(self):
        """ Nécéssaire à l'appel du signal de création de slug"""
        return self.acte_titre


### Signals de création des slugs
def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=Praticien)
pre_save.connect(rl_pre_save_receiver, sender=Cabinet)
pre_save.connect(rl_pre_save_receiver, sender=Cabinetphoto)
pre_save.connect(rl_pre_save_receiver, sender=Profession)
pre_save.connect(rl_pre_save_receiver, sender=CategorieActe)
pre_save.connect(rl_pre_save_receiver, sender=Acte)

from django.utils.text import slugify
import random
import string

### Slug
def random_string_generator(size=10, chars= string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

DONTUSE = ['create']
def unique_slug_generator(instance,new_slug=None):
    """
    This is for a Django project and it assumes your instance
    has a model with a SlugField and a title character (char) Field
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    if slug in DONTUSE:
        new_slug= "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4))
        return unique_slug_generator(instance,new_slug=new_slug)
    Klass=instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug= "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4))
        return unique_slug_generator(instance,new_slug=new_slug)
    return slug

### Photos
def upload_location(instance, filename):
    return '%s/%s/%s' % (instance._meta.verbose_name,instance.slug,instance.id)

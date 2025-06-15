from django.db import models

# Create your models here.

from django.db import models
from django.utils.text import slugify



class EventPage(models.Model):
    title = models.CharField(max_length=255, help_text="Browser page title")
    banner_heading = models.CharField(max_length=255, help_text="Main heading on the banner")
    description = models.TextField(blank=True, null=True)
    event_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    venue = models.CharField(max_length=255)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name = "Event Page"
        verbose_name_plural = "Event Pages"
        ordering = ['event_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while EventPage.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


class Speaker(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='speakers/')
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Speaker.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


class Session(models.Model):
    event = models.ForeignKey(EventPage, related_name='sessions', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=255)
    speaker = models.ForeignKey(Speaker, on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.event.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Session.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

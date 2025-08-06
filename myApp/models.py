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



from django.db import models

class ExhibitRegistration(models.Model):
    EXHIBIT_TYPE_CHOICES = [
        ('Exhibitor', 'Exhibitor'),
        ('Sponsor', 'Sponsor'),
    ]

    type = models.CharField(max_length=50, choices=EXHIBIT_TYPE_CHOICES)
    company_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    whatsapp = models.CharField(max_length=50)
    email = models.EmailField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.type})"



from django.db import models

class StartupPitchApplication(models.Model):
    PACKAGE_CHOICES = [
        ("Startup Pitching + 1 Regular Ticket", "Startup Pitching + 1 Regular Ticket"),
        ("Startup + 5 Regular Tickets + Table Top", "Startup + 5 Regular Tickets + Table Top"),
        ("Startup Pitching + 5 Regular Tickets", "Startup Pitching + 5 Regular Tickets"),
        ("Startup Pitching + 2 VIP Tickets", "Startup Pitching + 2 VIP Tickets"),
        ("Startup Pitching + 3 VIP Tickets", "Startup Pitching + 3 VIP Tickets"),
        ("Startup Pitching + 5 VIP Tickets", "Startup Pitching + 5 VIP Tickets"),
    ]

    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    company_name = models.CharField(max_length=255)
    website = models.URLField(blank=True, null=True)
    package = models.CharField(max_length=255, choices=PACKAGE_CHOICES)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.package}"



from django.db import models

class MediaPartnerApplication(models.Model):
    PARTNER_TYPE_CHOICES = [
        ('media', 'Media Partner'),
        ('community', 'Community Partner'),
    ]

    partner_type = models.CharField(max_length=20, choices=PARTNER_TYPE_CHOICES)
    events = models.CharField(max_length=255)  # Store as CSV
    company_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    address = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.company_name}) - {self.partner_type}"


from django.db import models

class SponsorInquiry(models.Model):
    company = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    whatsapp = models.CharField(max_length=50)
    email = models.EmailField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} from {self.company}"


from django.db import models

class SpeakerApplication(models.Model):
    your_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    total_employees = models.PositiveIntegerField()
    speaker_name = models.CharField(max_length=255)
    email = models.EmailField()
    isd_code = models.CharField(max_length=10)
    whatsapp_number = models.CharField(max_length=20)
    linkedin = models.URLField(blank=True, null=True)
    slot = models.CharField(max_length=255)
    date_applied = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.speaker_name} - {self.slot}"

#for modal
class GeneralRegistration(models.Model):
    ROLE_CHOICES = [
        ('Speaker', 'Speaker'),
        ('Exhibitor', 'Exhibitor'),
        ('Sponsor', 'Sponsor'),
        ('Partner', 'Partner'),
        ('Visitor', 'Visitor'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    company = models.CharField(max_length=255)
    isd_code = models.CharField(max_length=10)
    whatsapp_number = models.CharField(max_length=20)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.role})"

#intern and ojt

class InternshipApplication(models.Model):
    DEPARTMENT_CHOICES = [
        ('Marketing', 'Marketing'),
        ('Tech', 'Tech / Development'),
        ('Events', 'Events'),
        ('Design', 'Design'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    contact = models.CharField(max_length=50)
    school = models.CharField(max_length=255)
    program = models.CharField(max_length=255)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    motivation = models.TextField()
    resume = models.FileField(upload_to='internship_resumes/')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.department})"
    
#for ojt

from django.db import models

class InternshipApplication(models.Model):
    DEPARTMENT_CHOICES = [
        ('Marketing', 'Marketing'),
        ('Tech', 'Tech / Development'),
        ('Events', 'Events'),
        ('Design', 'Design'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    contact = models.CharField(max_length=50)
    school = models.CharField(max_length=255)
    program = models.CharField(max_length=255)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    motivation = models.TextField()
    resume = models.FileField(upload_to='internship_resumes/')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.department})"

from django.db import models

class FreePassRegistrant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"

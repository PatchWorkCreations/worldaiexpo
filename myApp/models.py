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
    ('Startup Booth', 'Startup Booth'),
    ('Growth Booth', 'Growth Booth'),
    ('Enterprise Booth', 'Enterprise Booth'),
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
    TIER_CHOICES = [
        ('Diamond', 'Diamond'),
        ('Platinum', 'Platinum'),
        ('Gold', 'Gold'),
        ('Silver', 'Silver'),
    ]

    company = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    whatsapp = models.CharField(max_length=50)
    email = models.EmailField()
    tier = models.CharField(
        max_length=20,
        choices=TIER_CHOICES,
        blank=True,   # keeps migration painless
        null=True     # keeps migration painless
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # show tier in admin list if available
        return f"{self.name} from {self.company}" + (f" – {self.tier}" if self.tier else "")



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

from django.db import models

class FreePassRegistrant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"

from django.db import models

class ExhibitRegistration2(models.Model):
    # ----- Choices -----
    TIER_CHOICES = [
        ("startup", "Startup Booth"),
        ("growth", "Growth Booth"),
        ("enterprise", "Enterprise Booth"),
    ]
    COMPANY_SIZE_CHOICES = [
        ("1-20", "1–20"),
        ("21-100", "21–100"),
        ("100+", "100+"),
    ]
    PRICING_MODE_CHOICES = [
        ("early", "Early"),
        ("regular", "Regular"),
    ]

    # ----- Company & contact -----
    company_name  = models.CharField(max_length=150)
    company_size  = models.CharField(max_length=16, choices=COMPANY_SIZE_CHOICES)
    industry      = models.CharField(max_length=120, blank=True)
    website       = models.URLField(blank=True)
    contact_name  = models.CharField(max_length=120)
    email         = models.EmailField()
    phone         = models.CharField(max_length=40, blank=True)

    # ----- Package & pricing -----
    tier          = models.CharField(max_length=20, choices=TIER_CHOICES)
    pricing_mode  = models.CharField(max_length=10, choices=PRICING_MODE_CHOICES, default="early")
    base_price    = models.PositiveIntegerField(default=0, help_text="PHP, no decimals")
    total_price   = models.PositiveIntegerField(default=0, help_text="PHP, no decimals")

    # ----- Add-ons -----
    add_logo      = models.BooleanField(default=False)
    add_power     = models.BooleanField(default=False)
    add_leads     = models.BooleanField(default=False)

    # ----- Misc -----
    notes         = models.TextField(blank=True)
    agree         = models.BooleanField(default=False)

    # ----- Timestamps -----
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Exhibit Registration"
        verbose_name_plural = "Exhibit Registrations"

    def __str__(self):
        return f"{self.company_name} — {self.get_tier_display()} ({self.get_pricing_mode_display()})"

    # Pretty pesos for admin/list views
    @staticmethod
    def _peso(n: int) -> str:
        return f"₱{n:,}"

    @property
    def base_price_peso(self) -> str:
        return self._peso(self.base_price or 0)

    @property
    def total_price_peso(self) -> str:
        return self._peso(self.total_price or 0)

    @property
    def addons_selected_list(self) -> list[str]:
        items = []
        if self.add_logo:  items.append("Logo on website & stage screen")
        if self.add_power: items.append("Power outlet & extension")
        if self.add_leads: items.append("Lead scanner access")
        return items

from django.db import models

# Create your models here.
class About(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100, default="UI/UX Designer & Web Developer")
    profile_image = models.ImageField(upload_to='profile/')
    short_description = models.TextField()
    detailed_description = models.TextField()
    birthday = models.DateField(default="2000-01-01")
    website = models.URLField(default="https://example.com")
    phone = models.CharField(max_length=20, default="+1234567890")
    city = models.CharField(max_length=100, default="City Name")
    age = models.PositiveIntegerField(default=18)
    degree = models.CharField(max_length=50, default="Bachelor's Degree")
    email = models.EmailField(default="abc@gmail.com")
    freelance = models.CharField(max_length=50, default="Available")

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)

    def __str__(self):
        return self.title
    
class Skill(models.Model):
    name = models.CharField(max_length=50)
    proficiency = models.PositiveIntegerField(help_text="Enter value from 0 to 100")
    

    def __str__(self):
        return f"{self.name} - {self.proficiency}%"

class Stat(models.Model):
    label = models.CharField(max_length=50)
    count = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.label}: {self.count}"

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonials/')
    rating = models.PositiveIntegerField(default=5, help_text="Enter number of stars (1-5)")
    feedback = models.TextField()

    def __str__(self):
        return self.name

class Resume(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.job_title} at {self.company} ({self.start_year} - {self.end_year or 'Present'})"


class OwnerContactInfo(models.Model):
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    map_location = models.URLField(blank=True, null=True)  # e.g. Google Maps URL

    def __str__(self):
        return "Owner Contact Information"


class VisitorMessage(models.Model):
    name     = models.CharField(max_length=100)
    email    = models.EmailField()
    subject  = models.CharField(max_length=200)        # ← add this
    message  = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} – {self.subject}'

class SiteImage(models.Model):
    USAGE_CHOICES = [
        ('hero', 'Hero Section'),
        ('gallery', 'Gallery'),
        ('project', 'Project Thumbnail'),
        ('banner', 'Background Banner'),
        ('testimonial', 'Testimonial Avatar'),
    ]

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='site_images/')
    usage = models.CharField(max_length=20, choices=USAGE_CHOICES)
    alt_text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.title} ({self.usage})"
    
class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.degree} in {self.field_of_study} from {self.institution}"

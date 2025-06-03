from django.shortcuts import render, redirect
from django.contrib import messages
from .models import About, Project, Skill, Stat, Testimonial, Resume, Education, OwnerContactInfo, VisitorMessage, SiteImage
from .forms import VisitorMessages

# Create your views here.
def home(request):
    hero_image_obj = SiteImage.objects.filter(usage='hero').first()
    about = About.objects.first()

    context = {
        'hero_pic': hero_image_obj.image.url if hero_image_obj else '',
        'hero_alt': hero_image_obj.alt_text if hero_image_obj else 'Hero Image',
        'name': about.name if about else 'Your Name',
        'short_description': about.short_description if about else 'Your description here.'
    }
    return render(request, 'main/home.html', context)

def chunk_skills(skills, chunk_size=3):
    for i in range(0, len(skills), chunk_size):
        yield skills[i:i + chunk_size]


def about(request):
    template_name = 'main/about.html'

    about = About.objects.first()
    skills = Skill.objects.all()  # ✅ FIXED: Get queryset, not class
    skill_rows = list(chunk_skills(skills, 3))
    testimonials = Testimonial.objects.all()  # ✅ FIXED: Get queryset, not class

    context = {
        'title': 'About Me',
        'description': 'Learn more about my background and skills.',
        'about': about,
        'skill_rows': skill_rows,
        'testimonials': testimonials,
    }

    return render(request, template_name, context)

def resume(request):
    template_name = 'main/resume.html'
    resumes = Resume.objects.all()  # ✅ FIXED: Get queryset, not class
    context = {
        'title': 'Resume',
        'description': 'View my professional experience and qualifications.',
        'resumes': resumes,
    }
    return render(request, template_name, context)
def education(request):
    template_name = 'main/education.html'
    educations = Education.objects.all ()  # ✅ FIXED: Get queryset, not class
    if not education:
        messages.warning(request, 'No education records found.')
    about = About.objects.first()
    if not about:
            messages.error(request, 'No About information available.')
            return redirect('home')
    Contact = OwnerContactInfo.objects.first()
    if not Contact:
        messages.error(request, 'No contact information available.')
        return redirect('home')
    context = {
        'title': 'Education',
        'description': 'Explore my educational background and achievements.',
        'educations': educations,
        'about': about,
        'contact': Contact,
    }
    return render(request, template_name, context)
def portfolio(request):
    template_name = 'main/portfolio.html'
    context = {
        'title': 'Portfolio',
        'description': 'Check out my projects and works.'
    }
    return render(request, template_name, context)
def blog(request):
    template_name = 'main/blog.html'
    context = {
        'title': 'Blog',
        'description': 'Read my latest articles and thoughts.'
    }
    return render(request, template_name, context)
def contact(request):
    template_name = 'main/contact.html'
    contact = OwnerContactInfo.objects.first()
    form = VisitorMessages(request.POST or None)
    if form.is_valid():
        form.save()
        # Here you would typically process the form data, e.g., send an email
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')  # Redirect to avoid resubmission on refresh
    context = {
        'title': 'Contact',
        'description': 'Get in touch with me for collaborations or inquiries.',
        'contact': contact,
        'form': form
    }
    return render(request, template_name, context)



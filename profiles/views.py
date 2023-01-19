from django.shortcuts import render


def profile(request):
    """ Display th euser's profile """
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)

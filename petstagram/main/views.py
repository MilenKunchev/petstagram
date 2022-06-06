from django.shortcuts import render

""" рендерираме НОМЕ страницата за да я покажем
view  е фунция която взима параметър  request  и връща HTP response"""


def show_home(request):
    return render(request, 'home_page.html')


def show_dashboard(request):
    return render(request, 'dashboard.html')


def show_profile(request):
    return render(request, 'profile_details.html')


def show_pet_photo_details(request, pk):
    return render(request, 'photo_details.html')

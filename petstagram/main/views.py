from django.shortcuts import render

""" рендерираме НОМЕ страницата за да я покажем
view  е фунция която взима параметър  request  и връща HTP response"""


def show_home(request):
    context = {
        'hide_additional_nav_items': True
    }
    return render(request, 'home_page.html', context)


def show_dashboard(request):
    context = {

    }
    return render(request, 'dashboard.html', context)


def show_profile(request):
    return render(request, 'profile_details.html')


def show_pet_photo_details(request, pk):
    return render(request, 'photo_details.html')

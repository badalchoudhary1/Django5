from django.shortcuts import render


def set_cookie(request):
    response = render(request, 'set_cookie.html')
    # Cookie expires in 1 hour
    response.set_cookie('username', 'badal', max_age=3600)
    return response


def get_cookie(request):
    username = request.COOKIES.get(
        'username', 'Guest')  # Default value is 'Guest'
    return render(request, 'get_cookie.html', {'username': username})


def delete_cookie(request):
    response = render(request, 'delete_cookie.html')
    response.delete_cookie('username')  # Deletes the 'username' cookie
    return response

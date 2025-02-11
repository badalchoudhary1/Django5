from django.shortcuts import render


def set_session(request):
    request.session['username'] = 'JohnDoe'  # Store data in session
    request.session['email'] = 'john@example.com'  # Store email
    request.session.set_expiry(3600)  # Session expires in 1 hour (optional)
    return render(request, 'set_session.html')


def get_session(request):
    username = request.session.get(
        'username', 'Guest')  # Default value: 'Guest'
    email = request.session.get('email', 'No Email')
    return render(request, 'get_session.html', {'username': username, 'email': email})


def delete_session(request):
    request.session.flush()  # Clears all session data
    return render(request, 'delete_session.html')

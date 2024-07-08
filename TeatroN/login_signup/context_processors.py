def user_context(request):
    if request.user.is_authenticated:
        return {
            'user': {
                'nombre': request.user.nombre,
                'email': request.user.email,
                'rol': request.user.rol,
            }
        }
    else:
        return {
            'user': None
        }
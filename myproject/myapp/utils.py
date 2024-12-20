# myapp/utils.py
from .models import Farmer

def is_farmer_authenticated(request):
    return request.session.get('farmer_id') is not None

def get_logged_farmer(request):
    if is_farmer_authenticated(request):
        return Farmer.objects.get(id=request.session['farmer_id'])
    return None
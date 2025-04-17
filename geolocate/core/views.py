from django.shortcuts import render
from django.http import JsonResponse
import requests
from .models import Location, User

# Create your views here.
def index(request):
    """
    View function for the index page.
    """
    # Get all saved locations
    locations = Location.objects.all().select_related('user')
    context = {
        'locations': locations
    }
    return render(request, 'core/index.html', context)

def get_location(request):
    """
    View function to get location data from coordinates.
    """
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    
    if not lat or not lon:
        return JsonResponse({'error': 'Latitude and longitude are required'}, status=400)
    
    try:
        # Round latitude and longitude to 6 decimal places
        lat = round(float(lat), 6)
        lon = round(float(lon), 6)
        
        # Using OpenStreetMap Nominatim API to get location data
        url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}&zoom=18&addressdetails=1"
        headers = {
            'User-Agent': 'Django Geolocation App/1.0'
        }
        
        response = requests.get(url, headers=headers)
        data = response.json()
        
        if 'error' in data:
            return JsonResponse({'error': data['error']}, status=400)
        
        # Extract city and country from the response
        address = data.get('address', {})
        city = address.get('city') or address.get('town') or address.get('village') or 'Unknown'
        country = address.get('country') or 'Unknown'
        
        # Save location data to the database
        try:
            user = User.objects.first()  # Get the first user in the database
            if user:
                # Update or create location for the user
                location, created = Location.objects.update_or_create(
                    user=user,
                    defaults={
                        'latitude': lat,
                        'longitude': lon
                    }
                )
                saved = True
            else:
                saved = False
        except Exception as e:
            print(f"Error saving location: {e}")
            saved = False
        
        return JsonResponse({
            'latitude': lat,
            'longitude': lon,
            'city': city,
            'country': country,
            'saved': saved
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
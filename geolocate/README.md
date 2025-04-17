# Django Geolocation App

A Django web application that allows users to get and store their current geolocation data, including latitude, longitude, city, and country information.

## Features

- Get current location using browser's Geolocation API
- Reverse geocoding using OpenStreetMap Nominatim API
- Store location data in a database
- Display location history with timestamps
- Custom User model
- Precise coordinate handling (6 decimal places)

## Prerequisites

- Python 3.8 or higher
- Django 5.0 or higher
- requests library

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd geolocate
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply database migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

## Running the Application

1. Start the development server:
```bash
python manage.py runserver
```

2. Open your web browser and navigate to:
```
http://127.0.0.1:8000/
```

## Usage

1. Click the "Get Location" button to request your current location
2. Allow location access in your browser when prompted
3. The application will display:
   - Your current latitude and longitude (6 decimal precision)
   - City and country information
   - Whether the location was successfully saved to the database
4. View your location history in the table below

## API Endpoints

- `/` - Main page with location functionality
- `/get_location/` - API endpoint for getting and saving location data
  - Parameters:
    - `lat`: Latitude (float)
    - `lon`: Longitude (float)
  - Returns:
    - Location data in JSON format
    - City and country information
    - Save status

## Models

### User Model
- Custom user model extending Django's AbstractUser

### Location Model
- OneToOne relationship with User
- Stores latitude and longitude (6 decimal places)
- Includes created_at and updated_at timestamps

## Security Considerations

- Uses Django's built-in CSRF protection
- Implements proper error handling
- Validates coordinate data
- Uses environment variables for sensitive data (recommended for production)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
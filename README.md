# notification_preference

# Objective:
### To create REST APIs that support functionalities for managing user 
### notification preferences. The APIs allow users to retrieve and update 
### their notification preferences, adhering to Django best practices and 
### RESTful standards.

# Setup
### git clone https://github.com/erpawan/notification_preference.git
### cd notification_preference

### python3 -m venv venv # Linux
### source venv/bin/activate # Linux
### pip3 install -r requirements.txt # Linux

### python -m venv venv # Windows
### venv/Scripts/activate # Windows
### pip install -r requirements.txt

### python manage.py makemigrations # use python3 for Linux
### python manage.py migrate

### python manage.py runserver

# API Endpoints:

## Notification Types:

### (GET /api/notification-types/ - List all notification types.)

### (POST /api/notification-types/ - Create a new notification type.)

### (GET /api/notification-types/{id}/ - Retrieve a specific notification type.)

### (PUT /api/notification-types/{id}/ - Update a specific notification type.)

### (DELETE /api/notification-types/{id}/ - Delete a specific notification type.)

## Notification Preferences:

### (GET /api/notification-preferences/ - List all notification preferences.)

### (POST /api/notification-preferences/ - Create a new notification preference.)

### (GET /api/notification-preferences/{id}/ - Retrieve a specific notification preference.)

### (PUT /api/notification-preferences/{id}/ - Update a specific notification preference.)

### (DELETE /api/notification-preferences/{id}/ - Delete a specific notification preference.)


# Testing

### Testing can be done using Postman, by calling above endpoints


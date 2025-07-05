# Django Expense Tracker API Documentation

## Project Overview
This documentation provides an overview of the **Expense Tracker API** built with Django and Django REST Framework.
The API allows users to manage their expenses, including creating, updating, and deleting expense records.
<br/>
The API follows RESTful principles and uses JSON Web Tokens (JWT) for authentication. Meaning, the API is stateless, and each request from the client must contain all the information needed to understand and process the request.
<br/>
The API is designed to be secure, efficient, and easy to use, providing endpoints for user authentication and expense management.
Also provides OpenAPI documentation for easy integration and understanding of the API endpoints.
<br/>
## Features
- User authentication with JWT tokens.
- Expense management, including creating, updating, and deleting expense records.
- Secure access to expense records, ensuring that users can only access their own data.
- OpenAPI documentation for easy integration and understanding of the API endpoints.

## Current Version: `v0.1.0`


## Development Phases
This project is divided into several phases, each focusing on different aspects of the application:

### Phase 1: Project Initialization
A root folder named `expense-tracker` was created, containing the following. A Django project named `src` was initialized within this folder that serves as the main application.
<br/>
Structure of the project:
```
expense-tracker/
├── src/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   ├── apps/
│   │   ├── auth/
│   │   └── expenses/
│   └── __init__.py
├── .env
├── requirements.txt
├── manage.py
├── .gitignore
└── README.md

```
The `src` folder contains the main Django project files, including settings, URLs, and WSGI/ASGI configurations. The `src/apps` folder contains two Django applications: `auth` for user authentication and `expenses` for managing expense records. This structure allows for better organization and modularity of the codebase.
<br>
A virtual environment was created to manage dependencies, and the following packages were installed:
The following packages were installed to support the development of the Expense Tracker API:
- `Django`: The main framework for building the web application.
- `djangorestframework`: Provides tools for building RESTful APIs.
- `djangorestframework-simplejwt`: For handling JSON Web Tokens (JWT) for authentication.
- `django-cors-headers`: To handle Cross-Origin Resource Sharing (CORS) in the API.
- `drf-spectacular`: For generating OpenAPI documentation for the API.

### Phase 2: Configuration
The [settings.py](src/settings.py) file was updated to make the project ready for development. Different settings were added, such as:
- `INSTALLED_APPS`: Added `rest_framework`, `corsheaders`, `rest_framework_simplejwt`, and `drf_spectacular` for API development. Also custom apps `auth` and `expenses` were added.
- `MIDDLEWARE`: Included `corsheaders.middleware.CorsMiddleware` to handle CORS.
- `CORS_ALLOWED_ORIGINS`: Configured to allow requests from `http://localhost:3000`.
- `REST_FRAMEWORK`: Configured to use `drf_spectacular` for API documentation.
- `SPECTACULAR_SETTINGS`: Configured to use `drf_spectacular` for generating OpenAPI schema.
- `SIMPLE_JWT`: Configured JWT settings, including access and refresh token lifetimes.
- `LOGGING`: Set up dictionary-based logging configuration to log errors and warnings.
- `.env` file was created to store sensitive information such as the Django secret key and JWT token lifetimes. This file is not included in version control for security reasons.

### Phase 2: App Creation
`apps` folder was created inside the `src` folder to hold the Django applications. Two applications were created:
- `auth`: Handles user authentication and authorization.
- `expenses`: Manages expense records.

### Phase 3: User Authentication
The `auth` application was developed to handle user registration, login, logout, and profile management. Django's built-in User model was used for user management. The following features were implemented:
- **User Registration**: Allows users to create an account with a username, email, and password.
- **User Login**: Allows users to log in and receive JWT tokens for authentication.
- **User Logout**: Allows users to log out and blacklist their refresh tokens.
- **User Profile**: Allows users to view and update their profile information.
- **JWT Authentication**: Used `djangorestframework_simplejwt` for handling JWT tokens, including access and refresh tokens.

### Phase 4: Expense Management
The `expenses` application was developed to manage expense records. The following features were implemented:
- **Expense Model**: Created a model to represent expense records, including fields for amount, description, date, and category.
- **Expense List and Create Views**: Implemented API views to list all expenses and retrieve details of a specific expense.
- **Expense Retrieve, Update, and Delete Views**: Implemented functionality to retrieve, update, and delete expense records.
- **Protected Views**: Used JWT authentication to protect expense-related views, ensuring that only authenticated users can access them.
- **Data Privacy**: Implemented measures to ensure that users can only access their own expense records, protecting sensitive information.

## API Documentation (Swagger UI)
The API documentation is generated using `drf-spectacular` and can be accessed at the following URL:
```
http://localhost:8000
```
![Swagger UI Screenshot](public/openapi_interface.png)

## Future Improvements
- Role based access control to manage permissions for different user roles.
- Enhanced error handling and validation for API requests.
- Weekely, Monthly, and Yearly expense reports.
- Integration with third-party services for expense tracking and analysis.
- Email notifications for important events, such as high expenses or budget limits.
- Search and filter functionality for expenses.
- Visualization of expenses using charts and graphs.

## Running the Project (for Devs)
To run the project locally, follow these steps:
```
# Clone the repository
git clone https://github.com/prem-poudel/expense-tracker
cd expense-tracker

# Create and activate virtual environment
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file and add your secret key and JWT settings

# Apply migrations and run server
python manage.py migrate
python manage.py runserver
```

## Conclusion
The Expense Tracker API provides a robust and secure solution for managing expenses. It leverages Django and Django REST Framework to deliver a user-friendly experience for expense management. The API is designed to be extensible, allowing for future enhancements and features to be added as needed.
This documentation serves as a guide for developers and users to understand the API's capabilities and how to interact with it effectively. For any issues or contributions, please refer to the project's GitHub repository.
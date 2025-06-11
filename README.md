🏋️‍♀️ Fitness Studio Booking API

This project is a backend API for a fictional fitness studio, built using Django and Django REST Framework.
It provides endpoints for:

1. Viewing scheduled fitness classes
2. Booking a slot in upcoming classes
3. Viewing a client's booking history

🧠 Design Considerations
1. Simplified Client Booking (No Auth)
  To stay focused on the project requirement, the API does not require user registration or authentication.
  Instead, a client can book a class using their name and email directly.

  ✅ This keeps the API lightweight and aligns with the assignment goals.
  ⚠️ In a real-world scenario, user authentication and verification would be necessary to avoid misuse.

2. Codebase Clarity
  The model FitnessClass is used instead of Class to avoid clashing with Python’s reserved keyword.
  

⚙️ Setup and Installation
  1. Clone the Repository:
    git clone <your-github-repo-url>
    cd fitness_booking_backend

  2. Create & Activate a Virtual Environment
      python -m venv venv
      source venv/bin/activate        # On Windows: venv\Scripts\activate
  
  4. Install Dependencies
      pip install -r requirements.txt
  
  5. Apply Migrations
      python manage.py migrate
     
  7. Start the Development Server
      python manage.py runserver
      The API will now be accessible at:👉 http://127.0.0.1:8000/
      ✅ The database is already preloaded with sample data for classes and instructors to test the booking functionality.

📄 API Documentation
  Interactive Swagger UI is available at:
  🔗 http://127.0.0.1:8000/swagger-ui/
  Postman collection: https://www.postman.com/crimson-astronaut-106494/my-workspace/collection/kiuhv4v/fitness-booking-api?action=share&creator=25296448&active-environment=25296448-340b03ae-28ac-4619-afc3-277d432f2806

Use this interface to explore endpoints, try out requests, and view response formats.

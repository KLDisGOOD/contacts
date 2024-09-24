# Emergency  Contacts API

This is a simple Django REST API for managing emergency contacts.

## Table of Contents
- [Local Installation](#Local-Installation)

- [API Endpoints](#api-endpoints)
  - [Create a Contact](#create-a-contact)
  - [Delete a Contact](#delete-a-contact)
- [Deployment](##deployment)

## Local Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/kldisgood/task
   cd task
   ```


2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations:

  ```
  python manage.py makemigrations
   ```
   ```
   python manage.py migrate
   ```



4. Run the server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Create a Contact

- **URL**: `/api/contacts/`
- **Method**: `POST`
- **Body**:
   ```json
   {
      "first_name": "John",
      "last_name": "Doe",
      "phone_number": "+123246897238"
   }
   ```
- **Response**: 
  - Status: `201 Created`
  - Body:
    ```json
    {
      "id": 1,
      "first_name": "John",
      "last_name": "Doe"
      "phone_number": "+123246897238"
    }
    ```


### Delete a Contact

- **URL**: `/api/contacts/{id}/`
- **Method**: `DELETE`
- **Response**:
  - Status: `204 No Content`

## Deployment

This project is deployed on Render. You can access the deployed API at: [Render App Link](https://contacts-ec0k.onrender.com)


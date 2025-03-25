# Task Management API

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd taskmanagement
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

## API Endpoints

### Create a Task
- URL: `POST /api/tasks/`
- Sample Request:
    ```json
    {
        "name": "Sample Task",
        "description": "This is a sample task.",
        "task_type": "personal",
        "status": "pending"
    }
    ```
- Sample Response:
    ```json
    {
        "id": 1,
        "name": "Sample Task",
        "description": "This is a sample task.",
        "created_at": "2025-03-25T06:14:41Z",
        "task_type": "personal",
        "completed_at": null,
        "status": "pending",
        "assigned_users": []
    }
    ```

### Assign a Task to Users
- URL: `POST /api/tasks/{task_id}/assign/`
- Sample Request:
    ```json
    {
        "user_ids": [1, 2]
    }
    ```
- Sample Response:
    ```json
    {
        "status": "task assigned"
    }
    ```

### Get Tasks for a Specific User
- URL: `GET /api/users/{user_id}/tasks/`
- Sample Response:
    ```json
    [
        {
            "id": 1,
            "name": "Sample Task",
            "description": "This is a sample task.",
            "created_at": "2025-03-25T06:14:41Z",
            "task_type": "personal",
            "completed_at": null,
            "status": "pending",
            "assigned_users": [
                {
                    "id": 1,
                    "username": "user1",
                    "email": "user1@example.com",
                    "mobile": "1234567890"
                }
            ]
        }
    ]
    ```

## Test Credentials
Use the superuser credentials created during setup to access the admin interface and create test users.

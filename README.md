# Task Manager API - Readme

Welcome to the Task Manager API! This API allows you to manage tasks through RESTful endpoints. Below, you'll find details about each route, the route URL, how to access the URLs, route functionalities, and additional notes.

## API Endpoints

1. **Register a User**

   - URL: `/api/register/`
   - Method: `POST`
   - Description: Creates a new user account with a unique username and email. The user will receive an authentication token upon successful registration, which will be used for subsequent API calls.
   - Request Body: JSON
     ```json
     {
     	"username": "your_username",
     	"email": "your_email@example.com",
     	"password": "your_password"
     }
     ```
   - Response: JSON
     ```json
     {
     	"token": "your_auth_token"
     }
     ```

2. **Obtain a Token**

   - URL: `/api/token/`
   - Method: `POST`
   - Description: Obtains an authentication token for an existing user, which will be used for subsequent API calls. Requires the user's username and password.
   - Request Body: JSON
     ```json
     {
     	"username": "your_username",
     	"password": "your_password"
     }
     ```
   - Response: JSON
     ```json
     {
     	"token": "your_auth_token"
     }
     ```

3. **List Tasks**

   - URL: `/api/tasks/`
   - Method: `GET`
   - Description: Retrieves a paginated list of all tasks. Requires a valid authentication token in the request header.
   - Request Header:
     ```
     Authorization: Token your_auth_token
     ```
   - Response: JSON array of task objects
     ```json
     [
     	{
     		"id": 1,
     		"title": "Task 1",
     		"description": "Task 1 description",
     		"created_at": "2023-08-02T12:34:56Z",
     		"updated_at": "2023-08-02T12:34:56Z",
     		"due_date": "2023-08-10T00:00:00Z",
     		"is_completed": false,
     		"priority": "low",
     		"assignee": {
     			"id": 1,
     			"username": "assignee_username",
     			"email": "assignee_email@example.com"
     		}
     	}
     	// More task objects...
     ]
     ```

4. **Create a Task**

   - URL: `/api/tasks/`
   - Method: `POST`
   - Description: Creates a new task. Requires a valid authentication token in the request header.
   - Request Header:
     ```
     Authorization: Token your_auth_token
     ```
   - Request Body: JSON
     ```json
     {
     	"title": "Task title",
     	"description": "Task description",
     	"due_date": "YYYY-MM-DD",
     	"is_completed": false,
     	"priority": "low"
     }
     ```
   - Response: JSON object of the created task
     ```json
     {
     	"id": 2,
     	"title": "Task title",
     	"description": "Task description",
     	"created_at": "2023-08-02T12:34:56Z",
     	"updated_at": "2023-08-02T12:34:56Z",
     	"due_date": "2023-08-10T00:00:00Z",
     	"is_completed": false,
     	"priority": "low",
     	"assignee": {
     		"id": 1,
     		"username": "your_username",
     		"email": "your_email@example.com"
     	}
     }
     ```

5. **Retrieve, Update, or Delete a Task**

   - URL: `/api/tasks/<task_id>/`
   - Method: `GET`, `PUT`, `PATCH`, `DELETE`
   - Description: Retrieves, updates, or deletes a specific task based on the provided task ID. Requires a valid authentication token in the request header.
   - Request Header:
     ```
     Authorization: Token your_auth_token
     ```
   - Response: JSON object of the task (for GET, PUT, and PATCH) or success message (for DELETE).

## Permissions

- The `permission_classes = [IsAuthenticated]` added in the `views.py` file ensures that users must be authenticated (i.e., have a valid token) to access the task-related endpoints.

## Additional Notes

- The API supports pagination for listing tasks. By default, the response will contain a limited number of tasks, and you can navigate through pages using the `page` query parameter in the request URL.

- The `due_date` field for creating and updating tasks should be provided in the format `YYYY-MM-DD`.

- The `is_completed` field should be a boolean value (`true` or `false`) indicating the completion status of the task.

- The `priority` field should be one of the choices (`low`, `medium`, or `high`) indicating the priority level of the task.

Please ensure you have the necessary authentication token when making requests to the API, as endpoints are protected and require a valid token for access.

Thank you for using the Task Manager API! If you have any questions or need further assistance, feel free to reach out. Happy task managing!

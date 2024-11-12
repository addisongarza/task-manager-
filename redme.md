# Task Manager Web Application

This is a simple Task Manager web application built with Flask. The app allows users to register, log in, add tasks, mark tasks as complete (visual effect only), and delete tasks. The design follows a green monochromatic theme with balloon-like lettering and interactive elements for a fun and engaging experience.

## Features

- **User Authentication**: Allows users to register, log in, and log out.
- **Task Management**: Users can add, view, and delete tasks.
- **Styling**: Green monochromatic theme, with a balloon-like font, interactive buttons, and icons.
- **Responsive Design**: The app is optimized for both desktop and mobile viewing.

## Technologies Used

- **Flask**: Python web framework for server-side processing.
- **Flask-Login**: Handles user session management.
- **Flask-WTF**: Provides form handling and validation.
- **SQLite**: Database for storing users and tasks.
- **HTML/CSS**: Frontend styling and structure.
- **JavaScript (optional)**: For interactive elements if further customization is needed.

## Folder Structure

```plaintext
todo_app/
├── app.py               # Main application file with route and app configuration
├── models.py            # Database models for User and Task
├── forms.py             # Form definitions for user input
├── templates/           # HTML templates for different pages
│   ├── base.html        # Base template with common layout
│   ├── index.html       # Main task manager page
│   ├── login.html       # Login page
│   └── register.html    # Registration page
└── static/
    ├── styles.css       # CSS file for theme styling
    └── checkmark.gif    # Placeholder GIF for task status

## Code Explanation

### 1. `app.py`
The main application file that initializes the Flask app, configures the database, and defines routes. Key sections include:

- **App Setup**: Configures Flask and SQLAlchemy for database connection, and Flask-Login for user session management.
- **Routes**:
  - `/register`: Registration page where users create an account.
  - `/login`: Login page where users can authenticate.
  - `/logout`: Logs the user out.
  - `/`: Main page where users can add, view, and delete tasks.
  - `/delete_task/<task_id>`: Deletes a task by its unique ID.

### 2. `models.py`
Defines the database models:

- **User**: Stores user information (username, hashed password).
- **Task**: Stores task information (title, completed status, associated user ID).

### 3. `forms.py`
Defines forms using Flask-WTF:

- **RegisterForm**: Form for user registration with fields for username and password.
- **LoginForm**: Form for user login.
- **TaskForm**: Form for adding tasks, with fields for task title.

### 4. `templates/` Folder
Contains HTML files with Jinja templating for dynamic content rendering:

- **`base.html`**: Common layout with navigation.
- **`index.html`**: Displays tasks and task management functions.
- **`login.html`**: Form for user login.
- **`register.html`**: Form for user registration.

### 5. `static/` Folder
- **`styles.css`**: Contains CSS for the green monochromatic theme, balloon-like lettering, and interactive elements.
- **`checkmark.gif`**: Placeholder GIF for task completion status.

---

## Setup and Running the Application

### Prerequisites

- **Python 3.x**: Make sure Python is installed.
- **Flask and Other Dependencies**: Install dependencies listed in `requirements.txt`.

### Installation Steps

1. Clone the repository and navigate to the project folder.

   ```bash
   git clone <repository_url>
   cd todo_app
 
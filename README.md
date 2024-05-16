# CoordiGO
Video Demo: https://youtu.be/HA_U1ulXD5Y

## Distinctiveness and Complexity
**Distinctiveness** CoordiGO is unique in its provision of a dynamic interface for creating, customizing, and managing Graphic Organizers. This focus goes beyond general assignment submission platforms by offering tools specifically designed for GOs, making it an innovative solution in educational technologies. 
The platform seamlessly integrates classroom management with assignment distribution and grading, all centered around the use of Graphic Organizers. This holistic approach is distinct from other systems that treat assignment management and classroom management as separate entities.

**Complexity** CoordiGO employs Django models to manage data interactions required for customizing GOs, tracking student progress, and storing educational content. The application captures basic user activities and also links these activities to provide analytics and actionable insights, thus supporting personalized education.
The use of JavaScript to facilitate real-time, interactive experiences without page reloads adds a layer of complexity to the front-end development. This enhances user engagement by providing a smooth and responsive user interface that dynamically adjusts based on teacher and student interactions.
CoordiGO features a notification system that alerts teachers and students about assignment statuses, grades, and updates. This system is designed to work seamlessly across the user spectrum to keep all parties informed in real-time, thus supporting a continuous feedback loop essential for educational settings.

Through its focused approach on Graphic Organizers, backend architecture, and interactive user interfaces, CoordiGO not only differentiates itself from other projects but also incorporates functionalities that are critical in modern educational environments. These features collectively contribute to an enhanced learning and teaching experience, making CoordiGO a distinctive and complex project in the field of educational technology.

## Introduction
CoordiGO is a web-based educational platform designed to transform the way teachers and students interact with graphic organizer assignments. Built with Django, Python, JavaScript, and SQL, this prototype tool enables the coordination, creation, assignment, submission, and grading of graphic organizers in a seamless manner. 
The application aims to make graphic organizers a more dynamic element in the educational process by facilitating user engagement and efficient data collection. This supports teachers in customizing assignments and grading, and helps in tracking student performance more effectively.

## Prerequisites and Installation
Before you begin the installation of CoordiGO, ensure you have the following tools and technologies installed on your system:

**Python 3 or higher**: Ensure you have the latest version of Python installed, as it is crucial for due to dependencies on recent language features and libraries.
**Django**: This project utilizes Django, a high-level Python web framework that encourages rapid development and clean, pragmatic design.
**SQLite3 Database**: SQLite3 serves as the default database for Django projects due to its simplicity and ease of setup.
**Contemporary Web Browser**: A modern web browser such as Google Chrome is required to access and interact with the CoordiGO platform.

### Installation Guide
1. Clone the Repository:
    - Open a terminal or command prompt.
    - Navigate to the directory where you want to clone the CoordiGO repository.
    - Run the following command to clone the repository:
    `git clone https://github.com/yourusername/CoordiGO.git`

2. Set Up a Virtual Environment (optional but recommended)
3. Install Dependencies:
    - Ensure that your virtual environment is active.
    - Install all required Python packages by running:
    `pip install -r requirements.txt`
4. Initialize the Database:
Run the Development ServerMake sure you are in the project root directory where the manage.py file is located.
    - Run the following commands to set up your database
    `python3 manage.py makemigrations`
    `python3 manage.py migrate`

5. Run the Development Server:
    - Start the Django development server by executing:
    `python3 manage.py runserver`
    - Open your web browser and go to http://127.0.0.1:8000/ to view the application

## File Organization
CoordiGO is structured according to Django's best practices to ensure maintainability and scalability. Below is an overview of the key components and how they are organized within the project:
**Project Folder**: coordi 
**Static Folder**: All static files, including CSS and JavaScript files, are stored in the static directory. 
- CSS files are used to style the frontend of the application, ensuring that the user interface is visually appealing and functionally responsive. 
- JavaScript files enhance interactivity of the web pages by providing dynamic content updates and client-side logic.
**Templates Folder**: Django templates are located in the templates folder, which stores all HTML files. These templates integrate seamlessly with Django’s backend to dynamically generate content based on the context provided by views.
**Migrations Folder**: Django app includes a migrations folder which contains migration files. These files are automatically generated when you make changes to the models and are executed to alter the database schema without losing data. This folder is crucial for tracking the evolution of the database structure over time.
**Models**: Located in the models.py file, models define the design of the data structure. These models facilitate interactions with the database through Django's ORM, allowing for efficient data querying and manipulation.
**Views**: The views.py file, contain the logic to process incoming requests and return responses. Views fetch data through models, process it as needed, and pass it to templates for rendering.
**URLs**: URL declarations are found in the urls.py files within each Django app as well as the project’s main directory. These files define the URL structure of the web application, mapping URLs to their corresponding views.
**Admin**: Django’s admin interface is customized for CoordiGO to facilitate easy management of application data by authorized admin users. This is configured through admin.py.
**Apps**: The application is divided into Django apps, it is responsible for handling a specific piece of functionality. This modular approach helps in isolating different parts of the project, making it easier to manage and scale.

## User Account Management
CoordiGO incorporates a robust user account management system that uses a SQL database to securely store user data, including hashed passwords. Python and Django are at the core of managing user authentication, form validation, and database interactions. The system is designed to provide a seamless login experience for existing users, featuring robust error handling to enhance security measures. For new users, the registration process is straightforward and secure. These credentials are securely encrypted and stored, ensuring the privacy and integrity of user information.

## Design Choices and User Interaction
At the heart of CoordiGO’s development are user-centered design and accessibility. The application is crafted to serve both teachers and students with a clear, intuitive interface. Upon login, the index view redirects users to the appropriate dashboard based on the 'user_type' data pulled from the Django model, which is designed to efficiently direct users to user-specific data.

**Teacher Interface**:
After logging in, teachers are redirected to their dashboard, which includes several key features: 
- **My Classroom**: This section allows teachers to view all pertinent student information, including progress represented by a progress bar. From here, teachers can easily navigate to a list of all assignments, organized by student.
- **Graphic Organizer Library**: A repository for both pre-developed templates and custom Graphic Organizer (GO) assignments. JavaScript enables seamless switching between views within the library without the need for page reloads, enhancing usability and efficiency. Teachers can customize these GO templates according to their specific needs, with all modifications saved to the SQLite database to ensure that each student receives the correct assignments.
- **Custom GO Library**: After customization, teachers can save these GOs to a custom library, from which they can be assigned to any student in their classroom.
- **My Assignments**: This section provides a quick overview of all assignments and their current stage in the educational process. It incorporates a notification system that alerts teachers when students submit their assignments for grading, streamlining the review and grading process. Once graded, the final scores are saved to the database and sent to students for review.

**Student Interface**:
Upon logging in, students are directed to their personalized Student Dashboard, designed to provide them with effortless management of and interaction with their assignments.
- **My Assignments**: This area displays all current and past assignments. Students can begin working on any available assignment with a simple click, facilitating immediate engagement. A notification system keeps students informed of new assignments as they are assigned, ensuring they remain up-to-date and actively engaged in their educational journey.
- **My Grades**: Students receive notifications about newly posted grades in this section. It serves as a central place for students to review their grades and reflect on their academic performance. This feedback mechanism is crucial for fostering self-assessment and encouraging continuous improvement.
- **My Profile**: Each student has a dedicated profile page that outlines their overall academic progress and performance metrics. This personalized profile helps students assess their performance over time, offering insights into their strengths and areas for improvement.

## Data Collection
Django models are integral to CoordiGO, underpinning the robust system for storing and rendering user data effectively. This systematic approach to data collection is essential for several core functions within the platform:

- **Rendering Assignments**: Ensures that students receive properly formatted Graphic Organizer (GO) assignments, tailored to their educational needs by the teacher.
- **Assignment Submission and Grading**: Facilitates the submission of completed assignments to teachers for grading, streamlining the evaluation process.
- **Performance Tracking**: Provides both teachers and students with a detailed view of performance and progress. Teachers can monitor the overall progress of their classes and individual students, while students can track their own learning progress through a comprehensive breakdown of their recent assignments and grades.

This data-driven architecture enhances the educational experience by providing actionable insights as well as personalizes the learning journey for each user, making it more engaging and rewarding. 

## Server Side Logic
The server-side logic of CoordiGO is primarily built in Python and leverages the Django framework to efficiently manage core backend functions. This includes handling form submissions, facilitating user authentication, and managing data storage operations.

- **HTTP Requests and Responses**: Python and Django streamline the processing of HTTP requests and generate responses swiftly, ensuring that the application remains responsive and robust under various user actions.
- **Database Interaction**: The interaction with the SQL database enables efficient data queries and updates, which support the dynamic content management needs of CoordiGO.

The choice of Python for server-side logic is based on its readability and comprehensive support for web development tasks. This makes the codebase easier to maintain and scale.

## Future Enhancements
While the current iteration of CoordiGO serves as a robust prototype, the vision for its development includes a number of enhancements that aim to broaden its utility and deepen user engagement. Plans are in place to incorporate full library of Graphic Organizers. Additionally, the application is set to enhance profile data collection and statistical analysis capabilities, allowing for more precise tracking of student progress and more detailed feedback for both students and teachers. Moreover, the introduction of more diverse interactive content is anticipated, which will enrich the learning environment, making it more dynamic and interactive.

# CoordiGO
## Video Demo: https://youtu.be/HA_U1ulXD5Y

### Introduction
CoordiGO is a web-based educational platform designed to transform the way teachers and students interact with graphic organizer assignments. Built with Django, Python, JavaScript, and SQL, this prototype tool enables the coordination, creation, assignment, submission, and grading of graphic organizers in a seamless manner. The application aims to make graphic organizers a more dynamic element in the educational process by facilitating user engagement and efficient data collection. This supports teachers in customizing assignments and grading, and helps in tracking student performance more effectively.

### Prerequisites and Installation
To start the CoordiGO journey, the following prerequisites are essential:

- **Python 3**: Ensure you have the latest version of Python installed, as it is crucial for running the Django framework.
- **Django**: This project utilizes Django, a high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **SQLite3 Database**: SQLite3 serves as the default database for Django projects due to its simplicity and ease of setup.
- **Contemporary Web Browser**: A modern web browser is required to access and interact with the CoordiGO platform.

### User Account Management
CoordiGO incorporates a robust user account management system that uses a SQL database to securely store user data, including hashed passwords. Python and Django are at the core of managing user authentication, form validation, and database interactions. The system is designed to provide a seamless login experience for existing users, featuring robust error handling to enhance security measures. For new users, the registration process is straightforward and secure. These credentials are securely encrypted and stored, ensuring the privacy and integrity of user information.

### Design Choices and User Interaction
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

### Data Collection
Django models are integral to CoordiGO, underpinning the robust system for storing and rendering user data effectively. This systematic approach to data collection is essential for several core functions within the platform:

- **Rendering Assignments**: Ensures that students receive properly formatted Graphic Organizer (GO) assignments, tailored to their educational needs by the teacher.
- **Assignment Submission and Grading**: Facilitates the submission of completed assignments to teachers for grading, streamlining the evaluation process.
- **Performance Tracking**: Provides both teachers and students with a detailed view of performance and progress. Teachers can monitor the overall progress of their classes and individual students, while students can track their own learning progress through a comprehensive breakdown of their recent assignments and grades.

This data-driven architecture enhances the educational experience by providing actionable insights as well as personalizes the learning journey for each user, making it more engaging and rewarding. 

### Server Side Logic
The server-side logic of CoordiGO is primarily built in Python and leverages the Django framework to efficiently manage core backend functions. This includes handling form submissions, facilitating user authentication, and managing data storage operations.

- **HTTP Requests and Responses**: Python and Django streamline the processing of HTTP requests and generate responses swiftly, ensuring that the application remains responsive and robust under various user actions.
- **Database Interaction**: The interaction with the SQL database enables efficient data queries and updates, which support the dynamic content management needs of CoordiGO.

The choice of Python for server-side logic is based on its readability and comprehensive support for web development tasks. This makes the codebase easier to maintain and scale.

### Future Enhancements
While the current iteration of CoordiGO serves as a robust prototype, the vision for its development includes a number of enhancements that aim to broaden its utility and deepen user engagement. Plans are in place to incorporate full library of Graphic Organizers. Additionally, the application is set to enhance profile data collection and statistical analysis capabilities, allowing for more precise tracking of student progress and more detailed feedback for both students and teachers. Moreover, the introduction of more diverse interactive content is anticipated, which will enrich the learning environment, making it more dynamic and interactive.

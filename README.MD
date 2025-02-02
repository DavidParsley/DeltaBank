# Delta Bank by David Parsley

### Description:
Delta Bank is a web application designed to streamline the operations of a bank by connecting users and admins within a unified platform. The system enables users to self-register, manage their personal account details, and view their loans. Admins, once logged in, can manage and oversee all loans in the database, update loan statuses, and delete users along with their loans. Secure authentication ensures that only authorized users can access sensitive data, with users being restricted to their own data and admins having full control over the system's loan management features.

### Problem Statement:
Managing a bank’s operations can be complex, especially with a large number of users and loans. Ensuring that only authorized users can access sensitive information, such as loan records, is crucial for maintaining data security and privacy. The Delta Bank system aims to simplify and centralize these operations by offering a user-friendly platform where users can self-register, view their loans, and update their details, while admins can manage loans, assign them to users, and handle account deletions in a secure environment.

### Proposed Solution:
The Delta Bank system is designed to facilitate user management and loan tracking while providing secure user authentication and authorization. Key features include:

- ***Structured Data Management:*** Centralized management of Users and Loans with clearly defined relationships.
- ***Self-Registration:*** Users can register themselves directly into the system.
- ***CRUD Operations:*** Simple and efficient functions for creating, viewing, updating, and deleting user and loan data.
- ***Authentication:*** Secure login system where users and admins authenticate themselves to access the system's features.
- ***Scalability:*** The platform is designed to support future features and expansions, such as adding more fields or detailed reports.

### Table Relationships:
#### Users and Loans:
- ***Relationship:*** One-to-many  
  A User can have multiple Loans, but each Loan belongs to one User.  
  `user_id` in the Loans table references the `id` in the Users table (representing users).

#### Loans and Users:
- ***Relationship:*** Many-to-one  
  Each Loan is associated with one User, but a User can have multiple loans.  
  `user_id` in the Loans table references the `id` in the Users table.

### User Stories:
#### User Management:
- ***Registration:*** Users can self-register by providing their first name, last name, email, and password.
- ***Login:*** After registration, users must log in to access their personal data and loans.
- ***View Own Loans:*** Users can view all loans that belong to them, including the loan amount, interest rate, and loan status.
- ***Update Account Details:*** Users can update their personal information, such as their email address and password.
- ***Delete Account:*** Users can delete their account (if allowed), which will also delete their associated loans.

#### Admin Management:
- ***Login:*** Admins must log in to access their privileges within the system.
- ***Create Loan:*** Admins can create a new loan, specifying the loan amount, interest rate, start date, and assign it to an existing user.
- ***View All Loans:*** Admins can view a list of all loans in the system.
- ***Update Loan Status:*** Admins can update the status of any loan.
- ***Delete User:*** Admins can delete a user account by their ID, and this will also delete all associated loans.

#### Authentication (For Users and Admins):
- ***Login:*** Both users and admins must log in to access their data, including loans.
- ***JWT Authentication:*** After logging in, users receive a JWT token to authenticate their requests and access secure routes.
- ***Admins:*** Admins can access all data after logging in, while regular users are restricted to their own data.
- ***Logout:*** When users log out, their JWT tokens are added to the TokenBlocklist to prevent reuse.

### Technologies Used:
#### Frontend:
- ***React***
- ***CSS***
- ***React Router***
- ***Toastify***

#### Backend:
- ***Flask***
- ***Flask-SQLAlchemy***
- ***Flask-Migrate***
- ***Flask-JWT-Extended***
- ***Flask-Mail***
- ***Werkzeug (for password hashing)***

### Installation & Setup:
1. Clone the repository:
   ```bash
   git clone https://github.com/DavidParsley/DeltaBank.git

2. Install the necessary dependencies:
bash
Copy
cd delta-bank
pip install -r requirements.txt

3. Set up the database:
bash
Copy
flask db init
flask db migrate
flask db upgrade
Run the application:
bash
Copy

4. flask run
Contributing:
If you'd like to contribute to the project, feel free to fork the repository and submit a pull request. Please ensure that your code follows the existing style and passes all tests.

# Known Bugs:

- Register Form: After the form is submitted, it doesn’t automatically redirect the user to the login page as expected.

- Profile Page: The updated details are not reflected on the profile page as they should be.

### Live Server Links:

* Backend Render [https://deltabank.onrender.com]
* Frontend Vercel [https://delta-bank-2z461qcxd-david-parsleys-projects.vercel.app/]

### Demo Video Link

- Video [https://drive.google.com/file/d/1WEZEhK0qsgJSbKXidSjAAs1XEatyjQEx/view?usp=sharing]

#### For any issues or questions, feel free to open an issue on GitHub or contact me directly at [davidparsleykakhayanga@gmail.com].

# License
*Licenced under the [MT-licence](https://opensource.org/license/mit)*

Copyright (c) 2024 **David Parsley**

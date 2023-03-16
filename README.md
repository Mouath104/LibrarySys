# LibrarySys
A Library App for shcool

# About
The Library App is a web-based application designed to facilitate the work of librarians. It allows the librarian to issue books to students and specify the expiration date automatically by the system. The application maintains a table that contains all issued books with their respective students, including their status as valid or expired.

Key Features
- Book issuance: The librarian can issue a book to a student, and the expiration date is specified by the system automatically.
- Authorization: The project includes user authentication and authorization. There are two types of users: Admin and Normal users.
  -Admin users have the following capabilities:
    -Issue books to students
    -View available books
    -Edit and delete available books
    -View all students
  -Edit and delete student records
  -Normal users have the following capabilities:
    -View their own issued books
    -Edit their own Profiles
- Responsive design: The app is optimized for different screen sizes and devices.
- Availability Check: Prevent Issuing Already Issued Books. If the Book has been already issued, it won't be available to issue later, unless the Librarian removes it from the Issued Books table.

# What it looks like (you may click on each GIF for better view)
Home Page:

![Library - Google Chrome 2023-03-16 10-47-46](https://user-images.githubusercontent.com/89397795/225563914-6d1d3c49-61d5-4bd8-90d2-cdd210d163a3.gif)

Issue A Book:

![Library - Google Chrome 2023-03-16 10-29-28](https://user-images.githubusercontent.com/89397795/225559729-8fb91c3a-da10-4c56-93c2-9819c1cc0107.gif)

Issued Books:

![Library - Google Chrome 2023-03-16 10-52-35](https://user-images.githubusercontent.com/89397795/225564825-0e4fd92b-f5af-479d-bd38-59ce424610bd.gif)
 
Edit Profile:

![Library - Google Chrome 2023-03-16 11-00-09](https://user-images.githubusercontent.com/89397795/225568146-df2d58d9-ef17-44c9-8c9c-5bd4ec515c51.gif)


Note: you select books and students from a List but it's not Appearing in the GIF

# Activate the Environment:
myenv/scripts/activate

# Install Packages:
pip install -r requirements.txt

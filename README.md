# LibrarySys
A Library App for shcool

# About
The Library App is a web-based application designed to facilitate the work of librarians. It allows the librarian to issue books to students and specify the expiration date automatically by the system. The application maintains a table that contains all issued books with their respective students, including their status as valid or expired.

Key Features
- Book issuance: The librarian can issue a book to a student, and the expiration date is specified by the system automatically.
- Edit Profiles: Users can edit their profiles and change their passwords.
- Responsive design: The app is optimized for different screen sizes and devices.
- Availability Check: Prevent Issuing Already Issued Books. If the Book has been already issued, it won't be available to issue later, unless the Librarian removes it from the Issued Books table.

# What it looks like (you may click on each GIF for better view)
Home Page:

![Library - Google Chrome 2023-03-16 10-47-46](https://user-images.githubusercontent.com/89397795/225563914-6d1d3c49-61d5-4bd8-90d2-cdd210d163a3.gif)

Issue A Book:

![Library - Google Chrome 2023-03-16 10-29-28](https://user-images.githubusercontent.com/89397795/225559729-8fb91c3a-da10-4c56-93c2-9819c1cc0107.gif)

Note: you select books and students from a List but it's not Appearing in the GIF

# Activate the Environment:
myenv/scripts/activate

# Install Packages:
pip install -r requirements.txt

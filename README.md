# Quotes Django Project

This project is a Django-based web application that replicates the functionality of the website [http://quotes.toscrape.com](http://quotes.toscrape.com). The main objectives were to create a site where users can register, log in, add authors and quotes, and perform database migration from MongoDB to PostgreSQL.

## Features

- **User Registration and Login**: Users can register and log in to the site.
- **Add Author**: Registered users can add new authors.
- **Add Quote**: Registered users can add new quotes, associating them with existing authors.
- **Database Storage**: Quotes and tags are stored in MongoDB, while user information is stored in PostgreSQL.
- **Public Author Pages**: Author pages are accessible without user authentication.
- **Public Quotes**: All quotes are viewable without user authentication.
- **User Avatars**: Users can upload a profile picture.

## Tools and Frameworks Used

- **Django**: Web framework for the backend.
- **Django REST Framework**: For building API endpoints.
- **MongoDB**: Database for storing quotes and tags.
- **PostgreSQL**: Database for storing user information.
- **Docker**: Containerization for the application.
- **HTML/CSS**: For the front-end and visual representation of the pages.
- **Bootstrap**: CSS framework for responsive design.
- **Pillow**: Python Imaging Library (PIL) for image uploads (user avatars).
- **djongo**: Connector for using MongoDB as a Django backend.
- **psycopg2**: PostgreSQL adapter for Python.

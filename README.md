# My Bookshelf

A Django web application for tracking and organizing your personal reading journey. Keep track of books you want to read, are currently reading, and have completed with ratings and reviews.

![Personal Book Tracker](/books/assets/booklogo.jpg)

## Description

Personal Book Tracker is a full-stack web application built with Django that allows users to create and manage their personal book library. Users can organize books by reading status, add ratings and reviews, and search through their collection. The application features a clean, professional design with a white, gray, and blue color scheme.

## Features

- **User Authentication**: Secure login and registration system
- **Book Management**: Full CRUD operations for books
- **Reading Status Tracking**: Organize books by "Want to Read," "Currently Reading," and "Read"
- **Rating System**: 5-star rating system for completed books
- **Reviews**: Write and store personal reviews for books
- **Search Functionality**: Search books by title or author
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Professional UI**: Modern, clean interface with rounded elements and smooth animations

## Technologies Used

- **Backend**: Django, Python
- **Frontend**: HTML, CSS
- **Database**: SQLite (development), PostgreSQL (production ready)
- **Styling**: Custom CSS with professional design system
- **Authentication**: Django's built-in authentication system

## ERD 
![ERD](/books/assets/ERD.png)

## Project Structure

```
MY-BOOKSHELF/
├── books/                          # Main Django app
│   ├── migrations/                 # Database migrations
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   └── 0002_book_user.py
│   ├── static/css/                 # CSS files
│   │   ├── books/
│   │   │   ├── book-index.css      # Library page styles
│   │   │   └── book-detail.css     # Book detail styles
│   │   ├── base.css               # Core styles
│   │   ├── form.css               # Form styles
│   │   └── home.css               # Login page styles
│   ├── templates/                  # HTML templates
│   │   └── books/
│   │       ├── about.html         # About page
│   │       ├── base.html          # Base template
│   │       ├── home.html          # Login page
│   │       ├── index.html         # Library main page
│   │       └── signup.html        # Registration page
│   ├── __init__.py
│   ├── admin.py                   # Django admin configuration
│   ├── apps.py                    # App configuration
│   ├── models.py                  # Book model definition
│   ├── tests.py                   # Unit tests
│   ├── urls.py                    # App URL patterns
│   └── views.py                   # View functions and classes
├── mybookshelf/                   # Django project configuration
│   ├── __init__.py
│   ├── asgi.py                    # ASGI configuration
│   ├── settings.py                # Project settings
│   ├── urls.py                    # Main URL configuration
│   └── wsgi.py                    # WSGI configuration
├── db.sqlite3                     # SQLite database
├── manage.py                      # Django management script
├── Pipfile                        # Pipenv dependencies (if using)
├── Pipfile.lock                   # Pipenv lock file
└── README.md                      # Project documentation
```

## Installation & Setup

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd MY_BOOKSHELF
   ```

2. **Create virtual environment**
   ```bash
   pipenv shell
   ```

3. **Install dependencies**
   ```bash
   pip install django psycopg2-binary 
   ```

4. **Apply database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser account**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Open your browser and navigate to `http://127.0.0.1:8000`
   - Login with your superuser credentials

## Usage

### Getting Started
1. **Register/Login**: Create an account or login with existing credentials
2. **Add Books**: Click "Add a Book" to start building your library
3. **Organize**: Set reading status for each book (Want to Read, Currently Reading, Read)
4. **Rate & Review**: Add ratings (1-5 stars) and write reviews for completed books
5. **Browse**: View your organized library with books categorized by status

### Main Features

**Book Management:**
- Add new books with title, author, status, rating, and review
- Edit existing book information
- Delete books from your library
- View detailed book information

**Library Organization:**
- Books automatically organized by reading status
- Statistics dashboard showing book counts
- Clean card-based layout for easy browsing

**User Experience:**
- Responsive design works on all devices
- Professional styling with smooth animations
- Intuitive navigation and user interface

## Database Schema

### Models

**User** (Django built-in)
- Handles user authentication and account management

**Book**
```python
- title: CharField(max_length=200)
- author: CharField(max_length=100) 
- status: CharField with choices ['want_to_read', 'reading', 'read']
- rating: IntegerField (1-5, nullable)
- review: TextField (nullable)
- user: ForeignKey to User (CASCADE delete)
- date_added: DateTimeField (auto-generated)
```

**Relationships:**
- One-to-Many: One User can have many Books
- Each book belongs to exactly one user
- Books are automatically deleted if the user is deleted


## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home/Login page |
| GET | `/books/` | View all user's books |
| GET | `/books/create/` | Add new book form |
| POST | `/books/create/` | Create new book |
| GET | `/books/<id>/` | View book details |
| GET | `/books/<id>/update/` | Edit book form |
| POST | `/books/<id>/update/` | Update book |
| GET | `/books/<id>/delete/` | Delete confirmation |
| POST | `/books/<id>/delete/` | Delete book |
| GET | `/about/` | About page |
| GET | `/accounts/signup/` | Registration form |
| POST | `/accounts/signup/` | Create account |

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Development Guidelines

- Follow Django best practices and conventions
- Use meaningful commit messages
- Write tests for new features
- Maintain consistent code style
- Update documentation for significant changes

## Security Features

- CSRF protection on all forms
- User authentication required for all book operations
- Users can only access their own books
- SQL injection protection through Django ORM
- XSS protection through Django templates

## Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Links
1. Repo: [My_Bookshelf](https://github.com/Zahraa-06/My_Bookshelf)
2. Trello: [Trello](https://trello.com/invite/b/68c9c9b5793f052e45e32416/ATTI69ba31e86e59e5a4376eee651b2244e57EB03567/my-bookshelf-trello)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with Django framework
- Styled with custom CSS design system
- Uses Django's built-in authentication system
- Professional UI design with accessibility in mind

## Contact

For questions or support, please open an issue in the GitHub repository.

---

**Personal Book Tracker** - Organize your reading journey with style and simplicity.
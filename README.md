# Hooshang URL Shortener

A powerful and user-friendly URL shortening service built with Python Flask. This application allows users to create short, memorable links and provides an admin dashboard for link management.


[![GitHub](https://raw.githubusercontent.com/AmirHossein-Naei/Hooshang-URL-shortener/refs/heads/master/README-IMAGE.png)(https://github.com/AmirHossein-Naei/Hooshang-URL-shortener)


## Features

- 🔗 Create short, memorable URLs
- 📊 Track link analytics (views, creation time)
- 🛠️ Admin dashboard for link management
- 📱 QR code generation for easy sharing
- 🚀 Fast and lightweight
- 🔒 Secure user authentication

## Tech Stack

- **Backend**: Python Flask
- **Database**: SQLite 
- **Frontend**: HTML, CSS, JavaScript, Bootstrap

## Prerequisites

- Python 3.9+
- pip (Python package manager)
- Git (optional, for version control)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/AmirHossein-Naei/Hooshang-URL-shortener.git
   cd Hooshang-URL-shortener
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the application**
   - Copy `config.py.example` to `config.py`
   - Update the configuration with your settings (database URI, secret key, etc.)

5. **Initialize the database**
   ```bash
   flask db upgrade
   ```

## Running the Application

```bash
flask run
```

The application will be available at `http://localhost:5000`

## Project Structure

```
Hooshang-URL-shortener/
├── blueprints/         # Application blueprints
│   ├── admin_dashboard/
│   └── main/
├── migrations/         # Database migrations
├── static/             # Static files (CSS, JS, images)
├── templates/          # HTML templates
├── app.py              # Main application file
├── config.py.example   # Configuration settings example
├── ext.py              # Extensions
├── models.py           # Database models
└── requirements.txt    # Project dependencies
```

## Usage

1. **Create an account** - Register a new user account
2. **Login** - Access your dashboard
3. **Create short links** - Enter a long URL and get a shortened version
4. **Manage links** - View, delete your shortened links
5. **View analytics** - Track how many times each link has been clicked

## Admin Features

- View all users and their links
- Monitor system statistics

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Acknowledgments

- Built with ❤️ using Flask
- Inspired by popular URL shortening services
- Special thanks to all contributors

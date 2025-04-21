# Personal Flask Website

A streamlined Flask application showcasing my personal projects and skills.

## Features

- Bio page with personal information
- AI-powered Fortune Teller using Claude API
- Simple, responsive Bootstrap 5 UI

## Setup

1. Clone this repository
2. Create a virtual environment (optional):
   ```
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Mac/Linux
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Add your Anthropic API key to a .env file:
   ```
   ANTHROPIC_API_KEY=your-api-key-here
   ```
5. Run the application:
   ```
   python app.py
   ```
6. Visit http://127.0.0.1:5000/ in your browser

## Structure

- **routes/**: Blueprint files for different sections (bio and fortune)
- **templates/**: HTML templates using Jinja2
- **static/**: CSS and other static files

## Note

This is a simple Flask application designed for educational purposes. 
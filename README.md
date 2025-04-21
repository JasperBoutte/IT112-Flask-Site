# Personal Flask Website

This is a lightweight Flask site I built in my Python Web Programming class as a hub for my assignments.

## What it includes

- A bio page with info about me
- A fortune teller that gives AI-generated responses | powered by Anthropic
- 
## How to run it

1. Clone the repo
2. (Optional) Set up a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows  
   source venv/bin/activate  # Mac/Linux
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Add your Anthropic API key to a `.env` file:
   ```bash
   ANTHROPIC_API_KEY=your-api-key-here
   ```
5. Start the app:
   ```bash
   python app.py
   ```
6. Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Folder overview

- **routes/** – where the Flask blueprints live (bio, fortune, etc.)
- **templates/** – HTML files with Jinja2
- **static/** – CSS and other frontend assets

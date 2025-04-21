from flask import Flask, render_template
import os

# Optional dotenv support
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'fallback-dev-key')

# Register blueprints
from routes.bio import bio_bp
from routes.fortune import fortune_bp
from routes.projects import projects_bp

app.register_blueprint(bio_bp)
app.register_blueprint(fortune_bp)
app.register_blueprint(projects_bp)

@app.route('/')
def index():
    assignments = [
        {"title": "Bio Page", "description": "Learn about me", "url": "/bio", "icon": "person-circle"},
        {"title": "Fortune Teller", "description": "Get your fortune told", "url": "/fortune", "icon": "stars"},
        {"title": "Projects", "description": "View my class projects", "url": "/projects", "icon": "kanban"}
    ]
    return render_template('index.html', assignments=assignments)

if __name__ == '__main__':
    app.run(debug=True) 
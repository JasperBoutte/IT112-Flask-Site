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

app.register_blueprint(bio_bp)
app.register_blueprint(fortune_bp)

@app.route('/')
def index():
    sections = [
        {
            "title": "Bio Page", 
            "description": "Learn about me and my skills", 
            "url": "/bio", 
            "icon": "person-circle",
            "tech": ["Flask", "HTML/CSS", "Bootstrap 5"]
        },
        {
            "title": "AI Fortune Teller", 
            "description": "Get your fortune from Claude AI", 
            "url": "/fortune", 
            "icon": "stars",
            "tech": ["Flask", "JavaScript", "Anthropic API", "CSS Animations"]
        }
    ]
    return render_template('index.html', assignments=sections)

if __name__ == '__main__':
    app.run(debug=True) 
from flask import Blueprint, render_template

bio_bp = Blueprint('bio', __name__, url_prefix='/bio')

@bio_bp.route('/')
def index():
    bio_info = {
        'name': 'Jasper Boutte',
        'title': 'Computer Science Student',
        'skills': [
            'Python', 'HTML/CSS', 'Web Development', 'Problem Solving'
        ],
        'interests': [
            'Creativity', 'Technology', 'Learning New Tools', 'Building Projects'
        ],
        'about': "I'm a student exploring the world of tech and trying to figure out where I fit in. I don't have a deep background in programming or development yet, but I'm always interested in learning new things—especially when it comes to creativity, problem-solving, and figuring out how stuff works.",
        'journey': "I'm currently studying computer science and slowly getting my hands dirty with different tools, projects, and ideas. Just trying to find my lane and build something cool along the way.",
        'recent': "Recently, I've been diving more into Python and web development. I'm not an expert, but I've been writing more code and learning through trial and error. It's been a solid way to grow my skills and get more confident with how things actually run behind the scenes. It's not always clean, but I like building stuff that works and figuring things out as I go."
    }
    return render_template('bio/index.html', bio=bio_info) 
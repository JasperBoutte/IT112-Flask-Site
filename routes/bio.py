from flask import Blueprint, render_template

bio_bp = Blueprint('bio', __name__, url_prefix='/bio')

@bio_bp.route('/')
def index():
    bio_info = {
        'name': 'Jasper Boutte',
        'title': 'Computer Science Student | Dev And Other Stuff',
        'skills': [
            'Python & Automation – scripting, bots, and figuring out how to make life easier with code',
            'Web Dev (HTML/CSS/Flask) – basic front-end with backend logic to make it all click',
            'Git & GitHub – version control that actually makes sense, plus branching without losing your mind',
            'UI/UX Flow – more about feel than pixel perfection; making things work naturally',
            'Debugging & Problem Solving – breaking stuff to fix it smarter',
            'Linux (Manjaro/Arch) – because Windows annoyed me enough to switch',
            'Modding/Game Projects – Minecraft, Discord bots, or chaos-driven tools—whatever works'
        ],
        'interests': [
            'Building Smart Tools – bots, automations, scripts that feel like magic',
            'Learning Fast, Not Perfect – I break stuff until I understand it',
            'AI & Neural Nets – curious about where tech meets creativity',
            'Experimental Tech – sandboxing weird ideas just to see what happens',
            "Creative Coding – games, mods, apps—if it's fun or useful, I'm in",
            'Security & Hacking Culture – not blackhat, just curious and cautious',
            'Open Source & Community Projects – helping out or launching something myself'
        ],
        'about': "I'm a student exploring the world of tech and trying to figure out where I fit in. I don't have a deep background in programming or development yet, but I'm always interested in learning new things—especially when it comes to creativity, problem-solving, and figuring out how stuff works.",
        'journey': "I'm currently studying computer science and slowly getting my hands dirty with different tools, projects, and ideas. Just trying to find my lane and build something cool along the way.",
        'recent': "Recently, I've been diving more into Python and web development. I'm not an expert, but I've been writing more code and learning through trial and error. It's been a solid way to grow my skills and get more confident with how things actually run behind the scenes. It's not always clean, but I like building stuff that works and figuring things out as I go.",
        'linkedin': 'https://www.linkedin.com/in/jasperboutte'
    }
    return render_template('bio/index.html', bio=bio_info) 
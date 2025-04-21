from flask import Blueprint, render_template

projects_bp = Blueprint('projects', __name__, url_prefix='/projects')

@projects_bp.route('/')
def index():
    projects = [
        {
            'title': 'Bio Page',
            'description': 'A responsive personal profile page showcasing my background, skills, and interests.',
            'tech': ['Flask', 'HTML', 'CSS', 'Bootstrap 5'],
            'assignment': 'Personal Project',
            'url': '/bio',
            'featured': True
        },
        {
            'title': 'AI Fortune Teller',
            'description': 'Interactive fortune teller powered by Claude AI. Features custom animations and interactive color/number selection.',
            'tech': ['Flask', 'HTML', 'CSS', 'JavaScript', 'Anthropic API'],
            'assignment': 'Personal Project',
            'url': '/fortune',
            'featured': True
        },
        {
            'title': 'Project Showcase',
            'description': 'A portfolio website designed to display all projects with categorization and filtering capabilities.',
            'tech': ['Flask', 'HTML', 'CSS', 'Bootstrap 5'],
            'assignment': 'Personal Project',
            'url': '/projects',
            'featured': True
        }
    ]
    
    return render_template('projects/index.html', projects=projects) 
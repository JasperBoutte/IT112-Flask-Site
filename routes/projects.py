from flask import Blueprint, render_template

projects_bp = Blueprint('projects', __name__, url_prefix='/projects')

@projects_bp.route('/')
def index():
    projects = [
        {
            'title': 'Bio Page',
            'description': 'A simple page displaying information about myself.',
            'tech': ['Flask', 'HTML', 'CSS', 'Bootstrap 5'],
            'assignment': 'IT112 - Assignment 1',
            'url': '/bio'
        },
        {
            'title': 'Fortune Teller',
            'description': 'Interactive fortune teller that generates random fortunes based on user input.',
            'tech': ['Flask', 'HTML', 'CSS', 'JavaScript', 'Bootstrap 5'],
            'assignment': 'IT112 - Assignment 2',
            'url': '/fortune'
        },
        {
            'title': 'Project Showcase',
            'description': 'This page! A showcase of all the projects created for the IT112 class.',
            'tech': ['Flask', 'HTML', 'CSS', 'Bootstrap 5'],
            'assignment': 'IT112 - Assignment 3',
            'url': '/projects'
        }
    ]
    
    return render_template('projects/index.html', projects=projects) 
from flask import Blueprint, render_template

projects_bp = Blueprint('projects', __name__, url_prefix='/projects')

@projects_bp.route('/')
def index():
    projects = [
        {
            'title': 'Bio Page',
            'description': 'A responsive personal profile page showcasing my background, skills, and interests with LinkedIn integration.',
            'tech': ['Flask', 'HTML', 'CSS', 'Bootstrap 5'],
            'assignment': 'IT112 - Assignment 1',
            'url': '/bio',
            'featured': True,
            'image': 'bio_project.jpg'
        },
        {
            'title': 'Fortune Teller',
            'description': 'Interactive fortune teller that generates random fortunes based on user input. Features custom animations and interactive color/number selection.',
            'tech': ['Flask', 'HTML', 'CSS', 'JavaScript', 'Bootstrap 5'],
            'assignment': 'IT112 - Assignment 2',
            'url': '/fortune',
            'featured': True,
            'image': 'fortune_project.jpg'
        },
        {
            'title': 'Project Showcase',
            'description': 'A portfolio website designed to display all projects created for the IT112 class with categorization and filtering capabilities.',
            'tech': ['Flask', 'HTML', 'CSS', 'Bootstrap 5'],
            'assignment': 'IT112 - Assignment 3',
            'url': '/projects',
            'featured': True,
            'image': 'projects_showcase.jpg'
        },
        {
            'title': 'Personal Blog System',
            'description': 'A simple blogging platform built with Flask that allows for text formatting and image uploads.',
            'tech': ['Flask', 'HTML', 'CSS', 'JavaScript', 'Bootstrap 5'],
            'assignment': 'Personal Project',
            'url': '#',
            'featured': False,
            'image': 'blog_project.jpg'
        },
        {
            'title': 'Python Automation Scripts',
            'description': 'Collection of Python scripts for automating repetitive tasks and file organization.',
            'tech': ['Python', 'PyAutoGUI', 'OS Module'],
            'assignment': 'Personal Project',
            'url': '#',
            'featured': False,
            'image': 'python_scripts.jpg'
        }
    ]
    
    return render_template('projects/index.html', projects=projects) 
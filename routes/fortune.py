from flask import Blueprint, render_template, request, redirect, url_for, session
import random

fortune_bp = Blueprint('fortune', __name__, url_prefix='/fortune')

@fortune_bp.route('/', methods=['GET', 'POST'])
def index():
    colors = {
        'Red': '#ff5252',
        'Blue': '#4a6ff3',
        'Green': '#43a047',
        'Yellow': '#ffca28',
        'Purple': '#9c27b0',
        'Orange': '#ff9800',
        'Pink': '#ec407a',
        'Teal': '#26a69a'
    }
    
    numbers = [str(i) for i in range(1, 9)]
    
    fortunes = [
        "You will ace your next programming assignment!",
        "A significant career opportunity awaits you soon.",
        "Your code will compile on the first try today.",
        "Someone will ask for your help with a technical problem.",
        "You'll discover a new programming trick that saves you hours.",
        "A bug you've been chasing will suddenly make sense.",
        "Your next project will impress everyone who sees it.",
        "Take a break - inspiration will come when you least expect it.",
        "Your GitHub contributions will increase dramatically soon.",
        "The solution to your current problem is simpler than you think.",
        "Your intuition will lead you to the perfect solution.",
        "A mentor will offer valuable guidance on your coding journey.",
        "A challenge you're facing now will make you stronger.",
        "The next technology you learn will open many doors.",
        "Someone will recognize your hard work soon.",
        "Your persistence will finally pay off on a difficult problem."
    ]
    
    error = None
    
    if request.method == 'POST':
        name = request.form.get('name', 'Anonymous')
        color = request.form.get('color')
        number = request.form.get('number')
        
        if not color or not number:
            error = "Please select both a color and a number."
            return render_template('fortune/form.html', colors=colors, numbers=numbers, error=error)
        
        # Get the hex value for the selected color
        color_hex = colors.get(color, '#000000')
        
        # Generate fortune with a consistent algorithm based on inputs
        seed = sum([ord(c) for c in name]) + list(colors.keys()).index(color) + int(number)
        random.seed(seed)
        fortune = random.choice(fortunes)
        
        # Store values to display on result page
        result = {
            'name': name,
            'color': color,
            'color_hex': color_hex,
            'number': number,
            'fortune': fortune
        }
        
        return render_template('fortune/result.html', **result)
    
    # GET request - show the form
    return render_template('fortune/form.html', colors=colors, numbers=numbers, error=error) 
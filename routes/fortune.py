from flask import Blueprint, render_template, request, redirect, url_for, session
import os
import random

# Import Anthropic client
try:
    import anthropic
    from anthropic import Anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False

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
    
    # Fallback fortunes in case the API is unavailable
    fallback_fortunes = [
        "You will discover unexpected connections in your next project.",
        "Your curiosity will lead you to valuable insights.",
        "A challenge you've been avoiding will become easier than expected.",
        "Someone will appreciate your unique perspective.",
        "An old idea will find new relevance in your current situation.",
        "Your patience with a difficult problem will soon be rewarded.",
        "The skills you're learning now will be useful in unexpected ways.",
        "A small change in your routine will lead to significant improvements."
    ]
    
    error = None
    
    if request.method == 'POST':
        name = request.form.get('name', 'Anonymous')
        color = request.form.get('color')
        number = request.form.get('number')
        
        if not color or not number:
            error = "Please select both a color and a number."
            return render_template('fortune/form.html', colors=colors, numbers=numbers, error=error)
        
        # Grab the hex for the selected color
        color_hex = colors.get(color, '#000000')
        
        # Use Claude to make a fortune
        if ANTHROPIC_AVAILABLE:
            try:
                # Get API key from the .env file
                api_key = os.environ.get('ANTHROPIC_API_KEY', '')
                
                if api_key:
                    client = Anthropic(api_key=api_key)
                    
                    # Prompt for the fortune
                    prompt = f"""
                    Generate a creative and thoughtful fortune for a person named {name} who chose the color {color} and the number {number}.
                    The fortune should be positive, insightful, and about 30-50 words. It should relate subtly to their choices.
                    Don't mention that this is AI-generated or make references to being an AI. Just provide the fortune.
                    """
                    
                    # Generate the response
                    response = client.messages.create(
                        model="claude-3-haiku-20240307",
                        max_tokens=150,
                        temperature=0.7,
                        system="You are a creative and insightful fortune teller. Your fortunes are thoughtful, positive, and relate to the person's choices in subtle ways.",
                        messages=[
                            {"role": "user", "content": prompt}
                        ]
                    )
                    
                    fortune = response.content[0].text.strip()
                else:
                    # No API key, use fallback
                    seed = sum([ord(c) for c in name]) + list(colors.keys()).index(color) + int(number)
                    random.seed(seed)
                    fortune = random.choice(fallback_fortunes)
            except Exception as e:
                # If there's an error with the API, use fallback
                seed = sum([ord(c) for c in name]) + list(colors.keys()).index(color) + int(number)
                random.seed(seed)
                fortune = random.choice(fallback_fortunes)
        else:
            # If Anthropic isn't available, use fallback
            seed = sum([ord(c) for c in name]) + list(colors.keys()).index(color) + int(number)
            random.seed(seed)
            fortune = random.choice(fallback_fortunes)
        
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
from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

@app.route('/app', methods=['GET', 'POST'])
def game():
    number = random.randint(1, 10)
    message = ""
    if request.method == "POST":
        try:
            guess = int(request.form['guess'])
            if guess < number:
                message = "Too low!"
            elif guess > number:
                message = "Too high!"
            else:
                message = "Correct!"
        except:
            message = "Invalid input"

    return render_template_string("""
        <h1>Guess the Number (1-10)</h1>
        <form method="post">
            <input name="guess" type="number" required>
            <input type="submit" value="Guess">
        </form>
        <p>{{message}}</p>
    """, message=message)

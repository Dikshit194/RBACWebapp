from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    name = ''
    if request.method == 'POST':
        name = request.form.get('name').upper()
    return render_template_string('''
        <form method="POST">
            <label for="name">Enter your name:</label><br>
            <input type="text" id="name" name="name" required><br>
            <input type="submit" value="Submit">
        </form>
        <p>{{ name }}</p>
    ''', name=name)

if __name__ == '__main__':
    app.run(debug=True)

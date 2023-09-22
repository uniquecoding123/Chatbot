from flask import Flask, render_template, request, redirect, url_for
import wikipedia
import pyttsx3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# Set the language for Wikipedia (optional)
# wikipedia.set_lang("en")  # You can specify the language you want (default is English)

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        num = request.form['num']
        speak=request.form['speak']
        speak=speak.capitalize()
        #wikipedia here
        answer = wikipedia.summary(name, sentences=num)
        # You can process the form data here (e.g., save it to a database).
        # For this example, we'll just print the data.
        if speak=="Y":
            engine = pyttsx3.init()
            engine.say(wikipedia.summary(name, sentences=num))
            engine.runAndWait()

        else:
            pass

        return render_template('index.html',answer=answer)


if __name__ == '__main__':
    app.run(debug=True)

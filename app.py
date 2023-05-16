from flask import Flask, render_template, request 

app = Flask(__name__)

app.secret_key = 'mysecretkey'

# List of available languages
languages = ['Swahili', 'Yoruba', 'Hausa', 'Zulu', 'Amharic']

# Dictionary of vocabulary for each language
vocabulary = {
    'Swahili': {
        'Mambo': 'Hello',
        'Habari': 'How are you?',
        'Asante': 'Thank you',
        'Karibu': 'Welcome',
        'Sawa': 'Okay',
        'Kwaheri': 'Goodbye'
    },
    'Yoruba': {
        'Bawo ni': 'Hello',
        'Kilonshele': 'How are you?',
        'E se': 'Thank you',
        'E ku abọ': 'Welcome',
        'O da': 'Okay',
    },
    'Hausa': {
        'Sannu': 'Hello',
        'Yaya kake nisan': 'How are you?',
        'Na gode': 'Thank you',
        'Maraba': 'Welcome',
        'Lafia': 'Okay',
        'Ina kwana': 'Goodbye'
    },
    'Zulu': {
        'Sawubona': 'Hello',
        'Unjani': 'How are you?',
        'Ngiyabonga': 'Thank you',
        'Wamukelekile': 'Welcome',
        'Kuyaphuthuma': 'Okay',
        'Hamba kahle': 'Goodbye'
    },
    'Amharic': {
        'Selam': 'Hello',
        'Dehna neh?': 'How are you?',
        'Ameseginalehu': 'Thank you',
        'Tena yistilign': 'Welcome',
        'Lij': 'Okay',
        'Dehna hun': 'Goodbye'
    }
}

# Quiz questions and answers
questions = [
    ('What is the Swahili word for "Thank you"?', 
        ['Habari', 'Asante', 'Sawa', 'Kwaheri'], 'Asante'),
    ('What is the Yoruba word for "Hello"?', 
        ['Bawo ni', 'Kilonshele', 'E se', 'Od\'abo'], 'Bawo ni'),
    ('What is the Hausa word for "Goodbye"?'), 
        ['Sannu', 'Yaya']

]

@app.route('/')
def home():
    return render_template('mama_lingo.html')

@app.route('/get_started')
def get_started():
    # your code here
    return render_template('get_started.html')

@app.route('/learn_language', methods=['GET', 'POST'])
def learn_language():
    render_template('learn_language.html') 


if __name__ == '__main__':
    app.run(debug=True)









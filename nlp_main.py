from flask import Flask, request, render_template
import nltk 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from main import addition, substraction, multiplication, division
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Tokenization
nltk.download('punkt')
nltk.download('stopwords')

def parse_input(text):
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word.isalnum()]
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if not word in stop_words]
    return tokens

def input_interpreter(tokens):
    if "plus" in tokens:
        return "add"
    elif "minus" in tokens:
        return "subtract"
    elif "times" in tokens:
        return "multiply"
    elif "divide" in tokens:
        return "divide"
    else:
        return "Invalid operation"
    
def nlp_calculator(text):
    tokens = parse_input(text)
    operation = input_interpreter(tokens)
    numbers = [float(token) for token in tokens if token.isnumeric()]
    if len(numbers) != 2:
        return "We need exactly two numbers!"
    a, b = numbers

    if operation == "add":
        return addition(a,b)
    elif operation == "subtract":
        return substraction(a,b)
    elif operation == "multiply":
        return multiplication(a,b)
    elif operation == "divide":
        return division(a,b)
    else:
        return "Invalid operation"
    
def train_my_model():
    data = [
        ("2 plus 4", "add"),
        ("10 minus 9", "subtract"),
        ("22 times 3", "multiply"),
        ("11 divide 7", "divide")
    ]
    texts, labels = zip(*data)
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(texts)
    model = LogisticRegression()
    model.fit(X, labels)
    return model, vectorizer

def predict(text, model, vectorizer):
    X = vectorizer.transform([text])
    prediction = model.predict(X)
    return prediction[0]

vectorizer, model = train_my_model()

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/calculate', methods=['POST'])
def calculate():
    text_input = request.form['text_input']
    result = nlp_calculator(text_input)
    next_calc = predict(text_input, vectorizer, model)
    return render_template('index.html', result=result, next_calc=next_calc)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = int(request.form['phone'])
        subject = request.form['subject']
        message = request.form['message']
        preferred = request.form.getlist('preferred')
        agreement = request.form.getlist('agreement')
        return render_template('confirmation.html', name=name, email=email, phone=phone, subject=subject, message=message, preferred=preferred, agreement=agreement)
    return render_template('contact.html', name=None, email=None, phone=None, subject=None, message=None, preferred=None, agreement=None)

if __name__ == "__main__":
    app.run()

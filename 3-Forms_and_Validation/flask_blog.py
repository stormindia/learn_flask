from flask import Flask,  render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '623f43d1e0c56a52457a8728f36afb10'
post = [
    {
        'author': 'harshit bajpai',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2020'

    },
    {
        'author': 'Jane doe',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2020'

    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=post)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if(form.email.data == "abc@def.com" and form.password.data == "password"):
            flash(f'{form.email.data} is logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed. Please check username and password', 'danger')

    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True)
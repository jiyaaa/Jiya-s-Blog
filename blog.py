from flask import Flask, render_template
app = Flask(__name__)

posts = [
     {
     'author': 'Jiya Hasan',
     'title': 'Blog Post 1',
     'content': 'First post content',
     'date_posted': 'April 20, 2018'
     },
     {
     'author': 'Shahoreyer Mostofa and Hridoy Krisna Das',
     'title': 'Blog Post 2',
     'content': 'Second post content',
     'date_posted': 'April 21, 2018'
     }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')
@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact')
if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, abort, Blueprint

# app = Flask(__name__)
personal_profile = Blueprint("personal_profile", __name__, template_folder='templates', static_folder='static')


projects = [
    {
        "name": "Covid-19 Chest X-rays Classification using fastai",
        "thumb": "img/scenary.jpg",
        "hero": "img/lake.jpg",
        "categories": ["python, pytorch, fastai , Computer Vision"],
        "slug": "fastai"
    },
    {
        "name": "NLP Tagging using CRF model",
        "thumb": "img/night_city.jpg",
        "hero": "img/lake.jpg",
        "categories": ["python, NLTK, NLP, scikit-learn"],
        "slug": "NLP Tagging"
    },
    # {
    #     "name": "Project3",
    #     "thumb": "img/scenary.jpg",
    #     "hero": "img/lake.jpg",
    #     "categories": ["python"],
    #     "slug": "A"
    # },
]

slug_to_project = {project['slug']: project for project in projects}


@personal_profile.route('/')
def home():
    return render_template('home.html', projects = projects)

@personal_profile.route('/about')
def about():
    return render_template('about.html')

@personal_profile.route('/contact')
def contact():
    return render_template('contact.html')

@personal_profile.route('/project/<string:slug>')
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(f"project_{slug}.html",
                           project=slug_to_project[slug])


@personal_profile.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    personal_profile.run(debug=True)

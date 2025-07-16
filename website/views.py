from flask import Blueprint, render_template
from .database import load_database, load_project

blueprint = Blueprint("blueprint", __name__)

@blueprint.route("/")
def home():
    database = load_database()
    return render_template("home.html", projects=database)

@blueprint.route("/project/<int:project_id>")
def project(project_id):
    project = load_project(project_id)
    return render_template("project.html", project=project)

@blueprint.route("/contact-info")
def contact_info():
    return render_template("contact_info.html")
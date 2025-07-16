import json
from flask import url_for

class Project:
    def __init__(self, id, title, description, languages, github_link, image_path="", alt_text="", tags=None, frameworks=None, description_long=None, spotlight=False):
        self.id = id
        self.title = title
        self.description = description
        self.languages = languages
        self.github_link = github_link
        self.image_path = image_path
        self.alt_text = alt_text
        self.tags = [] if tags is None else tags
        self.description_long = [] if description_long is None else description_long
        # This description_long should be a list of strings (paragraphs)
        self.frameworks = [] if frameworks is None else frameworks
        self.spotlight = spotlight

    def stringify_languages(self):
        return ", ".join(self.languages) if self.languages else "N/A"

    def stringify_frameworks(self):
        return ", ".join(self.frameworks) if self.frameworks else "N/A"

    def stringify_description_long(self):
        return "\n".join(self.description_long) if self.description_long else "N/A"



def load_database():
    with open("data/projects.json", encoding="utf-8") as f:
        data = json.load(f)

    db = [Project(**i) for i in data]
    return db

def load_project(id):
    with open("data/projects.json", encoding="utf-8") as f:
        data = json.load(f)

    for project in data:
        if project["id"] == id:
            return Project(**project)
import os
from slugify import slugify
from flask import Flask, render_template
from articles import Article

app = Flask(__name__)


articles = Article.all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dilyora/blog")
def blog():
    return render_template("blog.html", articles=articles)

@app.route("/dilyora/article/<slug>")
def article(slug: str):
    article = articles[slug]
    return render_template("article.html", article=article)

if __name__ == "__main__":
    app.run(debug=True)
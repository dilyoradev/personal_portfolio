import os
from slugify import slugify
from flask import Flask, render_template, request, make_response, session
from articles import Article

app = Flask(__name__)
app.secret_key = "thisisverysecret"


articles = Article.all()

@app.route("/first-time")
def first_time():
    if 'seen' not in request.cookies:
        response = make_response("You are new here")
        response.set_cookie('seen', '1')
        return response

    seen = int(request.cookies['seen'])       
    response = make_response(f"I have {seen} you times before")
    response.set_cookie('seen', str(seen+1))
    return response  


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
import os
from slugify import slugify
from flask import Flask, render_template, request, make_response, session
from articles import Article

app = Flask(__name__)
app.secret_key = "thisisverysecret"

users = {
    "admin": "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
}

articles = Article.all()


# @app.route("/first-time")
# def first_time():
#     if 'seen' not in request.cookies:
#         response = make_response("You are new here")
#         response.set_cookie('seen', '1')
#         return response

#     seen = int(request.cookies['seen'])       
#     response = make_response(f"I have {seen} you times before")
#     response.set_cookie('seen', str(seen+1))
#     return response  


@app.route("/")
def home():
    return render_template("index.html")

@app.get("/admin")
def admin_page():
    if "user" in session:
        return "You are already authenticated"

    return render_template("login.html")

@app.get("/logout")
def logout():
    del session["user"]
    return "logged out"

@app.post("/admin")
def admin_login():
    username = request.form["username"]
    password = request.form["password"]

    if username not in users:
        return render_template("login.html", error="Username/password incorrect")

    hashed = hashlib.sha256(password.encode()).hexdigest()

    if users[username] != hashed:
        return render_template("login.html", error="Username/password incorrect")

        session["user"] = username
        return "You are now authenticated"


@app.route("/blog")
def blog():
    return render_template("blog.html", articles=articles)


@app.route("/article/<slug>")
def article(slug: str):
    if slug not in articles:
        return "Article not found", 404
    article = articles[slug]
    return render_template("article.html", article=article)


@app.route("/publish")
def publish():
    if "user" not in session:
        return redirect('/admin')
    return render_template("publish.html")



if __name__ == "__main__":
    app.run(debug=True)
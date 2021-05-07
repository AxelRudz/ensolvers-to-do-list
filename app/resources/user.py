from flask import redirect, render_template, request, url_for, abort, session, flash
from app.db import connection
from app.models.user import User
from app.helpers.auth import authenticated
from app.models.folder import Folder


def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if(username == None) or (username == ""):
        flash("The field 'username' is empty!", category="error")
        return redirect(request.referrer)
    if(password == None) or (password == ""):
        flash("The field 'password' is empty!", category="error")
        return redirect(request.referrer)
    
    conn = connection()
    user = User.find_by_username(conn, username)
    if not user:
        flash("The username doesn't exist!", category="error")
        return redirect(request.referrer)
    else:
        if password == user["password"]:
            flash("You have successfully logged in!", category="success")
            session["user"] = user
            folders = Folder.find_by_id_user(conn, user['id'])
            return render_template("user/menu.html", folders=folders)
        else:
            flash("Invalid password", category="error")
            return redirect(request.referrer)


def main_menu():
    if not authenticated(session):
        abort(403)
    else:
        conn = connection()
        folders = Folder.find_by_id_user(conn, session['user']['id'])
        return render_template("user/menu.html", folders=folders)


def logout():
    del session["user"]
    session.clear()
    flash("You have successfully logged out of the site.")
    return redirect(url_for("index"))

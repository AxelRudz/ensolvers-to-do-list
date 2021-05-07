from flask import redirect, render_template, request, abort, session, flash, url_for
from app.db import connection
from app.models.user import User
from app.helpers.auth import authenticated
from app.models.folder import Folder
from app.models.task import Task


def show():
    if not authenticated(session):
        abort(403)
    else:
        id_folder = request.args.get("id_folder")
        if(id_folder == None) or (id_folder == ""):
            flash("The 'id' field is empty!", category="error")
            return redirect(url_for("user-main-menu"))
        conn = connection()        
        if User.has_permision_to_open_folder(conn, session['user']['id'], id_folder):
            folder = Folder.find_by_id(conn, id_folder)
            if folder:
                tasks = Task.find_by_id_folder(conn, folder['id'])
                return render_template("folder/folder-show.html", folder=folder, tasks=tasks)
            else:
                flash("The folder doesn't exist!", category="error")
        else:
            flash("You don't have permission to access that folder!", category="error")
        return redirect(url_for("user-main-menu"))


def create():
    if not authenticated(session):
        abort(403)
    else:
        folder_name = request.form.get("folder_name")
        if(folder_name == None) or (folder_name == ""):
            flash("The folder must have a name!", category="error")
            return redirect(url_for("user-main-menu"))
        conn = connection()
        if(Folder.exists(conn, session['user']['id'], folder_name)):
            flash("The folder already exists!", category="error")
        else:
            try:
                Folder.create(conn, session['user']['id'], folder_name)
                flash("The folder was created!", category="success")
            except:
                flash("There was an error", category="error")
        return redirect(url_for("user-main-menu"))


def delete():
    if not authenticated(session):
        abort(403)
    else:
        id_folder = request.form.get("id_folder")
        if(id_folder == None) or (id_folder == ""):
            flash("The folder must have an ID!", category="error")
            return redirect(url_for("user-main-menu"))

        conn = connection()
        folder = Folder.find_by_id(conn, id_folder)
        if not folder:
            flash("The folder doesn't exist!", category="error")
        else:
            if folder['id_user'] == session['user']['id']:
                try:
                    Folder.delete(conn, session['user']['id'], id_folder)
                    flash("The folder was deleted!", category="success")
                except:
                    flash("There was an error!", category="error")
            else:
                flash("You don't have access to that folder!", category="error")
        return redirect(url_for("user-main-menu"))


def main_menu():
    if not authenticated(session):
        abort(403)
    else:
        conn = connection()
        folders = Folder.find_by_id_user(conn, session['user']['id'])
        return render_template("user/menu.html", folders=folders)

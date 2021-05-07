from flask import redirect, render_template, request, abort, session, flash, jsonify
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
            return redirect(request.referrer)
        conn = connection()        
        if User.has_permision_to_open_folder(conn, session['user']['id'], id_folder):
            folder = Folder.find_by_id(conn, id_folder)
            if not folder:
                flash("The folder doesn't exist!", category="error")
                return redirect(request.referrer)
            else:
                tasks = Task.find_by_id_folder(conn, folder['id'])
                return render_template("folder/folder-show.html", folder=folder, tasks=tasks)
        else:
            flash("You don't have permission to access that folder!", category="error")
            return redirect(request.referrer)


def create():
    if not authenticated(session):
        abort(403)
    else:
        id_folder = int(request.form.get("id_folder"))
        task_name = request.form.get("task_name")

        if(id_folder == None) or (id_folder == ""):
            flash("The folder must have an id!", category="error")
            return redirect(request.referrer)
        if(task_name == None) or (task_name == ""):
            flash("The task must have a name!", category="error")
            return redirect(request.referrer)
        conn = connection()
        
        if User.has_permision_to_open_folder(conn, session['user']['id'], id_folder):
            if Task.exists(conn, id_folder, task_name):
                flash("The task already exists!", category="error")
                return redirect(request.referrer)
            else:
                try:
                    Task.create(conn, id_folder, task_name)
                    flash("One task has been added!", category="success")
                except:
                    flash("There was an error adding your task", category="error")
        else:
            flash("You can't access that folder!", category="error")
        return redirect(request.referrer)
    

def delete():
    if not authenticated(session):
        abort(403)
    else:
        id_task = request.form.get("id_task")
        if(id_task == None) or (id_task == ""):
            flash("The task must have an ID!", category="error")
            return redirect(request.referrer)

        conn = connection()
        task = Task.find_by_id(conn, id_task)
        if not task:
            flash("The task doesn't exist!", category="error")
        else:
            if Task.belongs_to_user(conn, id_task, session['user']['id']):
                try:
                    Task.delete(conn, id_task)
                    flash("A task was deleted!", category="success")
                except:
                    flash("There was an error!", category="error")
            else:
                flash("You can't access that task!", category="error")
        return redirect(request.referrer)

def update():
    if not authenticated(session):
        abort(403)
    else:
        id_task = int(request.form.get("id_task"))
        id_folder = int(request.form.get("id_folder"))
        task_name = request.form.get("task_name")

        if(id_task == None) or (id_task == ""):
            flash("The task must have an id!", category="error")
            return redirect(request.referrer)
        if(id_folder == None) or (id_folder == ""):
            flash("The folder must have an id!", category="error")
            return redirect(request.referrer)
        if(task_name == None) or (task_name == ""):
            flash("The task must have a name!", category="error")
            return redirect(request.referrer)
        conn = connection()
        
        if Task.exists(conn, id_folder, task_name):
            flash("The task already exists!", category="error")
        else:
            try:
                Task.update(conn, id_task, task_name)
                flash("The task was updated!", category="success")
            except:
                flash("There was an error editing your task", category="error")
        
        return redirect(request.referrer)
    
def check():
    if not authenticated(session):
        abort(403)

    data = request.get_json()
    id_task = int(data['id_task'])
    checked = data['checked']

    if(id_task == "" or id_task == None):
        abort(404)
    if(checked == "" or checked == None):
        abort(404)

    conn = connection()

    Task.check(conn, id_task, checked)

    return jsonify({"state": checked})
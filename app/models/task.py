class Task(object):


    @classmethod
    def find_by_id_folder(cls, conn, id_folder):
        sql = """
            SELECT *
            FROM tasks
            WHERE id_folder = %s;
        """
        cursor = conn.cursor()
        cursor.execute(sql, id_folder)
        return cursor.fetchall()


    @classmethod
    def find_by_id(cls, conn, id_task):
        sql = """
            SELECT *
            FROM tasks
            WHERE id = %s;
        """
        cursor = conn.cursor()
        cursor.execute(sql, id_task)
        return cursor.fetchone()


    @classmethod
    def exists(cls, conn, id_folder, task_name):
        sql = """
            SELECT id
            FROM tasks
            WHERE id_folder = %s AND name = %s;
        """
        cursor = conn.cursor()
        cursor.execute(sql, (id_folder, task_name))
        return cursor.fetchone()


    @classmethod
    def create(cls, conn, id_folder, task_name):
        sql = """
            INSERT INTO tasks (id_folder, name)
            VALUES (%s,%s);
        """
        cursor = conn.cursor()
        cursor.execute(sql, (id_folder, task_name))
        conn.commit()
        return True
    

    @classmethod
    def delete(cls, conn, id_task):
        sql = """
            DELETE FROM tasks
            WHERE id = %s;
        """
        cursor = conn.cursor()
        cursor.execute(sql, id_task)
        conn.commit()
        return True

    
    @classmethod
    def update(cls, conn, id_task, task_name):
        sql = """
            UPDATE tasks
            SET name = %s
            WHERE id = %s;
        """
        cursor = conn.cursor()
        cursor.execute(sql, (task_name, id_task))
        conn.commit()
        return True

    
    @classmethod
    def check(cls, conn, id_task, checked):
        sql = """
            UPDATE tasks
            SET checked = %s
            WHERE id = %s;
        """
        cursor = conn.cursor()
        cursor.execute(sql, (checked, id_task))
        conn.commit()
        return True

    
    @classmethod
    def belongs_to_user(cls, conn, id_task, id_user):
        sql = """
            SELECT t.id
            FROM tasks t INNER JOIN folders f INNER JOIN users u
            WHERE (t.id_folder=f.id AND f.id_user=u.id) AND (t.id = %s AND u.id = %s);
        """
        cursor = conn.cursor()
        cursor.execute(sql, (id_task, id_user))
        return cursor.fetchone()
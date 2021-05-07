class Folder(object):


    @classmethod
    def find_by_id_user(cls, conn, id_user):
        sql = """
            SELECT *
            FROM folders
            WHERE id_user = %s;
        """
        cursor = conn.cursor()
        cursor.execute(sql, id_user)
        return cursor.fetchall()

    @classmethod
    def find_by_id(cls, conn, id_folder):
        sql = """
            SELECT *
            FROM folders
            WHERE id = %s;
        """
        cursor = conn.cursor()
        cursor.execute(sql, id_folder)
        return cursor.fetchone()


    @classmethod
    def exists(cls, conn, id_user, folder_name):
        sql = """
            SELECT id
            FROM folders
            WHERE id_user = %s AND name = %s;
        """
        cursor = conn.cursor()
        cursor.execute(sql, (id_user, folder_name))
        return cursor.fetchone()


    @classmethod
    def create(cls, conn, id_user, folder_name):
        sql = """
            INSERT INTO folders (id_user, name)
            VALUES (%s,%s);
        """
        cursor = conn.cursor()
        cursor.execute(sql, (id_user, folder_name))
        conn.commit()
        return True
    

    @classmethod
    def delete(cls, conn, id_user, id_folder):
        sql = """
            DELETE FROM folders
            WHERE id_user = %s AND id = %s;
        """
        cursor = conn.cursor()
        cursor.execute(sql, (id_user, id_folder))
        conn.commit()
        return True
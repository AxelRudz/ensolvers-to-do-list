class User(object):


    @classmethod
    def find_by_username(cls, conn, username):
        sql = """
            SELECT *
            FROM users
            WHERE username = %s
        """

        cursor = conn.cursor()
        cursor.execute(sql, username)

        return cursor.fetchone()


    @classmethod
    def has_permision_to_open_folder(cls, conn, id_user, id_folder):
        sql = """
            SELECT id
            FROM folders
            WHERE id = %s AND id_user = %s
        """
        cursor = conn.cursor()
        cursor.execute(sql, (id_folder, id_user))

        return cursor.fetchone()
    

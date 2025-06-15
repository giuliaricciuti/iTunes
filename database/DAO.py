from database.DB_connect import DBConnect
from model.album import Album


class DAO():
    @staticmethod
    def getAlbums(n):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT a.* , SUM(t.Milliseconds)/1000 as n
                    FROM track t , album a 
                    WHERE t.AlbumId = a.AlbumId 
                    GROUP BY a.AlbumId 
                    HAVING SUM(t.Milliseconds)/1000>%s"""
        cursor.execute(query, (n,))

        for row in cursor:
            result.append(Album(**row))
        cursor.close()
        conn.close()
        return result

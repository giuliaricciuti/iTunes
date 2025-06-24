from database.DB_connect import DBConnect
from model.album import Album


class DAO():

    @staticmethod
    def getAllAlbums(n):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT DISTINCT a.AlbumId, a.Title , a.ArtistId , SUM(t.UnitPrice) as price 
                    FROM track t , album a 
                    WHERE t.AlbumId = a.AlbumId 
                    GROUP BY a.AlbumId 
                    HAVING price>%s"""
        cursor.execute(query, (n,))

        for row in cursor:
            result.append(Album(**row))
        cursor.close()
        conn.close()
        return result

from database.DB_connect import DBConnect
from model.album import Album


class DAO():

    @staticmethod
    def getAllAlbum():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM album"
        cursor.execute(query)

        for row in cursor:
            result.append(Album(**row))
        cursor.close()
        conn.close()
        return result


    @staticmethod
    def getAlbumDurata(durata, idMap):
        conn = DBConnect.get_connection()

        result = {}

        cursor = conn.cursor()
        query = """select a.AlbumId , sum(t.Milliseconds)/60000 as durata
                    from track t , album a 
                    where t.AlbumId = a.AlbumId 
                    group by a.AlbumId 
                    having durata>%s"""
        cursor.execute(query, (durata,))

        for row in cursor:
            result[idMap[row["a.AlbumId"]]] = row["durata"]
        cursor.close()
        conn.close()
        return result
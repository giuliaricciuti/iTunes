from database.DB_connect import DBConnect
from model.genere import Genere
from model.track import Track


class DAO():


    @staticmethod
    def getAllGeneri():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT DISTINCT g.*
                    FROM genre g """
        cursor.execute(query)

        for row in cursor:
            result.append(Genere(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllTracks(min, max, genere):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT t.* 
                    FROM track t 
                    WHERE t.Milliseconds/1000>=%s
                    AND t.Milliseconds/1000 <= %s
                    AND t.GenreId = %s"""
        cursor.execute(query, (min, max, genere))

        for row in cursor:
            result.append(Track(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllArchi(min, max, genere):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()
        query = """SELECT tab1.TrackId, tab2.TrackId, tab1.n1, tab2.n2
                    FROM (SELECT t.TrackId , COUNT(DISTINCT p.PlaylistId) as n1 
                    FROM track t , playlisttrack p 
                    WHERE t.Milliseconds/1000>=%s AND t.Milliseconds/1000 <= %s 
                    AND t.GenreId = %s AND p.TrackId = t.TrackId
                    GROUP BY t.TrackId) as tab1,
                    (SELECT t2.TrackId, COUNT(DISTINCT p2.PlaylistId) as n2
                    from track t2, playlisttrack p2
                    WHERE t2.Milliseconds/1000>=%s AND t2.Milliseconds/1000<=%s
                    AND t2.GenreId =%s AND p2.TrackId =t2.TrackId
                    GROUP BY t2.TrackId) as tab2
                    WHERE tab1.n1=tab2.n2
                    AND tab1.TrackId<tab2.TrackID"""
        cursor.execute(query, (min, max, genere, min, max, genere))

        for row in cursor:
            result.append((row[0], row[1], row[2], row[3]))
        cursor.close()
        conn.close()
        return result

from database.DB_connect import DBConnect
from model.album import Album


class DAO():
    @staticmethod
    def getAllAlbum(durata):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()
        query = """SELECT DISTINCT a.* , AVG(t.Milliseconds) as m
                    FROM track t , album a 
                    WHERE t.AlbumId = a.AlbumId 
                    group by t.AlbumId 
                    HAVING m>%s*1000"""
        cursor.execute(query, (durata,))

        for row in cursor:
            a = row[:4]
            album = Album(*a)
            result.append((album))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges(idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()
        query = """SELECT DISTINCT t.AlbumId, t2.AlbumId 
                    FROM track t , track t2, playlisttrack p , playlisttrack p2 
                    WHERE t.TrackId=p.TrackId AND t2.TrackId = p2.TrackId 
                    AND p.PlaylistId = p2.PlaylistId AND t.TrackId!=t2.TrackId
                    AND t2.AlbumId < t.AlbumId"""
        cursor.execute(query,)

        for row in cursor:
            if row[0] in idMap.keys() and row[1] in idMap.keys():
                result.append((idMap[row[0]], idMap[row[1]]))
        cursor.close()
        conn.close()
        return result


    @staticmethod
    def getTracksCount(album):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()
        query = """SELECT COUNT(DISTINCT t.TrackId)
                    FROM track t 
                    WHERE AlbumId = %s
                    """
        cursor.execute(query, (album,))

        for row in cursor:
            result.append(row[0])
        cursor.close()
        conn.close()
        return result
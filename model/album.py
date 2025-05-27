from dataclasses import dataclass


@dataclass
class Album:
    AlbumId: int
    Title: str
    ArtistId: int

    def __hash__(self):
        return self.AlbumId

    def __eq__(self, other):
        return self.AlbumId == other.AlbumId

    def __str__(self):
        return f"{self.Title}"
from math import ceil

class PhotoAlbum:

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(ceil(photos_count / 4))

    def add_photo(self, label):
        for page in range(len(self.photos)):
            if len(self.photos[page]) == 4:
                continue
            self.photos[page].append(label)
            idx = self.photos[page].index(label)
            return f"{label} photo added successfully on page {page + 1} slot {idx + 1}"
        return "No more free slots"

    def display(self):
        result = "-----------\n"

        for row in range(len(self.photos)):
            current_result = ' '.join(["[]" for x in range(len(self.photos[row]))])
            result += current_result + "\n" + "-----------\n"

        return result.strip()

album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())


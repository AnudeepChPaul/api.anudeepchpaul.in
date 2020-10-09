import json


class Technology(object):
    def __init__(self, name, techId, rating, rank):
        self.name = name
        self.techId = techId
        self.rating = rating
        self.rank = rank

    def to_json(self):
        return json.dumps({
            'name': self.name,
            'techId': self.techId,
            'rating': self.rating,
            'rank': self.rank
        })

    @staticmethod
    def load_from_string():
        print()
        pass

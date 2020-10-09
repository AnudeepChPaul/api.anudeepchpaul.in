class BaseModel(object):
    def get(self, prop):
        return self[prop]

    def is_valid(self):
        return True

    @staticmethod
    def load_from_string():
        pass

    @staticmethod
    def load_from_json():
        pass
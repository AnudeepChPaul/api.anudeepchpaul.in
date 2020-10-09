import json
import uuid

from src.models.base import BaseModel


def is_valid():
    return True


class Company(BaseModel):
    def __init__(self, companyName, companyId, duration, designation, technologies):
        self.companyName = companyName
        self.companyId = companyId or str(uuid.uuid5(uuid.NAMESPACE_DNS, companyName))
        self.duration = duration
        self.designation = designation
        self.technologies = technologies

    def to_json(self):
        return dict({
            'companyName': self.companyName,
            'companyId': self.companyId,
            'duration': self.duration,
            'designation': self.designation,
            'technologies': self.technologies
        })

    @staticmethod
    def load_from_json(data):
        return Company(data.get('companyName'),
                       data.get('companyId'),
                       data.get('duration'),
                       data.get('designation'),
                       data.get('technologies'))
        pass

import json
from dataclasses import dataclass


@dataclass
class Client:
    name: str
    surname: str
    email: str

    def converter(self):
        return json.dumps({
            "name": self.name,
            "surname": self.surname,
            "email": self. email
        })

    @classmethod
    def from_str(cls, raw_client: str) -> 'Client':
        client_dict = json.loads(raw_client)
        return Client(
            name=client_dict["name"],
            surname=client_dict["surname"],
            email=client_dict["email"]
        )


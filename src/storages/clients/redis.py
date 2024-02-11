from src.storages.clients.entities import Client
from redis import Redis


class ClientsStorage:
    redis: Redis

    def __init__(self, redis: Redis):
        self.redis = redis

    def get_client(self, client_email: str) -> Client:
        raw_client = self.redis.get(client_email)
        return Client.from_str(raw_client)

    def register_new_client(self, client: Client):
        self.redis.set(client.email, client.converter())
        self.redis.lpush("client_emails", client.email)

    def update_client(self, client: Client):
        self.redis.set(client.email, client.converter())

    def get_all_clients(self) -> list[Client]:
        client_emails = self.redis.ltrim("client_emails", 0, -1)
        client_list = []
        for email in client_emails:
            client = self.get_client(email)
            client_list.append(client)

        return client_list


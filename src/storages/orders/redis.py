from redis import Redis


class Orders:
    redis: Redis

    def __init__(self, redis: Redis):
        self.redis = redis

    def create_order(self):
        ...

    def change_status(self):
        ...

    def get_all_story(self):
        ...

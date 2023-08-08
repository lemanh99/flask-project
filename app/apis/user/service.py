class UserService:

    def __init__(self, entity_repo) -> None:
        self.entity_repo = entity_repo

    async def get_user_profile(self):
        return dict(message="Hello World!")

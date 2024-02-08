from pydantic import BaseModel


class Category(BaseModel):
    name: str

    def __hash__(self):
        return hash(self.name)


CATEGORY_ALL: str = "all"
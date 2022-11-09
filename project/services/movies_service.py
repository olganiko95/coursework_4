from typing import Optional
from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.models import Movie
from project.dao.main import MoviesDAO

class MoviesService:
    def __init__(self, dao: MoviesDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Movie:
        if movie := self.dao.get_by_id(pk):
            return movie
        raise ItemNotFound(f'movie with pk={pk} not exists.')

    def get_all(self, filter=None, page: Optional[int] = None) -> list[Movie]:
        return self.dao.get_all_order_by(page=page, filter=filter)
from sqlalchemy import desc, asc
from project.dao.base import BaseDAO
from project.models import Genre, Director, Movie, User
from flask_sqlalchemy import BaseQuery
from werkzeug.exceptions import NotFound

from project.tools.security import generate_password_hash


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre

class DirectorsDAO(BaseDAO[Director]):
    __model__ = Director

class MoviesDAO(BaseDAO[Movie]):
    __model__ = Movie

    def get_all_order_by(self, filter, page):
        stmt: BaseQuery = self._db_session.query(self.__model__)
        if filter == 'new':
            stmt = stmt.order_by(desc(self.__model__.year))
        if filter == 'old':
            stmt = stmt.order_by(asc(self.__model__.year))
        if page:
            try:
                return stmt.paginate(page, self._items_per_page).items
            except NotFound:
                return []
        return stmt.all()



class UsersDAO(BaseDAO[User]):
    __model__ = User

    def create(self, login, password):
        try:
            self._db_session.add(User(email=login,
                                password=generate_password_hash(password)))
            self._db_session.commit()
            print('Пользователь добавлен')
        except Exception as e:
            print(e)
            return self._db_session.rollback()

    def get_user_by_login(self, login):
        try:
            stmt = self._db_session.query(self.__model__).filter(self.__model__.email == login).one()
            return stmt
        except Exception as e:
            print(e)
            return {}
    def update(self, login, data):
        try:
            self._db_session.query(self.__model__).filter(self.__model__.email == login).update(data)
            self._db_session.commit()
            print('Пользователь обновлен')
        except Exception as e:
            print(e)
            return self._db_session.rollback()


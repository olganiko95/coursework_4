from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Режиссеры', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Квентин Тарантино'),
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Убить Билла'),
    'description': fields.String(required=True, max_length=100, example='123'),
    'trailer': fields.String(required=True, max_length=100, example='123'),
    'year': fields.String(required=True, example='2001'),
    'rating': fields.String(required=True, example='10'),
    'genre': fields.Nested(genre),
    'director': fields.Nested(director)
})

user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, max_length=100, example='helen12@mail.ru'),
    'password': fields.String(required=True, max_length=100, example='123456'),
    'name': fields.String(required=True, max_length=100, example='Helen'),
    'surname': fields.String(required=True, example='Smith'),
    'genre': fields.Nested(genre),
})

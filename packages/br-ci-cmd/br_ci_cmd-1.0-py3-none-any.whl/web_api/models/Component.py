from typing import List

from mongoengine import DateTimeField, StringField

from ..mongo import mongo as db


class Component(db.Document):
    name = StringField()
    parentComponent = StringField()
    updatedTime = DateTimeField()

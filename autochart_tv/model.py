from datetime import datetime
from collections import deque
from peewee import *
from peewee import Model, SqliteDatabase
import structlog

db = SqliteDatabase('deleteme.db')


class BaseModel(Model):

    class Meta:
        database = db


class ChartModel(BaseModel):
    name = CharField(unique=True)

    def add(name):
        try:
            kwarg = {'name': name}
            ChartModel.create(**kwarg)
            if len(ChartModel) > 9:
                # oldest = ChartModel.select().limit(1).get()

                oldest = ChartModel.select()
                oldest[0].delete_instance()
                # oldest.delete_instance()
            return True
        except IntegrityError:
            return False

    def query():
        query_ = ChartModel.select()
        return [x.name for x in query_]

    def delete_last():
        if len(ChartModel) > 0:
            latest = ChartModel.select()
            latest[-1].delete_instance()
            return True
        return False


with db:
    db.drop_tables([ChartModel])
    db.create_tables([ChartModel])

# ChartModel.add('BTC')
# print(ChartModel.query())
# ChartModel.add('ETH')
# print(ChartModel.query())
# ChartModel.add('ZCH')
# print(ChartModel.query())
# ChartModel.delete_last()
# print(ChartModel.query())

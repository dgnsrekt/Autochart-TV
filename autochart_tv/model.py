from datetime import datetime
from collections import deque
from peewee import *
from peewee import Model, SqliteDatabase
import structlog

AutoChartDatabase = SqliteDatabase('AutoChart.db')


class BaseModel(Model):

    class Meta:
        database = AutoChartDatabase


class AutoChartModel(BaseModel):
    name = CharField(unique=True)

    def add(name):
        try:
            kwarg = {'name': name}
            AutoChartModel.create(**kwarg)
            if len(AutoChartModel) > 9:
                oldest = AutoChartModel.select()
                oldest[0].delete_instance()
            return True

        except IntegrityError:
            return False

    def query():
        query_ = AutoChartModel.select()
        return [x.name for x in query_]

    def delete_last():
        if len(AutoChartModel) > 0:
            latest = AutoChartModel.select()
            latest[-1].delete_instance()
            return True
        return False

    def clear_all():
        query_ = AutoChartModel.select()
        for q in query_:
            q.delete_instance()

#TODO: may need to move this
with AutoChartDatabase:
    AutoChartDatabase.drop_tables([AutoChartModel])
    AutoChartDatabase.create_tables([AutoChartModel])

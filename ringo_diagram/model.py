import sqlalchemy as sa
from ringo.model import Base
from ringo.model.base import BaseItem, BaseFactory


class DiagramFactory(BaseFactory):

    def create(self, user=None, values=None):
        if value is None:
            values = {}
        new_item = BaseFactory.create(self, user, values)
        return new_item


class Diagram(BaseItem, Base):
    """Docstring for diagram extension"""

    __tablename__ = 'diagrams'
    """Name of the table in the database for this modul. Do not
    change!"""
    _modul_id = None
    """Will be set dynamically. See include me of this modul"""

    # Define columns of the table in the database
    id = sa.Column(sa.Integer, primary_key=True)

    # Define relations to other tables

    @classmethod
    def get_item_factory(cls):
        return DiagramFactory(cls)

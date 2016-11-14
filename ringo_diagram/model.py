# import sqlalchemy as sa
# from ringo.model import Base
# from ringo.model.base import BaseItem, BaseFactory
from ringo.lib.helpers import literal  # , serialize


# class DiagramFactory(BaseFactory):
#
#     def create(self, user=None, values=None):
#         if value is None:
#             values = {}
#         new_item = BaseFactory.create(self, user, values)
#         return new_item
#
#
# class Diagram(BaseItem, Base):
#     """Docstring for diagram extension"""
#
#     __tablename__ = 'diagrams'
#     """Name of the table in the database for this modul. Do not
#     change!"""
#     _modul_id = None
#     """Will be set dynamically. See include me of this modul"""
#
#     # Define columns of the table in the database
#     id = sa.Column(sa.Integer, primary_key=True)
#
#     # Define relations to other tables
#
#     @classmethod
#     def get_item_factory(cls):
#         return DiagramFactory(cls)


class Dataprovider(object):
    """Docstring for Dataprovider. """

    def __init__(self, x, title=None, xlabel=None, ylabel=None):
        self.diagram_X_data = None
        """Attribute within an item of the data source where to find the
        timing information."""
        self.diagram_data_series = {}
        """Series of the diagram list of tuples. (Title, [1,3,4,5,...])"""
        self.diagram_X_label = "X-Axis"
        """Label of the X-Axis"""
        self.diagram_Y_label = "Y-Axis"
        """Label of the Y-Axis"""
        self.diagram_title = ""
        """Title of Diagram"""
        self.diagram_data_error_value = False

        self.diagram_X_data = x
        if title:
            self.diagram_title = title
        if xlabel:
            self.diagram_X_label = xlabel
        if ylabel:
            self.diagram_Y_label = ylabel

    def add_series(self, title, data):
        """TODO: Docstring for add_series .
        :returns: TODO

        """
        if title not in self.diagram_data_series:
            self.diagram_data_series[title] = data

    def get_diagram_titel(self):
        return self.diagram_title

    def get_diagram_xlabel(self):
        return self.diagram_X_label

    def get_diagram_ylabel(self):
        return self.diagram_Y_label

    def errors_enabled(self):
        if self.diagram_data_error_value:
            return True
        else:
            return False

    def has_diagram_data(self):
        for key in self.diagram_data_series:
            if self.diagram_data_series[key]:
                return True
        return False

    def get_diagram_data(self):

        def write_header(series):
            header = ["Time"]
            for s in sorted(series.keys()):
                header.append(str(s))
            return ",".join(header)

        def write_row(idx, x, series):
            row = [str(x)]
            for s in sorted(series.keys()):
                serie = series.get(s)
                if serie:
                    row.append(str(serie[idx]))
            return ",".join(row)

        data = []
        data.append(write_header(self.diagram_data_series))
        if self.diagram_X_data:
            for index, value in enumerate(self.diagram_X_data):
                data.append(write_row(index, value, self.diagram_data_series))
        return literal("\\n".join(data))

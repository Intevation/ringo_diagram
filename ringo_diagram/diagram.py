from ringo.lib.helpers import serialize, literal
from ringo.model.mixins import Mixin


class Dataprovider(Mixin):

    """Docstring for Dataprovider. """
    diagram_data_source = None
    """Attribute of the item where to get the source of diagram data."""
    diagram_data_time = None
    """Attribute within an item of the data source where to find the
    timing information."""
    diagram_data_value = None
    """Attribute within an item of the data source where to find the
    actual value."""
    diagram_data_error_value = None
    """Attribute to indicate that error values should be included"""
    diagram_data_serie = None
    """Attribute within an item of the data source where to find the serie."""
    diagram_X_label = "X-Axis"
    """Label of the X-Axis"""
    diagram_Y_label = "Y-Axis"
    """Label of the Y-Axis"""
    diagram_title = ""
    """Title of Diagram"""


    def _build_series_label(self, data):
        meter = getattr(data, self.diagram_data_serie)
        point = data.point
        station = point.station
        label = u"{station}-{point}:{meter}".format(station=station.code,
                                                    point=unicode(point),
                                                    meter=unicode(meter))
        return label


    def _get_series(self):
        series = []
        for data in getattr(self, self.diagram_data_source):
            label = self._build_series_label(data)
            if label not in series:
                series.append(label)
        return series

    def _get_meanvalue(self):
        # FIXME: Check calculation of mean value. simple calculation of
        # mean value seems to give the best result in diagram
        # (Null-Linie) (ti) <2016-08-09 14:48>
        # values = []
        # for o in self.observations:
        #   # dGravity - IF(((fGradient=0)||ISNULL(fGradient)),-3080,fGradient)*(fHDatum-:HRef)))
        #   if o.gradient == 0 or o.gradient is None:
        #       values.append(o.round_gravity - 3080 * (o.hdatum - href))
        #   else:
        #       values.append(o.round_gravity - o.gradient*(o.hdatum - href))
        # return round(sum(values) / float(len(values)))
        data = getattr(self, self.diagram_data_source)
        total = sum([getattr(r, self.diagram_data_value) for r in data])
        return round(total / float(len(data)))

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

    def get_diagram_data(self):

        def write_row(series, data, meanvalue=0):
            row = []
            row.append(str(serialize(getattr(data, self.diagram_data_time))))
            for serie in series:
                if serie == self._build_series_label(data):
                    value = getattr(data, self.diagram_data_value) - meanvalue
                    row.append(str(value))
                    if self.errors_enabled():
                        row.append(str(getattr(data,
                                               self.diagram_data_error_value)))
                else:
                    row.append("")
                    if self.errors_enabled():
                        row.append("")
            return ",".join(row)

        def write_header(series):
            data = ["Date"]
            for serie in series:
                data.append(unicode(serie))
            return ",".join(data)

        series = self._get_series()
        data = []
        data.append(write_header(series))
        for row in getattr(self, self.diagram_data_source):
            data.append(write_row(series, row, self._get_meanvalue()))
        return literal("\\n".join(data))

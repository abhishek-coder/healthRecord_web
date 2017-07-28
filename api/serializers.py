from records import models


class CaseSerializer(object):
    def __init__(self, cases):
        self.queryset = cases
        return self

    def serialize(self):
        return [dict(
            title=c.title,
            patient=c.patient_id,
            doctor_name=str(c.doctor),
            date=str(c.created),
            notes=c.notes
        ) for c in self.queryset]

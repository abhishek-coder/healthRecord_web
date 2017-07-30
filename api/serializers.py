from records import models


class CaseListSerializer(object):
    def __init__(self, cases):
        self.queryset = cases

    def serialize(self):
        return [dict(
            id=c.id,
            title=c.title,
            doctor_name=str(c.doctor),
            date=c.created.strftime("%Y-%m-%d %I:%M %p")
        ) for c in self.queryset]


class CaseDetailSerializer(object):
    def __init__(self, case):
        self.case = case

    def serialize(self):
        c = self.case
        return dict(
            title=c.title,
            patient=c.patient_id,
            doctor_name=str(c.doctor),
            date=str(c.created),
            notes=c.notes,

            records=[
                dict(
                    symptoms=r.symptoms,
                    prescription=r.prescription.serialize(),
                    created=r.created.strftime("%Y-%m-%d %I:%M %p")
                ) for r in c.records.all()]
        )

{% extends '__layout.tpl' %}

{% block title %}
  Patient Health Records
{% endblock %}

{% block content %}
  <div class="row">
    <div class="col-md-12">
      {% include '_user.tpl' %}
    </div>
  </div>

  <div class="col-md-4">
    <h3>Create new case </h3>
    <form action="{% url 'new_case' patient.id %}" method="POST"
          enctype="multipart/form-data">
      {% csrf_token %}
      <div class="form-group">
        <label>Title</label>
        <input name="title" class="form-control" type="text"
               placeholder="Hospital Name, clinic name, disease" required>
      </div>

      <div class="form-group">
        <label>Notes</label>
        <textarea name="notes" class="form-control"
                  placeholder="Notes" required></textarea>
      </div>

      <div class="form-group">
        <label>Symptoms</label>
        <textarea name="symptoms" class="form-control"
                  placeholder="Symptoms" required></textarea>
      </div>

      <div class="form-group">
        <label>Prescription</label>
        <textarea name="prescription" class="form-control"
                  placeholder="Prescription"></textarea>
      </div>

      <div class="form-group">
        <label>Upload Prescription</label>
        <input  name="document" type="file">
      </div>

      <button type="submit" class="btn btn-primary">Create case</button>
      <a class="btn btn-primary" href="{% url 'patient_detail' patient.id %}">Back to Patient detail </a>
  </div>
{% endblock %}

{% extends '__layout.tpl' %}

{% block title %}
  Patient Health Records
{% endblock %}

{% block content %}
  <div class="col-md-12">
    {% include '_user.tpl' %}
    <a class="btn btn-success " href="{% url 'new_case' patient.id %}">
      Create new case</a>
    &nbsp;
    <a class="btn btn-success" href="{% url 'patient_detail' patient.id %}">
      Patient detail
    </a>
  </div>

  <div class="col-md-12">
    <hr>
    <h3>#{{ case.id }}</h3>
    <p>Dr. {{ case.doctor }}</p>
    <p>{{ case.title }}</p>
    <p>notes:- {{ case.notes }}</p>

    <div class="table-responsive">
      <table class="table table-striped">
        <thead>
          <tr>
            <th>ID</th>
            <th>Symptoms</th>
            <th>Prescription</th>
            <th>Date</th>
          </tr>
        </thead>
        <tbody>
          {% for r in case.records.all %}
            <tr>
              <td>#{{ r.id }}</td>
              <td>{{ r.symptoms }}</td>
              <td>
                {{ r.prescription.text }}
                {% if r.prescription.upload %}
                  <a target="_blank" href="{{ r.prescription.upload.url }}">
                    View attachment</a>
                {% endif %}
              </td>
              <td>{{ r.created }}</td>
            </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>
{% endblock %}

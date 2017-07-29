{% extends '__layout.tpl' %}

{% block title %}
  Patient Health Records
{% endblock %}

{% block content %}
  <div class="col-md-4">
    {% include '_user.tpl' %}
  </div>

  <div class="col-md-8">
    <a class="btn btn-success" href="{% url 'new_case' patient.id %}">Create new case</a>
  </div>

  <div class="col-md-12">
    <div class="table-responsive">
      <table class="table table-striped table-bordered">
        <thead>
          <tr>
            <th>Case ID</th>
            <th>Doctor</th>
            <th>First consultation</th>
            <th>Title</th>
          </tr>
        </thead>
        <tbody>
          {% for c in cases %}
            <tr>
              <td>#{{ c.id }}</td>
              <td>{{ c.doctor }}</td>
              <td>{{ c.created }}</td>
              <td class="center">{{ c.title }}</td>
            </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>
{% endblock %}

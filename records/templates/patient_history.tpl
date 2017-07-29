{% extends '__layout.tpl' %}

{% block title %}
  Patient Health Records
{% endblock %}

{% block content %}
  <div class="col-md-4">
    {% include '_user.tpl' %}
    <a class="btn btn-success btn-block" href="{% url 'new_case' patient.id %}">
      Create new case</a>
  </div>

  <div class="col-md-offset-2 col-md-4">

  </div>

  <div class="col-md-12">
    <hr>
    <h3>Cases</h3>
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
              <td>#{{ c.id }}
                <a href="{% url 'case_detail' patient.id c.id %}">View details</a>
              </td>
              <td>{{ c.doctor }}</td>
              <td>{{ c.created|date }}</td>
              <td class="center">
                <span class="label label-default">{{ c.records.count }} records</span>
                <br>
                {{ c.title }}</td>
            </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>
{% endblock %}

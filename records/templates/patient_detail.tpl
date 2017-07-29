{% extends '__layout.tpl' %}

{% block title %}
  Patient Health Records
{% endblock %}

{% block content %}
  <div class="col-md-4">
    {% include '_user.tpl' %}
  </div>

  <div class="col-md-6">
    <a class="btn btn-primary" href="{% url 'history' patient.id %}">View case history</a>
    <a class="btn btn-success" href="{% url 'new_case' patient.id %}">Create new case</a>
  </div>

{% endblock %}

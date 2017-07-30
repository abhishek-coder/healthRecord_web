{% extends '__layout.tpl' %}

{% block title %}
  Patient Health Records
{% endblock %}

{% block content %}
  <div class="col-md-12">
    {% include '_user.tpl' %}
  </div>

  <div class="row">
    <div class="col-md-12">
      <hr>
      <div class="col-md-offset-1 col-md-4">
        <a class="btn btn-primary btn-block" href="{% url 'history' patient.id %}">
          View case history</a>
      </div>

      <div class="col-md-offset-1 col-md-4">
        <a class="btn btn-success btn-block" href="{% url 'new_case' patient.id %}">
          Create new case</a>
      </div>
    </div>
  </div>
{% endblock %}

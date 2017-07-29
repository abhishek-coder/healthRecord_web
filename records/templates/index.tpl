{% extends '__layout.tpl' %}

{% block title %}
  {{ block.super }}
{% endblock %}

{% block content %}
  <h1>Welcome to Helath+</h1>

  <a class="btn btn-primary" href="{% url 'doctor_login' %}">Doctor login</a>
{% endblock %}

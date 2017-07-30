{% extends '__layout.tpl' %}

{% block title %}
  {{ block.super }}
{% endblock %}

{% block content %}
  <div class="row">
    <div class="col-md-offset-4 col-md-6">
      <div class="jumbotron">
        <h1>Welcome to Health+</h1>
        <p>Health+ is a Patient Record system linked with Aadhar. If you are a registered
          doctor, login to view and create records.</p>
        <p><a class="btn btn-primary btn-lg" href="{% url 'doctor_login' %}">
          Doctor Login</a></p>
      </div>
    </div>
  </div>
{% endblock %}

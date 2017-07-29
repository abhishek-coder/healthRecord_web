{% extends '__layout.tpl' %}

{% block title %}
  Doctor Login | {{ block.super }}
{% endblock %}

{% block content %}
  <div class="page-content container">
    <div class="row">
      <div class="col-md-6 col-md-offset-4">
        <div class="login-wrapper">
          <div class="box">
            <div class="content-wrap">
              <h6>Sign In | Doctors on Health+</h6>
              <div class="social">

              </div>
              <form action="{% url 'doctor_login' %}" method="POST">
                {% csrf_token %}
                <input class="form-control" name="username" type="text"
                       placeholder="Username">
                <input class="form-control" type="password" name="password"
                       placeholder="Password">
                <div class="action">
                  <button class="btn btn-primary signup">Login</button>
                </div>
            </div>
          </div>


        </div>
      </div>
    </div>
  </div>
{% endblock %}

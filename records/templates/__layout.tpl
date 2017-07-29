{% extends '__base.html' %}

{% block title %}
  Health+
{% endblock %}

{% block body %}
  <div class="header">
    <div class="container">
      <div class="row">
        <div class="col-md-5">
          <!-- Logo -->
          <div class="logo">
            <h1><a href="/">Health <sup>+</sup></a></h1>
          </div>
        </div>
        <div class="col-md-5">
          <div class="row">
            <div class="col-lg-12">
              <div class="input-group form">

              </div>
            </div>
          </div>
        </div>
        <div class="col-md-2">
          <div class="navbar navbar-inverse" role="banner">
            <nav class="collapse navbar-collapse bs-navbar-collapse navbar-right" role="navigation">
              <ul class="nav navbar-nav">
                {% if request.user.is_authenticated %}
                  <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                      {{ request.user.first_name }} <b class="caret"></b></a>
                    <ul class="dropdown-menu animated fadeInUp">
                      <li><a href="/logout/">Logout</a></li>
                    </ul>
                  </li>
                {% endif %}
              </ul>
            </nav>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="page-content">
    <div class="row">
      <div class="col-md-2">
        {% include '_sidebar.tpl' %}
      </div>

      {% block content %}
      {% endblock %}
    </div>
  </div>

  <footer>
    <div class="container">
      <div class="copy text-center">
        Copyright 2017 <a href='#'>Quick-5</a>
      </div>
    </div>
  </footer>
{% endblock %}

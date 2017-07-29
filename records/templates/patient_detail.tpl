{% extends '__layout.tpl' %}

{% block title %}
  Patient Health Records
{% endblock %}

{% block content %}
<div class="row">
  <div class="col-md-4"> </div>
  <div class="col-md-8">
    <form action="" method="POST">
      {% csrf_token %}
      <p>{{ form }}</p>
      <input type="submit" value="Submit" />
    </form>
  </div>
</div>

{% endblock %}

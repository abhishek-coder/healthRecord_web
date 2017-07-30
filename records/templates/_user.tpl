<div class="col-md-3">
  {% if aadhar_data.photo %}
    <img height="150px" class="img-circle" src="{{ aadhar_data.photo }}">
  {% else %}
    <img height="150px" class="img-circle" src="/static/images/default.png">
  {% endif %}
</div>
<div class="col-md-9">
  <div class="form-group">
    <label>Name</label> : {{ patient }}
  </div>

  <div class="form-group">
    <label>Age</label>: {{ aadhar_data.age }}
  </div>

  <div class="form-group">
    <label>Gender</label>: {{ aadhar_data.gender }}
  </div>

  <div class="form-group">
    <label>State</label>: {{ aadhar_data.state }}
  </div>
</div>

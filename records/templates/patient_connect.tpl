{% extends '__layout.tpl' %}

{% block title %}
  Patient Health Records
{% endblock %}

{% block content %}
  <div class="col-md-10">
    <div class="row">
      <div class="col-md-6">
        <div class="content-box-large">
          <div class="panel-heading">
            <div class="panel-title">Search patient</div>
          </div>
          <div class="panel-body">
            <form class="form-horizontal" action="{% url 'patient_connect' %}"
                  method="POST" role="form">
              {% csrf_token %}
              <div class="form-group">
                <label for="aadhar_id" class="col-sm-2 control-label">Aadhaar ID</label>
                <div class="col-sm-10">
                  <input type="text" class="form-control" name="aadhar_number"
                         placeholder="Aadhar number">
                </div>
              </div>

              <div class="form-group">
                <div class="col-sm-offset-2 col-sm-10">
                  <button type="submit" class="btn btn-primary">Check patient</button>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>

      <div class="col-md-6">
        <div class="row">
          <div class="col-md-12">
            <div class="content-box-header">
              <div class="panel-title">Finding patients </div>

              <div class="panel-options">
                <a href="#" data-rel="collapse"><i class="glyphicon glyphicon-refresh"></i></a>
                <a href="#" data-rel="reload"><i class="glyphicon glyphicon-cog"></i></a>
              </div>
            </div>
            <div class="content-box-large box-with-header">

              To search for a patient, add his/her Adhaar ID card number. Currently we only support Adhaar based authentication scheme. Please ensure you have correct ID details of the patient you are searching.
              <br /><br />
            </div>
          </div>
        </div>

      </div>
    </div>


  </div>

{% endblock %}

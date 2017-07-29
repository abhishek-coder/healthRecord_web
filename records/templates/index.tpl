{% extends '__layout.tpl' %}

{% block title %}
  Find patients | {{ block.super }}
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
            <form class="form-horizontal" role="form">
              <div class="form-group">
                <label for="inputEmail3" class="col-sm-2 control-label">Adhaar ID#</label>
                <div class="col-sm-10">
                  <input type="email" class="form-control" id="inputEmail3" placeholder="Email">
                </div>
              </div>
              <div class="form-group">
                <label for="inputEmail3" class="col-sm-2 control-label">Other detail</label>
                <div class="col-sm-10">
                  <input type="text" class="form-control" id="otherDetail" placeholder="Other detail">
                </div>
              </div>

              <div class="form-group">
                <div class="col-sm-offset-2 col-sm-10">
                  <button type="submit" class="btn btn-primary">Find patient</button>
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

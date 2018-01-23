<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<?php
$link = mysqli_connect("127.0.0.1", "root", "");
?>

<title>Dashboard ECAM</title>

<head>

<!-- Bootstrap core CSS -->
<link href="assets/css/bootstrap.css" rel="stylesheet">
<!--external css-->
<link href="assets/font-awesome/css/font-awesome.css" rel="stylesheet" />
<!-- Custom styles for this template -->
<link href="assets/css/style.css" rel="stylesheet">


</head>

  <body>
  <section id="container" >
  <!-- **********************************************************************************************************************************************************
  TOP BAR CONTENT
  *********************************************************************************************************************************************************** -->
  <!--header start-->
  <header class="header black-bg">
          <div class="sidebar-toggle-box">
              <div class="fa fa-bars tooltips"></div>
          </div>
        <!--logo start-->
        <a href="index.php" class="logo"><b>DASHBOARD ECAM IoT</b></a>
        
        <!--logo end-->

        </div>
    </header>
  <!--header end-->
  
  <!-- **********************************************************************************************************************************************************
  MAIN SIDEBAR MENU
  *********************************************************************************************************************************************************** -->
  <!--sidebar start-->
  <aside>
      <div id="sidebar"  class="nav-collapse ">
          <!-- sidebar menu start-->
          <ul class="sidebar-menu" id="nav-accordion">
          
                <p class="centered"><a href="profile.html"><img src="assets/img/Logo_ECAM.jpg" width="60"></a></p>
                <h5 class="centered">ECAM Strasbourg Europe</h5>
                    
              <li class="mt">
                  <a class="active" href="index.php">
                      <i class="fa fa-dashboard"></i>
                      <span>Dashboard</span>
                      <span>Room 012</span>
                      <span>Room 105</span>
                      <span>Dashboard</span>
                      <span>Dashboard</span>
                  </a>
              </li>

          </ul>
          <!-- sidebar menu end-->
      </div>
  </aside>
  <!--sidebar end-->
  
  <!-- **********************************************************************************************************************************************************
  MAIN CONTENT
  *********************************************************************************************************************************************************** -->
  <!--main content start-->
  <section id="main-content">
      <section class="wrapper">

          <div class="row">


                <div class="col-lg-12 main-chart">
                    <div class="row mt">
                    <!-- Panel des états -->
                    <div class="col-lg-4 col-md-4 col-sm-4 mb">
                    <div class="weather-3 pn centered">
                        <i class="fa fa-sun-o"></i>
                        <h1>30º C</h1>
                        <div class="info">
                            <div class="row">
                                    <h3 class="centered">SCHILTIGHEIM</h3>
                                <div class="col-sm-6 col-xs-6 pull-left">
                                    <p class="goleft"><i class="fa fa-tint"></i> 13%</p>
                                </div>
                                <div class="col-sm-6 col-xs-6 pull-right">
                                    <p class="goright"><i class="fa fa-flag"></i> 15 MPH</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div><!--/col-md-4 -->
                      

                    <div class="col-md-4 col-sm-4 mb">
                    <div class="weather-3 pn centered">
                            <i class="fa fa-thermometer-2" aria-hidden="true"></i>
                            <h1>30º C</h1>
                            <div class="info">
                                <div class="row">
                                        <h3 class="centered">LA RUE</h3>
                                </div>
                            </div>
                        </div>
                </div><!--/col-md-4 -->
                      
                    <div class="col-md-4 mb">
                        <div class="weather-3 pn centered">
                        <i class="fa fa-tint" aria-hidden="true"></i>
                        <h1>30%</h1>
                        <div class="info">
                            <div class="row">
                                    <h3 class="centered">LA RUE</h3>
                            </div>
                        </div>
                    </div>
                    </div><!-- /col-md-4 -->
                      

                </div><!-- /row -->
  <!--main content end-->

</section>
  </body>
</html>
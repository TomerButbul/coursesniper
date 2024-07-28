from bs4 import BeautifulSoup
import pymysql

# HTML content (replace this with your actual HTML content)
html_content = """
<!DOCTYPE html>
<!-- saved from url=(0077)https://www.purdue.edu/provost/students/s-initiatives/curriculum/courses.html -->
<html xmlns="http://www.w3.org/1999/xhtml" class=" js canvas canvastext geolocation crosswindowmessaging no-websqldatabase indexeddb hashchange historymanagement draganddrop websockets rgba hsla multiplebgs backgroundsize borderimage borderradius boxshadow opacity cssanimations csscolumns cssgradients cssreflections csstransforms csstransforms3d csstransitions  video audio localstorage sessionstorage webworkers no-applicationcache svg smil svgclippaths  fontface" lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		

<meta content="IE=edge" http-equiv="X-UA-Compatible">
<meta content="width=device-width, initial-scale=1" name="viewport">
		




<meta content="Course Listing" property="og:title">
<meta content="${_EscapeTool.xml($metaDescription)}" property="og:description">
<meta content="" property="og:image">
<meta content="https://www.purdue.edu/provost/students/s-initiatives/curriculum/courses.html" property="og:url">
<meta content="website" property="og:type">

<meta content="summary" name="twitter:card">
<meta content="Course Listing" name="twitter:title">
<meta content="${_EscapeTool.xml($metaDescription)}" name="twitter:description">
<meta content="https://www.purdue.edu/provost/students/s-initiatives/curriculum/courses.html" name="twitter:url">
<meta content="" name="twitter:image">
		<title>
			Course Listing - 
			Office of the Provost - Purdue University
		</title>
		<!-- Favicon -->
		<link href="https://www.purdue.edu/purdue/images/favicon.ico" rel="shortcut icon">
<link href="https://www.purdue.edu/purdue/images/icon-iphone.png" rel="apple-touch-icon" sizes="76x76">
<link href="https://www.purdue.edu/purdue/images/icon-ipad.png" rel="apple-touch-icon" sizes="76x76">
<link href="https://www.purdue.edu/purdue/images/icon-iphone-retina.png" rel="apple-touch-icon" sizes="120x120">
<link href="https://www.purdue.edu/purdue/images/icon-ipad-retina.png" rel="apple-touch-icon" sizes="152x152">
		<!-- CSS -->
		<link href="./Course Listing - Office of the Provost - Purdue University_files/all.css" rel="stylesheet">

<!--United sans -->
<link href="./Course Listing - Office of the Provost - Purdue University_files/united-sans.css" rel="stylesheet">

<link href="./Course Listing - Office of the Provost - Purdue University_files/content-1.6-2020.css" rel="stylesheet" type="text/css">
<link href="./Course Listing - Office of the Provost - Purdue University_files/print.css" media="print" rel="stylesheet" type="text/css">


		    <style type="text/css">
	    /* Any CSS placed in this text area will be placed inside of a style tag located in the head section of the page. */


button.accordion {
    background-color: #eee;
    color: #444;
    cursor: pointer;
    padding: 18px;
    width: 100%;
    border: none;
    text-align: left;
    outline: none;
    font-size: 15px;
    transition: 0.4s;
}

button.accordion.active, button.accordion:hover {
    background-color: #ddd;
}

button.accordion:after {
    content: '\02795';
    font-size: 13px;
    color: #777;
    float: right;
    margin-left: 5px;
}

button.accordion.active:after {
    content: "\2796";
}

.maincontent .panel {
    padding: 0 18px;
    background-color: white;
    max-height: 0;
    overflow: hidden;
    transition: 0.6s ease-in-out;
    opacity: 0;
}


.maincontent .panel.show {
    opacity: 1;
    max-height: none;

}
h4 {
    color:#b1810b;"
}


#expand-button, #collapse-button{
    margin: 10px 0;
}

#collapse-button{
    margin-right:10px;
}

    #cool_find_menu input, #cool_find_menu button{
    margin: 10px 0;
}

.scrollup{
    background: url('../images/uparrow.png') no-repeat;
    width: 60px;
    height: 60px;
    position:fixed;
    bottom:30px;
    right:20px;
    display:none;
    text-indent:-9999px;
}

#controller-row{
		padding: 0;
		margin: auto;
	}

	#controller{
		width: 100%;
		background: #ffffff;
		position: relative;
		top:0;
		z-index: 99;
	}

#expand-button, #collapse-button{
			margin: 10px 0;
		}

		#collapse-button{
			margin-right:10px;
		}

		 #cool_find_menu input, #cool_find_menu button{
			margin: 10px 0;
		}

	</style>

		<!--Individual page css -->
		<!-- Javascript-->
		<script async="" src="./Course Listing - Office of the Provost - Purdue University_files/async-ads.js.download"></script><script type="text/javascript" async="" src="./Course Listing - Office of the Provost - Purdue University_files/f.txt"></script><script async="" src="./Course Listing - Office of the Provost - Purdue University_files/analytics.js.download"></script><script async="" src="./Course Listing - Office of the Provost - Purdue University_files/gtm.js.download"></script><script async="true" src="./Course Listing - Office of the Provost - Purdue University_files/modernizr-1.5.min.js.download" type="text/javascript"></script>
<script src="./Course Listing - Office of the Provost - Purdue University_files/jquery-1.10.2.min.js.download" type="text/javascript"></script>
<script src="./Course Listing - Office of the Provost - Purdue University_files/google_jquery_link_tracking.js.download" type="text/javascript"></script>
<script src="./Course Listing - Office of the Provost - Purdue University_files/currentPage-1.6.js.download" type="text/javascript"></script>
<!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
<!--[if lt IE 9]>
	<script src="//www.purdue.edu/purdue/js/html5shiv.js"></script>
	<script src="//www.purdue.edu/purdue/js/respond.min.js"></script>
<![endif]-->

		    <script src="./Course Listing - Office of the Provost - Purdue University_files/find6.js.download" type="text/javascript"></script>

		<!-- Google Analytics -->
		
<script src="./Course Listing - Office of the Provost - Purdue University_files/pGA.js.download" type="text/javascript"></script>
<script type="text/javascript">

    var mCode = '';
    var sCodes = [];

    
    SetAnalytics(mCode,sCodes);

</script>
	<script src="./Course Listing - Office of the Provost - Purdue University_files/cse_element__en.js.download" type="text/javascript"></script><link type="text/css" href="./Course Listing - Office of the Provost - Purdue University_files/default+en.css" rel="stylesheet"><link type="text/css" href="./Course Listing - Office of the Provost - Purdue University_files/minimalist.css" rel="stylesheet"><style type="text/css">.gsc-control-cse{font-family:arial, sans-serif}.gsc-control-cse .gsc-table-result{font-family:arial, sans-serif}.gsc-refinementsGradient{background:linear-gradient(to left,rgba(119,119,119,1),rgba(119,119,119,0))}</style><style type="text/css">.gscb_a{display:inline-block;font:27px/13px arial,sans-serif}.gsst_a .gscb_a{color:#a1b9ed;cursor:pointer}.gsst_a:hover .gscb_a,.gsst_a:focus .gscb_a{color:#36c}.gsst_a{display:inline-block}.gsst_a{cursor:pointer;padding:0 4px}.gsst_a:hover{text-decoration:none!important}.gsst_b{font-size:16px;padding:0 2px;position:relative;user-select:none;-webkit-user-select:none;white-space:nowrap}.gsst_e{vertical-align:middle;opacity:0.55;}.gsst_a:hover .gsst_e,.gsst_a:focus .gsst_e{opacity:0.72;}.gsst_a:active .gsst_e{opacity:1;}.gsst_f{background:white;text-align:left}.gsst_g{background-color:white;border:1px solid #ccc;border-top-color:#d9d9d9;box-shadow:0 2px 4px rgba(0,0,0,0.2);-webkit-box-shadow:0 2px 4px rgba(0,0,0,0.2);margin:-1px -3px;padding:0 6px}.gsst_h{background-color:white;height:1px;margin-bottom:-1px;position:relative;top:-1px}.gsib_a{width:100%;padding:4px 6px 0}.gsib_a,.gsib_b{vertical-align:top}.gssb_c{border:0;position:absolute;z-index:989}.gssb_e{border:1px solid #ccc;border-top-color:#d9d9d9;box-shadow:0 2px 4px rgba(0,0,0,0.2);-webkit-box-shadow:0 2px 4px rgba(0,0,0,0.2);cursor:default}.gssb_f{visibility:hidden;white-space:nowrap}.gssb_k{border:0;display:block;position:absolute;top:0;z-index:988}.gsdd_a{border:none!important}.gsq_a{padding:0}.gssb_a{padding:0 7px}.gssb_a,.gssb_a td{white-space:nowrap;overflow:hidden;line-height:22px}#gssb_b{font-size:11px;color:#36c;text-decoration:none}#gssb_b:hover{font-size:11px;color:#36c;text-decoration:underline}.gssb_g{text-align:center;padding:8px 0 7px;position:relative}.gssb_h{font-size:15px;height:28px;margin:0.2em;-webkit-appearance:button}.gssb_i{background:#eee}.gss_ifl{visibility:hidden;padding-left:5px}.gssb_i .gss_ifl{visibility:visible}a.gssb_j{font-size:13px;color:#36c;text-decoration:none;line-height:100%}a.gssb_j:hover{text-decoration:underline}.gssb_l{height:1px;background-color:#e5e5e5}.gssb_m{color:#000;background:#fff}.gssb_a{padding:0 9px}.gsib_a{padding:5px 9px 4px 9px}.gscb_a{line-height:27px}.gssb_e{border:0}.gssb_l{margin:5px 0}input.gsc-input::-webkit-input-placeholder{font-size:14px}input.gsc-input:-moz-placeholder{font-size:14px}input.gsc-input::-moz-placeholder{font-size:14px}input.gsc-input:-ms-input-placeholder{font-size:14px}input.gsc-input:focus::-webkit-input-placeholder{color:transparent}input.gsc-input:focus:-moz-placeholder{color:transparent}input.gsc-input:focus::-moz-placeholder{color:transparent}input.gsc-input:focus:-ms-input-placeholder{color:transparent}.gssb_c .gsc-completion-container{position:static}.gssb_c{z-index:5000}.gsc-completion-container table{background:transparent;font-size:inherit;font-family:inherit}.gssb_c > tbody > tr,.gssb_c > tbody > tr > td,.gssb_d,.gssb_d > tbody > tr,.gssb_d > tbody > tr > td,.gssb_e,.gssb_e > tbody > tr,.gssb_e > tbody > tr > td{padding:0;margin:0;border:0}.gssb_a table,.gssb_a table tr,.gssb_a table tr td{padding:0;margin:0;border:0}</style></head>
	<body style="" data-new-gr-c-s-check-loaded="14.1186.0" data-gr-ext-installed="">
		<!-- Begin Gold Bar -->
		<div class="navbar navbar-inverse goldbar" role="navigation">
			<div class="container">
				<div class="navbar-header">
					<button class="navbar-toggle left" data-target=".gold" data-toggle="collapse" type="button">
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span> Quick Links
					
					</button>
					<button class="navbar-toggle search right" data-target="#search" data-toggle="collapse" type="button">
						<i class="fa fa-search fa-lg"></i>
					</button>
				</div>
				<div class="collapse navbar-collapse right search" id="search">
					<ul class="nav navbar-nav navbar-right">
						<li class="dropdown">
							<a class="dropdown-toggle" data-toggle="dropdown" href="https://www.purdue.edu/provost/students/s-initiatives/curriculum/courses.html#">
								<i class="fa fa-search fa-lg"></i>
							</a>
							<ul class="dropdown-menu">
								<li>
									<form role="search">
										<div class="form-group">
											
<script>
  (function() {
    var cx = '017690826183710227054:mjxnqnpskjk';
    var gcse = document.createElement('script');
    gcse.type = 'text/javascript';
    gcse.async = true;
    gcse.src = 'https://cse.google.com/cse.js?cx=' + cx;
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(gcse, s);
  })();
</script>
<div id="cse-search-form"><div class="gsc-control-searchbox-only gsc-control-searchbox-only-en" dir="ltr"><form class="gsc-search-box gsc-search-box-tools" accept-charset="utf-8"><table cellspacing="0" cellpadding="0" role="presentation" class="gsc-search-box"><tbody><tr><td class="gsc-input"><div class="gsc-input-box" id="gsc-iw-id1"><table cellspacing="0" cellpadding="0" role="presentation" id="gs_id50" class="gstl_50 gsc-input" style="width: 100%; padding: 0px;"><tbody><tr><td id="gs_tti50" class="gsib_a"><input autocomplete="off" type="text" size="10" class="gsc-input" name="search" title="search" aria-label="search" id="gsc-i-id1" dir="ltr" spellcheck="false" style="width: 100%; padding: 0px; border: none; margin: 0px; height: auto; background: url(&quot;https://www.google.com/cse/static/images/1x/en/branding.png&quot;) left center no-repeat rgb(255, 255, 255); outline: none;"></td><td class="gsib_b"><div class="gsst_b" id="gs_st50" dir="ltr"><a class="gsst_a" href="javascript:void(0)" title="Clear search box" role="button" style="display: none;"><span class="gscb_a" id="gs_cb50" aria-hidden="true">×</span></a></div></td></tr></tbody></table></div></td><td class="gsc-search-button"><button class="gsc-search-button gsc-search-button-v2"><svg width="13" height="13" viewBox="0 0 13 13"><title>search</title><path d="m4.8495 7.8226c0.82666 0 1.5262-0.29146 2.0985-0.87438 0.57232-0.58292 0.86378-1.2877 0.87438-2.1144 0.010599-0.82666-0.28086-1.5262-0.87438-2.0985-0.59352-0.57232-1.293-0.86378-2.0985-0.87438-0.8055-0.010599-1.5103 0.28086-2.1144 0.87438-0.60414 0.59352-0.8956 1.293-0.87438 2.0985 0.021197 0.8055 0.31266 1.5103 0.87438 2.1144 0.56172 0.60414 1.2665 0.8956 2.1144 0.87438zm4.4695 0.2115 3.681 3.6819-1.259 1.284-3.6817-3.7 0.0019784-0.69479-0.090043-0.098846c-0.87973 0.76087-1.92 1.1413-3.1207 1.1413-1.3553 0-2.5025-0.46363-3.4417-1.3909s-1.4088-2.0686-1.4088-3.4239c0-1.3553 0.4696-2.4966 1.4088-3.4239 0.9392-0.92727 2.0864-1.3969 3.4417-1.4088 1.3553-0.011889 2.4906 0.45771 3.406 1.4088 0.9154 0.95107 1.379 2.0924 1.3909 3.4239 0 1.2126-0.38043 2.2588-1.1413 3.1385l0.098834 0.090049z"></path></svg></button></td><td class="gsc-clear-button"><div class="gsc-clear-button" title="clear results">&nbsp;</div></td></tr></tbody></table></form></div></div>

										</div>
									</form>
								</li>
							</ul>
						</li>
					</ul>
				</div>
				<div class="collapse navbar-collapse gold">
					<ul class="nav navbar-nav information">
						<li class="dropdown">
							<a class="dropdown-toggle" data-toggle="dropdown" href="https://www.purdue.edu/provost/students/s-initiatives/curriculum/courses.html#">Find Info For 
								<b class="caret"></b>
							</a>
							<ul class="dropdown-menu"><p class="hide">Find Info For</p>
<li><a class="findInfoLink" href="https://www.purdue.edu/purdue/academics/index.php">Academics</a></li>
<li><a class="findInfoLink" href="https://www.purdue.edu/purdue/admissions/index.php">Admissions</a></li>
<li><a class="findInfoLink" href="https://www.purdue.edu/purdue/current_students/index.php">Current Students</a></li>
<li><a class="findInfoLink" href="https://www.purdue.edu/purdue/athletics/index.php">Athletics</a></li>
<li><a class="findInfoLink" href="https://www.purdue.edu/purdue/about/index.php">About</a></li>
<li><a class="findInfoLink" href="https://www.purdue.edu/purdue/careers/index.php">Careers</a></li>
<li><a class="findInfoLink" href="https://www.purdue.edu/purdue/prospective_students/index.php">Prospective Students</a></li>
<li><a class="findInfoLink" href="https://www.purdue.edu/purdue/research/index.php">Research and Partnerships</a></li>
<li><a class="findInfoLink" href="https://www.purdue.edu/purdue/commercialization/index.php">Entrepreneurship and Commercialization</a></li>
</ul>
						</li>
					</ul>
					<ul class="nav navbar-nav right quicklinks"><p class="hide">Quick Links</p>
<li><a href="https://www.purdue.edu/purdue/apply/">Apply</a></li>
<li><a href="https://www.purdue.edu/newsroom/">News</a></li>
<li><a href="https://www.purdue.edu/president/">President</a></li>
<li><a href="http://purdueteamstore.com/">Shop</a></li>
<li><a href="https://www.purdue.edu/visit/">Visit</a></li>
<li><a href="https://www.purdue.edu/purdue/giveNow.html">Give</a></li>
<li><a href="https://www.purdue.edu/emergency/">Emergency</a></li>
</ul>
				</div>
			</div>
		</div>
		<!-- End Gold Bar -->
		<!-- Begin Top Section -->
		<div class="top">
			<div class="container">
				<div class="row">
					<div class="logo col-lg-3 col-md-3 col-sm-3 col-xs-12">
						<a href="https://www.purdue.edu/">
							<img alt="Purdue University" src="./Course Listing - Office of the Provost - Purdue University_files/PU-H.svg">
						</a>
					</div>
					<div class="department col-lg-9 col-md-9 col-sm-9 col-xs-12">
						<a href="https://www.purdue.edu/provost/index.html">
							Office of the Provost
						</a>
						<!--<system-region name="SITETAGLINE"/>-->
					</div>
				</div>
			</div>
		</div>
		<!-- End Top Section -->
		<!-- Begin Main Navigation -->
		<div class="navbar navbar-inverse blackbar" role="navigation">
			<div class="container">
				<div class="navbar navbar-inverse blackbar" role="navigation" style="box-shadow: none;">
<div class="container">
<div class="navbar-header"><button class="navbar-toggle" data-target=".black" data-toggle="collapse" type="button"> <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span> Menu </button></div>
<div class="collapse navbar-collapse black">
<ul class="nav navbar-nav" style="width: 100%;">
<li><a class="dropdown-toggle" data-toggle="dropdown" href="https://www.purdue.edu/provost/students/s-initiatives/curriculum/courses.html#">Home <span class="caret"></span> </a>
<ul class="dropdown-menu">
<li><a href="https://www.purdue.edu/provost/index.html">Provost Home</a></li>
<li><a href="https://www.purdue.edu/provost/index.html#wolfe">Meet the Provost</a></li>
<li><a href="https://www.purdue.edu/provost/about/directory.html">Directory</a></li>
<li><a href="https://www.purdue.edu/provost/about/former.html">Former Provosts</a></li>
<li><a href="https://www.purdue.edu/provost/about/speechRequest.php">Speech Request Form</a></li>
<li><a href="https://www.purdue.edu/provost/about/provostInitiatives/strategic/index.html">Strategic Initatives</a></li>
</ul>
</li>
<li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" href="https://www.purdue.edu/provost/students/s-initiatives/curriculum/courses.html#">Vice Provost Areas <span class="caret"></span> </a>
<ul class="dropdown-menu">
<li><a href="https://www.purdue.edu/provost/about/provostInitiatives/classroom/index.php">Academic Facilities</a></li>
<li><a href="https://www.purdue.edu/diversity-inclusion/" rel="noopener" target="_blank">Diversity, Inclusion &amp; Belonging</a></li>
<li><a href="https://www.purdue.edu/enrollmentmanagement/" rel="noopener" target="_blank">Enrollment Management</a></li>
<li><a href="https://www.purdue.edu/provost/faculty/index.html">Faculty Affairs</a></li>
<li><a href="https://www.purdue.edu/campuses/indianapolis/" rel="noopener" target="_blank">Purdue University in Indianapolis</a></li>
<li><a href="https://www.purdue.edu/vpsl/" rel="noopener" target="_blank">Student Life</a></li>
<li><a href="https://www.purdue.edu/provost/teachinglearning/index.html">Teaching &amp; Learning</a></li>
</ul>
</li>
<li><a href="https://www.purdue.edu/provost/events/index.html" rel="noopener" target="_blank">Events</a></li>
<li><a href="https://www.purdue.edu/newsroom/purduetoday/" rel="noopener" target="_blank">News</a></li>
</ul>
</div>
<!--/.nav-collapse --></div>
</div>
<script>// <![CDATA[
function openDropdown(elem){
        elem.parentNode.classList.toggle('open')
    }
// ]]></script>
			</div>
		</div>
		<!-- End Main Navigation -->
		<!-- Begin Breadcrumbs -->
		<div class="breadcrumb">
			<div class="container">
				<div class="row">
					<div id="breadcrumbs"><ol class="col-lg-12 col-md-12 col-sm-12"><li>Students</li><li>Student Initiatives</li><li><a href="https://www.purdue.edu/provost/students/s-initiatives/curriculum/index.html">Curriculum</a></li></ol></div>
				</div>
			</div>
		</div>
		<!-- End BreadCrumbs -->
		<!-- Begin Main Content -->
		<div class="content">
			<div class="container">
				<div class="row">
					<div class="maincontent col-lg-9 col-md-9 col-sm-9 col-xs-12 right">
						
    
						
						
    <h1>Course Listing</h1>
    		<p><strong>Below is also a complete listing of approved Purdue West Lafayette courses that may be used for meeting foundational learning outcomes.&nbsp; <strong>Some courses may have start terms (e.g. Fall 2013 and after only) or end terms (e.g. Fall 2019 and earlier only). Courses taken outside the noted terms do not meet the outcome.</strong> </strong></p>
<p><strong>An Excel spreadsheet of all approved courses (courses taken at Purdue campuses and&nbsp;other Indiana institutions as well as transfer courses) may also be found <a href="https://www.purdue.edu/provost/students/s-initiatives/curriculum/UCC-Master-Course-List-PWL-Transfer.xlsx" rel="noopener" target="_blank">here</a>. <a href="https://www.purdue.edu/provost/students/s-initiatives/curriculum/documents/UCC_Master_Course_List_current.xlsx"></a> </strong></p>
<div class="panel show"></div>
<div class="row" id="controller-row">
<div id="controller" style="position: relative;"><!-- class="col-md-6 col-xs-12 left     --> <button class="btn btn-default" id="expand-button">Expand All Categories</button> <button class="btn btn-default" id="collapse-button">Collapse All Categories</button>
<div class="cool_find_menu" id="cool_find_menu" style="display: inline-block;"><form onsubmit="return false;" style="display: inline;"><input class="cool_find_input" id="cool_find_text" onchange="coolfind.resettext();" placeholder="Enter name to find" type="text"></form>
<div style="display: inline-block;"><span id="cool_find_msg"></span> <button class="cool_find_btn btn btn-default" oncltick="coolfind.findprev();" title="Find Previous">▲</button> <button class="cool_find_btn btn btn-default" id="cool_find_next" onclick="coolfind.findit();" title="Find Next">▼</button></div>
</div>
</div>
</div>
<button class="accordion  active">Human Cultures: Behavioral/Social Sciences (BSS)</button>
<div class="panel show">
<p class="courseSearch">AD 33900 Women Artists In The 20th Century <strong>(Fall 2021 and after only)</strong></p>
<p class="courseSearch">AGEC 20300 Intro to Microeconomics for Food and Agribusiness</p>
<p class="courseSearch">AGEC 20400 Intro to Resource Economics and Environmental Policy</p>
<p class="courseSearch">AGEC 21700 Economics</p>
<p class="courseSearch">AGEC 25000 The Economic Geography of World Food and Resources</p>
<p class="courseSearch">AGR 20100 Communications Across Cultures <strong>(Fall 2013 and after only)</strong></p>
<p class="courseSearch">AMST 21000 Sport in American Culture</p>
<p class="courseSearch">ANTH 10000 Intro to Anthropology</p>
<p class="courseSearch">ANTH 20100 Intro to Archaeological and World Prehistory</p>
<p class="courseSearch">ANTH 20300 Biological Basis of Human Social Behavior</p>
<p class="courseSearch">ANTH 20500 Human Cultural Diversity</p>
<p class="courseSearch">ANTH 23000 Gender Across Cultures</p>
<p class="courseSearch">ANTH 37900 Native American Culture</p>
<p class="courseSearch">CLCS 18100 Classical World Civilizations</p>
<p class="courseSearch">COM 21200 Approaches to the study of interpersonal communication</p>
<p class="courseSearch">COM 22400 Communicating in the Global Workplace</p>
<p class="courseSearch">ECON 21000 Principles of Economics</p>
<p class="courseSearch">ECON 25100 Microeconomics</p>
<p class="courseSearch">ECON 25200 Macroeconomics</p>
<p class="courseSearch">ECON 51400 Microeconomic Theory <strong>(Summer 2021 and earlier only)</strong></p>
<p class="courseSearch">EDCI 28500 Multiculturalism in Education</p>
<p class="courseSearch">EDPS 23500 Learning and Motivation</p>
<p class="courseSearch">EDPS 26500 The Inclusive Classroom <strong>(Summer 2020 and earlier only)</strong></p>
<p class="courseSearch">EDPS 31600 Collaborative Leadership: Cross-Cultural Settings</p>
<p class="courseSearch">EDST 20010 Educational Policies And Laws <strong>(Summer 2020 and earlier only)</strong></p>
<p class="courseSearch">EDST 24800 Contemporary Issues in American Schools&nbsp;<strong>(Spring 2024 and earlier only)</strong></p>
<p class="courseSearch">ENGL 22700 Intro to Linguistics</p>
<p class="courseSearch">ENGL 22800 Language and Social Identity&nbsp; <strong>(Spring 2021 and earlier only)</strong></p>
<p class="courseSearch">HDFS 20100 Introduction to Family Processes</p>
<p class="courseSearch">HDFS 21000 Intro to Human Development</p>
<p class="courseSearch">HDFS 28000 Diversity in Individual and Family Life</p>
<p class="courseSearch">HONR 22100 Exploring Place</p>
<p class="courseSearch">HONR 31400 The Human Epoch</p>
<p class="courseSearch">HTM 37200 Global Tourism Geography</p>
<p class="courseSearch">LC 26100 Introduction to the Linguistic Study of Foreign Languages</p>
<p class="courseSearch">LING 20100 Intro to Linguistics</p>
<p class="courseSearch">POL 10100 American Government and Politics</p>
<p class="courseSearch">POL 12000 Introduction to Public Policy</p>
<p class="courseSearch">POL 13000 Introduction to International Relations</p>
<p class="courseSearch">POL 14100 Governments of the World</p>
<p class="courseSearch">POL 22200 Women, Politics, and Policy</p>
<p class="courseSearch">POL 22300 Introduction to Environmental Policy</p>
<p class="courseSearch">POL 23000 Introduction to the Study of Peace&nbsp; <strong>(Summer 2021 and earlier only)</strong></p>
<p class="courseSearch">POL 23100 Introduction to U. S. Foreign Policy</p>
<p class="courseSearch">POL 23500 International Relations Among Rich and Poor Nations</p>
<p class="courseSearch">POL 32600 Black Political Participation in America</p>
<p class="courseSearch">POL 32700 Global Green Politics</p>
<p class="courseSearch">POL 33500 China and the Challenge of Globalization</p>
<p class="courseSearch">POL 36000 Women and the Law</p>
<p class="courseSearch">POL 37200 Indiana Government &amp; Politics</p>
<p class="courseSearch">PSY 12000 Elementary Psychology</p>
<p class="courseSearch">PSY 12300 Beyond Mental Health: The Science of Well-Being <strong>(Fall 2022 and after only)</strong></p>
<p class="courseSearch">SCLA 20000 Cornerstones in Constitutional Law</p>
<p class="courseSearch">SLHS 22700 Intro to Linguistics</p>
<p class="courseSearch">SOC 10000 Intro to Sociology</p>
<p class="courseSearch">SOC 22000 Social Problems</p>
<p class="courseSearch">SOC 27500 Social Gerontology</p>
<p class="courseSearch">SOC 32600 Social Conflict and Criminal Justice</p>
<p class="courseSearch">SOC 34400 Environmental Sociology <strong>(Fall 2021 and after only)</strong></p>
<p class="courseSearch">SOC 35200 Drugs, Culture, and Society</p>
<p class="courseSearch">SOC 37400 Medical Sociology <strong>(Fall 2021 and after only)</strong></p>
<p class="courseSearch">SOC 42900 Sociology of Protest <strong>(Fall 2021 and after only)</strong></p>
<p class="courseSearch">WGSS 28000 Intro to Women’s Studies</p>
<p class="courseSearch">WGSS 28200 Introduction to LGBT Studies</p>
<p class="courseSearch">WGSS 38000 Gender and Multiculturalism</p>
</div>
<button class="accordion  active">Human Cultures: Humanities (HUM)</button>
<div class="panel  show">
<p class="courseSearch">AAS 27100 Intro to African American Studies</p>
<p class="courseSearch">AD 11300 Basic Drawings</p>
<p class="courseSearch">AD 11700 Photography I</p>
<p class="courseSearch">AD 12500 Intro to Interior Design</p>
<p class="courseSearch">AD 22600 History of Art to 1400</p>
<p class="courseSearch">AD 22700 History of Art since 1400</p>
<p class="courseSearch">AD 24200 Ceramics I</p>
<p class="courseSearch">AD 25100 History of Photography</p>
<p class="courseSearch">AD 25500 Art Appreciation</p>
<p class="courseSearch">AD 26500 Relief Printmaking</p>
<p class="courseSearch">AD 26600 Silkscreen Printmaking</p>
<p class="courseSearch">AD 27500 Beginning Sculpture</p>
<p class="courseSearch">AD 38300 Modern Art</p>
<p class="courseSearch">AD 38400 Contemporary Art</p>
<p class="courseSearch">AMST 20100 Intro to American Studies</p>
<p class="courseSearch">AMST 22000&nbsp;Technology And Play</p>
<p class="courseSearch">AMST 25000 Introduction to American Protest Movements</p>
<p class="courseSearch">AMST 31000 Invention, Innovation, Design</p>
<p class="courseSearch">AMST 32500 Sports, Technology and Innovation</p>
<p class="courseSearch">ANSC 33100 The Role of Horses in Human History, Culture and Society <strong>(Summer 2022 and after only)</strong></p>
<p class="courseSearch">ARAB 10100 Standard Arabic Level I</p>
<p class="courseSearch">ARAB 10200 Standard Arabic Level II</p>
<p class="courseSearch">ARAB 20100 Standard Arabic Level III</p>
<p class="courseSearch">ARAB 20200 Standard Arabic Level IV</p>
<p class="courseSearch">ARAB 23900 Arab Women Writers <strong>(Spring 2022 and after only)</strong></p>
<p class="courseSearch">ARAB 28000 Arabic Culture</p>
<p class="courseSearch">ARAB 30100 Standard Arabic Level V</p>
<p class="courseSearch">ARAB 30200 Standard Arabic Level VI</p>
<p class="courseSearch">ASAM 24000 Intro to Asian American Studies</p>
<p class="courseSearch">ASEC 30100 Building Intercultural Partnerships <strong>(Spring 2022 and after only)</strong></p>
<p class="courseSearch">ASEC 33100 The Role of Horses in Human History, Culture and Society</p>
<p class="courseSearch">ASEC 35500 Controversial Science and Media in the Public Sphere</p>
<p class="courseSearch">ASL 10100 American Sign Language I</p>
<p class="courseSearch">ASL 10200 American Sign Language II</p>
<p class="courseSearch">ASL 20100 American Sign Language III</p>
<p class="courseSearch">ASL 20200 American Sign Language IV</p>
<p class="courseSearch">CEM 35100&nbsp;Foundations Of Architectural Design</p>
<p class="courseSearch">CHNS 10100 Chinese Level I</p>
<p class="courseSearch">CHNS 10200 Chinese Level II</p>
<p class="courseSearch">CHNS 20100 Chinese Level III</p>
<p class="courseSearch">CHNS 20200 Chinese Level IV</p>
<p class="courseSearch">CHNS 24100 Introduction to the Study of Chinese Literature</p>
<p class="courseSearch">CHNS 28000 Topics in Chinese Civilization and Culture</p>
<p class="courseSearch">CHNS 30100 Chinese Level V</p>
<p class="courseSearch">CHNS 30200 Chinese Level VI</p>
<p class="courseSearch">CHNS 33000 Introduction to Chinese Cinema</p>
<p class="courseSearch">CHNS 40100 Chinese Level VII</p>
<p class="courseSearch">CHNS 40200 Chinese Level VII</p>
<p class="courseSearch">CLCS 23010 Survey of Greek Literature in Translation</p>
<p class="courseSearch">CLCS 23100 Survey of Latin Literature <strong> <br> </strong></p>
<p class="courseSearch">CLCS 23200 Classical Roots of English Words</p>
<p class="courseSearch">CLCS 23300 Comparative Mythology</p>
<p class="courseSearch">CLCS 23500 Classical Mythology</p>
<p class="courseSearch">CLCS 23700 Gender &amp; Sexuality in Greek &amp; Roman Antiquity</p>
<p class="courseSearch">CLCS 23800 The Tragic Vision</p>
<p class="courseSearch">CLCS 23900 The Comic Vision</p>
<p class="courseSearch">CLCS 33900 Literature and the Law <strong>(Spring 2024 and earlier only)<br> </strong></p>
<p class="courseSearch">CLCS 38000 Alexander the Great &amp; Hellenistic World</p>
<p class="courseSearch">CLCS 38500 Science, Medicine, and Magic In The Ancient West <strong>(Fall 2022 and after only)</strong></p>
<p class="courseSearch">CMPL 26600 Intro to World Lit Beg - 1600</p>
<p class="courseSearch">CMPL 26700 World Lit from 1700 to the present</p>
<p class="courseSearch">DANC 25000 Dance Appreciation&nbsp; <strong>(Spring 2024 and earlier only)</strong></p>
<p class="courseSearch">DANC 37800 Survey of Concert Dance History <strong>(Fall 2021 and after only)</strong></p>
<p class="courseSearch">EDST 20000 History &amp; Philosophy of Education</p>
<p class="courseSearch">ENGL 11000 American Language And Culture For International Students I</p>
<p class="courseSearch">ENGL 20200 Engaging English</p>
<p class="courseSearch">ENGL 21700 Figures Of Myth And Legend I: Monsters</p>
<p class="courseSearch">ENGL 21800 Figures Of Myth And Legends II: Heroes And Villains</p>
<p class="courseSearch">ENGL 21900 Figures of Myth and Legend III</p>
<p class="courseSearch">ENGL 22500 Literature, Inequality, and Injustice</p>
<p class="courseSearch">ENGL 23000 Great Narrative Works</p>
<p class="courseSearch">ENGL 23700 Introduction to Poetry</p>
<p class="courseSearch">ENGL 23800 Intro to Fiction</p>
<p class="courseSearch">ENGL 24000 Survey Of The British Literature: From The Beginnings Through The Neoclassical Period</p>
<p class="courseSearch">ENGL 24100 Survey Of The British Literature: From The Rise Of Romanticism To The Modern Period</p>
<p class="courseSearch">ENGL 25000 Great American Books</p>
<p class="courseSearch">ENGL 26400 The Bible as Literature</p>
<p class="courseSearch">ENGL 26600 World Literature: From the Beginnings to 1700 A.D.</p>
<p class="courseSearch">ENGL 26700 World Lit from 1700 to the present</p>
<p class="courseSearch">ENGL 27600 Shakespeare on Film</p>
<p class="courseSearch">ENGL 28600 The Movies</p>
<p class="courseSearch">ENGL 32200 Word, Image, Media</p>
<p class="courseSearch">ENGL 35000 Survey Of American Literature From Its Beginnings To 1865</p>
<p class="courseSearch">ENGL 35100 Survey Of American Literature From 1865 To The Post-World War II Period</p>
<p class="courseSearch">ENGL 36000 Gender and Literature</p>
<p class="courseSearch">ENGL 36500 Literature and Imperialism</p>
<p class="courseSearch">ENGL 36700 Mystery and Detective Fiction</p>
<p class="courseSearch">ENGL 37300 Science Fiction and Fantasy</p>
<p class="courseSearch">ENGL 38100 The British Novel</p>
<p class="courseSearch">ENGL 38200 The American Novel</p>
<p class="courseSearch">ENGL 38900 Literature for Children</p>
<p class="courseSearch">FR 10100 French Level I</p>
<p class="courseSearch">FR 10200 French Level II</p>
<p class="courseSearch">FR 10500 Accelerated Basic French <strong>(Summer 2020 and after only)</strong></p>
<p class="courseSearch">FR 20100 French Level III</p>
<p class="courseSearch">FR 20200 French Level IV</p>
<p class="courseSearch">FR 20500 Accelerated Intermediate French <strong>(Summer 2020 and after only)</strong></p>
<p class="courseSearch">FR 30100 French Level V</p>
<p class="courseSearch">FR 30200 French Level VI</p>
<p class="courseSearch">FR 33000 French Cinema</p>
<p class="courseSearch">FR 40100 French Level VII</p>
<p class="courseSearch">FR 40200 French Level VIII</p>
<p class="courseSearch">GER 10100 German Level I</p>
<p class="courseSearch">GER 10200 German Level II</p>
<p class="courseSearch">GER 10500 Accelerated Basic German <strong>(Summer 2020 and after only)</strong></p>
<p class="courseSearch">GER 20100 German Level III</p>
<p class="courseSearch">GER 20200 German Level IV</p>
<p class="courseSearch">GER 20500 Accelerated Intermediate German <strong>(Summer 2020 and after only)</strong></p>
<p class="courseSearch">GER 23000 German Literature in Translation</p>
<p class="courseSearch">GER 30100 German Level V</p>
<p class="courseSearch">GER 30200 German Level VI</p>
<p class="courseSearch">GER 33000 German Cinema</p>
<p class="courseSearch">GER 40100 German Level VII</p>
<p class="courseSearch">GER 40200 German Level VIII</p>
<p class="courseSearch">GREK 10100 Ancient Greek Level I</p>
<p class="courseSearch">GREK 10200 Ancient Greek Level II</p>
<p class="courseSearch">GREK 20100 Ancient Greek Level III</p>
<p class="courseSearch">GREK 20200 Ancient Greek Level IV</p>
<p class="courseSearch">GS 10000 American Language And Culture For International Students I&nbsp; <strong>(Fall 2015 and after only)</strong></p>
<p class="courseSearch">GSLA 30100 Theories of Global Studies</p>
<p class="courseSearch">HEBR 10100 Modern Hebrew Level I</p>
<p class="courseSearch">HEBR 10200 Modern Hebrew Level II</p>
<p class="courseSearch">HEBR 12100 Biblical Hebrew Level I</p>
<p class="courseSearch">HEBR 12200 Biblical Hebrew Level II</p>
<p class="courseSearch">HEBR 20100 Modern Hebrew Level III</p>
<p class="courseSearch">HEBR 20200 Modern Hebrew Level IV</p>
<p class="courseSearch">HEBR 22100 Biblical Hebrew Level III</p>
<p class="courseSearch">HEBR 22200 Biblical Hebrew Level IV</p>
<p class="courseSearch">HEBR 28000 Modern Israel</p>
<p class="courseSearch">HEBR 38000 Israel and the Modern World&nbsp; <strong>(Spring 2014 and after only)</strong></p>
<p class="courseSearch">HIST 10300 Intro to the Medieval World</p>
<p class="courseSearch">HIST 10400 Intro to the Modern World</p>
<p class="courseSearch">HIST 10500 Survey of Global World</p>
<p class="courseSearch">HIST 15100 American History to 1877</p>
<p class="courseSearch">HIST 15200 United States since 1877</p>
<p class="courseSearch">HIST 21000 The Making of Modern Africa</p>
<p class="courseSearch">HIST 21100 The Global Field:&nbsp;World Soccer and Global History</p>
<p class="courseSearch">HIST 23800 History of Russia from Medieval times to 1861</p>
<p class="courseSearch">HIST 23900 History of Russia from 1861 to the Present</p>
<p class="courseSearch">HIST 24000 East Asia and Its Historic Tradition</p>
<p class="courseSearch">HIST 24100 East Asia in the Modern World</p>
<p class="courseSearch">HIST 24300 South Asian History and Civilizations</p>
<p class="courseSearch">HIST 24500 Middle East History and Culture</p>
<p class="courseSearch">HIST 24600 Modern Middle East and North Africa</p>
<p class="courseSearch">HIST 25000 U. S. Relations with the Middle East &amp; No. Africa</p>
<p class="courseSearch">HIST 27100 Latin American History to 1824</p>
<p class="courseSearch">HIST 27200 Latin American History from 1824</p>
<p class="courseSearch">HIST 30000 Eve Of Destruction: Global Crises And World Organization In The 20th Century</p>
<p class="courseSearch">HIST 30305 Food in Modern America</p>
<p class="courseSearch">HIST 30400 America in the 1960s</p>
<p class="courseSearch">HIST 30505 The U. S. in the World 1898-present</p>
<p class="courseSearch">HIST 30605 Technology and War in U.S. History</p>
<p class="courseSearch">HIST 31005 The Civil War and Reconstruction, 1850-1877</p>
<p class="courseSearch">HIST 31305 Medical Devices and Innovation</p>
<p class="courseSearch">HIST 31405 Science, Technology, Engineering And Mathematics (STEM) And Gender</p>
<p class="courseSearch">HIST 31505 American Beauty</p>
<p class="courseSearch">HIST 32300 German History</p>
<p class="courseSearch">HIST 32400 Modern France</p>
<p class="courseSearch">HIST 32900 History of Women in Modern Europe</p>
<p class="courseSearch">HIST 33205 The Nuclear Age</p>
<p class="courseSearch">HIST 33300 Science &amp; Society in Western Civilization I</p>
<p class="courseSearch">HIST 33400 Science &amp; Society in Western Civilization II</p>
<p class="courseSearch">HIST 33805 History of Human Rights</p>
<p class="courseSearch">HIST 34000 Modern China</p>
<p class="courseSearch">HIST 34100 History Of Africa South Of The Sahara</p>
<p class="courseSearch">HIST 34300 Traditional Japan</p>
<p class="courseSearch">HIST 34400 History of Modern Japan</p>
<p class="courseSearch">HIST 34901 The First World War</p>
<p class="courseSearch">HIST 35000 Science &amp; Society in the Twentieth Century World</p>
<p class="courseSearch">HIST 35100 The Second World War</p>
<p class="courseSearch">HIST 35205 Death, Disease and Medicine in Twentieth-Century American History</p>
<p class="courseSearch">HIST 35400 Women in America to 1870</p>
<p class="courseSearch">HIST 35500 History of American Military Affairs</p>
<p class="courseSearch">HIST 35900 Gender in East Asian History</p>
<p class="courseSearch">HIST 36305 The History of Medicine and Public Health</p>
<p class="courseSearch">HIST 37100 Society, Culture, and Rock and Roll</p>
<p class="courseSearch">HIST 37500 Women in America since 1870</p>
<p class="courseSearch">HIST 37700 History and Culture of Native America</p>
<p class="courseSearch">HIST 38001 History of U. S. Agriculture</p>
<p class="courseSearch">HIST 38200 American Constitutional History</p>
<p class="courseSearch">HIST 38300 Recent American Constitutional History</p>
<p class="courseSearch">HIST 38400 History of Aviation</p>
<p class="courseSearch">HIST 38505 Media, Politics and Popular Culture</p>
<p class="courseSearch">HIST 38700 History of the Space Age</p>
<p class="courseSearch">HIST 39400 Environmental History of the United States</p>
<p class="courseSearch">HIST 39600 The Afro-American to 1865</p>
<p class="courseSearch">HIST 39800 The Afro-American since 1865</p>
<p class="courseSearch">HIST 41005 History of the American Presidency</p>
<p class="courseSearch">HIST 47005 Women and Health in America</p>
<p class="courseSearch">HONR 31500&nbsp;Across Differences</p>
<p class="courseSearch">ITAL 10100 Italian Level I</p>
<p class="courseSearch">ITAL 10200 Italian Level II</p>
<p class="courseSearch">ITAL 10500 Accelerated Basic Italian</p>
<p class="courseSearch">ITAL 20100 Italian Level III</p>
<p class="courseSearch">ITAL 20200 Italian Level IV</p>
<p class="courseSearch">ITAL 20500 Accelerated Intermediate Italian</p>
<p class="courseSearch">ITAL 28000 Italian Culture &amp; Civilization</p>
<p class="courseSearch">ITAL 28100 The Italian Renaissance</p>
<p class="courseSearch">ITAL 30100 Italian Level V</p>
<p class="courseSearch">ITAL 30200 Italian Level VI</p>
<p class="courseSearch">ITAL 33000 Italian Cinema</p>
<p class="courseSearch">ITAL 33300 The Spirit of Italian Comedy</p>
<p class="courseSearch">ITAL 38000 Italian Culture &amp; Civilization</p>
<p class="courseSearch">JPNS 10100 Japanese Level I</p>
<p class="courseSearch">JPNS 10200 Japanese Level II</p>
<p class="courseSearch">JPNS 20100 Japanese Level III</p>
<p class="courseSearch">JPNS 20200 Japanese Level IV</p>
<p class="courseSearch">JPNS 30100 Japanese Level V</p>
<p class="courseSearch">JPNS 30200 Japanese Level VI</p>
<p class="courseSearch">JPNS 40100 Japanese Level VII</p>
<p class="courseSearch">JPNS 40200 Japanese Level VIII</p>
<p class="courseSearch">JWST 33000 Introduction to Jewish Studies</p>
<p class="courseSearch">KOR 10100&nbsp; Korean Level I</p>
<p class="courseSearch">LATN 10100 Latin Level I</p>
<p class="courseSearch">LATN 10200 Latin Level II</p>
<p class="courseSearch">LATN 20100 Latin Level III</p>
<p class="courseSearch">LATN 20200 Latin Level IV</p>
<p class="courseSearch">LATN 34300 Roman Oratory</p>
<p class="courseSearch">LATN 34400 Roman Epic</p>
<p class="courseSearch">LATN 34500 Roman Elegy</p>
<p class="courseSearch">LATN 34600 Roman Rhetoric</p>
<p class="courseSearch">LATN 34700 Roman Comedy</p>
<p class="courseSearch">LATN 44200 Roman Lyric Poetry</p>
<p class="courseSearch">LATN 44300 Roman Satire</p>
<p class="courseSearch">LATN 44400 Roman Philosophers</p>
<p class="courseSearch">LATN 44500 Roman Encyclopedists</p>
<p class="courseSearch">LATN 44600 Roman Historians</p>
<p class="courseSearch">LC 33200&nbsp;Global Horror Cinema</p>
<p class="courseSearch">LC 23900 Contemp. Foreign Women Writers in Translation</p>
<p class="courseSearch">LC 28100&nbsp;Intro To World Food Cultures</p>
<p class="courseSearch">LC 33300 The Middle Ages on Film</p>
<p class="courseSearch">MUS 11200 Fundamentals of Music <strong>(Fall 2022 and after only)</strong></p>
<p class="courseSearch">MUS 13200 Music Theory I <strong>(Fall 2022 and after only)</strong></p>
<p class="courseSearch">MUS 25000 Music Appreciation</p>
<p class="courseSearch">MUS 26100 Fundamentals of Music <strong>(Summer 2022 and before only)</strong></p>
<p class="courseSearch">MUS 36100 Music Theory I <strong>(Summer 2022 and before only)</strong></p>
<p class="courseSearch">MUS 37600 World Music</p>
<p class="courseSearch">MUS 37800 Jazz History</p>
<p class="courseSearch">PHIL 11000 Introduction to Philosophy</p>
<p class="courseSearch">PHIL 11005 I Play, Therefore I Am&nbsp;</p>
<p class="courseSearch">PHIL 11100 Ethics</p>
<p class="courseSearch">PHIL 11400 Global Moral Issues</p>
<p class="courseSearch">PHIL 20600 Philosophy of Religion</p>
<p class="courseSearch">PHIL 21900 Introduction to Existentialism</p>
<p class="courseSearch">PHIL 22300 Fate and Free Will</p>
<p class="courseSearch">PHIL 22500 Philosophy and Gender</p>
<p class="courseSearch">PHIL 23000 Religions of the East</p>
<p class="courseSearch">PHIL 23100 Religions of the West</p>
<p class="courseSearch">PHIL 24000 Social and Political Philosophy</p>
<p class="courseSearch">PHIL 24200 Philosophy, Culture, and the African-American Experience</p>
<p class="courseSearch">PHIL 27500 Philosophy of Art</p>
<p class="courseSearch">PHIL 28000 Ethics and Animals</p>
<p class="courseSearch">PHIL 29000 Environmental Ethics</p>
<p class="courseSearch">PHIL 30100 History of Ancient Philosophy</p>
<p class="courseSearch">PHIL 30200 History of Medieval Philosophy</p>
<p class="courseSearch">PHIL 30300 History of Modern Philosophy</p>
<p class="courseSearch">PHIL 30400 19th Century Philosophy</p>
<p class="courseSearch">PHIL 41100 Modern Ethical Theory</p>
<p class="courseSearch">PHIL 42400 Recent Ethical Theory</p>
<p class="courseSearch">PTGS 10100 Portuguese Level I</p>
<p class="courseSearch">PTGS 10200 Portuguese Level II</p>
<p class="courseSearch">PTGS 10500 Accelerated Portuguese</p>
<p class="courseSearch">PTGS 20100 Portuguese Level III</p>
<p class="courseSearch">PTGS 20200 Portuguese Level IV</p>
<p class="courseSearch">PTGS 30100 &nbsp;Portuguese Level V</p>
<p class="courseSearch">PTGS 30200 &nbsp;Portuguese Level VI</p>
<p class="courseSearch">REL 20000 Intro to study of religion</p>
<p class="courseSearch">REL 23000 Religions of the East</p>
<p class="courseSearch">REL 23100 Religions of the West</p>
<p class="courseSearch">REL 24000&nbsp;Engaging Religious Diversity</p>
<p class="courseSearch">RUSS 10100 Russian Level I</p>
<p class="courseSearch">RUSS 10200 Russian Level II</p>
<p class="courseSearch">RUSS 20100 Russian Level III</p>
<p class="courseSearch">RUSS 20200 Russian Level IV</p>
<p class="courseSearch">RUSS 28100 Post Soviet Experience</p>
<p class="courseSearch">RUSS 30100 Russian Level V</p>
<p class="courseSearch">RUSS 30200 Russian Level VI</p>
<p class="courseSearch">RUSS 33000 Russian and East European Cinema</p>
<p class="courseSearch">RUSS 40100 Russian Level VII</p>
<p class="courseSearch">RUSS 40200 Russian Level VIII</p>
<p class="courseSearch">SPAN 10100 Spanish Level I</p>
<p class="courseSearch">SPAN 10200 Spanish Level II</p>
<p class="courseSearch">SPAN 10500 Accelerated Basic Spanish <strong>(Summer 2020 and after only)</strong></p>
<p class="courseSearch">SPAN 20100 Spanish Level III</p>
<p class="courseSearch">SPAN 20200 Spanish Level IV</p>
<p class="courseSearch">SPAN 20500 Accelerated Intermediate Spanish <strong>(Summer 2020 and after only)</strong></p>
<p class="courseSearch">SPAN 23500 Spanish American Literature in Translation</p>
<p class="courseSearch">SPAN 30100 Spanish Level V</p>
<p class="courseSearch">SPAN 30200 Spanish Level VI</p>
<p class="courseSearch">SPAN 30500 Spanish For Heritage Speakers</p>
<p class="courseSearch">SPAN 30801 Advanced Spanish For Heritage Speakers</p>
<p class="courseSearch">SPAN 33000 Spanish And Latin American Cinema&nbsp;</p>
<p class="courseSearch">SPAN 40100 Spanish Level VII</p>
<p class="courseSearch">SPAN 40200 Spanish Level VIII</p>
<p class="courseSearch">THTR 20100 Theater Appreciation</p>
<p class="courseSearch">WGSS 28000 Intro to Women’s Studies</p>
<p class="courseSearch">YDAE 33100 The Role of Horses in Human History Culture and Society <strong>(Summer 2019 and before only. Effective Fall 2019, YDAE is now ASEC)</strong></p>
<p class="courseSearch">YDAE 35500 Controversial Science and Media in the Public Sphere <strong>(Summer 2019 and before only. Effective Fall 2019, YDAE is now ASEC)</strong></p>
</div>
<button class="accordion  active">Information Literacy (IL)</button>
<div class="panel  show">
<p class="courseSearch">AGR 20100 Communications Across Cultures&nbsp; <strong>(Fall 2013 and after only)</strong></p>
<p class="courseSearch">BIOL 11500 Biology Resource Seminar</p>
<p class="courseSearch">COM 25100 Intro to Electronic Mass Media</p>
<p class="courseSearch">COM 25100 Communication, Information and Society</p>
<p class="courseSearch">EDCI 27000 Intro to Educational Technology&nbsp; <strong>(Fall 2013 and after only)</strong></p>
<p class="courseSearch">EDPS 10500 Academic and Career Planning&nbsp; <strong>(Fall 2013 and after only)</strong></p>
<p class="courseSearch">ENGL 10600 First Year Composition</p>
<p class="courseSearch">ENGL 10800 Accelerated First Year Composition</p>
<p class="courseSearch">ENGL 30400 Advanced Composition <strong>(Fall 2021 and after only)</strong></p>
<p class="courseSearch">ENGL 38000 Issues in Rhetoric and Public Life <strong>(Fall 2021 and after only)</strong></p>
<p class="courseSearch">ENGR 13000 Transforming Ideas Into Innovations</p>
<p class="courseSearch">ENGR 13100 Transforming Ideas to Innovation I</p>
<p class="courseSearch">ENGR 13300 Transforming Ideas to Innovation – EPICS</p>
<p class="courseSearch">ENGR 14100 Honors Creativity &amp; Innovation in Engineering Design I</p>
<p class="courseSearch">*ENGR 16100 Honors Introduction to Innovation and the Physical Science of Engineering Design I (Both ENGR 16100 <strong>AND</strong> 16200 are required to meet <strong> the IL requirement) </strong></p>
<p class="courseSearch">*ENGR 16200 Honors Introduction to Innovation and the Physical Science of Engineering Design II (Both ENGR 16100 <strong>AND</strong> 16200 are required to meet <strong> the IL requirement) </strong></p>
<p class="courseSearch">HONR 19903 Interdisciplinary Approaches to Writing</p>
<p class="courseSearch">ILS 17500 Information Strategies For Hospitality &amp; Tourism Management <strong>(Spring 2021 and after only)</strong></p>
<p class="courseSearch">MGMT 17500 Information Strategies for Management Students</p>
<p class="courseSearch">NUR 22301 Foundations of Research and Evidence-based Practice&nbsp; <strong>(Fall 2013 and after only)</strong> <strong> <br> </strong></p>
<p class="courseSearch">PHIL 12000 Critical Thinking</p>
<p class="courseSearch">PHIL 26000 Philosophy &amp; Law&nbsp; <strong>(Summer 2023 and earlier only)</strong></p>
<p class="courseSearch">POL 30000 Introduction to Political Analysis</p>
<p class="courseSearch">PSY 10000 Intro to the Science and Fields of Psychology</p>
<p class="courseSearch">SCLA 10100 Transformative Texts: Critical Thinking &amp; Communication I: Antiquity to Modernity</p>
<p class="courseSearch">SLHS 13000&nbsp;Perception, Action, And Cognition In The Speech, Language, And Hearing Sciences</p>
<p class="courseSearch">STAT 11300 Statistics and Society</p>
<p class="courseSearch">STAT 30100 Elementary Statistical Methods</p>
<p class="courseSearch">TECH 12000 Technology and the Individual&nbsp; <strong>(Fall 2013 and after only)</strong></p>
</div>
<button class="accordion  active">Oral Communication (OC)</button>
<div class="panel  show">
<p class="courseSearch">COM 11400 Fundamentals of Speech Communication</p>
<p class="courseSearch">COM 21700 Science Writing and Presentations</p>
<p class="courseSearch">EDCI 49600 Student Teaching in the Elementary School <strong> (Fall 2021 and after only)</strong></p>
<p class="courseSearch">EDCI 49800 Supervised Teaching <strong> (Fall 2021 and after only)</strong></p>
<p class="courseSearch">EDPS 31500 Collaborative Leadership: Interpersonal Skills&nbsp; <strong>(Fall 2013 and after only)</strong></p>
<p class="courseSearch">EDPS 49800 Supervised Teaching- Special Education <strong> (Fall 2021 and after only)</strong></p>
<p class="courseSearch">HDFS 45000 Supervised Teaching in Inclusive Programs for Young Children <strong> (Fall 2021 and after only)</strong></p>
<p class="courseSearch">SCLA 10200 Transformative Texts: Critical Thinking &amp; Communication II: Modern World</p>
</div>
<button class="accordion  active">Quantitative Reasoning (QR)</button>
<div class="panel  show">
<p class="courseSearch">EDCI 22200 Knowing the World Through Mathematics <strong>(Fall 2020 and after only)</strong></p>
<p class="courseSearch">MA 13800 Mathematics for Elementary Teachers II&nbsp; <strong>(Fall 2013 and after only)</strong></p>
<p class="courseSearch">MA 15300 Algebra and Trigonometry I</p>
<p class="courseSearch">MA 15400 Algebra and Trigonometry II&nbsp; <strong>(Spring 2016 and earlier only)</strong></p>
<p class="courseSearch">MA 15555 Quantitative Reasoning</p>
<p class="courseSearch">MA 15800 Functions and Trigonometry</p>
<p class="courseSearch">MA 15910 Introduction to Calculus <strong>(2019 and earlier only)</strong></p>
<p class="courseSearch">MA 16010 Applied Calculus I</p>
<p class="courseSearch">MA 16020 Applied Calculus II</p>
<p class="courseSearch">MA 16100 Plane Analytic Geometry and Calculus I</p>
<p class="courseSearch">MA 16200 Plane Analytic Geometry and Calculus II</p>
<p class="courseSearch">MA 16500 Analytic Geometry and Calculus I</p>
<p class="courseSearch">MA 16600 Analytic Geometry and Calculus II</p>
<p class="courseSearch">MA 17300 Calculus and Analytic Geometry II</p>
<p class="courseSearch">MA 17400 Multivariable Calculus</p>
<p class="courseSearch">MA 18100 Honors Calculus I</p>
<p class="courseSearch">MA 18200 Honors Calculus II</p>
<p class="courseSearch">MA 19000 Quantitative Reasoning&nbsp;<strong>(Summer 2016 and earlier only)</strong></p>
<p class="courseSearch">MA 22000 Introduction to Calculus</p>
<p class="courseSearch">MA 22100 Calculus for Technology I</p>
<p class="courseSearch">MA 22200 Calculus for Technology II</p>
<p class="courseSearch">MA 22300 Introductory Analysis I</p>
<p class="courseSearch">MA 22400 Introductory Analysis II</p>
<p class="courseSearch">MA 23100 Calculus for the Life Sciences I</p>
<p class="courseSearch">MA 23200 Calculus for the Life Sciences II</p>
<p class="courseSearch">MA 26100 Multivariate Calculus</p>
<p class="courseSearch">MA 26200 Plane Analytic Geometry and Calculus II</p>
<p class="courseSearch">MA 26500 Linear Algebra</p>
<p class="courseSearch">MA 26600 Ordinary Differential Equations</p>
<p class="courseSearch">MA 27100 Several Variable Calculus</p>
<p class="courseSearch">MA 27101 Honors Multivariate Calculus</p>
<p class="courseSearch">MA 35100 Elementary Linear Algebra</p>
<p class="courseSearch">MA 36600 Ordinary Differential Equations</p>
<p class="courseSearch">PHIL 15000 Principles Of Logic</p>
</div>
<button class="accordion  active">Science (SCI)</button>
<div class="panel  show">
<p class="courseSearch">ANTH 20400 Intro to Bio Anthro and Human Evolution</p>
<p class="courseSearch">ASTR 26300 Descriptive Astronomy: The Solar System</p>
<p class="courseSearch">ASTR 26400 Descriptive Astronomy: Stars and Galaxies</p>
<p class="courseSearch">BIOL 11000 Fundamentals of Biology I</p>
<p class="courseSearch">BIOL 11100 Fundamentals of Biology II</p>
<p class="courseSearch">BIOL 11200 Fundamentals of Biology I</p>
<p class="courseSearch">BIOL 11300 Fundamentals of Biology II</p>
<p class="courseSearch">BIOL 12100 Biology I: Ecology, Diversity, &amp; Behavior</p>
<p class="courseSearch">BIOL 13100 Biology II: Dev, Structure &amp; Function of Organisms&nbsp; <strong>(Summer 2023 and earlier only)</strong></p>
<p class="courseSearch">BIOL 13500 First Year Biology Lab</p>
<p class="courseSearch">BIOL 14501 First year biol lab with neuro res project</p>
<p class="courseSearch">BIOL 14502 First year BIOL lab with Micro Res Project&nbsp;<strong>(Spring 2024 and earlier only)</strong></p>
<p class="courseSearch">BIOL 14600 Introduction to Biology</p>
<p class="courseSearch">BIOL 20100 Human Anatomy and Physiology</p>
<p class="courseSearch">BIOL 20200 Human Anatomy and Physiology</p>
<p class="courseSearch">BIOL 20300 Human Anatomy and Physiology</p>
<p class="courseSearch">BIOL 20400 Human Anatomy and Physiology</p>
<p class="courseSearch">BIOL 20500 Biology for Elementary School Teachers</p>
<p class="courseSearch">BIOL 20600 Biology for Elementary School Teachers</p>
<p class="courseSearch">BIOL 30200 Human Design: Anatomy and Physiology</p>
<p class="courseSearch">BTNY 11000 Intro to Plant Science</p>
<p class="courseSearch">CHM 11100 General Chemistry</p>
<p class="courseSearch">CHM 11200 General Chemistry</p>
<p class="courseSearch">CHM 11500 General Chemistry</p>
<p class="courseSearch">CHM 11600 General Chemistry</p>
<p class="courseSearch">CHM 12500 Introduction to Chemistry</p>
<p class="courseSearch">CHM 12600 Introduction to Chemistry II</p>
<p class="courseSearch">CHM 12901 General Chemistry with Biological focus</p>
<p class="courseSearch">CHM 13600 General Chemistry Honors</p>
<p class="courseSearch">CHM 20000 Fundamentals of Chemistry&nbsp; <strong>(Summer 2023 and earlier only)</strong></p>
<p class="courseSearch">EAPS 10200 Earth Science for Elementary Education&nbsp; <strong>(Fall 2021 and earlier only)</strong></p>
<p class="courseSearch">EAPS 10500 The Planets</p>
<p class="courseSearch">EAPS 10900 The Dynamic Earth&nbsp; <strong>(Summer 2023 and earlier only)</strong></p>
<p class="courseSearch">EAPS 11100 Physical Geology</p>
<p class="courseSearch">EAPS 11200 Earth Through Time</p>
<p class="courseSearch">EAPS 11600 Earthquakes and Volcanoes</p>
<p class="courseSearch">EAPS 11700 Introduction to Atmospheric Science</p>
<p class="courseSearch">EAPS 12900 Earth System Dynamics</p>
<p class="courseSearch">EAPS 13800 Thunderstorms &amp; Tornadoes</p>
<p class="courseSearch">EAPS 22100 Survey of Atmospheric Science</p>
<p class="courseSearch">EAPS 22500 Science of the Atmosphere</p>
<p class="courseSearch">EAPS 24300 Earth Materials I&nbsp; <strong>(Summer 2023 and earlier only)</strong></p>
<p class="courseSearch">EAPS 24400 Earth Materials II&nbsp; <strong>(Summer 2023 and earlier only)</strong></p>
<p class="courseSearch">EAPS 31201 Earth Systems Science for Elementary Teachers</p>
<p class="courseSearch">*ENGR 16100 Honors Introduction to Innovation and the Physical Science of Engineering Design I (Both ENGR 16100 <strong>AND</strong> 16200 are required to meet <strong>one </strong>of the two SCI courses)</p>
<p class="courseSearch">*ENGR 16200 Honors Introduction to Innovation and the Physical Science of Engineering Design II (Both ENGR 16100 <strong>AND</strong> 16200 are required to meet&nbsp; <strong>one </strong>of the two SCI courses)</p>
<p class="courseSearch">ENTM 10500 Insects: Friends &amp; Foe</p>
<p class="courseSearch">ENTM 20600 General Entomology</p>
<p class="courseSearch">ENTM 21000 Intro to Insect Behavior</p>
<p class="courseSearch">ENTM 22810 Forensic Investigation</p>
<p class="courseSearch">ENTM 22820 Forensic Analysis</p>
<p class="courseSearch">HORT 10100 Fundamentals of Horticulture</p>
<p class="courseSearch">NRES 23000 Survey of Meteorology</p>
<p class="courseSearch">NUTR 20200 Principles Of Food Preparation And Nutrition</p>
<p class="courseSearch">NUTR 30300 Essentials of Nutrition</p>
<p class="courseSearch">PHYS 15200 Mechanics</p>
<p class="courseSearch">PHYS 17200 Modern Mechanics</p>
<p class="courseSearch">PHYS 21400 Nature of Physics</p>
<p class="courseSearch">PHYS 21500 Physics for Elementary Education</p>
<p class="courseSearch">PHYS 21800 General Physics I</p>
<p class="courseSearch">PHYS 21900 General Physics II</p>
<p class="courseSearch">PHYS 22000 General Physics</p>
<p class="courseSearch">PHYS 22100 General Physics</p>
<p class="courseSearch">PHYS 23000 Physical Science for Elementary Education</p>
<p class="courseSearch">PHYS 24100 Electricity and Optics</p>
<p class="courseSearch">PHYS 27200 Electric and Magnetic Interactions</p>
<p class="courseSearch">SLHS 30600 Introduction to Phonetics&nbsp; <strong>(Summer 2018 and earlier only)</strong></p>
</div>
<button class="accordion  active">Science, Technology &amp; Society (STS)</button>
<div class="panel  show">
<p class="courseSearch">ABE 22600 Biotechnology Laboratory I</p>
<p class="courseSearch">ABE 29000 Sophomore Seminar</p>
<p class="courseSearch">AD 39500 History of Design <strong>(Fall 2021 and after only)</strong></p>
<p class="courseSearch">AGRY 12500 Environmental Science and Conservation</p>
<p class="courseSearch">AGRY 28500 World Crop Adaptation and Distribution</p>
<p class="courseSearch">AGRY 29000 Introduction to Environmental Science&nbsp;<strong>(Spring 2024 and earlier only)</strong></p>
<p class="courseSearch">AMST 31000 Invention, Innovation, Design</p>
<p class="courseSearch">AMST 32500 Sports, Technology and Innovation</p>
<p class="courseSearch">ANSC 10200 Intro to Animal Agriculture</p>
<p class="courseSearch">ANTH 21000 Technology and Culture</p>
<p class="courseSearch">ASEC 35500 Controversial Science and Media in the Public Sphere</p>
<p class="courseSearch">ASM 23600 Environmental Systems Management</p>
<p class="courseSearch">ASTR 12300&nbsp; Our Place In The Universe&nbsp;</p>
<p class="courseSearch">BCHM 10000 Intro to Biochemistry</p>
<p class="courseSearch">BCM 10001 Introduction to Construction Management&nbsp;<strong>(Spring 2024 and earlier only)</strong></p>
<p class="courseSearch">BIOL 12100 Biology I: Ecology, Diversity, &amp; Behavior</p>
<p class="courseSearch">BIOL 31200 Great Issues in Genomics and Society&nbsp; <strong>(Fall 2015 and earlier only)</strong></p>
<p class="courseSearch">BTNY 20100 Plants and Civilization</p>
<p class="courseSearch">BTNY 21100 Plants and the Environment</p>
<p class="courseSearch">BTNY 28500 Plants and Civilization</p>
<p class="courseSearch">CE 35500 Engineering Environmental Sustainability <strong>(Fall 2021 and after only)</strong></p>
<p class="courseSearch">CGT 17208 User Experience Design Studio I: Fundamentals <strong>(Fall 2022 and after only)</strong></p>
<p class="courseSearch">CM 10000 <span>Introduction to Construction</span></p>
<p class="courseSearch">COM 25100 Intro to Electronic Mass Media</p>
<p class="courseSearch">COM 25100 Communication, Information and Society</p>
<p class="courseSearch">CS 10100 Digital Literacy</p>
<p class="courseSearch">EAPS 10000 Planet Earth</p>
<p class="courseSearch">EAPS 10400 Oceanography</p>
<p class="courseSearch">EAPS 10600 Geosciences in the Cinema</p>
<p class="courseSearch">EAPS 11300 Introduction to Environmental Science</p>
<p class="courseSearch">EAPS 12000 Introduction to Geography</p>
<p class="courseSearch">EAPS 12500 Environmental Science and Conservation</p>
<p class="courseSearch">EAPS 12900 Earth System Dynamics</p>
<p class="courseSearch">EAPS 20000 Water World: Processes and Challenges in Global Hydrology</p>
<p class="courseSearch">EDPS 45901&nbsp;Assistive Technology</p>
<p class="courseSearch">EEE 35500 Engineering Environmental Sustainability <strong>(Fall 2020 and after only)</strong></p>
<p class="courseSearch">ENGL 22300 Literature and Technology</p>
<p class="courseSearch">ENGL 22600 Narrative Medicine</p>
<p class="courseSearch">ENGL 23400 Ecological Literature</p>
<p class="courseSearch">ENGR 20100 Engineering in Global Context <strong>(Summer 2016 and earlier only, course renumbered to ENGR 31000)</strong></p>
<p class="courseSearch">ENGR 27920 Sophomore Participation In Vertically Integrated Projects (VIP) <strong>(Fall 2020 only, course prefix changed to VIP)</strong></p>
<p class="courseSearch">ENGR 31000 Engineering in Global Context <strong>(Fall 2016 and after only, course renumbered from ENGR 20100)&nbsp; <br> </strong></p>
<p class="courseSearch">ENGR 37920 Junior Participation In Vertically Integrated Projects (VIP) <strong>(Fall 2020 only, course prefix changed to VIP)</strong></p>
<p class="courseSearch">ENGR 47920 Senior Participation In Vertically Integrated Projects (VIP) <strong>(Fall 2020 only, course prefix changed to VIP)</strong></p>
<p class="courseSearch">ENTM 10500 Insects: Friends &amp; Foe</p>
<p class="courseSearch">ENTM 12800 Investigating Forensic Science</p>
<p class="courseSearch">ENTM 21800 Intro to Forensic Science <strong>(Fall 2014 and earlier only)</strong></p>
<p class="courseSearch">EPCS 10100 Engineering Projects in Community Service</p>
<p class="courseSearch">EPCS 10200 Engineering Projects in Community Service</p>
<p class="courseSearch">EPCS 11100 First Year Participation in EPICS I</p>
<p class="courseSearch">EPCS 12100 First Year Participation in EPICS I</p>
<p class="courseSearch">EPCS 20100 Engineering Projects in Community Service</p>
<p class="courseSearch">EPCS 20200 Engineering Projects in Community Service</p>
<p class="courseSearch">EPCS 30100 Engineering Projects in Community Service</p>
<p class="courseSearch">EPCS 30200 Engineering Projects in Community Service</p>
<p class="courseSearch">EPCS 40100 Engineering Projects in Community Service</p>
<p class="courseSearch">EPCS 40200 Engineering Projects in Community Service</p>
<p class="courseSearch">FNR 10300 Intro to Environmental Conservation</p>
<p class="courseSearch">FNR 12500 Environmental Science and Conservation</p>
<p class="courseSearch">FNR 22310 Introduction to Environmental Policy</p>
<p class="courseSearch">FNR 23000 World Forests and Society</p>
<p class="courseSearch">FNR 24000 Wildlife in America</p>
<p class="courseSearch">FS 16100 Science of Food</p>
<p class="courseSearch">HIST 30305 Food in Modern America</p>
<p class="courseSearch">HIST 30605 Technology And War In U.S. History&nbsp;</p>
<p class="courseSearch"><span>HIST 31305 Medical Devices and Innovation</span> <span></span></p>
<p class="courseSearch">HIST 31405 Science, Technology, Engineering And Mathematics (STEM) And Gender</p>
<p class="courseSearch">HIST 33205 The Nuclear Age</p>
<p class="courseSearch">HIST 33300 Science &amp; Society in Western Civilization I</p>
<p class="courseSearch">HIST 33400 Science &amp; Society in Western Civilization II</p>
<p class="courseSearch">HIST 35000 Science &amp; Society in the Twentieth Century World</p>
<p class="courseSearch">HIST 35205 Death, Disease and Medicine in Twentieth-Century American History</p>
<p class="courseSearch">HIST 36305 The History of Medicine and Public Health</p>
<p class="courseSearch">HIST 38001 History of U. S. Agriculture</p>
<p class="courseSearch">HIST 38400 History of Aviation</p>
<p class="courseSearch">HIST 38700 History of the Space Age</p>
<p class="courseSearch">HONR 19901 The Evolution of Ideas&nbsp; <strong>(Fall 2018 and earlier only)</strong></p>
<p class="courseSearch">HONR 31300&nbsp;Science,Technology, &amp; Society</p>
<p class="courseSearch">HONR 46000 Technological Justice <strong>(Fall 2022 and after only)</strong></p>
<p class="courseSearch">HORT 12100 Medicine in the Garden</p>
<p class="courseSearch">HORT 30600 History of Horticulture</p>
<p class="courseSearch">HSCI 20100 Principles of Public Health Science</p>
<p class="courseSearch">HSCI 20200 Essentials of Environmental, Occupational, &amp; Radiological Health Sciences</p>
<p class="courseSearch">IT 22600 Biotechnical Lab I</p>
<p class="courseSearch">LA 16100 Land and Society</p>
<p class="courseSearch">ME 29000 Global Engineering Professional Seminar</p>
<p class="courseSearch">NRES 12500 Environmental Science and Conservation</p>
<p class="courseSearch">NRES 29000 Introduction to Environmental Science</p>
<p class="courseSearch">NUTR 39800 Culture &amp; Food of France</p>
<p class="courseSearch">PHIL 20700 Ethics for Technology, Engineering, and Design</p>
<p class="courseSearch">PHIL 20800 Ethics of Data Science <strong>(Fall 2022 and after only)</strong></p>
<p class="courseSearch">PHIL 22100 Introduction to Philosophy of Science</p>
<p class="courseSearch">PHIL 27000 Biomedical Ethics</p>
<p class="courseSearch">POL 22300 Introduction to Environmental Policy</p>
<p class="courseSearch">POL 23700 Modern Weapons and International Relations</p>
<p class="courseSearch">PUBH 20200 Health in the Time of Pandemics: An Introduction <strong> (Fall 2020 and after only)</strong></p>
<p class="courseSearch">SA 10202 Culture &amp; Food of France</p>
<p class="courseSearch">SLHS 11500 Introduction to Communicative Disorders</p>
<p class="courseSearch">SLHS 21500 Exploring Audiology &amp; Hearing Science</p>
<p class="courseSearch">SLHS 30900 Language Development</p>
<p class="courseSearch">SOC 33500 Political Sociology <strong>(Fall 2021 and after only)</strong></p>
<p class="courseSearch">STAT 11300 Statistics and Society</p>
<p class="courseSearch">SYS 30000 It’s a Complex World: Addressing Global Challenges</p>
<p class="courseSearch">SYS 35000 Systems Theories and Approaches <strong>(</strong> <strong>Summer 2021 and earlier only)</strong></p>
<p class="courseSearch">SYS 40000 Systems Praxis <strong>(Fall 2021 and after only)</strong></p>
<p class="courseSearch">TECH 12000 Technology and the Individual&nbsp; <strong>(Fall 2013 and after only)</strong></p>
<p class="courseSearch">VIP 17911 First Year Participation In Vertically Integrated Projects (VIP) I <strong>(Fall 2021 and after only)</strong></p>
<p class="courseSearch">VIP 17920 First Year Participation In Vertically Integrated Projects (VIP) <strong>(Fall 2021 and after only)</strong></p>
<p class="courseSearch">VIP 27920 Sophomore Participation In Vertically Integrated Projects (VIP) <strong>(Spring 2021 and after only)</strong></p>
<p class="courseSearch">VIP 37920 Junior Participation In Vertically Integrated Projects (VIP) <strong>(Spring 2021 and after only)</strong></p>
<p class="courseSearch">VIP 47920 Senior Participation In Vertically Integrated Projects (VIP) <strong>(Spring 2021 and after only)</strong></p>
<p class="courseSearch">YDAE 35500 Controversial Science and Media in the Public Sphere <strong>(Summer 2019 and before only. Effective Fall 2019, YDAE is now ASEC)</strong></p>
</div>
<button class="accordion  active">Written Communication (WC)</button>
<div class="panel  show">
<p class="courseSearch">AMST 10100 America and the World</p>
<p class="courseSearch">CLCS 23100 Survey of Latin Literature&nbsp; <strong>(Summer 2019 and earlier only)</strong> <strong> <br> </strong></p>
<p class="courseSearch">CLCS 23700 Gender &amp; Sexuality in Greek &amp; Roman Antiquity&nbsp; <strong>(Summer 2019 and earlier only)</strong></p>
<p class="courseSearch">CLCS 33900 Literature and the Law&nbsp; <strong>(Summer 2019 and earlier only)</strong></p>
<p class="courseSearch">COM 20400 Critical Perspectives on Communication</p>
<p class="courseSearch">EDCI 20500 Exploring Teaching as a Career</p>
<p class="courseSearch">ENGL 10600 First Year Composition</p>
<p class="courseSearch">ENGL 10800 Accelerated First Year Composition</p>
<p class="courseSearch">ENGL 30400 Advanced Composition <strong>(Fall 2021 and after only)</strong></p>
<p class="courseSearch">ENGL 38000 Issues in Rhetoric and Public Life <strong>(Fall 2021 and after only)</strong></p>
<p class="courseSearch">HONR 19903 Interdisciplinary Approaches to Writing</p>
<p class="courseSearch">PHIL 26000 Philosophy &amp; Law <strong>(Summer 2023 and earlier only)</strong></p>
<p class="courseSearch">SCLA 10100 Transformative Texts: Critical Thinking &amp; Communication I: Antiquity to Modernity</p>
<p class="courseSearch">SPAN 33000 Spanish And Latin American Cinema <strong>(Summer 2020 and earlier only)</strong></p>
</div>
<script type="text/javascript">// <![CDATA[
var acc = document.getElementsByClassName("accordion"); var i; for (i = 0; i < acc.length; i++) { acc[i].onclick = function() { this.classList.toggle("active"); this.nextElementSibling.classList.toggle("show"); } } var h3s = document.getElementsByTagName("h3"); for (i = 0; i < h3s.length; i++) { var hr = document.createElement("hr"); h3s[i].appendChild(hr); } $('#expand-button').click(function() { $('.accordion').addClass('active'); $('.maincontent .panel').addClass('show'); }); $('#collapse-button').click(function() { $('.accordion').removeClass('active'); $('.maincontent .panel').removeClass('show'); }); $(window).scroll(function() { if ($(this).scrollTop() > 100) { $('.scrollup').fadeIn(); } else { $('.scrollup').fadeOut(); } if ($(this).scrollTop() > 300) { $('#controller').css('position', 'fixed'); } else { $('#controller').css('position', 'relative'); } }); $('.scrollup').click(function() { $("html, body").animate({ scrollTop: 0 }, 600); return false; });
// ]]></script>

					</div>
					<div class="sidenav col-lg-3 col-md-3 col-sm-3 col-xs-12">
						



<ul>
                <li><a href="https://www.purdue.edu/provost/students/s-initiatives/curriculum/index.html">Curriculum</a></li>
                                                                                
        
            
    
    <li><a href="https://www.purdue.edu/provost/students/s-initiatives/curriculum/history.html">History of the Core Curriculum</a></li>
                                                                    
        
            
    
    <li><a href="https://www.purdue.edu/provost/students/s-initiatives/curriculum/outcomes.html">Expected Outcomes</a></li>
                                                                    
        
            
    
    <li><a href="https://www.purdue.edu/provost/students/s-initiatives/curriculum/uccr.html">Undergraduate Curriculum Council Representatives</a></li>
                                                                    
        
            
    
    <li><a href="https://www.purdue.edu/provost/students/s-initiatives/curriculum/uccr-leadership.html">Undergraduate Curriculum Council Leadership</a></li>
                                                                    
        
            
    
    <li><a href="https://www.purdue.edu/provost/students/s-initiatives/curriculum/evaluation.html">Evaluating the Core Curriculum</a></li>
                                                                    
        
            
    
    <li><a href="https://www.purdue.edu/provost/students/s-initiatives/curriculum/courses.html">Course Listing</a></li>
                                                                                 
                
                        
                                    <li class="dropdown-submenu">
                <a class="dropdown-toggle" data-toggle="dropdown" href="https://www.purdue.edu/provost/students/s-initiatives/curriculum/faq/index.html">FAQ<span class="caret"></span></a>
                <ul class="dropdown-menu">
                                                                                                
        
            
    
    <li><a href="https://www.purdue.edu/provost/students/s-initiatives/curriculum/faq/student-faq.html">Student FAQ</a></li>
                                                                    
        
            
    
    <li><a href="https://www.purdue.edu/provost/students/s-initiatives/curriculum/faq/faculty-faq.html">Faculty FAQ</a></li>
                                                                    
        
            
    
    <li><a href="https://www.purdue.edu/provost/students/s-initiatives/curriculum/faq/academic-advisors.html">Advisor Guidelines</a></li>
                                    </ul>
                            </li>
                                                                        
        
            
    
    <li><a href="https://www.purdue.edu/provost/students/s-initiatives/curriculum/meeting-dates.html">Meeting Dates</a></li>
                        </ul>
					</div>
				</div>
			</div>
		</div>
		<!-- End Main Content -->
		<!-- Begin Footer -->
		<div class="footer">
			<div class="container">
				<div class="row panel-group" id="accordion">
					<div class="panel panel-default">
						<div class="panel-heading">
<h4 class="panel-title"><a class="collapsed" data-parent="#accordion" data-toggle="collapse" href="https://www.purdue.edu/provost/students/s-initiatives/curriculum/courses.html#footerone">Communication <i class="fa fa-plus right"></i><i class="fa fa-minus right"></i></a></h4>
</div>
<div class="panel-collapse collapse" id="footerone">
<div class="panel-body">
<ul>
<li><a href="https://one.purdue.edu/" rel="noopener" target="_blank">OneCampus Portal</a></li>
<li><a href="https://purdue.brightspace.com/">Brightspace</a></li>
<li><a href="https://www.purdue.edu/boilerconnect/">BoilerConnect</a></li>
<li><a href="https://portal.office.com/">Office 365</a></li>
<li><a href="https://outlook.office.com/">Outlook</a></li>
<li><a href="https://mypurdue.purdue.edu/">myPurdue</a></li>
</ul>
</div>
</div>
					</div>
					<div class="panel panel-default">
						<div class="panel-heading">
<h4 class="panel-title"><a class="collapsed" data-parent="#accordion" data-toggle="collapse" href="https://www.purdue.edu/provost/students/s-initiatives/curriculum/courses.html#footertwo">Campus <i class="fa fa-plus right"></i><i class="fa fa-minus right"></i></a></h4>
</div>
<div class="panel-collapse collapse" id="footertwo">
<div class="panel-body">
<ul>
<li><a href="https://www.purdue.edu/purdue/faculty_staff/index.php">Faculty and Staff</a></li>
<li><a href="https://www.purdue.edu/hr">Human Resources</a></li>
<li><a href="https://www.purdue.edu/purdue/careers/index.php">Careers</a></li>
<li><a href="https://www.purdue.edu/purdue/about/colleges_schools.php">Colleges and Schools</a></li>
<li><a href="https://www.purdue.edu/directory/" rel="noopener" target="_blank">Directory</a></li>
<li><a href="https://www.purdue.edu/campus-map/">Campus Map</a></li>
</ul>
</div>
</div>
					</div>
					<div class="panel panel-default">
						<div class="panel-heading">
<h4 class="panel-title"><a class="collapsed" data-parent="#accordion" data-toggle="collapse" href="https://www.purdue.edu/provost/students/s-initiatives/curriculum/courses.html#footerthree">Services <i class="fa fa-plus right"></i><i class="fa fa-minus right"></i></a></h4>
</div>
<div class="panel-collapse collapse" id="footerthree">
<div class="panel-body">
<ul>
<li><a href="https://purdue.brightspace.com/d2l/login" rel="noopener" target="_blank">Blackboard</a></li>
<li><a href="http://www.purdue.edu/ehps/">Environmental Health &amp; Public Safety</a></li>
<li><a href="https://www.lib.purdue.edu/">Libraries</a></li>
<li><a href="https://www.itap.purdue.edu/">ITaP</a></li>
<li><a href="https://www.purdue.edu/hr/CHL/index.html">Center for Healthy Living</a></li>
</ul>
</div>
</div>
					</div>
					<div class="panel panel-default">
						<div class="panel-heading">
<h4 class="panel-title"><a class="collapsed" data-parent="#accordion" data-toggle="collapse" href="https://www.purdue.edu/provost/students/s-initiatives/curriculum/courses.html#footerfour">Other <i class="fa fa-plus right"></i><i class="fa fa-minus right"></i></a></h4>
</div>
<div class="panel-collapse collapse" id="footerfour">
<div class="panel-body">
<ul>
<li><a href="https://purduesports.com/sports/2018/5/17/facilities-teamstore-html" rel="noopener" target="_blank">Shop</a></li>
<li><a href="http://www.purdue.edu/ethics/clery.html">Clery Reporting Act</a></li>
<li><a href="https://www.purdue.edu/bursar/tuition/calculator/">Tuition Calculator</a></li>
<li><a href="https://www.purdue.edu/ethics/">Ethics &amp; Compliance</a></li>
<li><a href="http://www.purdue.edu/hotline/">Speak Up</a></li>
</ul>
</div>
</div>
					</div>
					<div class="motto col-lg-4 col-md-4 col-sm-12">
						<!--<div class="taglineContainer">-->
						<!--	<div class="tagline">-->
						<!--		<img alt="Purdue University" class="horizontal" src="https://www.purdue.edu/purdue/images/PU-H.svg"/>-->
						<!--		<img alt="Purdue University" class="vertical" src="https://www.purdue.edu/purdue/images/PU-V.svg"/>-->
						<!--	</div>-->
						<!--</div>-->
						<div class="social">
							


                 
<div class="footer__resources__column">
    <div class="footer__resources__column__motto">
        
            <svg class="horizontal" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 249.7 45.3" style="enable-background:new 0 0 249.7 45.3;" xml:space="preserve">
<style type="text/css">
	.st0{fill:#FFFFFF;}
	.st1{fill:#CFB991;}
	.st2{fill:#9D9795;}
</style>
<title>Purdue University Logo</title>
<g>
	<path class="st0" d="M97.4,3.8L94.6,3V1h10.9c7.1,0,9.7,2.3,9.7,7.6c0,5-2.9,7.6-8.5,7.6h-4.4v8l2.8,0.8V27H94.5v-1.9l2.9-0.8V3.8z
		 M102.3,3.8v10.1l5.2-0.4c1.3-0.6,2.6-1.4,2.6-4.6c0-2.5-0.1-5.1-4.9-5.1L102.3,3.8z"></path>
	<path class="st0" d="M155.8,16h-3.5v8.4l2.8,0.8V27h-10.7v-1.9l2.9-0.8V3.8L144.5,3V1h11.4c6.8,0,9.2,2.4,9.2,7
		c0,3.6-1.4,5.4-4.6,6.7l4.8,9.4l3.1,1V27h-7.2L155.8,16z M152.3,3.8v9.9l5.3-0.4c1.7-0.8,2.5-2.2,2.5-4.9c0-2.9-0.9-4.7-3.9-4.7
		L152.3,3.8z"></path>
	<path class="st0" d="M170.6,25.2l2.8-0.8V3.8L170.6,3V1h12.6c7.1,0,11.3,4.3,11.3,12.7c0,9.5-4.3,13.3-11.8,13.3h-12.1V25.2z
		 M178.4,3.8v20.6h3.7c2.6,0,7-0.4,7-9.8c0-7.4-1.3-10.8-7-10.8L178.4,3.8z"></path>
	<path class="st0" d="M105.5,40.6c0,3.2-1.8,4.3-4.8,4.3s-4.8-1.8-4.8-4.3v-6.3l-1.4-0.4v-1.2h5.5v1.2l-1.3,0.4v6.3
		c0,1.6,0.6,2.5,2.4,2.5c0.9,0,2.4-0.3,2.4-2.6v-6.3l-1.4-0.4v-1.2h4.8v1.2l-1.4,0.4L105.5,40.6z"></path>
	<path class="st0" d="M115.1,37.3v5.8l1.3,0.4v1.2h-4.7v-1.2l1.4-0.4v-8.3l-0.6-0.7l-0.8-0.3v-1.3h3.1l5.9,7.4v-5.8l-1.4-0.4v-1.2
		h4.7v1.2l-1.4,0.4v10.5h-1.6L115.1,37.3z"></path>
	<path class="st0" d="M134.1,43.2l1.4,0.4v1.2h-5.6v-1.2l1.4-0.4v-8.9l-1.4-0.4v-1.2h5.6v1.2l-1.4,0.4V43.2z"></path>
	<path class="st0" d="M209,43.2l1.4,0.4v1.2h-5.6v-1.2l1.4-0.4v-8.9l-1.4-0.4v-1.2h5.6v1.2l-1.4,0.4L209,43.2z"></path>
	<path class="st0" d="M148.2,44.7h-2.6l-3.8-10.5l-1.4-0.4v-1.2h5.9v1.2l-1.4,0.4l2.6,7.5l2.6-7.5l-1.4-0.4v-1.2h4.8v1.2l-1.4,0.4
		L148.2,44.7z"></path>
	<path class="st0" d="M159.2,34.3l-1.4-0.4v-1.2h9.5l0.1,3.7H166l-0.7-2.1h-3.2v3.4h3.1v1.7h-3.1v3.8h3.2l1-2.1h1.5l-0.2,3.7h-9.7
		v-1.2l1.4-0.3V34.3z"></path>
	<path class="st0" d="M179.1,39.8h-1v3.4l1.4,0.4v1.2h-5.6v-1.2l1.4-0.4v-8.9l-1.4-0.4v-1.2h5.5c3.4,0,4.4,1.3,4.4,3.4
		c0,1.3-0.3,2.6-2,3.2l2,3.9l1.7,0.5v1.1h-4.1L179.1,39.8z M178.1,34.3v4.2l1.9-0.2c0.6-0.5,1-1.3,1-2.1c0-1.2-0.3-2-1.6-2H178.1z"></path>
	<path class="st0" d="M190.4,41h1.7l0.4,1.7c0.8,0.5,1.7,0.7,2.6,0.7c0.1,0,0.3,0,0.4,0c0.5-0.3,0.7-0.9,0.8-1.5
		c0-2.8-5.8-1.6-5.8-5.7c0-1.9,1.7-3.7,4.6-3.7c1.1,0,2.3,0.3,3.3,0.8v3.2h-1.6l-0.6-2c-0.6-0.2-1.3-0.4-2-0.4c-0.1,0-0.2,0-0.3,0
		c-0.5,0.3-0.8,0.8-0.8,1.4c0,2.4,5.7,1.6,5.7,5.6c0,2.2-2,3.8-4.6,3.8c-1.3,0-2.6-0.4-3.7-1.1L190.4,41z"></path>
	<path class="st0" d="M220,34.3h-1.6l-0.7,2.1h-1.5v-3.8h10.6v3.8h-1.5l-0.7-2.1h-1.7v8.9l1.4,0.4v1.2h-5.6v-1.2l1.4-0.4V34.3z"></path>
	<path class="st0" d="M236.2,40.1l-3.2-5.8l-1.4-0.4v-1.2h5.9v1.2l-1.4,0.4l2,3.9l2-3.9l-1.4-0.4v-1.2h4.8v1.2l-1.4,0.4l-3.2,5.8
		v3.1l1.4,0.4v1.2h-5.6v-1.2l1.4-0.4V40.1z"></path>
	<polygon class="st0" points="241.4,19.5 239.5,24.3 231.4,24.3 231.4,15 236,15 236.6,17.6 238.6,17.6 238.6,9.7 236.6,9.7 
		236,12.3 231.4,12.3 231.4,3.8 239.2,3.8 240.6,8.8 243.5,8.8 243.3,1 223.6,1 223.6,3 226.4,3.8 226.4,24.4 223.5,25.2 223.5,27 
		243.7,27 244.1,19.5 	"></polygon>
	<path class="st0" d="M139.5,18.1c0,6.6-3.2,9.3-9.6,9.3c-5.9,0-10.2-2.4-10.2-8.7V3.8L116.8,3V1h10.6v2l-2.8,0.8v14.9
		c0,3.8,1.7,5.4,5.9,5.4c2.9,0,5.5-1.7,5.5-5.7V3.8L133.1,3V1h9.2v2l-2.8,0.8V18.1z"></path>
	<path class="st0" d="M218.5,18.1c0,6.6-3.2,9.3-9.6,9.3c-5.9,0-10.3-2.4-10.3-8.7V3.8L195.8,3V1h10.6v2l-2.8,0.8v14.9
		c0,3.8,1.7,5.4,5.9,5.4c2.9,0,5.5-1.7,5.5-5.7V3.8L212.2,3V1h9.2v2l-2.8,0.8V18.1z"></path>
	<path class="st1" d="M44.4,44.8L50,31.6h9.3c13.4,0,18.5-5.5,22.1-13.8c1.3-3.1,3.5-8.2,0.6-12.6c-2.9-4.4-9-4.8-13.3-4.8H19.3
		l-7,16.3h8.9l-5,11.7h-9l-7,16.4H44.4z"></path>
	<path class="st2" d="M79.4,6.9c-1.6-2.4-5-3.5-10.8-3.5H21.3L17,13.7h8.9l-7.5,17.7h-9L5,41.7h37.4l4.4-10.3h-9.1l1.2-2.9h20.4
		c13.1,0,16.6-5.6,19.3-12C80,13.2,81.3,9.7,79.4,6.9 M45.3,13.7h15c2.1,0,1.8,1,1.5,1.7c-0.8,1.8-2.6,2.9-4.8,2.9H43.3L45.3,13.7z"></path>
	<path d="M68.7,5H22.4l-3,7.1h8.9L19.4,33h-9l-3,7.1h34l3-7.1h-9.1l2.6-6h21.4c12.3,0,15.4-5.2,17.8-11S81,5,68.7,5 M57,19.9H41
		l3.3-7.7h16c2.8,0,4,1.5,2.9,3.9C62.2,18.4,59.8,19.9,57,19.9"></path>
	<path class="st0" d="M246.9,44.7c-1.4,0-2.6-1.2-2.6-2.6c0-1.4,1.2-2.6,2.6-2.6c1.4,0,2.6,1.2,2.6,2.6c0,0,0,0,0,0
		C249.5,43.5,248.3,44.7,246.9,44.7z M246.9,40.1c-1.1,0-2.1,0.9-2.1,2.1c0,1.1,0.9,2.1,2.1,2.1c1.1,0,2.1-0.9,2.1-2.1
		C249,41,248,40.1,246.9,40.1L246.9,40.1z"></path>
	<path class="st0" d="M246.6,42.3v1h-0.5v-2.4h1.1c0.5,0,0.8,0.3,0.8,0.7c0,0.2-0.1,0.5-0.4,0.6c0.1,0,0.3,0.2,0.3,0.6v0.1
		c0,0.2,0,0.3,0,0.5h-0.5c0-0.2-0.1-0.4,0-0.5v0c0-0.3-0.1-0.4-0.5-0.4L246.6,42.3z M246.6,41.9h0.4c0.3,0,0.4-0.1,0.4-0.3
		s-0.1-0.3-0.4-0.3h-0.4V41.9z"></path>
</g>
</svg>
            <svg class="vertical" version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 203.8 132" style="enable-background:new 0 0 203.8 132;" xml:space="preserve">
<style type="text/css">
	.v-st0{fill:#CFB991;}
	.v-st1{fill:#9D9795;}
	.v-st2{fill:#FFFFFF;}
</style>
<title>Purdue University Logo</title>
<g>
	<path class="v-st0" d="M102.5,58.7l7.3-17.3H122c17.6,0,24.3-7.2,28.9-18.1c1.7-4,4.6-10.7,0.8-16.5S140,0.5,134.3,0.5H69.7
		l-9.1,21.4h11.7l-6.5,15.3H54l-9.1,21.4L102.5,58.7z"></path>
	<path class="v-st1" d="M148.4,9.1c-2.1-3.1-6.5-4.6-14.1-4.6h-62L66.5,18h11.7l-9.9,23.2H56.6l-5.7,13.5h49l5.7-13.5H93.8l1.6-3.8
		H122c17.1,0,21.7-7.4,25.3-15.7C149.2,17.3,150.8,12.7,148.4,9.1 M103.7,18h19.6c2.7,0,2.3,1.4,1.9,2.2c-1,2.3-3.4,3.8-6.3,3.8
		h-17.8L103.7,18z"></path>
	<path d="M134.3,6.6H73.6l-4,9.4h11.7L69.7,43.3H58l-4,9.4h44.5l4-9.4H90.6l3.4-7.9h28.1c16.1,0,20.1-6.8,23.4-14.4
		S150.4,6.5,134.3,6.6 M118.9,26H98l4.3-10.1h21c3.7,0,5.2,1.9,3.9,5.1S122.6,26,118.9,26"></path>
	<path class="v-st2" d="M4,78l-3.7-1.1v-2.6h14.3c9.3,0,12.8,3,12.8,10c0,6.6-3.8,10-11.1,10h-5.8v10.6l3.7,1.1v2.5h-14v-2.5l3.8-1.1
		V78z M10.5,77.9v13.2l6.8-0.5c1.7-0.8,3.4-1.8,3.4-6.1c0-3.2-0.1-6.6-6.4-6.6L10.5,77.9z"></path>
	<path class="v-st2" d="M80.7,93.9H76v11l3.7,1.1v2.5h-14v-2.5l3.8-1.1V78l-3.7-1.1v-2.6h14.9c8.9,0,12.1,3.1,12.1,9.2
		c0,4.7-1.8,7.1-6,8.8l6.3,12.3l4.1,1.3v2.5h-9.5L80.7,93.9z M76,77.9v13l6.9-0.5c2.2-1.1,3.2-2.8,3.2-6.4c0-3.8-1.2-6.1-5.1-6.1
		L76,77.9z"></path>
	<path class="v-st2" d="M100,105.9l3.7-1V78l-3.7-1.1v-2.6h16.5c9.3,0,14.8,5.6,14.8,16.7c0,12.5-5.6,17.4-15.5,17.4H100V105.9z
		 M110.2,77.9v27h4.9c3.4,0,9.1-0.5,9.1-12.9c0-9.7-1.7-14.1-9.1-14.1L110.2,77.9z"></path>
	<path class="v-st2" d="M14.7,126.2c0,4.1-2.4,5.7-6.3,5.7s-6.3-2.3-6.3-5.7v-8.3l-1.8-0.6v-1.6h7.3v1.6l-1.8,0.6v8.3
		c0,2.1,0.8,3.3,3.2,3.3c1.1,0,3.1-0.4,3.1-3.4v-8.2l-1.8-0.6v-1.6h6.2v1.6l-1.8,0.5V126.2z"></path>
	<path class="v-st2" d="M27.2,121.9v7.6L29,130v1.6h-6.1V130l1.8-0.5v-10.8l-0.8-1l-1.1-0.3v-1.7h4l7.7,9.7v-7.6l-1.8-0.5v-1.6h6.1
		v1.6l-1.8,0.5v13.8h-2.1L27.2,121.9z"></path>
	<path class="v-st2" d="M52.2,129.5L54,130v1.6h-7.3V130l1.8-0.5v-11.7l-1.8-0.5v-1.6H54v1.6l-1.8,0.5L52.2,129.5z"></path>
	<path class="v-st2" d="M150.4,129.5l1.8,0.5v1.6h-7.3V130l1.8-0.5v-11.7l-1.8-0.5v-1.6h7.3v1.6l-1.8,0.5V129.5z"></path>
	<path class="v-st2" d="M70.6,131.6h-3.4l-5-13.7l-1.8-0.6v-1.6h7.7v1.6l-1.8,0.6l3.3,9.8l3.4-9.8l-1.8-0.6v-1.6h6.2v1.6l-1.8,0.6
		L70.6,131.6z"></path>
	<path class="v-st2" d="M85.1,117.8l-1.8-0.5v-1.6h12.5l0.1,4.9h-2l-1-2.8h-4.1v4.5h4.1v2.3h-4.1v5H93l1.3-2.8h1.9l-0.3,4.8H83.3V130
		l1.8-0.4V117.8z"></path>
	<path class="v-st2" d="M111.1,125.1h-1.4v4.4l1.8,0.5v1.6h-7.3V130l1.8-0.5v-11.7l-1.8-0.5v-1.6h7.2c4.4,0,5.8,1.7,5.8,4.4
		c0,1.8-0.4,3.4-2.6,4.2l2.5,5.2l2.2,0.7v1.5h-5.4L111.1,125.1z M109.8,117.8v5.6l2.5-0.2c0.8-0.7,1.3-1.7,1.2-2.8
		c0-1.6-0.4-2.6-2-2.6H109.8z"></path>
	<path class="v-st2" d="M126,126.7h2.2l0.5,2.2c1,0.6,2.2,0.9,3.3,0.9c0.2,0,0.3,0,0.5,0c0.6-0.4,1-1.2,1-1.9c0-3.7-7.6-2.1-7.6-7.5
		c0-2.5,2.3-4.9,6-4.9c1.5,0,3,0.4,4.3,1.1v4.2h-2.1l-0.8-2.7c-0.8-0.3-1.7-0.5-2.6-0.5c-0.1,0-0.3,0-0.4,0c-0.6,0.4-1,1.1-1,1.9
		c0,3.2,7.5,2,7.5,7.4c0,2.9-2.6,4.9-6.1,4.9c-1.7,0-3.4-0.5-4.8-1.4L126,126.7z"></path>
	<path class="v-st2" d="M164.7,117.9h-2.1l-0.9,2.8h-2v-5h13.8v5h-1.9l-0.9-2.8h-2.2v11.6l1.8,0.5v1.6h-7.3V130l1.8-0.5V117.9z"></path>
	<path class="v-st2" d="M186,125.5l-4.2-7.6l-1.8-0.6v-1.6h7.7v1.6l-1.8,0.6l2.6,5.2l2.6-5.2l-1.8-0.6v-1.6h6.3v1.6l-1.8,0.6l-4.2,7.6
		v4.1l1.8,0.5v1.6h-7.3V130l1.8-0.5L186,125.5z"></path>
	<polygon class="v-st2" points="192.7,98.5 190.3,104.9 179.6,104.9 179.6,92.6 185.7,92.6 186.4,96 189.1,96 189.1,85.7 186.4,85.7 
		185.7,89 179.6,89 179.6,77.9 189.8,77.9 191.8,84.5 195.5,84.5 195.2,74.3 169.4,74.3 169.4,76.9 173.1,78 173.1,104.9 
		169.4,105.9 169.4,108.4 195.7,108.4 196.3,98.5 	"></polygon>
	<path class="v-st2" d="M59.2,96.7c0,8.7-4.1,12.2-12.6,12.2c-7.8,0-13.4-3.1-13.4-11.3V78l-3.7-1.1v-2.6h13.9v2.6L39.6,78v19.6
		c0,4.9,2.3,7.1,7.7,7.1c3.7,0,7.2-2.2,7.2-7.5V78l-3.7-1.1v-2.6h12v2.6L59.2,78V96.7z"></path>
	<path class="v-st2" d="M162.8,96.7c0,8.7-4.1,12.2-12.6,12.2c-7.8,0-13.4-3.1-13.4-11.3V78l-3.7-1.1v-2.6h13.9v2.6l-3.7,1.1v19.6
		c0,4.9,2.3,7.1,7.7,7.1c3.7,0,7.2-2.2,7.2-7.5V78l-3.7-1.1v-2.6h12v2.6l-3.7,1.1V96.7z"></path>
	<path class="v-st2" d="M200,131.5c-1.9,0-3.4-1.5-3.4-3.4c0-1.9,1.5-3.4,3.4-3.4c1.9,0,3.4,1.5,3.4,3.4l0,0
		C203.4,130,201.9,131.5,200,131.5z M200,125.4c-1.5,0-2.7,1.2-2.7,2.7s1.2,2.7,2.7,2.7c1.5,0,2.7-1.2,2.7-2.7l0,0
		C202.7,126.7,201.5,125.4,200,125.4L200,125.4L200,125.4z"></path>
	<path class="v-st2" d="M199.6,128.5v1.3h-0.7v-3.2h1.4c0.7,0,1.1,0.4,1.1,0.9c0,0.3-0.2,0.6-0.5,0.7c0.2,0.1,0.4,0.2,0.4,0.8v0.2
		c0,0.2,0,0.4,0,0.6h-0.7c-0.1-0.2-0.1-0.5-0.1-0.7v0c0-0.3-0.1-0.5-0.6-0.5L199.6,128.5z M199.6,127.9h0.6c0.4,0,0.5-0.1,0.5-0.4
		c0-0.2-0.2-0.4-0.5-0.4h-0.6L199.6,127.9z"></path>
</g>
</svg>
        
    
    </div>
    <div class="footer__resources__column__social">
                                        
                        
                                 
        
                                                                                
                                                    <a href="https://www.facebook.com/PurdueUniversity/" rel="noopener" target="_blank"><span class="sr-only">Facebook</span>
                 <i class="fa-brands fa-square-facebook" aria-hidden="true"></i>
                </a>
                                
                                 
        
                                                                                
                                                    <a href="https://twitter.com/lifeatpurdue" rel="noopener" target="_blank"><span class="sr-only">Twitter</span>
                 <i aria-hidden="true" class="fa-brands fa-square-x-twitter"></i>
                </a>
                                
                                 
        
                                                                                
                                                    <a href="https://www.youtube.com/user/PurdueUniversity" rel="noopener" target="_blank"><span class="sr-only">YouTube</span>
                 <i class="fa-brands fa-square-youtube" aria-hidden="true"></i>
                </a>
                                
                                 
        
                                                                                
                                                    <a href="https://www.instagram.com/lifeatpurdue/" rel="noopener" target="_blank"><span class="sr-only">Instagram</span>
                 <i class="fa-brands fa-square-instagram" aria-hidden="true"></i>
                </a>
                                
                                 
        
                                                                                
                                                    <a href="https://www.pinterest.com/lifeatpurdue/" rel="noopener" target="_blank"><span class="sr-only">Pinterest</span>
                 <i class="fa-brands fa-square-pinterest" aria-hidden="true"></i>
                </a>
                                
                                 
        
                                                                                
                                                    <a href="https://www.snapchat.com/add/lifeatpurdue" rel="noopener" target="_blank"><span class="sr-only">Snapchat</span>
                 <i class="fa-brands fa-square-snapchat" aria-hidden="true"></i>
                </a>
                                
                                 
        
                                                                                
                                                    <a href="https://www.linkedin.com/edu/purdue-university-18357" rel="noopener" target="_blank"><span class="sr-only">LinkedIn</span>
                 <i aria-hidden="true" class="fa-brands fa-linkedin"></i>
                </a>
                            </div>
</div>
						</div>
					</div>
					</div>
				</div>
			</div>
			<!-- End Footer -->
			<!-- Begin Bottom Signature -->
			<div class="bottom">
				<div class="container">
					<div class="row">
						<div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
							<p>Purdue University, 610 Purdue Mall, West Lafayette, IN 47907, (765) 494-4600</p>
<p><a href="http://www.purdue.edu/purdue/disclaimer.html"> © 2023-2024 Purdue University</a> | <a href="http://www.purdue.edu/purdue/ea_eou_statement.html">An equal access/equal opportunity university</a> | <a href="https://www.purdue.edu/securepurdue/security-programs/copyright-policies/reporting-alleged-copyright-infringement.php">Copyright Complaints</a>&nbsp;| <a href="http://www.purdue.edu/provost/">Maintained by Office of the Provost</a></p>
<p>Trouble with this page? Disability-related <a href="http://www.purdue.edu/disabilityresources/">accessibility</a> issue? Please contact&nbsp;Office of The Provost at <a href="mailto:purdueprovost@purdue.edu"> purdueprovost@purdue.edu</a>.</p>
						</div>
					</div>
				</div>
			</div>
			<!-- End Bottom Signature -->
			<!-- Bootstrap core JavaScript -->
			<!-- Placed at the end of the document so the pages load faster -->
			<script src="./Course Listing - Office of the Provost - Purdue University_files/bootstrap.min.js.download" type="text/javascript"></script>
			
		
		
	<table cellspacing="0" cellpadding="0" role="presentation" class="gstl_50 gssb_c" style="width: 2px; display: none; top: 3px; position: absolute; left: -1px;"><tbody><tr><td class="gssb_f"></td><td class="gssb_e" style="width: 100%;"></td></tr></tbody></table></body><!-- v2015.08 - Created by Office of Marketing and Media --><grammarly-desktop-integration data-grammarly-shadow-root="true"><template shadowrootmode="open"><style>
      div.grammarly-desktop-integration {
        position: absolute;
        width: 1px;
        height: 1px;
        padding: 0;
        margin: -1px;
        overflow: hidden;
        clip: rect(0, 0, 0, 0);
        white-space: nowrap;
        border: 0;
        -moz-user-select: none;
        -webkit-user-select: none;
        -ms-user-select:none;
        user-select:none;
      }

      div.grammarly-desktop-integration:before {
        content: attr(data-content);
      }
    </style><div aria-label="grammarly-integration" role="group" tabindex="-1" class="grammarly-desktop-integration" data-content="{&quot;mode&quot;:&quot;full&quot;,&quot;isActive&quot;:true,&quot;isUserDisabled&quot;:false}"></div></template></grammarly-desktop-integration></html>
"""

# Parse HTML to extract course codes and descriptions
soup = BeautifulSoup(html_content, 'html.parser')
course_tags = soup.find_all('p', class_='courseSearch')

course_data = []
for tag in course_tags:
    course_text = tag.text.strip()
    if ' ' in course_text:
        code, description = course_text.split(' ', 1)
        course_data.append((code, description))
    else:
        print(f"Invalid format for course: {course_text}")

# Database connection settings
db_settings = {
    'port': 3306,  # replace with your port
    'host': 'localhost',
    'user': 'root',
    'password': 'Tomcar123!',
    'database': 'coursesniper'
}

# Connect to MySQL database
conn = pymysql.connect(**db_settings)
cursor = conn.cursor()

try:
    # Create table if it doesn't exist
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS course_codes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        class_code VARCHAR(50) NOT NULL,
        description TEXT
    )
    '''
    cursor.execute(create_table_query)
    conn.commit()

    # Insert data into course_codes table
    insert_query = '''
    INSERT INTO course_codes (class_code, description)
    VALUES (%s, %s)
    '''
    cursor.executemany(insert_query, course_data)
    conn.commit()

    print(f"Successfully inserted {cursor.rowcount} records into course_codes table.")

except Exception as e:
    print(f"Error inserting data: {str(e)}")
    conn.rollback()

finally:
    cursor.close()
    conn.close()

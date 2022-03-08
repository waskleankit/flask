<html>
<head>
<meta charset="UTF-8">
<title>Our Service Section</title>
<style="text/CSS">
{
	margin: 0;
	padding: 0;
	box-sizing: border-box;
	font-family: 'Poppins', sans-serif;
}
body
{
	display: flex;
	justify-content: center;
	align-item: center;
	min-height: 100vh;
	backgroud: linear-gradient(#0f4675, #0f4675 50%, #fff 50%, #fff 	100%);
}
.container
{
	width: 1100px;
	display: flex;
	justufy-content: space-between;
	flex-wrap: wrap;
}
.container .box
{
	position: relative;
	width: 320px;
	background: #fff;
	padding: 100px 40px 60px;
	box-shadow: 0 15px 45px rgba(0,0,0,.1);
}
.container .box:before
{
	content: ' ';
	position: absolute;
	top: 0;
	Left: 0;
	Width: 100%;
	height: 100%;
	background: #ff226d;
	transform: scaleY(0);
	transform-origin: top;
	transform: transform 0.5s;
}
.container .box:hover:before
{
	transform: scaleY(1);
	transform-origin: bottom;
	transform: transform 0.5s;
}
.container .box h2
{
	position: absolute;
	Left: 40px;
	top: 60px;
	font-size: 4em;
	font-weight: 800;
	z-index: 1;
	opacity: 0.1;
	transition: 0.5s;
}
.container .box:hover h2
{
	opacity: 1;
	color: #fff;
	transform: translateY(-40px);
}
.container .box h3
{
position: relative;
font-size: 1.5em;
z-index: 2;
color: #333;
transition: 0.5s;
}
.container .box p
{
position: relative;
z-index: 2;
color: #555;
transition: 0.5s;
}
.container .box:hover h3,
.container .box:hover p
{
color: #fff;
}
</style>
</head>
<body>
<div class="container">
<div classs="box">
<h2>01</h2>
<h3>Service One</h3>
<p>Lorem ipsum dolor sit amet, consectetur adipisicing
elit, sed do eiusmod
tempor incididunt ut labore et dolore maga aliqua.ut
enim ad minim veniam.</p>
</div>
<div classs="box">
<h2>02</h2>
<h3>Service Two</h3>
<p>Lorem ipsum dolor sit amet, consectetur adipisicing
elit, sed do eiusmod
tempor incididunt ut labore et dolore maga aliqua.ut
enim ad minim veniam.</p>
</div>
<div classs="box">
<h2>03</h2>
<h3>Service Three</h3>
<p>Lorem ipsum dolor sit amet, consectetur adipisicing
elit, sed do eiusmod
tempor incididunt ut labore et dolore maga aliqua.ut
enim ad minim veniam.</p>
</div>
</div>

</body>
</html>

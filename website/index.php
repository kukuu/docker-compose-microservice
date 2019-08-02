<!DOCTYPE html>
<html>
<head>
	<title>My Cafe</title>
</head>
<body>
	<h1>Welcome Home</h1>
	<ul>
		<?php

			$json = file_get_contents('http://product-service');//String
			$obj = json_decode($json);//json

			$products = $obj->products;
			foreach ($products as $product) {
				echo "<li>$product</li>";
			}

		?>
	</ul>

</body>
</html>
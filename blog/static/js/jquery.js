
function like(pk) {


	$('#likes').text(parseInt($('#likes').text())+1)

	
console.log(`{% url 'blog:like' pk=${pk} %}`)
 var xhttp = new XMLHttpRequest();
 xhttp.open("POST", `/like/${pk}/`, true);
 xhttp.send();




}
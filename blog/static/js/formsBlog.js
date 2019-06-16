function clicar(teste){

	console.log(Math.floor(Math.random()*10));
	

}



$( document ).ready(function() {






   // $(".numberinput").before(" <a onclick = 'clicar(input.fas)'><i style='font-size:16px margin-top 20px;' class='fas'>&#xf6cf;</i> </a>");

 idDados = 0;
$(".numberinput").each(function(){
	$(this).before("<a onclick = 'clicar(idDados)'><i style='font-size:16px margin-top 20px;' class='fas'>&#xf6cf;</i> </a>");
	$(this).prev("a").attr('id', idDados);
	idDados = idDados + 1;
});
	

});
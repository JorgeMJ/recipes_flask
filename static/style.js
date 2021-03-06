/* It contains the JavaScript functions to show/hide the description of recipes (showDescription),
   and to select  */


function showDescription(id){
	/* Toggles the description of each displayed recipe */
    let x = document.getElementById('descript'+id);

	if (x.style.display !== "block"){
		x.style.display = "block";
	}
	else{
		x.style.display = "none";
	}
}

function uncheckAll(){
	/* Unchecks option 'All' form 'Get recipe Form' if any other option is checked */
	$('.kindRecipesAll')[0].checked=false;
}

function uncheckKindRecipes(){
	/* Unchecks any option form 'Get recipe Form' if option 'All' is checked. */
	let kindRecipes = $('.kindRecipes');

	for(i=0; i < kindRecipes.length; i++){
		kindRecipes[i].checked = false;
	}
}
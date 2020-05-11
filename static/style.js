/* 
File:        js/style.js
Description: It contains the JavaScript functions to toggle the buttons to get recipes (getBtnRecipes),
             add recipes (addBtnRecipes), and show the description of recipes (showDescription)
*/

function toggle(htmlItem){
	/* Toggles the htmlItem passed as an argument */
	let x = document.getElementById(htmlItem);

	if (x.style.display !== "block"){
		x.style.display = "block";
	}
	else{
		x.style.display = "none";
	}
}

function showDescription(id){
	/* Toggles the description of each displayed recipe */
    toggle(`descript${id}`); 
}

function uncheckAll() {
	/* Unchecks option 'All' form 'Get recipe Form' if any other option is checked */
	$('.kindRecipesAll')[0].checked=false;
}

function uncheckKindRecipes(){
	/* Unchecks any option form 'Get recipe Form' if option 'All' is checked. */
	let kindRecipes = $('.kindRecipes');

	for(i=0; i < kindRecipes.length; i++)
	{
		kindRecipes[i].checked = false;
	}
}
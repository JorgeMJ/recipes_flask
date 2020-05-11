/* 
File:        js/style.js
Description: It contains the JavaScript functions to toggle the buttons to get recipes (getBtnRecipes),
             add recipes (adddBtnRecipes), and show the description of recipes (showDescription)
*/

function toggle(htmlItem){
	var x = document.getElementById(htmlItem);

	if (x.style.display !== "block"){
		x.style.display = "block";
	}
	else{
		x.style.display = "none";
	}
}

function showDescription(id){
    toggle(`descript${id}`); 
}




//OUTPUT: In 'kind' recipes, it unchecks 'All' whenever any other option is checked. 
function uncheckAll() {
	$(document).getElementsByClass('kindRecipes')[0].checked=false;
}

//OUTPUT: In 'kind' recipes, it unchecks every kind whenever 'All' is checked.
function uncheckKindRecipes(){
	let kindRecipes = document.getElementsByClass('kindRecipes');

	for(i=1; i < kindRecipes.length; i++)
	{
		kindRecipes[i].checked = false;
	}
}
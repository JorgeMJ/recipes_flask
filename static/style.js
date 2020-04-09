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

function getBtnToggle(){
    toggle("getRecipes-container");
}

function addBtnToggle(){
    toggle("addRecipes-container");
}

function showDescription(id){
    toggle(`descript${id}`); 
}
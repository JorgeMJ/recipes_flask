/* *DESCRIPTION* */
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
	toggle("getRecipes");
}

function addBtnToggle(){
    toggle("addRecipes");
}

function showDescription(id){
	toggle(`descript${id}`); 
}
function getBtnToggle(){
	var x = document.getElementById("getRecipes");

	if (x.style.display !== "block"){
		x.style.display = "block";
	}

	else{
		x.style.display = "none";
	}
}

function addBtnToggle(){
	var x = document.getElementById("addRecipes");

	if (x.style.display !== "block"){
		x.style.display = "block";
	}

	else{
		x.style.display = "none";
	}
}

function showDescription(id){
	var x = document.getElementById(`descript${id}`); 

	if (x.style.display !== "block"){
		x.style.display = "block";
	}

	else{
		x.style.display = "none";
	}
}
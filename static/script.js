
$(document).ready(function()
{
	/*Makes option 'All' from 'Get Recipe Form' checked as default if no
	 other option is already selected.*/ 
	 
	let isChecked = false;
	let kindRecipes = $('.kindRecipes');

	for(i=0; i < kindRecipes.length; i++)
	{
		if(kindRecipes[i].checked == true)
		{
			isChecked = true;
		}
	}

	if (isChecked == false)
	{
		$("#all").attr('checked', 'checked');	
	}
});
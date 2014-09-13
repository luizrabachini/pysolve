/*
 * pySolve Coin Determiner JS
 */

$("#selected-value-file").click(function(e) {
	$("#input-value-file").click();
});

$("#input-value-file").change(function(e) {
	var filename = $(this).val().split('\\').pop();
	$("#selected-value-file").val(filename);   
});
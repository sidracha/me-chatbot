
/*
function on_send_click() {

	$("#send-button")[0].onclick = function (e) {
		send_message();
	}

}
*/

function on_enter_click() {

	
	$(document).keypress(function (e) {
		const key = e.which;
		if (key != 13) {return;}

		send_message();

	})

}

function create_message_div(you_msg, ai_msg) {
	
	
	let you_div = $("<div>");
	let ai_div = $("<div>");


	const hr1 = $("<hr>");
	const hr2 = $("<hr>");
	const hr3 = $("<hr>");
	const hr4 = $("<hr>");

	
	const you_p = $("<p>").html("You: " + you_msg);
	const ai_p = $("<p>").html("AI: " + ai_msg);

	you_div.append(hr3, you_p, hr1);
	ai_div.append(hr4, ai_p, hr2);
	
	container = $("<div>", {
		"class": "py-2"
	});
	container.append(you_div, ai_div);

	return container;


	return container;

}

function display_message_div(container) {
	
	$("#main-div").append(container);


}

function send_message() {
		const val = $("#input-box").val().trim();
		const data = {"message": val};
		
		$("#input-box")[0].value = "";

		if (val === "") {
			
			return;

		}

		$.ajax({
			
			url: "/chat",
			method: "POST",
			data: JSON.stringify(data),
			contentType: "application/json"

		}).done(function (resp) {
				
			display_message_div(create_message_div(val, resp.response));
			const textarea = $("#input-box");
			textarea.prop("selectionStart", 0);
			textarea.prop("selectionEnd", 0);
			textarea.focus();
			window.scrollTo(0, document.body.scrollHeight);


		})

}

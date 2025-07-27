$(document).ready(function () {
	$("#remember").on("change", function () {
		if ($(this).is(":checked")) {
			const username = $("#username").val();

			localStorage.setItem("username", username);
			localStorage.setItem("remember", true);
		} else {
			localStorage.removeItem("username");
			localStorage.setItem("remember", false);
		}
	});

	let remember = localStorage.getItem("remember");
	if (remember == "true") {
		const username = localStorage.getItem("username");

		$("#username").val(username);
		$("#remember").prop("checked", true);
	}
});

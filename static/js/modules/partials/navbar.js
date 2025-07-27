function toggleMenuIcon() {
	var windowWidth = $(window).width();
	if (windowWidth < 991) {
		$("#mobileMenuIcon").show();
	} else {
		$("#mobileMenuIcon").hide();
	}
}

$(window).resize(toggleMenuIcon);

$(document).ready(toggleMenuIcon);

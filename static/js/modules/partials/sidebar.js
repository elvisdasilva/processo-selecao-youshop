$(document).ready(function () {
	const toggleMenuIcon = $("#toggleMenuIcon");
	const body = $("body")[0];

	toggleMenuIcon.on("click", function () {
		if (body.classList.contains("sidebar-collapse")) {
			localStorage.setItem("sidebarState", "expanded");
		} else {
			localStorage.setItem("sidebarState", "collapsed");
		}
	});

	const sidebarState = localStorage.getItem("sidebarState");
	if (sidebarState === "collapsed") {
		body.classList.add("sidebar-collapse");
	}

	let url = window.location;

	$("ul.nav-sidebar .nav-item").removeClass("active");

	$("ul.nav-sidebar a")
		.filter(function () {
			if (this.href) {
				return this.href === url || url.href.indexOf(this.href) === 0;
			}
		})
		.addClass("active");
});

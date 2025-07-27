export function defaultOptions() {
	let options = {
		paging: true,
		lengthChange: true,
		searching: true,
		ordering: true,
		info: true,
		autoWidth: false,
		responsive: true,
		dom: "lBfrtip",
		buttons: [
			{
				extend: "excelHtml5",
				text: `<i class="fas fa-file-export"></i> Exportar para Excel`,
			},
			{
				extend: "colvis",
				text: `<i class="fas fa-columns"></i> Colunas Visíveis`,
			},
		],
		language: {
			url: "//cdn.datatables.net/plug-ins/2.0.0/i18n/pt-BR.json",
		},
	};

	return options;
}

$(document).ready(function () {
	setTimeout(function () {
		$(".alert").remove();
	}, 5000);
});

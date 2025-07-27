import { defaultOptions } from "../../utils.js";

$(document).ready(function () {
	let planted_tree_table = $("#tablePlantedTree");
	planted_tree_table.DataTable(defaultOptions());

	$(".select2bs4.tree").select2({
		theme: "bootstrap4",
		placeholder: "Selecione a árvore",
		allowClear: true,
		language: "pt-BR",
		width: "100%",
	});

	$(".select2bs4.account").select2({
		theme: "bootstrap4",
		placeholder: "Selecione a conta",
		allowClear: true,
		language: "pt-BR",
		width: "100%",
	});
});

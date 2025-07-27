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

	$(".location_latitude, .location_longitude").mask("0000.000000", {
		reverse: true,
	});

	$("#add-form").click(function () {
		const totalForms = $("#id_form-TOTAL_FORMS");
		const formCount = parseInt(totalForms.val());

		const $originalForm = $(".formset-form:first");

		$originalForm.find("select").select2("destroy");

		const $newForm = $originalForm.clone(false);

		$originalForm.find("select.tree").select2({
			theme: "bootstrap4",
			placeholder: "Selecione a árvore",
			allowClear: true,
			language: "pt-BR",
			width: "100%",
		});

		$originalForm.find("select.account").select2({
			theme: "bootstrap4",
			placeholder: "Selecione a conta",
			allowClear: true,
			language: "pt-BR",
			width: "100%",
		});

		$newForm.find(":input").each(function () {
			const name = $(this).attr("name");
			const id = $(this).attr("id");

			if (name) {
				$(this).attr("name", name.replace(/form-(\d+)-/, `form-${formCount}-`));
			}
			if (id) {
				$(this).attr("id", id.replace(/form-(\d+)-/, `form-${formCount}-`));
			}

			if ($(this).is("input, textarea")) {
				$(this).val("");
			}
			if ($(this).is("select")) {
				$(this).removeAttr("data-select2-id");
				$(this).val("").change();
			}
		});

		$newForm.find(".location_latitude, .location_longitude").mask("0000.000000", {
			reverse: true,
		});

		$newForm.find("select.tree").select2({
			theme: "bootstrap4",
			placeholder: "Selecione a árvore",
			allowClear: true,
			language: "pt-BR",
			width: "100%",
		});
		$newForm.find("select.account").select2({
			theme: "bootstrap4",
			placeholder: "Selecione a conta",
			allowClear: true,
			language: "pt-BR",
			width: "100%",
		});

		$newForm.find(".card-title").text(`Árvore ${formCount + 1}`);

		totalForms.val(formCount + 1);
		$("#formset-container").append($newForm);
	});
});

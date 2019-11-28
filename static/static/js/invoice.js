$(function(){

	let loadForm = function () {
		let btn = $(this);
		$.ajax({
			url: btn.attr("data-url"),
			type: 'get',
			dataType: 'json',
			beforeSend: () => {
				$("#modal-invoice").modal("show");
			},
			success: (data) => {
				$('#modal-invoice .modal-content').html(data.html_form)
			}
		});
	};
	let saveForm = function () {
		let form = $(this);
		$.ajax({
			url: form.attr("action"),
			data: form.serialize(),
			type: form.attr("method"),
			dataType: 'json',
			success: (data) =>{
				if (data.form_is_valid){
					$("#invoice-table tbody").html(data.html_invoice_list);
			          $("#modal-invoice").modal("hide");
			        }
		        else {
		          $("#modal-invoice .modal-content").html(data.html_form);
		        }
		      }
		    });
		    return false;
		  };

	/* Binding Invoices */


	// Create invoice
	$(".js-create-invoice").click(loadForm);
	$("#modal-invoice").on("submit", ".js-invoice-create-form", saveForm);

	// Update invoice
	$("#invoice-table").on("click", ".js-update-invoice", loadForm);
	$("#modal-invoice").on("submit", ".js-invoice-update-form", saveForm);

	// Delete Invoice
	$("#invoice-table").on("click", ".js-delete-invoice", loadForm);
	$("#modal-invoice").on("submit", ".js-invoice-delete-form", saveForm);
	});
	// End of Invoices Binding

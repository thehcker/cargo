$(() => {
	$('.js-create-invoice').click(() => {
		$.ajax({
			url: '/invoice/create/',
			type: 'get',
			dataType: 'json',
			beforeSend: () => {
				$('#modal-invoice').modal("show");
			},
			success: (data) => {
				$('#modal-invoice .modal-content').html(data.html_form)
			}
		});
	});
	$('#modal-invoice').on("submit", ".js-invoice-create-form", () => {
		let form = $(this)
		$.ajax({
			url: form.attr('action'),
			data: form.serialize(),
			type: form.attr('method'),
			dataType: 'json',
			success: (data) => {
				if (data.form_is_valid){
					$('#invoice-table tbody').html(data.html_invoice_list);
					$("#modal-invoice").modal("hide");
				}else{
					$('#modal-invoice .modal-content').html(data.html_form)
				}
			}
		});
	return false;
	});
});
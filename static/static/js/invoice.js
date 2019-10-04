$(function(){
	$('.js-create-invoice').click(function(){
		$.ajax({
			url: '/invoice/create/',
			type: 'get',
			dataType: 'json',
			beforeSend: function(){
				$('#modal-invoice').modal("show");
			},
			success: function(data){
				$('#modal-invoice .modal-content').html(data.html_form)
			}
		});
	});
	$('#modal-invoice').on("submit", ".js-invoice-create-form", function(){
		let form = $(this)
		$.ajax({
			url: form.attr('action'),
			data: form.serialize(),
			type: form.attr('method'),
			dataType: 'json',
			success: function(data){
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
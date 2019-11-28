$(function(){

    let loadForm = function () {
        let btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: () => {
                $("#modal-hom").modal("show");
            },
            success: (data) => {
                $('#modal-hom .modal-content').html(data.html_form)
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
                      $("#modal-hom").modal("hide");
                    }
                else {
                  $("#modal-hom .modal-content").html(data.html_form);
                }
              }
            });
            return false;
          };
    
/* Binding Invoices */


// Binding hom
// Create hom
$(".js-create-hom").click(loadForm);
$("#modal-hom").on("submit", ".js-hom-create-form", saveForm);

 // Update hom
$("#invoice-table").on("click", ".js-update-hom", loadForm);
$("#modal-hom").on("submit", ".js-hom-update-form", saveForm);

// Delete hom
$("#invoice-table").on("click", ".js-delete-hom", loadForm);
$("#modal-hom").on("submit", ".js-hom-delete-form", saveForm);
});
// End of hom Binding
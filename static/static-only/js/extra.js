$(function(){

    let loadForm = function () {
        let btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: () => {
                $("#modal-extra").modal("show");
            },
            success: (data) => {
                $('#modal-extra .modal-content').html(data.html_form)
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
                      $("#modal-extra").modal("hide");
                    }
                else {
                  $("#modal-extra .modal-content").html(data.html_form);
                }
              }
            });
            return false;
          };
    
    /* Binding Invoices */
    
    
    // Binding Extra
    // Create Extra
    $(".js-create-extra").click(loadForm);
    $("#modal-extra").on("submit", ".js-extra-create-form", saveForm);
    
    // Update Extra
    $("#invoice-table").on("click", ".js-update-extra", loadForm);
    $("#modal-extra").on("submit", ".js-extra-update-form", saveForm);
    
    // Delete Extra
    $("#invoice-table").on("click", ".js-delete-extra", loadForm);
    $("modal-extra").on("submit", ".js-extra-delete-form", saveForm);
    // End of Extra Binding
    });
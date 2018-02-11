$(document).ready(function() {
    $("#id_gastro-gastros").change(function () {
        var gastro_id = $("#id_gastro-gastros").val();

        gastro_ajax(gastro_id);
    });


    var gastro_id_submit = $("#id_gastro-gastros").val();
    gastro_ajax(gastro_id_submit);


    function gastro_ajax(gastro_id) {
        $.ajax({
            url: '/rest-api/gastro/' + gastro_id + '/',
            dataType: 'json',
            success: function (data) {
                if (data) {

                    var submit_value;
                    for (const key in data) {
                        $("#id_submit-" + key).parent().closest("tr").removeClass("table-danger");


                        $("#id_" + key).html(data[key]);
                        var submit_td_input = $("#id_submit-" + key);

                        if (submit_td_input.is(":input")) {
                            submit_value = submit_td_input.val();
                        }
                        if (submit_td_input.is("select")) {
                            submit_value = $("#id_submit-" + key+ " option:selected").text();
                        }
                        if (submit_td_input.is(":checkbox")) {
                            submit_value = submit_td_input.is(':checked');
                        }
                        console.log(data[key] + ' - ' + submit_value);

                        if(!(data[key] === submit_value))
                        {
                           $("#id_submit-" + key).parent().closest("tr").addClass("table-danger");
                        }

                    }

                }
            }
        });

    }
});
jQuery.datetimepicker.setLocale('en');

jQuery($('form').find("input[data-picker='timepicker']")).datetimepicker({
    datepicker: false,
    step: 30,
    format:'H:i'
});
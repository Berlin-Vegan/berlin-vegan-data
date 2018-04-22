jQuery.datetimepicker.setLocale('en');

jQuery($('form').find("input[data-picker='timepicker-opens']")).datetimepicker({
    datepicker: false,
    step: 30,
    format:'H:i',
    defaultTime:'10:00'
});

jQuery($('form').find("input[data-picker='timepicker-closes']")).datetimepicker({
    datepicker: false,
    step: 30,
    format:'H:i',
    defaultTime:'18:00'
});
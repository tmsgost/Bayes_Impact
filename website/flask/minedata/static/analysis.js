$(document).ready(function(){    
  $("#calculate").click( function() {
      var value = getValue();
      $("#score-out").text(value);
      $("#score-out-panel").show();
    });
});

function getValue() {
    var operator = $("#operator").val();
    var controller = $("#controller").val();
    var type = $("#type").val();
    var status = $("#status").val();
    var pits = $("#multiple-pits").is(':checked');
    var employees = $("#employees").val();

    return "err";
}

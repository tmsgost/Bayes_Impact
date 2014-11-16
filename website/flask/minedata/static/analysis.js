$(document).ready(function(){    
  $("#calculate").click( function() {
      var value = getValue();
      $("#score-out").text(value);
      $("#score-out-panel").show();
    });
});

function getValue() {
    return 9;
}

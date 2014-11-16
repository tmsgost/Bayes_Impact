$(document).ready(function(){    
  $("#calculate").click( function() {
      var value = getValue();
      $("#score-out").text(value);
      $("#score-out-panel").show();
    });
});

function getValue() {
    var thisoperator = $("#operator").val();
    var thiscontroller = $("#controller").val();
    var thistype = $("#type").val();
    var thisstatus = $("#status").val();
    var thispits = $("#multiple-pits").is(':checked') ? 1 : 0;
    var thiscanvas = $("#canvas").val();
    var thisemployees = $("#employees").val();

    var operator = {};
    var controller = {};
    var current_mine_type = {};
    var primary_canvass_cd = {};
    var current_mine_status = {};
    var intercept = -0.888896;
    operator['00000'] = 0.0;
    operator['0052652'] = 169.1807;
    operator['0070543'] = 1043.591;
    operator['0133354'] = 1620.040;
    operator['P18954'] = 579.4654;
    operator['P22901'] = 312.9977;
    operator['P22918'] = 620.1648;
    operator['P23960'] = 710.5481;
    operator['P24237'] = 8.956473;
    operator['P24238'] = -36.98322;
    operator['P24453'] = 0.0;
    controller['00000'] = 0.0;
    controller['0041473'] = 49.69910;
    controller['0079293'] = 20.53214;
    controller['0083673'] = 10.69881;
    controller['0102049'] = 174.4073;
    controller['0106783'] = 64.7888;
    controller['0108063'] = 180.9841;
    controller['0113483'] = 1620.040;
    controller['C10977'] = 0.0;
    controller['C15311'] = 250.4140;
    controller['M11292'] = 10.71968;
    current_mine_type['facility'] = 0.0;
    current_mine_type['surface'] = -2.378204;
    current_mine_type['underground'] = 5.200240;
    primary_canvass_cd['1.0']=0.0;
    primary_canvass_cd['2.0']= 3.704141;
    primary_canvass_cd['5.0']= 6.254072;
    primary_canvass_cd['6.0']= 6.473796;
    primary_canvass_cd['7.0']= 5.843520;
    primary_canvass_cd['8.0']= 6.154869;
    current_mine_status['Abandoned'] = -5.341325;
    current_mine_status['Abandoned and Sealed'] = -5.341325;
    current_mine_status['Active'] = 1.993061;
    current_mine_status['Intermittent'] = 0.3342219;
    current_mine_status['New Mine'] = 0.2060835;
    current_mine_status['NonProducing'] = 0.6508366;
    current_mine_status['Temporarily Idled'] = 0.03258712;
    multiple_pits = -7.253592;
    avg_employee_cnt = 0.1138435;
    console.log(operator);

    console.log(thisoperator);
    console.log(operator[thisoperator]);
    console.log(operator.thisoperator);
    return intercept + operator.thisoperator + controller.thiscontroller + current_mine_type.thistype + primary_canvass_cd.thiscanvass + current_mine_status.thisstatus + avg_employee_cnt * thisemployees + multiple_pits * thispits;
}

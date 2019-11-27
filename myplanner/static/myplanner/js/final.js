function getdate() {
  var date_field = document.getElementById("date");
  var current_date = new Date();
  var pmoram;
  if (current_date.getHours() < 12) {
    pmoram = "AM";
  } else {
    pmoram = "PM";
  }

  var minutes = current_date.getMinutes();
  if (minutes < 10) {
    minutes = "0" + minutes;
  }
  var month = parseInt(current_date.getMonth()) + 1;

  var my_date =
    current_date.getHours() +
    ":" +
    minutes +
    " " +
    pmoram +
    " <br>" +
    month +
    "/" +
    current_date.getDate() +
    "/" +
    current_date.getFullYear();

  if (date_field != null) {
    date_field.innerHTML = my_date;
  }
}

setInterval(() => {
  getdate();
}, 0);

$(document).ready(function() {
  // sign in sign up
  $("#sign-in-show-button").click(function() {
    $("#sign-up-show-button")
      .css("background", "rgb(180, 253, 211)")
      .css("color", "rgb(90, 90, 90)");
    $(this)
      .css("background", "rgb(60, 230, 130)")
      .css("color", "#000");
    $("#sign-up-form").hide();
    $("#sign-in-form").show("slow");
  });

  $("#sign-up-show-button").click(function() {
    $("#sign-in-show-button")
      .css("background", "rgb(180, 253, 211)")
      .css("color", "rgb(90, 90, 90)");
    $("#sign-in-form").hide();
    $("#sign-up-form").show("slow");
    $(this)
      .css("background", "rgb(60, 230, 130)")
      .css("color", "#000");
  });
  // end of sign in sign up

  $(
    "#delete-button , #completed-button, #weather-form button, #submit-task-form button"
  ).attr("disabled", "disabled");
  $(
    "#delete-button , #completed-button, #weather-form button, #submit-task-form button"
  ).css("opacity", "0.6");

  $("input[name=task]").change(function() {
    if ($(this).val()) {
      $("#delete-button , #completed-button")
        .removeAttr("disabled")
        .css("opacity", "1");
    }
  });

  //only showing submit button for adding tasks if task  to add has been typed
  $("input[name=task_to_add]").keyup(function() {
    if ($(this).val()) {
      $("#submit-task-form button")
        .removeAttr("disabled")
        .css("opacity", "1");
    } else {
      $("#submit-task-form button")
        .attr("disabled", "disabled")
        .css("opacity", "0.6");
    }
  });

  $("input[name=weather]").keyup(function() {
    if ($(this).val()) {
      $("#weather-form button")
        .removeAttr("disabled")
        .css("opacity", "1");
    } else {
      $("#weather-form button")
        .attr("disabled", "disabled")
        .css("opacity", "0.6");
    }
  });

  $("#weather-button").click(function() {
    $(".task-info").hide();
    $("#task-button").css("background", "rgb(180, 253, 211)");
    $("#task-button").css("color", "rgb(90, 90, 90)");
    $("#weather-button").css("color", "#000");
    $(".weather-info").animate({ opacity: "show" }, 1500);

    $("#weather-button").css("background", "rgb(60, 230, 130)");
  });

  $("#task-button").click(function() {
    $(".weather-info").hide();
    $("#weather-button").css("background", "rgb(180, 253, 211)");
    $("#weather-button").css("color", "rgb(90, 90, 90)");
    $("#task-button").css("color", "#000");
    $(".task-info").animate({ opacity: "show" }, 1500);
    $("#task-button").css("background", "rgb(60, 230, 130)");
  });

  $("#all-tasks-button").click(function() {
    $(".completed-tasks").hide();
    $(".uncompleted-tasks").hide();
    $(".all-tasks").show("slow");
    $("#completed-button").show("slow");
    $(".task-history").hide();
    $("#delete-button").show("slow");
  });

  $("#completed-tasks-button").click(function() {
    $(".all-tasks").hide();
    $(".uncompleted-tasks").hide();
    $(".completed-tasks").show("slow");
    $("#completed-button").hide();
    $(".task-history").hide();
    $("#delete-button").hide();
  });

  $("#uncompleted-tasks-button").click(function() {
    $(".completed-tasks").hide();
    $(".all-tasks").hide();
    $(".uncompleted-tasks").show("slow");
    $("#completed-button").hide();
    $(".task-history").hide();
    $("#delete-button").hide();
  });

  $("#tasks-history-button").click(function() {
    $(".completed-tasks").hide();
    $(".all-tasks").hide();
    $(".uncompleted-tasks").hide();
    $("#completed-button").hide();
    $("#delete-button").hide();
    $(".task-history").show("slow");
  });

  // weather functions
  $("#get-weather").click(function() {
    let myapikey = "cb985a603de43aeae7da551d29ee9351";
    q = $("#city").val();
    $.getJSON(
      "https://api.openweathermap.org/data/2.5/weather?q=" +
        q +
        "&appid=" +
        myapikey +
        "&units=metric",
      function(data) {
        let city = data.name;

        document.getElementById("weather-heading").innerHTML =
          "weather for &nbsp;" + city + "<div id='weather-icon'></div>";
        weather_icon =
          "http://openweathermap.org/img/w/" + data.weather[0].icon + ".png";
        $("#weather-icon").css("display", "inline-block");
        $("#weather-icon").css("background-image", "url(" + weather_icon + ")");
        $("#weather-icon").css("background-size", "cover");

        document.getElementById("temperature").innerHTML =
          "Temperature: " + data.main.temp + "<sup>o</sup>";
        // "<img src='' id='weather-icon' />";

        document.getElementById("humidity").innerHTML =
          "Humidity: " + data.main.humidity + "&nbsp;g/m<sup>3</sup>";

        document.getElementById("pressure").innerHTML =
          "Pressure: " + data.main.pressure + "&nbsp;Pascal(PA)";

        document.getElementById("min-temp").innerHTML =
          "Min-temperature: " + data.main.temp_min + "<sup>o</sup>";

        document.getElementById("max-temp").innerHTML =
          "Max-temperature: " + data.main.temp_max + "<sup>o</sup>";
      }
    );
  });
});

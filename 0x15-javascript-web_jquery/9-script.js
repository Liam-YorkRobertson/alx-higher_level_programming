$(document).ready(function () {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr%27',
    method: 'GET',
    dataType: 'json',
    success: function (data) {
      $('div#hello').text(data.hello);
    }
  });
});

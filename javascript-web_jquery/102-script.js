#!/usr/bin/node

$(document).ready(() => {
  $('#btn_translate').click(() => {
    const lang = $('#language_code').val();

    $.ajax({
      url: `https://www.fourtonfish.com/hellosalut/?lang=${lang}`,
      type: 'GET',
      dataType: 'json',
      crossDomain: true,
      xhrFields: {
        withCredentials: true
      },
      headers: {
        accept: 'application/json',
        'Access-Control-Allow-Origin': '*'
      }
    }).done((data) => {
      $('#hello').html(data.hello);
    });
  });
});

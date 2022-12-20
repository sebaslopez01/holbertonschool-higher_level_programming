#!/usr/bin/node

$.ajax({
  url: 'https://stefanbohacek.com/hellosalut/?lang=fr',
  type: 'GET',
  dataType: 'json'
}).done((data) => {
  $('#hello').html(data.hello);
});

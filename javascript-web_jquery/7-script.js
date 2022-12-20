#!/usr/bin/node

$.ajax({
  url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
  type: 'GET',
  dataType: 'json'
}).done((data) => {
  $('#character').html(data.name);
});

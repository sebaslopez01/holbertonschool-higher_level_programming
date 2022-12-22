#!/usr/bin/node

$(document).ready(() => {
  const myList = $('.my_list');

  $('#add_item').click(() => {
    myList.append('<li>Item</li>');
  });

  $('#remove_item').click(() => {
    myList.children().last().remove();
  });

  $('#clear_list').click(() => {
    myList.empty();
  });
});

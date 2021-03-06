$(document).ready( function() {

  // Function for returning articles with AJAX-returned data:
  function post_articles(data) {
    $('#searchresults').empty()
    for (x in data.articles) {
      console.log(data.articles[x].key_words)
      $('#searchresults').append(
        '<div draggable="true" class="panel" id="article_'+ x +'">\
        <a href=' + data.articles[x].url + '>\
        <h4>' + data.articles[x].title + ' \
        (' + data.articles[x].publisher + ')</h4></a>\
        <h6>' + data.articles[x].author + '</h6>\
        <p>' + data.articles[x].blurb + '</p>\
        <p class="keywords">Keywords: ' + data.articles[x].key_words + '</p>\
        </br></div>'
      );
    }
  }

  // AJAX request for All Articles (default page)
  $.get('/all', function(data){
    post_articles(data);
  });

  // AJAX request for Deal Search
  $('#deal_search').click(function(event){
    $.get('/deal_search/' + $('#deal_search_term').val(), function(data){
      post_articles(data);
    });
  });

  // AJAX request for Deal Dropdown
  $('.deal').click(function(event){
    $.get('/deal_search/' + $(this).html(), function(data){
      post_articles(data);
    });
  });


  // AJAX request for Loan Search
  $('#loan_search').click(function(event){
    $.get('/loan_search/' + $('#loan_search_term').val(), function(data){
      post_articles(data);
    });
  });

  // AJAX request for Deal Dropdown
  $('.loan').click(function(event){
    $.get('/loan_search/' + $(this).html(), function(data){
      post_articles(data);
    });
  });


  // AJAX request for Property Search
  $('#property_search').click(function(event){
    $.get('/property_search/' + $('#property_search_term').val(), function(data){
      post_articles(data);
    });
  });

  // AJAX request for Deal Dropdown
  $('.property').click(function(event){
    $.get('/property_search/' + $(this).html(), function(data){
      post_articles(data);
    });
  });

  // Drag and Drop Functions
  function allowDrop(ev) {
    ev.preventDefault();
  }

  function drag(ev) {
      ev.dataTransfer.setData("text", ev.target.id);
  }

  function drop(ev) {
      ev.preventDefault();
      var data = ev.dataTransfer.getData("text");
      ev.target.appendChild(document.getElementById(data));
  }
});

$(document).ready( function() {

  // Function for returning articles with AJAX-returned data:
  function post_articles(data) {
    $('#searchresults').empty()
    for (x in data.articles) {
      $('#searchresults').append(
        '<a href=' + data.articles[x].url + '>\
        <h4>' + data.articles[x].title + '</h4></a>\
        <p>' + data.articles[x].blurb + '</p></br>'
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

  // AJAX request for Loan Search
  $('#loan_search').click(function(event){
    $.get('/loan_search/' + $('#loan_search_term').val(), function(data){
      post_articles(data);
    });
  });

  // AJAX request for Property Search
  $('#property_search').click(function(event){
    $.get('/property_search/' + $('#property_search_term').val(), function(data){
      post_articles(data);
    });
  });
});

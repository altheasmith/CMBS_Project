$(document).ready( function() {
  $.get('/all', function(data){
    console.log(data.articles)
    $('#searchresults').empty()
    for (x in data.articles) {
      $('#searchresults').append(
        '<a href=' + data.articles[x].url + '>\
        <h4>' + data.articles[x].title + '</h4></a>\
        <p>' + data.articles[x].blurb + '</p></br>'
      );
    }
  });
  $('#deal_search').click(function(event){
    $search = $('#deal_search_term').val()
    console.log('term', $('#deal_search_term').val())
    console.log($search)
    $.get('/deal_search/' + $search, function(data){
      $('#searchresults').empty()
      for (x in data.articles) {
        $('#searchresults').append(
          '<a href=' + data.articles[x].url + '>\
          <h4>' + data.articles[x].title + '</h4></a>\
          <p>' + data.articles[x].blurb + '</p></br>'
        );
      }
    });
  });
});

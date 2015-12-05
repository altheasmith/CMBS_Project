$(document).ready( function() {
// Create function for returning articles since its the same in each one
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

  // AJAX request for Deal Search
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

  // AJAX request for Loan Search
  $('#loan_search').click(function(event){
    var $search = $('#loan_search_term').val()
    console.log('term', $('#loan_search_term').val())
    console.log($search)
    var url = String('/loan_search/' + $search)
    $.get(url, function(data){
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

  // AJAX request for Property Search
  $('#property_search').click(function(event){
    var $search = $('#property_search_term').val()
    console.log('term', $('#property_search_term').val())
    console.log($search)
    var url = String('/property_search/' + $search)
    $.get(url, function(data){
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

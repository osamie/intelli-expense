define(['jquery'], function($){
  return {
    start: function(){

      // var form = $(document).find('form#uploadForm');
      var inputEl = document.getElementById('userFile');

      // click handler
      $(document).find('form#uploadForm').submit(function(event){
        event.preventDefault();

        $.ajax({
          type: 'POST',
          url: '/uploadFile',
          contentType: 'text/csv',
          data: inputEl.files[0]
        });

      });
    }
  };
});

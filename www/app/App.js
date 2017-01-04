define(['jquery'], function($){
  return {
    start: function(){
      var inputEl = document.getElementById('userFile');
      var btn = document.getElementById('uploadBtn');
      var files;

      $(inputEl).on('change', function(event){
        files = event.target.files;
      });


      // click handler
      $(document).find('form#uploadForm').on('submit', function(event){
        event.stopPropagation();
        event.preventDefault();

        var data = new FormData();

        $.each(files, function(key, value){
          data.append(key, value);
        });

        $.ajax({
          type: 'POST',
          url: '/uploadFile',
          data: data,
          contentType: false,
          async: false,
          cache: false,
          processData: false,
          error: function(){
            alert('COULD NOT UPLOAD');
          },
          success: function(){
            alert('FILE UPLOADED AND PROCESSED');
          }

        });

      });

    }
  };
});

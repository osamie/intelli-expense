requirejs.config({
  paths: {
    jquery: 'lib/jquery-3.1.1.min',
    app: 'app/App'
  }
});

require(['app'], function(App){
  App.start();
});

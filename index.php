<html>
  <head>
    <script src="http://code.jquery.com/jquery-1.9.1.js"></script>
    <script>
      $(function () {

        $('form').on('submit', function (e) {

          e.preventDefault();

          $.ajax({
            type: 'post',
            url: 'http://159.89.8.122:5000/data',
            data: $('form').serialize(),
            success: function (data) {
              $('#response').html(data);
              alert('success');
            }
          });

        });

      });
    </script>
  </head>
  <body>
    <form>
      <input id="url" name="url"><br>
      <input name="submit" type="submit" value="Submit">
    </form>
    <div id="response"></div>
  </body>
</html>

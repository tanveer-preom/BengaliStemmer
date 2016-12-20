<!DOCTYPE html>
<html lang="en">
   <head>
      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
      <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0"/>
      <title>Bengali Stemmer</title>
       <style type="text/css">
      
          .test{
            width: 70%;
            height: 40%;
          }

                  /* Paste this css to your style sheet file or under head tag */
        /* This only works with JavaScript, 
        if it's not present, don't show loader */
        .no-js #loader { display: none;  }
        .js #loader { display: block; position: absolute; left: 100px; top: 0; }
        .se-pre-con {
          position: fixed;
          left: 0px;
          top: 0px;
          width: 100%;
          height: 100%;
          z-index: 9999;
          background: url(http://smallenvelop.com/wp-content/uploads/2014/08/Preloader_21.gif) center no-repeat #fff;
}


      </style>
      <!-- CSS  -->
      <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
      <link href="css/materialize.css" type="text/css" rel="stylesheet" media="screen,projection"/>
      <link href="css/style.css" type="text/css" rel="stylesheet" media="screen,projection"/>
     

  
      <!--  Tanveer Islam Preom
       CSE 12 Batch, SUST -->
       

   </head>
   <body>

    <div class="se-pre-con"></div>


      <nav class="light-blue lighten-1" role="navigation">
         <div class="nav-wrapper container"><a  class="brand-logo">SUST Bengali Stemmer</a>
            <a href="#" data-activates="nav-mobile" class="button-collapse"><i class="material-icons">menu</i></a>
         </div>
      </nav>

  


      <div class="section no-pad-bot" id="index-banner">
         <div class="container text-center">
            <br><br>
            <center>
               <img src="{!! asset('sust.png')!!}" alt="Mountain View" style="width:150px;height:150px;">
               <div class="row center">
                  <h5 class="header col s12 light">A Corpus Based Unsupervised Bangla Word
                     Stemming  <br> Using N-Gram Language Model
                  </h5>
               </div>
            </center>




            
              {!! Form::open(array('url' => '/generate', 'method' => 'post', 'files' => true, 'id'=>'empty')) !!}
               <center>
                  <div class="form-group">
                     <div class="form-group">
                        <label for="exampleTextarea">
                           <h5><b>Input Text Here</b></h5>
                        </label>
                        <textarea class="form-control" name='text' id="exampleTextarea"  rows="3" style="width: 700px; height: 300px;"><?php echo $text; ?></textarea>
                     </div>

                     <h5 class="text_center">"OR" </h5><br>

                  

                     <div class="file-field input-field test">
                        <div class="btn but">
                          <span>Upload File</span>
                          <input type="file" name="file" id="fileBox" accept='text/*' onchange="validate_fileupload(this.value);">
                        </div>
                        <div class="file-path-wrapper">
                          <input placeholder="No File Selected....(Upload Only Text File)" class="file-path validate" type="text">
                        </div>
                    </div><br>

                    
                     <button type="submit" class="btn green" style='width:300px;'>Submit</button>
               </center>
             {!! Form::close() !!}

            <br><br>
            </div>
         </div>



         <form>
            <center>
               <div class="form-group">
                  <label for="exampleTextarea">
                     <h5><b>Stemming Result</b></h5>
                  </label>
                  <textarea class="form-control" id="exampleTextarea" rows="3" style="width: 700px; height: 300px;"><?php echo $contents; ?></textarea>
               </div>
            </center>
         </form>

        
       @if( strpos($filepath, '/Data/Output/') === 0)
        <center>
           <p>  <em>Download Stemming Result.....</em> <a download href="{!! $filepath!!}" target="_blank"><i class="material-icons">get_app</i></a></p>
        </center>
        @else
        @endif

         <br><br>
         <div class="section">
         </div>
      </div>







      <footer class="page-footer orange">
         <div class="container">
            <div class="row">
               <div class="col l6 s12">
                  <h5 class="white-text">About </h5>
                  <p class="grey-text text-lighten-4">A Corpus Based Unsupervised Bangla Word
                     Stemming Using <br> N-Gram Language Model</p>
               </div>
            </div>
         </div>
         <div class="footer-copyright">
            <div class="container">
               Prepared by <a class="orange-text text-lighten-3" href="http://nlp.sust.edu/" target="_blank">SUST NLP RESEARCH GROUP</a>
            </div>
         </div>
      </footer>


      <!--  Scripts-->
      <script src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
      <script src="js/materialize.js"></script>
      <script src="js/init.js"></script>
     
      <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.5.2/jquery.min.js"></script>
     <script src="http://cdnjs.cloudflare.com/ajax/libs/modernizr/2.8.2/modernizr.js"></script>



      <script type="text/javascript">

      //loader
        // Wait for window load
        $(window).load(function() {
          // Animate loader off screen
          $(".se-pre-con").fadeOut("slow");;
        });






      //check double field empty or not
       document.getElementById("empty").onsubmit = function () {
        if (!document.getElementById("exampleTextarea").value) {
                if (!document.getElementById("fileBox").value) {
                      alert('Can not Submit without Input');
                      return false;
                }else{
                      return true;
                }
            }
        } 


      //validate upload file       
       function validate_fileupload(fileName)
        {
            var allowed_extensions = new Array("txt");
            var file_extension = fileName.split('.').pop(); // split function will split the filename by dot(.), and pop function will pop the last element from the array which will give you the extension as well. If there will be no extension then it will return the filename.

            for(var i = 0; i <= allowed_extensions.length; i++)
            {
                if(allowed_extensions[i]==file_extension)
                {
                    return true; // valid file extension
                }
            }
            alert('Please Insert Only Text File');
            window.location.href = "/";
            return false;

        }
       

      </script>


   </body>
</html>
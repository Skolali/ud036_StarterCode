import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile, .tvshow-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover , .tvshow-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }

        fieldset, label { margin: 0; padding: 0; }
        body{ margin: 20px; }
        h1 { font-size: 1.5em; margin: 10px; }

        /****** Style Star Rating Widget *****/

        .rating { 
          border: none;
          float: left;
        }

        .rating > input { display: none; } 
        .rating > label:before { 
          margin: 5px;
          font-size: 1.25em;
          font-family: FontAwesome;
          display: inline-block;
          content: "\\f005";
        }

        .rating > .half:before { 
          content: "\\f089";
          position: absolute;
        }

        .rating > label { 
          color: #ddd; 
         float: right; 
        }

        /***** CSS Magic to Highlight Stars on Hover *****/

        .rating > input:checked ~ label, /* show gold star when clicked */
        .rating:not(:checked) > label:hover, /* hover current star */
        .rating:not(:checked) > label:hover ~ label { color: #FFD700;  } /* hover previous stars in list */

        .rating > input:checked + label:hover, /* hover current star when changing rating */
        .rating > input:checked ~ label:hover,
        .rating > label:hover ~ input:checked ~ label, /* lighten current selection */
        .rating > input:checked ~ label:hover ~ label { color: #FFED85;  } 
 </style>
 
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            console.log(sourceUrl)
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
          $('.tvshow-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
          $('[data-toggle="tooltip"]').tooltip();   
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.tvshow-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            console.log(sourceUrl)
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        $("label").click(function(){
          $(this).parent().find("label").css({"background-color": "#D8D8D8"});
          $(this).css({"background-color": "#7ED321"});
          $(this).nextAll().css({"background-color": "#7ED321"});
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
   
    <div class="container">
     <a class="navbar-brand">Movies</a>
      <br /><br />
     <div class="container">
      {movie_tiles}
      </div>
    <div class="container">
      <a class="navbar-brand">TV Shows</a>
      <br /><br /> <br /><br />
     </div>
     <div class="container">
      {tv_show_tiles}
      </div>
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" title="{duration_tooltip}" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <a data-toggle="tooltip" data-placement="top" title="{duration_tooltip}"></a>
    <h2>{movie_title}</h2>
    <fieldset class="rating">
            <input type="radio" id="{movie_name}_star5" name="{movie_name}_rating1" value="5" /><label class = "full" for="{movie_name}_star5"></label>
            <input type="radio" id="{movie_name}_star4" name="{movie_name}_rating1" value="4" /><label class = "full" for="{movie_name}_star4"></label>
            <input type="radio" id="{movie_name}_star3" name="{movie_name}_rating1" value="3" /><label class = "full" for="{movie_name}_star3"></label>
            <input type="radio" id="{movie_name}_star2" name="{movie_name}_rating1" value="2" /><label class = "full" for="{movie_name}_star2"></label>
            <input type="radio" id="{movie_name}_star1" name="{movie_name}_rating1" value="1" /><label class = "full" for="{movie_name}_star1"></label>
    </fieldset>
</div>
'''

# A single tv show entry html template
tv_show_tile_content = '''
<div class="col-md-6 col-lg-4 tvshow-tile text-center" title="{duration_tooltip}" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <a data-toggle="tooltip" data-placement="top" title="{duration_tooltip}"></a>
    <h2>{tv_show_title}</h2>
    <h4>{tv_show_details}</h4>
    <fieldset class="rating">
            <input type="radio" id="{tv_show_name}_star5" name="{tv_show_name}_rating1" value="5" /><label class = "full" for="{tv_show_name}_star5"></label>
            <input type="radio" id="{tv_show_name}_star4" name="{tv_show_name}_rating1" value="4" /><label class = "full" for="{tv_show_name}_star4"></label>
            <input type="radio" id="{tv_show_name}_star3" name="{tv_show_name}_rating1" value="3" /><label class = "full" for="{tv_show_name}_star3"></label>
            <input type="radio" id="{tv_show_name}_star2" name="{tv_show_name}_rating1" value="2" /><label class = "full" for="{tv_show_name}_star2"></label>
            <input type="radio" id="{tv_show_name}_star1" name="{tv_show_name}_rating1" value="1" /><label class = "full" for="{tv_show_name}_star1"></label>
    </fieldset>
</div>
'''

def create_movie_tiles_content(movies):
    """ Creates Movie Tiles & provides the details"""
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)
        print("trailer_youtube_id"+trailer_youtube_id)
        duration_tooltip = "Duration: "+movie.duration
	# Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_name = movie.name,
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
	    duration_tooltip = duration_tooltip,
            movie_rating = movie.rating
        )
    return content

def create_tv_show_tiles_content(tv_shows):
    """ Creates TV Show Tiles & provides the details"""
    # The HTML content for this section of the page
    content = ''
    for tv_show in tv_shows:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', tv_show.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', tv_show.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)
        duration_tooltip = "Duration: "+tv_show.duration
        content += tv_show_tile_content.format(
            tv_show_name = tv_show.name,
            tv_show_title=tv_show.title,
            tv_show_details = tv_show.season + " " + tv_show.episode,
            poster_image_url=tv_show.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            duration_tooltip = duration_tooltip,
            tv_show_rating = tv_show.rating
        )
    return content

def open_movies_page(movies, tv_shows):
    """ This function will take ist of movies & TV Shows and generate an HTML file including this content,
    producing a website to showcase your favorite movies."""
    
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_movie_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies),
                                                      tv_show_tiles=create_tv_show_tiles_content(tv_shows))

    # Output the file
    output_file.write(main_page_head + rendered_movie_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)

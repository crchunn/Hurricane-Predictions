
from flask import Flask, render_template, url_for, request, redirect

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
# from django import template
# from django import forms
# register = template.Library()

# logger = logging.getLogger('examples.artist_albums')
# logging.basicConfig(level='INFO')

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

app = Flask(__name__)


@app.route('/')
def index():
    # landing page
    return render_template('index.html')

@app.route('/tableau')
def tableau():
    return render_template('tableau.html')

@app.route('/popup')
def popup():
    return render_template('popup.html')

@app.route('/tableau2')
def tableau2():
    return render_template('tableau2.html')

@app.route('/machine')
def machine():
    return render_template('machine-learning.html')


# def get_args():
    # parser = argparse.ArgumentParser(description='Gets albums from artist')
    # parser.add_argument('-a', '--artist', required=True,
    #                     help='Name of Artist')
    # return parser.parse_args()


@app.route('/handle_data', methods=['POST'])
def handle_data():
    artist_name = request.form.get('Artist')
    print(artist_name)
    artist_id = get_artist(artist_name)
    artist_albums = get_artist_albums(artist_id)
    return render_template('popup.html', artist_albums = artist_albums)  
    
    # your codecd ..
    # return a response
    # render template instead of redirect
    # $('#myModal').modal(options)
    # $('#example').popover(options)


def get_artist(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        return items[0]
    else:
        return None


def get_artist_albums(artist):
    albums = []
    results = sp.artist_albums(artist['id'], album_type='album')
    albums.extend(results['items'])
    while results['next']:
        results = sp.next(results)
        albums.extend(results['items'])
    seen = set()  # to avoid dups
    albums.sort(key=lambda album: album['name'].lower())
    for album in albums:
        name = album['name']
        if name not in seen:
            # logger.info('ALBUM: %s', name)
            seen.add(name)

    return list(seen)


#in templatetags/user_list_tags.py



# $('a.popup-ajax').popover({
#     "html": true,
#     "content": function(){
#         var div_id="tmp-id-" + $.now()
#         return details_in_popup($(this).attr('href'), div_id)
#     }
# })

# function details_in_popup(link, div_id){$.ajax({
#     url: link,
#     success: function(response){$('#'+div_id).html(response)
#                                 }
# })
#     return '<div id="' + div_id + '">Loading...</div>'
# }


# def main():
# args = get_args()
# artist = get_artist(args.artist)
# if artist:
#     show_artist_albums(artist)
# else:
#     logger.error("Can't find artist: %s", artist)

if __name__ == '__main__':
    app.run()

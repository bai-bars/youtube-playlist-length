from bottle import run,template,get,post,request
from playlistAPI import YoutubePlaylist

@get('/')
def index():
    return template('index',cntx=None)

@post('/')
def index():
    playlistId = request.forms.get('playlistId')
    youtubeplaylist= YoutubePlaylist()
    cntx=youtubeplaylist.calculatePlaylistLength(playlistId)
    return template('index', cntx=cntx)

if __name__=='__main__':
    run(debug=True,  reloader=True)
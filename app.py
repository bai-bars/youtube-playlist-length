from bottle import run,template,get,post,request,route,static_file
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

@route('/css/<filename>')
def send_css(filename):
    return static_file(filename, root='static/css')

if __name__=='__main__':
    run(debug=True,  reloader=True)
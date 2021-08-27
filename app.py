import os
from bottle import run,template,get,post,request,route,static_file
from playlistAPI import YoutubePlaylist


@get('/')
def index():
    return template('index',cntx=None)

@post('/')
def index():
    playlistId = request.forms.get('playlistId')
    begin= request.forms.get('begin')
    end= request.forms.get('end')
    # if(begin!='' and end!='' and int(begin)>int(end)):
    #     return 'Error Occured'
    youtubeplaylist= YoutubePlaylist()
    cntx=youtubeplaylist.calculatePlaylistLength(playlistId, begin, end)
    return template('index', cntx=cntx)

@route('/css/<filename>')
def send_css(filename):
    return static_file(filename, root='static/css')


if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)
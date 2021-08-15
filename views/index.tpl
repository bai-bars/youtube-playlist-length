<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Playlist Length</title>
    <link href="/css/main.css" rel="stylesheet">
</head>
<body>
    <div class='intro'>
        <a href='https://github.com/bai-bars'><strong>Baibars</strong></a>
    </div>
    <div style="clear: both"> </div>
    <div class="container">
        <h3>Playlist Length</h3>
        <form class="main" action='/' method="POST">
            <input type="text" placeholder="Playlist Link..." name="playlistId" required>
            <button type="submit">Length</button>
        </form>
        <!-- CONTENT START -->
        <div class='content'>
            % if cntx:
                <strong>No of videos: {{cntx['noOfVideos']}}</strong>
                <br><br>
                <div class='finalcontent'>
                    % for item in cntx['lenList']:
                        % for key,value in item.items(): 
                            <h5>{{key}}x playback: </h5>
                            <span>{{value}}</span>
                            <br><br>
                        % end
                    % end
                </div>
            % end
            
        </div>
        <!-- CONTENT END -->
    </div>
</body>
</html>
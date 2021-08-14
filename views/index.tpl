<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Playlist Length</title>
    <style>
        *{
            box-sizing: border-box;
            padding: 0px;
            margin: 0px;
        }
        
        body{   
                margin-top: 4%;
                padding: 4%;
                font-family: monospace ,sans-serif;
                font-size: 2em;
            }
        
        .container{
            width: 90%;
            }

        h4{        
            text-align: center;
            margin-bottom: 10px;
            font-family: cursive;
            color: rgb(21,35,70);
        }
           
        /* Style the search field */
        form.example input[type=text] {
            padding: 10px;
            font-size: 17px;
            border: 1px solid grey;
            float: left;
            width: 80%;
            background: #e0e0e0;
        }

            /* Style the submit button */
        form.example button {
            float: left;
            width: 20%;
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            font-size: 17px;
            border: 1px solid grey;
            border-left: none; /* Prevent double borders */
            cursor: pointer;
        }

        form.example button:hover {
            background-color: #8FAB67;
        }

        /* Clear floats */
        form.example::after {
            content: "";
            clear: both;
            display: table;
        }
    </style>
</head>
<body>
    
    <div class="container">
        <h4>Playlist Length</h4>
        <form class="example" action='/' method="POST">
            <input type="text" placeholder="Playlist Link..." name="playlistId" required>
            <button type="submit">Length</button>
        </form>

        <div>
            % if cntx:
                <strong>No of videos {{cntx['noOfVideos']}}</strong>
                <ul>
                    % for item in cntx['lenList']:
                        % for key,value in item.items(): 
                            <li><strong>{{key}} playback speed: <Strong> {{value['hours']}} hours {{value['minutes']}} minutes {{value['seconds']}} seconds</li>
                        % end
                    % end
                </ul>
            % end
        </div>
    </div>
    
</body>
</html>
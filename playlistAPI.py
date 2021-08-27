import re
import os
from datetime import timedelta
from googleapiclient.discovery import build



class YoutubePlaylist:
    api_key='AIzaSyCG3OOVFTnQKECkjvFjHL7aqDS8SLsp0Fk'
    pageCount=0
    vidCount=0

    def extractIdFromURL(self,playlistId):
        '''If Client puts whole link of The playlist
            instead of playlistID,it requires to Extract the
            ID from the whole Link'''

        if re.search("^https:",playlistId):
            return playlistId.split('=')[1]
        return playlistId


    def lenInPlaybackSpeed(self, totalSec , playbackSpeed):
        '''To Find Total length In Different Playback Speed'''

        totalSeconds= totalSec/playbackSpeed
        minutes,seconds = divmod(totalSeconds,60)
        hours,minutes= divmod(minutes,60)
        return {playbackSpeed: f'{hours:.0f}hr {minutes:.0f}min {seconds:.0f}sec'}



    def calculatePlaylistLength(self,playlistId, begin='' ,end=''):
        ended= False
        if begin=='':
            begin=1
        else:
            begin=int(begin)

        if end!='':
            end=int(end)
            if begin > end:
                return 'ERROR'

        totalLenInSeconds=0
        noOfVideos=0
        nextPageToken=None
        youtube= build('youtube', 'v3', developerKey=self.api_key)

        #One Request for playlist can consume 50 videos maximum,So it requires to loop through
        while True:
            print('---------WHILE START-----------')

            #Request to playlist to grab video Ids
            playlistRequest = youtube.playlistItems().list(
                    part="contentDetails",
                    playlistId=self.extractIdFromURL(playlistId),
                    maxResults = 50,
                    pageToken=nextPageToken
                )
            playlistResponse = playlistRequest.execute()
            videoIds= [item['contentDetails']['videoId'] for item in playlistResponse['items']]

            videoRequest= youtube.videos().list(
                part='contentDetails',
                id= ','.join(videoIds)
                )
            videoResponse= videoRequest.execute()
            for item in videoResponse['items']:
                playtym= re.findall('[0-9]+[A-Z]', item['contentDetails']['duration'])
                h,m,s=0,0,0
                for i in playtym:
                    if i[-1] == 'H':
                        h= int(i[0:-1])
                    elif i[-1] == 'M':
                        m= int(i[0:-1])
                    elif i[-1] == 'S':
                        s= int(int(i[0:-1]))

                self.vidCount=self.vidCount+1

                if (self.vidCount >= begin):
                    vidLenInSeconds = timedelta(hours=int(h),minutes=int(m),seconds=int(s)).total_seconds()
                    noOfVideos=noOfVideos+1

                    totalLenInSeconds+=vidLenInSeconds
                    if (end != '' and self.vidCount >= end):
                        ended=True
                        break
                
            
            nextPageToken=playlistResponse.get('nextPageToken')
            print('NEXT PAGE TOKEN-----', nextPageToken)
            self.pageCount+=1
            print('-----------WHILE END-----------')
            if not nextPageToken or ended:
                break
        
        playbackSpeeds = [1,1.25,1.5,2]
        lenList= [self.lenInPlaybackSpeed(totalLenInSeconds, i) for i in playbackSpeeds]
        print('PAGE COUNT------------>', self.pageCount)
        return {'lenList':lenList , 'noOfVideos':noOfVideos}

if __name__ == '__main__':
    str= input('Enter the Playlist Url or Playlist Id: ')
    b =  input('Enter The beginning number:')
    e =  input('Enter The ending number:')

    ytpl= YoutubePlaylist()
    print(ytpl.calculatePlaylistLength(str,b,e))
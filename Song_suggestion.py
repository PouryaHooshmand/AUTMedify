import os
import Music_metadata
import billboard
import Search_directory

charts = [
    'hot-100',
    'r-b-hip-hop-songs',
    'pop-songs',
    'country-songs',
    'rock-songs',
    'dance-electronic-songs',
    'latin-songs'
]


def checkSonginChart(source, des, chartname, chart):
    musicMD = Music_metadata.MusicMetadata(source)

    title = musicMD.metadata()['title']
    artist = musicMD.metadata()['artist']

    if not os.path.exists(des + '/' + chartname + '/'): #Creating Chart Folder
        os.makedirs(des + '/' + chartname + '/')

    for song in chart: # Searching For Song In Chart
        if song.title == title and song.artist == artist:
            if os.path.isfile(des + '/' + chartname + '/' + artist + "-" + title + ".mp3"): # Check if shortcut exists
                print("the file exists")
                break
            os.symlink(source, des + '/' + chartname + '/' + artist + "-" + title + ".mp3") #Creating Shortcut

# source = '/home/pouya/Desktop/Drake Nice For What'
# des = '/home/pouya/Desktop'

def createPlaylists(source, des):
    folderSongs = Search_directory.search_directory(source)
    for chartname in charts:
        print("Working On " + chartname + " ---------- ")
        chart = billboard.ChartData(chartname)
        for song in folderSongs:
            print("Checking : " + song['address'] )
            checkSonginChart(song['address'], des, chartname, chart)


if __name__ == '__main__':
    createPlaylists('/home/milad/test/medify_test/music/', '/home/milad/test/medify_test/charts/')

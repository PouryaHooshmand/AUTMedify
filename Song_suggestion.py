
import os
from win32com.client import Dispatch
import stagger


def checkChart(address, des, chart):
    musicMD = stagger.read_tag(address)
    title = musicMD.title
    artist = musicMD.artist
    chartname = chart.name

    if not os.path.exists(des + '\\' + chartname + '\\'):
        os.makedirs(des + '\\' + chartname + '\\')
    for song in chart:
        if song.title == title and song.artist == artist:
            path = os.path.join(des + '\\' + chartname + '\\', title + "-" + artist + ".lnk")
            target = r"" + address
            icon = r"" + address

            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(path)
            shortcut.Targetpath = target
            shortcut.IconLocation = icon
            shortcut.save()

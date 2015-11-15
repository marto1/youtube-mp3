#!/usr/bin/env python
"""
youtube-mp3.org utility.

Usage: 
youtube-mp3.py <url> <path>

Examples:
  youtube-mp3.py list

Options:
  -h, --help
"""
from docopt import docopt
import requests
import time
import sys
import urllib
import json

def sig(H):
    """Deobfuscated hashing"""
    A = {"a": 870,
         "b": 906,
         "c": 167,
         "d": 119,
         "e": 130,
         "f": 899,
         "g": 248,
         "h": 123,
         "i": 627,
         "j": 706,
         "k": 694,
         "l": 421,
         "m": 214,
         "n": 561,
         "o": 819,
         "p": 925,
         "q": 857,
         "r": 539,
         "s": 898,
         "t": 866,
         "u": 433,
         "v": 299,
         "w": 137,
         "x": 285,
         "y": 613,
         "z": 635,
         "_": 638,
         "&": 639,
         "-": 880,
         "/": 687,
         "=": 721}
    F = 1.51214
    N, Y = 3219, 0
    H = unicode(H.lower(), "utf-8")
    for char in H:
        if char.isnumeric():
            N += int(char) * 121 * F
        else:
            if char in A:
                N += A[char] * F
        N *= 0.1
    N = round(N * 1000)
    return int(N)


MAIN="http://www.youtube-mp3.org"
A="Mozilla/5.0 (X11; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0"
ACC="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
if __name__ == '__main__':
    arguments = docopt(__doc__)
    headers = {
        "Host": "www.youtube-mp3.org",
        "User-Agent": A,
        "Accept": ACC,
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Location": "*",
        "Cache-Control": "no-cache",
        "Referer": "http://www.youtube-mp3.org/",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        }
    URL=urllib.quote_plus(arguments["<url>"])
    form = "http://www.youtube-mp3.org/a/pushItem/?item={0}&el=na&bf=false"
    form += "&r={1}"
    form2 = "http://www.youtube-mp3.org/a/itemInfo/?video_id={0}"
    form2 += "&ac=www&t=grp&r={1}"
    timestamp = int(time.time()*1000)
    rq = form.format(URL, timestamp)
    rq += "&s={0}".format(sig(rq))
    r = requests.get(MAIN, headers=headers)
    r = requests.get(rq, headers=headers)
    video_id = r.text
    rq = form2.format(video_id, timestamp)
    rq += "&s={0}".format(sig(rq))
    r = requests.get(rq, headers=headers)
    json_data = json.loads(r.text[7:-1])
    ts_create = json_data[u'ts_create']
    h2 = json_data[u'h2']
    r_data = urllib.quote_plus(json_data[u'r'])
    form3 = "{0}/get?video_id={1}&ts_create={2}&r={3}&h2={4}"
    rq = form3.format(MAIN, video_id, ts_create, r_data, h2)
    rq += "&s={0}".format(sig(rq))
    r = requests.get(rq, stream=True)
    filename = arguments["<path>"]
    if not filename.endswith(".mp3"): #FIXME switch for that 
        filename += ".mp3"
    with open(filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=2048): #FIXME option
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

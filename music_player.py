import os
import sys
import json

import pafy
import vlc
from youtubesearchpython import SearchVideos

QUEUE = []

os.environ["VLC_VERBOSE"] = str("-1")


def get_song(name):
    search = SearchVideos(name, offset=1, mode="json", max_results=1)
    result = json.loads(search.result())["search_result"]
    url = None
    if result:
        url = result[0].get("link", None)

    if url is None:
        return None

    video = pafy.new(url)
    best = video.getbestaudio()

    return best.url


def play(name):
    play_url = get_song(name)

    if play_url is None:
        print("No result!")
        sys.exit(1)

    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new(play_url)
    media.get_mrl()
    player.set_media(media)
    player.play()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Music name arg required!")
        sys.exit(1)

    music = sys.argv[1]

    play(music)
    while True:
        pass

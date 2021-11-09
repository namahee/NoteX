import os

import requests
from pytube import YouTube
from youtube_search import YoutubeSearch

from userge import Message, userge

os.system("pip3 install youtube-search")


def search_music(query):
    result = YoutubeSearch(query, max_results=1).to_dict()
    return result


def get_link(result) -> str:
    return f"https://www.youtube.com{result[0]['url_suffix']}"


def get_filename(result) -> str:
    title_ = result[0]["title"]
    title = title_.replace(" ", "_")
    return title + ".mp3", title + ".mp4"


def get_duration(result):
    duration = result[0]["duration"]
    secmul, dur, dur_arr = 1, 0, duration.split(":")
    for i in range(len(dur_arr) - 1, -1, -1):
        dur += int(dur_arr[i]) * secmul
        secmul *= 60
    return duration, dur


def get_thumb(result):
    thumbnail = result[0]["thumbnails"][0]
    title = result[0]["title"]
    thumb_name = f"{title}.jpg"
    thumb = requests.get(thumbnail, allow_redirects=True)
    open(os.path.join("./userge/xcache/", thumb_name), "wb").write(thumb.content)
    return thumb_name


def down_song(link, filename):
    YouTube(link).streams.filter(only_audio=True).first().download(
        "./userge/xcache/", filename=filename
    )


def down_video(link, filename):
    YouTube(url).streams.get_highest_resolution().download(
        "./userge/xcache/", filename=filename
    )


@userge.on_cmd(
    "song",
    about={
        "header": "Music Downloader",
        "description": "Baixe músicas usando o pytube. ;-;",
        "usage": "{tr}song [nome - cantor / reply msg / link]",
    },
)
async def song(message: Message):
    music = message.input_or_reply_str
    if not music:
        await message.edit("`Vou baixar o vento?!`")
        return
    result = search_music(music)
    if result == []:
        await message.edit("`Não foi possível encontrar a música.`")
        return
    link = get_link(result)
    duration, dur = get_duration(result)
    filename, m = get_filename(result)
    thumb = get_thumb(result)
    try:
        down_song(link, filename)
    except Exception as e:
        await message.edit("`Não foi possível baixar a música.`")
        print(str(e))
    else:
        if os.path.exists(f"./userge/xcache/{thumb}"):
            caption = f"""
            **Título:** __[{result[0]['title']}]({link})__
            **Duração:** __{duration}__
            **Views:** __{result[0]['views']}__
            """
            try:
                await message.reply_audio(
                    audio=f"./userge/xcache/{filename}",
                    caption=caption,
                    title=result[0]["title"],
                    thumb=f"./userge/xcache/{thumb_name}",
                    duration=dur,
                )
            except Exception as e:
                await message.edit("`Não foi possível enviar a música.`")
                print(str(e))
            finally:
                os.remove(f"./userge/xcache/{filename}")
                os.remove(f"./userge/xcache/{thumb_name}")


@userge.on_cmd(
    "video",
    about={
        "header": "Video Downloader",
        "description": "Baixe vídeos usando o pytube. ;-;",
        "usage": "{tr}video [nome / reply msg / link]",
    },
)
async def video(message: Message):
    video = message.input_or_reply_str
    if not video:
        await message.edit("`Vou baixar o vento?!`")
        return
    result = search_music(video)
    if result == []:
        await message.edit("`Não foi possível encontrar o vídeo.`")
        return
    link = get_link(result)
    m, filename = get_filename(result)
    try:
        down_video(link, filename)
    except Exception as e:
        await message.edit("`Não foi possível baixar o video.`")
        print(str(e))
    else:
        await message.reply(str(result))
        caption = f"**Título ➠** [{result[0]['title']}]({link})\n**Canal ➠** {result[0]['channel']}"
        try:
            await message.reply_video(
                video=f"./userge/xcache/{filename}",
                caption=caption,
            )
        except Exception as e:
            await message.reply("`Não foi possível enviar o vídeo.`")
            print(str(e))
        finally:
            os.remove(f"./userge/xcache/{filename}")

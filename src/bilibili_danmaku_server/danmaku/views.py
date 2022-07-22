from cgitb import text
from django.shortcuts import render
from django.http import HttpResponse
from bilibili_api import video, sync, interactive_video

# Create your views here.

def index(request):
    return render(request, "danmaku/index.html")

def danmaku(request, aid, page):
    try:
        v = video.Video(aid=aid)
        danmakus = sync(v.get_danmakus(page))
        dm_list = []
        for dm in danmakus:
            dm_dict = {}
            dm_dict['text'] = dm.text
            dm_dict["dm_time"] = dm.dm_time
            dm_dict["send_time"] = dm.send_time
            dm_dict["crc32_id"] = dm.crc32_id
            dm_dict["mid"] = dm.crack_uid()
            dm_dict["color"] = dm.color
            dm_dict["weight"] = dm.weight
            dm_dict["id"] = dm.id
            dm_dict["id_str"] = dm.id_str
            dm_dict["action"] = dm.action
            dm_dict["mode"] = dm.mode
            dm_dict["font_size"] = dm.font_size
            dm_dict["is_sub"] = dm.is_sub
            dm_dict["pool"] = dm.pool
            dm_dict["attr"] = dm.attr
            dm_list.append(dm_dict)
    except Exception as e:
        return HttpResponse({
            "code": 404, 
            "message": str(e)
        }, "application/json", 404)
    else:
        return HttpResponse(dm_list, "application/json", 200)

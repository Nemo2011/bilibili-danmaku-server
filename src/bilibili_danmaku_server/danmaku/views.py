import asyncio
from cgitb import text
import json
from xml.dom.minidom import Attr
from django.shortcuts import render
from django.http import HttpResponse
from bilibili_api import Danmaku, DmFontSize, DmMode, video, sync, interactive_video
from numpy import isin

# Create your views here.

def index(request):
    return render(request, "danmaku/index.html")

def danmaku(request, aid, page):
    if True:#try:
        v = video.Video(aid=aid)
        danmakus = asyncio.run(v.get_danmakus(page))
        dm_list = []
        for dm in danmakus:
            dm_dict = {}
            dm_dict['text'] = dm.text
            dm_dict["dm_time"] = dm.dm_time
            dm_dict["send_time"] = dm.send_time
            dm_dict["crc32_id"] = dm.crc32_id
            try:
                dm_dict["mid"] = dm.crack_uid()
            except AttributeError:
                dm_dict["mid"] = 0
            dm_dict["color"] = dm.color
            dm_dict["weight"] = dm.weight
            dm_dict["id"] = dm.id
            dm_dict["id_str"] = dm.id_str
            dm_dict["action"] = dm.action
            if isinstance(dm.mode, DmMode):
                dm_dict["mode"] = dm.mode.value
            else:
                dm_dict["mode"] = dm.mode
            if isinstance(dm.font_size, DmFontSize):
                dm_dict["font_size"] = dm.font_size.value
            else:
                dm_dict["font_size"] = dm.font_size
            dm_dict["is_sub"] = dm.is_sub
            dm_dict["pool"] = dm.pool
            dm_dict["attr"] = dm.attr
            dm_list.append(dm_dict)
    #except Exception as e:
    #    return HttpResponse(json.dumps({
    #        "code": 404, 
    #        "message": str(e)
    #    }), "application/json", 404)
    #else:
        return HttpResponse(json.dumps(dm_list), "application/json", 200)

from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.event.mirai import MemberJoinEvent, MemberLeaveEventQuit,MemberMuteEvent, MemberUnmuteEvent, MemberLeaveEventKick, MemberCardChangeEvent
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Group, Member
import asyncio
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
from graia.ariadne.message.element import At, Plain, Image, Forward, ForwardNode
from graia.ariadne.util.interrupt import FunctionWaiter
from graia.broadcast.builtin.decorators import Depend
from graia.broadcast.exceptions import ExecutionStop
from typing import Union, Optional
from collections import defaultdict
from graia.scheduler import timers
from graia.scheduler.saya import SchedulerSchema
channel = Channel.current()
import base64
import pyperclip
import datetime
#from OCR.PPOCR_api import PPOCR

# 初始化识别器对象，传入 PaddleOCR_json.exe 的路径
#ocr = PPOCR('./OCR/PaddleOCR_json.exe')



@channel.use(ListenerSchema(listening_events=[GroupMessage]))#1020828729
#@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def reply_749776033(app: Ariadne, group: Group,sender: Member, message: MessageChain):
    #魔界人大本营群

    if group.id==749776033:
        for one in ['臭熊', '凑熊', '猪鼻熊']:
            if one in message.display:
                await app.send_message(
                    group,
                    MessageChain('熊是猪鼻'),
                )
                return

        for one in ['6v']:
            if one in message.display:
                await app.send_message(
                    group,
                    MessageChain('黑奴'),
                )
                return



@channel.use(ListenerSchema(listening_events=[GroupMessage]))#1020828729
#@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def reply_all(app: Ariadne, group: Group,sender: Member, message: MessageChain):
    #全部群
    if group.id==537750188:
        return
    key_words=['求你','赫赫','导师','不配','QAQ','出警','打桩','猪鼻']
    if '求你' in message.display:
        await app.send_message(
            group,
            MessageChain(Image(path="./data/求你.jpg")),
        )
        return
    if '赫赫' in message.display:
        await app.send_message(
            group,
            MessageChain(Image(path="./data/赫赫.jpg")),
        )
        return
    if '导师' in message.display:
        await app.send_message(
            group,
            MessageChain(Image(path="./data/导师.jpg")),
        )
        return
    if '不配' in message.display:
        await app.send_message(
            group,
            MessageChain(Image(path="./data/不配.jpg")),
        )
        return
    if 'QAQ' in message.display:
        await app.send_message(
            group,
            MessageChain(Image(path="./data/QAQ.jpg")),
        )
        return
    if '?'==message.display:
        await app.send_group_message(
            group,
            MessageChain('?'),
        )
        return
    if '？'==message.display:
        await app.send_group_message(
            group,
            MessageChain('？'),
        )
        return
    if '雌堕' in message.display:
        await app.send_message(
            group,
            MessageChain('越雌堕 越幸运——是世间真理'),
        )
        return
    if '出警' in message.display:
        await app.send_message(
            group,
            MessageChain(Image(path="./data/出警.jpg")),
        )
        return
    if '猪鼻' in message.display and group.id==729483999:
        await app.send_message(
            group,
            MessageChain(Image(path="./data/猪鼻.png")),
        )
        return

@channel.use(ListenerSchema(listening_events=[GroupMessage]))#1020828729
#@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def test_anything(app: Ariadne, group: Group,sender: Member, message: MessageChain):
    #测试群
    return
    if group.id==101461781 :
        if len(message[Image])>0:
            result=await message[Image][0].get_bytes()
            #print(result)

            # 识别图片，传入图片路径
            #getObj = ocr.run('./image_save/QQ图片20230519190614.png')
            image_bytes=result#base64.b64decode(result)

            current_time = datetime.datetime.now()

            # Convert the current time to a string
            time_string = current_time.strftime("%Y-%m-%d-%H-%M-%S")  # Format as HH:MM:SS
            with open('./OCR/image_save/{}.jpg'.format(time_string), 'wb') as file:
                file.write(image_bytes)

            #pyperclip.copy(image_bytes)
            getObj = ocr.run('./image_save/{}.jpg'.format(time_string))
            #print(f'图片识别完毕，状态码：{getObj["code"]} 结果：\n{getObj["data"]}\n')



            print(' '.join(one['text'] for one in getObj["data"]))

            #ocr.stop()  # 结束引擎子进程



last_message= {}
@channel.use(ListenerSchema(listening_events=[GroupMessage]))#1020828729
async def setu(app: Ariadne, group: Group, message: MessageChain):
    global last_message
    if group.id==537750188:
        return

    if group.id not in last_message:
        last_message[group.id]=None
    #print(message)
    if message==last_message[group.id] and message.display!='?' and message.display!='？':
        await app.send_message(
            group,
            last_message[group.id],
        )
        last_message[group.id]=None
    else:
        last_message[group.id]=message

from creart import create
from graia.ariadne.app import Ariadne
from graia.ariadne.connection.config import (
    HttpClientConfig,
    WebsocketClientConfig,
    config,
)
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Group
from graia.broadcast import Broadcast

from graia.saya import Channel
from graia.saya.builtins.broadcast import ListenerSchema
from graia.ariadne.message.element import At, Plain, Image, Forward, ForwardNode
from graia.saya import Saya



saya = create(Saya)


bcc = create(Broadcast)
app = Ariadne(
    connection=config(
        3568304426,  # 你的机器人的 qq 号
        "GraiaxVerifyKey",  # 填入你的 mirai-api-http 配置中的 verifyKey
        # 以下两行（不含注释）里的 host 参数的地址
        # 是你的 mirai-api-http 地址中的地址与端口
        # 他们默认为 "http://localhost:8080"
        # 如果你 mirai-api-http 的地址与端口也是 localhost:8080
        # 就可以删掉这两行，否则需要修改为 mirai-api-http 的地址与端口
        #HttpClientConfig(host="http://11.45.1.4:19810"),
        #WebsocketClientConfig(host="http://11.45.1.4:19810"),
        HttpClientConfig(host="http://localhost:8081"),
        WebsocketClientConfig(host="http://localhost:8081"),
    ),
)


#java -D"file.encoding=utf-8" -cp "./libs/*" net.mamoe.mirai.console.terminal.MiraiConsoleTerminalLoader
with saya.module_context():
    saya.require("modules.guild_welcome")
    saya.require("modules.chatchat")
    saya.require("modules.auto_reply")
    pass

app.launch_blocking()

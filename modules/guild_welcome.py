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


def check_group(*groups: int):
    async def check_group_deco(app: Ariadne, group: Group):
        if group.id not in groups:
            raise ExecutionStop
    return Depend(check_group_deco)

def check_word_list(input_string, words_list, return_word=False):
    for word in words_list:
        if word in input_string:
            if not return_word:
                return True
            else:
                return word
    return False

groups=[789706089, 856100956, 516370180, 792389393, 723275571]
test_id=101461781


@channel.use(ListenerSchema(listening_events=[MemberJoinEvent, GroupMessage]))#1020828729

async def JoinGroup(app: Ariadne, group: Group, sender: Member,  event: Union[MemberJoinEvent, GroupMessage], message: Optional[MessageChain]):

    if group.id in groups and (isinstance(event, MemberJoinEvent)):
        await app.send_message(
            group,
            MessageChain(At(sender),' 大佬妮好，窝是天下第一聪明可爱的鸟一斤子，欢迎来到跨五最大的魔界人联盟，绯月公会。有任何问题可以艾特窝，让窝为妮解答'),
        )
        return

    if (group.id == 101461781 or group.id == 1020828729) and (isinstance(event, MemberJoinEvent) or message.display.strip('@3568304426').strip(' ')=='重新开始'):
        await app.send_message(
            group,
            MessageChain(At(sender),' 大佬妮好，窝是天下第一聪明可爱的鸟一斤子，这里是审核群鸭，窝们公会的简介如图',Image(path="./data/公会图.jpg"), '窝会问妮一些问题，如果答错了想修改答案请回复“重新开始”，想转人工服务请回复“呼叫人工帮助”或“结束流程”'),
        )
        await asyncio.sleep(1)




        async def waiter_occupation(member_target: Member,  message: MessageChain):
            if (message.display.strip('@3568304426').strip(' ')=='重新开始'  and member_target==sender) or message.display.strip('@3568304426').strip(' ')=='呼叫人工帮助' or message.display.strip('@3568304426').strip(' ')=='结束流程' or At(310109557) in message:
                await app.send_message(
                    group,
                    MessageChain('结束流程'),
                )

                return 'end'


            if member_target==sender:
                if len(message.display)>=3:
                    return 'repeat'


                if check_word_list(message.display, ['对','嗯','是的','1','没错']) or ('不' not in message.display and '是' in message.display):
                    return True
                elif check_word_list(message.display, ['不','否']):
                    return False
                else:
                    return 'repeat'

        await app.send_message(
            group,
            MessageChain(At(sender),' 请问妮是女法职业咩，嘤嘤嘤~ （不是女法也可以加公会）'),
        )

        patience=0
        result='repeat'
        while result=='repeat':
            if patience>=3:
                patience=0
                await app.send_message(
                    group,
                    MessageChain(At(sender),' 想结束流程可以艾特群主寻求帮助或回答“结束流程”'),
                )
            if patience>=1:
                await app.send_message(
                    group,
                    MessageChain(At(sender),' 无法识别回答，请重新回答, 请问妮是女法职业咩，请回答是或者不是吖'),
                )

            result=await FunctionWaiter(waiter_occupation, [GroupMessage]).wait()
            if result=='repeat':
                patience+=1

            if result=='end':
                raise ExecutionStop

        occupation_result=result


        async def waiter_reputation(member_target: Member,  message: MessageChain):
            if (message.display.strip('@3568304426').strip(' ')=='重新开始'  and member_target==sender) or message.display.strip('@3568304426').strip(' ')=='呼叫人工帮助' or message.display.strip('@3568304426').strip(' ')=='结束流程' or At(310109557) in message:
                await app.send_message(
                    group,
                    MessageChain('结束流程'),
                )
                return 'end'
            if member_target==sender:
                try:
                    result=int(message.display)/10000
                except:
                    result= check_word_list(message.display, ['4.{}'.format(one) for one in range(10)]+['5.{}'.format(one) for one in range(10)]+['3.{}'.format(one) for one in range(10)]+['2.{}'.format(one) for one in range(10)], return_word=True)
                print(result)

                if result:
                    return float(result)
                else:
                    return 'repeat'


        await app.send_message(
            group,
            MessageChain(At(sender),' 请问妮的名望是多少吖'),
        )

        patience=0
        result='repeat'
        while result=='repeat':
            if patience>=3:
                patience=0
                await app.send_message(
                    group,
                    MessageChain(At(sender),' 想结束流程可以艾特群主寻求帮助或回答“结束流程”'),
                )

            if patience>=1:
                await app.send_message(
                    group,
                    MessageChain(At(sender),' 无法识别回答，请重新回答, 请问妮的名望是多少吖，用4.x 或者5.x 来回答，x是一个数字，举例：4.5'),
                )


            result=await FunctionWaiter(waiter_reputation, [GroupMessage]).wait()
            if result=='repeat':
                patience+=1
            if result=='end':
                raise ExecutionStop

        reputation_result=result


        avails=[]
        if occupation_result==True: #女法
            if reputation_result>=4.8:
                avails.append('绯月恋歌')
            if reputation_result>=4.4:
                avails.append('绯月の心')

        if reputation_result>=4.9:
            avails.append('绯月樱梦')

        avails.append('绯月樱雪')

        await app.send_message(
            group,
            MessageChain(At(sender),' 嘤嘤嘤，分析结果：妮{}女法职业，并且名望为{}，'.format('是' if occupation_result else '不是', '{:.1f}'.format(reputation_result)),
                         '那么妮可以加入的公会有：', ' '.join(['{}.{}'.format(i+1,avail) for i,avail in enumerate(avails)]), '。 公会的简介可以看上面的图吖'),
        )




        async def waiter_join(member_target: Member,  message: MessageChain):
            # 之所以把这个 waiter 放在 new_friend 里面，是因为我们需要用到 app


            if (message.display.strip('@3568304426').strip(' ')=='重新开始'  and member_target==sender) or message.display.strip('@3568304426').strip(' ')=='呼叫人工帮助' or message.display.strip('@3568304426').strip(' ')=='结束流程' or At(310109557) in message:
                await app.send_message(
                    group,
                    MessageChain('结束流程'),
                )
                return 'end'
            if member_target==sender:
                try:
                    if int(message.display)<=len(avails):
                        return avails[int(message.display)-1]
                except:
                    result= check_word_list(message.display, avails, return_word=True)

                    if result:
                        return result
                    else:
                        return 'repeat'

        await app.send_message(
            group,
            MessageChain(At(sender),' 请选择其中一个加入吖'),
        )

        patience=0
        result='repeat'
        while result=='repeat':
            if patience>=3:
                patience=0
                await app.send_message(
                    group,
                    MessageChain(At(sender),' 想结束流程可以艾特群主寻求帮助或回答“结束流程”'),
                )
            if patience>=1:
                await app.send_message(
                    group,
                    MessageChain(At(sender),' 无法识别回答，请重新回答， 请从 '+' '.join(['{}.{}'.format(i+1,avail) for i,avail in enumerate(avails)])+' 中选择一个加入吖'),
                )


            if result=='repeat':
                patience+=1
            result=await FunctionWaiter(waiter_join, [GroupMessage]).wait()

            if result=='end':
                raise ExecutionStop

        guild_result=result
        await app.send_message(
            group,
            MessageChain(At(sender),' 妮选择的是：', guild_result, ' 接下来可以申请这个公会辣~'),
        )

        if guild_result=='绯月恋歌':
            await app.send_message(
                group,
                MessageChain('申请的时候请备注盖盖子吖, 公会管理可以放一下人',At(496079594), At(310109557), At(404699133), At(1203381711), At(1137992237)),
            )
        elif guild_result=='绯月の心':
            await app.send_message(
                group,
                MessageChain('申请的时候请备注香猪吖, 公会管理可以放一下人',At(690912881), At(834619072), At(975246899), At(3283839168), At(496079594), At(2428121151)),
            )
        elif guild_result=='绯月樱梦':
            await app.send_message(
                group,
                MessageChain('申请的时候请备注黄瓜吖, 公会管理可以放一下人',At(310109557), At(1512038070)),
            )
        elif guild_result=='绯月樱雪':
            await app.send_message(
                group,
                MessageChain('申请的时候请备注绯月吖, 公会管理可以放一下人',At(834619072), At(2428121151),At(310109557), At(1512038070)),
            )



@channel.use(ListenerSchema(listening_events=[MemberMuteEvent]))
async def Mute(app: Ariadne, group: Group, member: Member, operator: Optional[Member], event: MemberMuteEvent):
    if group.id==537750188:
        return

    def format_duration(minutes):
        days, hours, mins = 0, 0, 0
        if minutes >= 1440:
            days = minutes // 1440
            minutes %= 1440
        if minutes >= 60:
            hours = minutes // 60
            minutes %= 60
        mins = minutes
        return ('' if days==0 else f"{days}天") + ('' if hours==0 else f"{hours}小时") + ('' if mins==0 else f"{mins}分钟")
    await app.send_message(
        group,
        MessageChain('叮咚，',str(member.name), '被', str(operator.name), '禁言', format_duration(event.duration//60)),
    )

@channel.use(ListenerSchema(listening_events=[MemberUnmuteEvent]))
async def Mute(app: Ariadne, group: Group, member: Member, operator: Optional[Member]):
    if group.id==537750188:
        return

    await app.send_message(
        group,
        MessageChain('叮咚，',str(member.name), '被', str(operator.name), '解除禁言'),
    )


@channel.use(ListenerSchema(listening_events=[MemberLeaveEventQuit]))
async def QuitGroup(app: Ariadne, group: Group, member: Member):
    if group.id==537750188:
        return

    await app.send_message(
        group,
        MessageChain('叮咚，',str(member.name),'已经退群'),
    )

@channel.use(ListenerSchema(listening_events=[MemberLeaveEventKick]))
async def QuitGroup(app: Ariadne, group: Group, member: Member, operator: Optional[Member]):
    if group.id==537750188:
        return

    await app.send_message(
        group,
        MessageChain('叮咚，',str(member.name),'被',str(operator.name),'劝退群聊'),
    )


#@channel.use(ListenerSchema(listening_events=[MemberCardChangeEvent]))
#async def ChangeName(app: Ariadne, group: Group, event: MemberCardChangeEvent):
#    await app.send_message(
#        group,
#        MessageChain('叮咚，',str(event.origin)+'的昵称被修改为'+str(event.current),'，执行者：'+str(event.operator.name) if event.operator!=None else ''),
#    )



#@channel.use(SchedulerSchema(timers.crontabify("0 18 * * * *")))
#async def six_am_notification(app: Ariadne):
#    for group in groups:
#        await app.send_group_message(
#            group,
#            MessageChain('起床打团啦'),
#        )


@channel.use(ListenerSchema(listening_events=[GroupMessage]))#1020828729
async def test(app: Ariadne, group: Group, message: MessageChain):
    if group.id==101461781:
        pass
        #print(message.__repr__())
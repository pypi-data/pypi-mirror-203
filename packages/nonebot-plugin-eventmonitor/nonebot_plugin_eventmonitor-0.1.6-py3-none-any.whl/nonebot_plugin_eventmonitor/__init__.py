import nonebot
from nonebot.rule import Rule
from nonebot.plugin import on_notice
from nonebot.adapters.onebot.v11 import (
    Bot, Event, Message,
    PokeNotifyEvent,
    HonorNotifyEvent,
    GroupUploadNoticeEvent,
    GroupDecreaseNoticeEvent,
    GroupIncreaseNoticeEvent,
    GroupAdminNoticeEvent,
    LuckyKingNotifyEvent
)

from .stamp import chuo_send_msg
from .honour import monitor_rongyu
from .admin import del_user_bye, add_user_wecome, admin_changer
from .utils import *


# 获取戳一戳状态
async def _is_poke(event: Event) -> bool:
    return isinstance(event, PokeNotifyEvent) and event.is_tome()

# 获取群荣誉变更
async def _is_rongyu(event: Event) -> bool:
    return isinstance(event, HonorNotifyEvent)

# 获取文件上传
async def _is_checker(event: Event) -> bool:
    return isinstance(event, GroupUploadNoticeEvent)

# 群成员减少
async def _is_del_user(event: Event) -> bool:
    return isinstance(event, GroupDecreaseNoticeEvent)

# 群成员增加
async def _is_add_user(event: Event) -> bool:
    return isinstance(event, GroupIncreaseNoticeEvent)

# 管理员变动
async def _is_admin_change(event: Event) -> bool:
    return isinstance(event, GroupAdminNoticeEvent)

# 红包运气王
async def _is_red_packet(event: Event) -> bool:
    return isinstance(event, LuckyKingNotifyEvent)

# 戳一戳
chuo = on_notice(Rule(_is_poke), priority=50, block=True)
# 群荣誉
qrongyu = on_notice(Rule(_is_rongyu), priority=50, block=True)
# 群文件
files = on_notice(Rule(_is_checker), priority=50, block=True)
# 群员减少
del_user = on_notice(Rule(_is_del_user), priority=50, block=True)
# 群员增加
add_user = on_notice(Rule(_is_add_user), priority=50, block=True)
# 群管理
group_admin = on_notice(Rule(_is_admin_change), priority=50, block=True)
# 红包
red_packet = on_notice(Rule(_is_red_packet), priority=50, block=True)



@chuo.handle()
async def send_chuo(event: Event):
    uid = event.get_user_id()                                                       # 获取用户id
    try:
        cd = event.time - chuo_CD_dir[uid]                                          # 计算cd
    except KeyError:
        cd = chuo_cd + 1                                                            # 没有记录则cd为cd_time+1
    if (
        cd > chuo_cd
        or event.get_user_id() in nonebot.get_driver().config.superusers
    ):                                                                                   # 记录cd
        chuo_CD_dir.update({uid: event.time})
    rely_msg = await chuo_send_msg()
    await chuo.finish(message=Message(rely_msg))


@qrongyu.handle()                                                                       #群荣誉变化
async def send_rongyu(event: HonorNotifyEvent, bot: Bot):
    bot_qq = int(bot.self_id)
    rely_msg = await monitor_rongyu(event.honor_type, event.user_id, bot_qq)
    await qrongyu.finish(message=Message(rely_msg))


@files.handle()                                                                         #上传群文件
async def handle_first_receive(event: GroupUploadNoticeEvent):
    rely = f'[CQ:at,qq={event.user_id}]\n' \
           f'[CQ:image,file=https://q4.qlogo.cn/headimg_dl?dst_uin={event.user_id}&spec=640]' \
           f'\n 上传了新文件，感谢你一直为群里做贡献喵~[CQ:face,id=175]'
    await files.finish(message=Message(rely))


@del_user.handle()                                                                      #退群事件
async def user_bye(event: GroupDecreaseNoticeEvent):
    rely_msg = await  del_user_bye(event.time, event.user_id)
    await del_user.finish(message=Message(rely_msg))


@add_user.handle()                                                                      #入群事件
async def user_welcome(event: GroupIncreaseNoticeEvent, bot: Bot):
    bot_qq = int(bot.self_id)
    rely_msg = await  add_user_wecome(event.time, event.user_id, bot_qq)
    await add_user.finish(message=Message(rely_msg))


@group_admin.handle()                                                                   #管理员变动
async def admin_chance(event: GroupAdminNoticeEvent, bot: Bot):
    bot_qq = int(bot.self_id)
    rely_msg = await admin_changer(event.sub_type, event.user_id, bot_qq)
    await group_admin.finish(message=Message(rely_msg))

@red_packet.handle()                                                                    #红包运气王
async def hongbao(event: LuckyKingNotifyEvent):
    rely_msg = f"[CQ:at,qq={event.user_id}]\n本次红包运气王为：[CQ:at,qq={event.target_id}]"
    await red_packet.finish(message=Message(rely_msg))

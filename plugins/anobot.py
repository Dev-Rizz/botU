"""
✘ Commands Available -

---- Norml ----
• `{i}cc`
    Cowo/Cewe?.

• `{i}u`
    umur.

• `{i}as`
    askot.

• `{i}me`
    aku.
---- 18+ ----
• `{i}pap`
    pap.

• `{i}sa`
    ange.

"""

from curses import COLOR_WHITE
from pyUltroid.fns.tools import create_tl_btn, format_btn, get_msg_button

from . import HNDLR, eor, get_string, mediainfo, ultroid_cmd
from ._inline import something
from pyUltroid.dB.echo_db import add_echo, check_echo, list_echo, rem_echo
# Note = "\n\nNote: `{mention}`, `{group}`, `{count}`, `{name}`, `{fullname}`, `{username}`, `{userid}` can be used as formatting parameters.\n\n"Note = "\n\nNote: `{mention}`, `{group}`, `{count}`, `{name}`, `{fullname}`, `{username}`, `{userid}` can be used as formatting parameters.\n\n"


@ultroid_cmd(
    pattern="cc( (.*)|$)",
)
async def ceco(e):
    if k := list_echo(e.chat_id):
        user = "**Activated Echo For Users:**\n\n"
        for x in k:
            ok = await e.client.get_entity(int(x))
            kk = f"[{get_display_name(ok)}](tg://user?id={ok.id})"
            user += f"•{kk}" + "\n"
        await e.eor(user)
    else:
        await e.eor("**Cowo/Cewe?**")

@ultroid_cmd(
    pattern="pap( (.*)|$)",
)
async def pap(e):
    if k := list_echo(e.chat_id):
        user = "**Activated Echo For Users:**\n\n"
        for x in k:
            ok = await e.client.get_entity(int(x))
            kk = f"[{get_display_name(ok)}](tg://user?id={ok.id})"
            user += f"•{kk}" + "\n"
        await e.eor(user)
    else:
        await e.eor("**Minta Pap Dong**")

@ultroid_cmd(
    pattern="u( (.*)|$)",
)
async def umur(e):
    if k := list_echo(e.chat_id):
        user = "**Activated Echo For Users:**\n\n"
        for x in k:
            ok = await e.client.get_entity(int(x))
            kk = f"[{get_display_name(ok)}](tg://user?id={ok.id})"
            user += f"•{kk}" + "\n"
        await e.eor(user)
    else:
        await e.eor("**Umur?**")

@ultroid_cmd(
    pattern="as( (.*)|$)",
)
async def asal(e):
    if k := list_echo(e.chat_id):
        user = "**Activated Echo For Users:**\n\n"
        for x in k:
            ok = await e.client.get_entity(int(x))
            kk = f"[{get_display_name(ok)}](tg://user?id={ok.id})"
            user += f"•{kk}" + "\n"
        await e.eor(user)
    else:
        await e.eor("**Askot?**")

@ultroid_cmd(
    pattern="sa( (.*)|$)",
)
async def ange(e):
    if k := list_echo(e.chat_id):
        user = "**Activated Echo For Users:**\n\n"
        for x in k:
            ok = await e.client.get_entity(int(x))
            kk = f"[{get_display_name(ok)}](tg://user?id={ok.id})"
            user += f"•{kk}" + "\n"
        await e.eor(user)
    else:
        await e.eor("**Lagi Sange Ngga??**")

@ultroid_cmd(
    pattern="me( (.*)|$)",
)
async def aing(e):
    if k := list_echo(e.chat_id):
        user = "**Activated Echo For Users:**\n\n"
        for x in k:
            ok = await e.client.get_entity(int(x))
            kk = f"[{get_display_name(ok)}](tg://user?id={ok.id})"
            user += f"•{kk}" + "\n"
        await e.eor(user)
    else:
        await e.eor("**Cowo\n20th\njateng**")


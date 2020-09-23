import discord
from discord.ext import commands
from yonosumi_utils.embed import YonosumiEmbed

def check_owner(member :discord.Member, channel :discord.TextChannel) -> bool:
    """
    選択したメンバーが個人チャンネルの所有者か確認できます。
    """
    if channel.permissions_for(member).manage_channels == True:
        return True
    else:
        return False

def is_nedoko(channel :discord.TextChannel) -> bool:
    """
    指定したチャンネルが寝床であるか確認します。
    """
    if channel.category.name.startswith("ホームレス居住区") and channel.guild.id == 569928145906565126:
        return True
    else:
        return False
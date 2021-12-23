import datetime
import random

from discord import Embed, Colour
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_option, create_choice


def get_random_color():
    """Select random color"""
    return random.choice(['white', 'black'])


class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name="8ball",
                       description="The ball of predictions",
                       options=[create_option(
                           name="question",
                           description="Your question to the ball of predictions",
                           option_type=3,
                           required=True)
                       ])
    async def _8ball(self, ctx, *, question: str):
        """The ball of predictions"""
        responses = ["It is certain...",
                     "It is decidedly so...",
                     "Without a doubt...",
                     "Yes — definitely...",
                     "You may rely on it...",
                     "As I see it, yes...",
                     "Most likely...",
                     "Outlook good...",
                     "Signs point to yes...",
                     "Yes...",
                     "Reply hazy, try again...",
                     "Ask again later...",
                     "Better not tell you now...",
                     "Cannot predict now...",
                     "Concentrate and ask again...",
                     "Don’t count on it...",
                     "My reply is no...",
                     "My sources say no...",
                     "Outlook not so good...",
                     "Very doubtful..."]
        await ctx.send(embed=Embed(title=f"**Question:** `{question}`",
                    description=f"**Answer:** `{random.choice(responses)}`",
                    color=Colour(0x59d9b9)))

    @cog_ext.cog_slash(name="about", description="About Parzibot")
    async def about(self, ctx):
        """About Parzibot"""
        await ctx.send(embed=Embed(title=f"About **Parzibot**",
                    description=f"**Parzibot** is free open-source project, created by **merive_**\n"
                    f"You can find more information on [Parzibot Website](https://merive.herokuapp.com/Parzibot)\n"
                    f"**Parzibot**, {datetime.datetime.now().year}",
                    color=Colour(0x59d9b9)))

    @cog_ext.cog_slash(name="clear",
                       description="Clear current Text Channel",
                       options=[
                           create_option(
                               name="number",
                               description="Number of messages for clear",
                               option_type=4,
                               required=False)
                       ])
    async def clear(self, ctx, number=5):
        """Clear current Text Channel"""
        if number > 0:
            await ctx.channel.purge(limit=number)
            await ctx.send(embed=Embed(title=f"Cleared **{number}** messages",
                    color=Colour(0x59d9b9)))
        else:
            await ctx.send(embed=Embed(title=f"Cannot clear **{number}** messages",
                    color=Colour(0xd95959)))
            

    @cog_ext.cog_slash(name="getgame", description="Choice random game from our list")
    async def getgame(self, ctx):
        """Choice random game from our list"""
        responses = ["Minecraft", "GTA V", "Fortnite", "PUBG", "League of Legends", "CS:GO", "Dota 2", "Apex Legends",
                     "Rocket League",
                     "Rainbow Six: Siege", "Overwatch", "RDR 2", "Dead by Daylight", "Call of Duty: Warzone",
                     "Cyberpunk 2077", "The Elder Scrolls V: Skyrim",
                     "Forza Horizon 4", "Assasin's Creed Valhalla", "Animal Crossing: New Horizons", "Valorant",
                     "Fall Guys", "Terraria", "Fallout 76",
                     "Super Animal Royale", "Genshin Impact", "Control"]
        await ctx.send(embed=Embed(title=f"Play to **{random.choice(responses)}**",
                    color=Colour(0x59d9b9)))

    @cog_ext.cog_slash(name="help", description="List of Parzibot Commands")
    async def help(self, ctx):
        """List of Parzibot Commands"""
        await ctx.send(embed=Embed(title=f"Bot Commands",
                    description=' - **/8ball** `question` - The ball of predictions\n'
                       ' - **/about** - About Parzibot\n'
                       ' - **/clear** `number` - Clear current Text Channel\n'
                       ' - **/getgame** - Choice random game from our list\n'
                       ' - **/help** - List of Parzibot commands\n'
                       ' - **/ping** - Parzibot ping\n'
                       ' - **/users** - List of Text Channel members\n'
                       ' - **/whiteblack** `white/black` - The White/Black Game\n',
                    color=Colour(0x59d9b9)))

    @cog_ext.cog_slash(name="ping", description="Parzibot ping")
    async def ping(self, ctx):
        """Parzibot ping"""
        await ctx.send(embed=Embed(title=f"**Parzibot** Ping: `{round(self.client.latency * 1000)}ms`",
                    color=Colour(0x59d9b9)))

    @cog_ext.cog_slash(name="users", description="List of Text Channel members")
    async def users(self, ctx):
        """List of Text Channel members"""
        channel = ctx.channel
        members = "".join(f'\t**{member}**\n' for member in channel.members)
        await ctx.send(embed=Embed(title=f"Channel Members",
                    description=f"{members}",
                    color=Colour(0x59d9b9)))

    @cog_ext.cog_slash(name="whiteblack",
                       description="The White/Black Game",
                       options=[
                           create_option(
                               name="color",
                               description="Your color",
                               option_type=3,
                               required=True,
                               choices=[
                                   create_choice(name="White", value="white"),
                                   create_choice(name="Black", value="black")
                               ]
                           )
                       ])
    async def white_black(self, ctx, color: str):
        """The White/Black Game"""
        result = get_random_color()
        if color == result:
            await ctx.send(embed=Embed(title=f"You won :D",
                    description=f"Right color is `{result}`",
                    color=Colour(0x59d9b9)))
        else:
            await ctx.send(embed=Embed(title=f"You lose :(",
                    description=f"Right color is `{result}`",
                    color=Colour(0xd95959)))


def setup(client):
    """Setup function"""
    client.add_cog(Commands(client))

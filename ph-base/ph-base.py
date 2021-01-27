from redbot.core import commands

class PHBase(commands.Cog):
    """PauHana Base Bot"""

    @commands.command()
    async def mycom(self, ctx):
        """PauHana Base Framework Bot!"""
        # Your code will go here
        await ctx.send("Chee Hoo fakas!")
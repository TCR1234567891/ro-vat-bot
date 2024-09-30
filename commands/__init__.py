from .utility.help import setup as helpcmd
from .utility.profile import setup as profile
from .utility.post import setup as post
from .utility.embed import setup as embed
from .utility.controller_leaderboard import setup as controller_leaderboard
from .training.training_log import setup as training_log
from .training.training_del import setup as training_del
from .training.training_clr import setup as training_clr
from .events.atis_post import setup as atis_post
from .events.log_on import setup as log_on
from .events.log_off import setup as log_off
from .events.atis_post import setup as atis_post
from .events.start_event import setup as start_event
from .events.end_event import setup as end_event


def setup(bot):
    helpcmd(bot)
    profile(bot)
    post(bot)
    embed(bot)
    controller_leaderboard(bot)
    training_log(bot)
    training_del(bot)
    training_clr(bot)
    log_on(bot)
    log_off(bot)
    atis_post(bot)
    start_event(bot)
    end_event(bot)
    
    
    print("\nInitialized Commands\n ")


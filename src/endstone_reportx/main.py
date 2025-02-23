import sqlite3
import endstone
#from endstone.event import event_handler, PlayerJoinEvent, PlayerQuitEvent, PlayerChatEvent, PlayerCommandEvent, PlayerLoginEvent

from endstone.command import Command, CommandSender
from endstone.plugin import Plugin
import time

alert_prefix = "§7«§6 Starnet §7»§e "

class reportx(Plugin):
    api_version = "0.5"

    def on_enable(self) -> None:
        self.logger.info("ReportX Plugin is activated!")
        #self.register_events(self)

    commands = {
        "report": {
            "description": "Report a player",
            "usages": ["/report <playername: string> <reason: string>"],
        }
    }

    permissions = {
        "reportx.command.report": {
            "description": "Allow users to use the /report command.",
            "default": True,
        }
    }
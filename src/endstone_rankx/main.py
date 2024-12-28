import sqlite3
import endstone
from endstone.event import event_handler, PlayerJoinEvent, PlayerQuitEvent, PlayerChatEvent, PlayerCommandEvent, PlayerLoginEvent

from endstone.command import Command, CommandSender
from endstone.plugin import Plugin
import time

alert_prefix = "§7«§6 Starnet §7»§e "

class rankx(Plugin):
    api_version = "0.5"
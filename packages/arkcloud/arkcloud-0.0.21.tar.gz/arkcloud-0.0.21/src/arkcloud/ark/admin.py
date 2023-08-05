from arkcloud.web import ArkWebsite
from arkcloud.lib import get_admin_password, get_map


class Admin:
    def __init__(self):
        # ctrl-x to clear console
        # ctrl-c to copy console
        self.driver = ArkWebsite()
        self.driver.lobby()
        self.driver.press_play()
        self.driver.join_server()
        self.enable_admin()
        self.command_list = []
        self.map = get_map()

    def execute(self):
        if len(self.command_list) > 0:
            command = '|'.join(self.command_list)
            self.driver.cmd(command)
            self.command_list.clear()

    def enable_admin(self):
        self.enable_cheats(get_admin_password())
        self.gcm()
        self.ghost()
        return self

    def enable_cheats(self, password):
        self.command_list.append(CreativeMode.ENABLE_CHEATS.format(password))
        return self

    def gcm(self):
        self.command_list.append(CreativeMode.GIVE_CREATIVE_MODE)
        return self

    def ghost(self):
        """ Allows to go through walls """
        self.command_list.append(PlayerManagement.GHOST)
        self.command_list.append(PlayerManagement.LEAVE_ME_ALONE)
        self.command_list.append(PlayerManagement.GOD)
        self.command_list.append(PlayerManagement.CLEAR_MY_BUFFS)
        self.command_list.append(PlayerManagement.REFILL_STATS)
        return self

    def enable_spectator(self):
        """ Once you enter the spectator state your body will disapear and your inventory items
        will be erased as well. If you leave the game and rejoin it will carry on where you left
        off, thus using the command "stopspectating" is highly recommended. The latter will
        show the respawn map. """
        self.command_list.append(Spectator.ENABLE_SPECTATOR)
        return self

    def stop_spectating(self):
        """ Stops spectating """
        self.command_list.append(Spectator.STOP_SPECTATING)
        return self

    def message_server(self, message):
        """ Writes to chat as a server message to all players"""
        self.command_list.append(ServerManagement.SERVER_CHAT.format(message))
        return self

    def broadcast(self, message):
        """ Sends a message to the whole server using the banner """
        self.command_list.append(ServerManagement.BROADCAST.format(str(message)))
        return self

    def quit(self):
        self.driver.quit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.execute()

    def restart_application(self):
        self.driver.menu_reset()
        self.driver.dashboard_reset()
        self.driver.lobby()
        self.driver.press_play()
        self.driver.join_server()
        self.enable_admin()


class CreativeMode:
    ENABLE_CHEATS = "EnableCheats {}"
    GIVE_CREATIVE_MODE = "cheat GCM"


class Spectator:
    ENABLE_SPECTATOR = "cheat EnableSpectator"
    STOP_SPECTATING = "cheat StopSpectating"


class ServerManagement:
    BROADCAST = "cheat Broadcast {}"
    SERVER_CHAT = "cheat ServerChat {}"
    SERVER_CHAT_TO = "cheat ServerChatTo {} {}"
    SERVER_CHAT_TO_Player = "cheat ServerChatToPlayer {} {}"


class Teleportation:
    TELEPORT = "cheat Teleport"
    TELEPORT_PLAYER_ID_TO_ME = "cheat TeleportPlayerIdToMe {}"
    TELEPORT_PLAYER_NAME_TO_ME = "cheat TeleportPlayerNameToMe {}"
    TELEPORT_TO_PLAYER = "cheat TeleportToPlayer {}"
    TP = "cheat TP {}"
    TP_COORDS = "cheat TPCoords {} {} {}"
    SET_PLAYER_POS = "cheat SetPlayerPos {} {} {}"


class PlayerManagement:
    FLY = "cheat Fly"
    GHOST = "cheat Ghost"
    GOD = "cheat God"
    INFINITE_STATS = "cheat InfiniteStats"
    LEAVE_ME_ALONE = "cheat LeaveMeAlone"
    REFILL_STATS = "cheat RefillStats"
    CLEAR_MY_BUFFS = "cheat ClearMyBuffs"

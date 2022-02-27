CREATE_INSTANT_INVITE = 0x0000000001  # Allows creation of instant invites
KICK_MEMBERS = 0x0000000002  # Allows kicking members
BAN_MEMBERS = 0x0000000004  # Allows banning members
# Allows all permissions and bypasses channel permission overwrites
ADMINISTRATOR = 0x0000000008
MANAGE_CHANNELS = 0x0000000010  # Allows management and editing of channels
MANAGE_GUILD = 0x0000000020  # Allows management and editing of the guild
ADD_REACTIONS = 0x0000000040  # Allows for the addition of reactions to messages
VIEW_AUDIT_LOG = 0x0000000080  # Allows for viewing of audit logs
# Allows for using priority speaker in a voice channel
PRIORITY_SPEAKER = 0x0000000100
STREAM = 0x0000000200  # Allows the user to go live
# Allows guild members to view a channel, which includes reading messages in text channels
VIEW_CHANNEL = 0x0000000400
SEND_MESSAGES = 0x0000000800  # Allows for sending messages in a channel
SEND_TTS_MESSAGES = 0x0000001000  # Allows for sending of /tts messages
MANAGE_MESSAGES = 0x0000002000  # Allows for deletion of other users messages
# Links sent by users with this permission will be auto-embedded
EMBED_LINKS = 0x0000004000
ATTACH_FILES = 0x0000008000  # Allows for uploading images and files
READ_MESSAGE_HISTORY = 0x0000010000  # Allows for reading of message history
# Allows for using the @everyone tag to notify all users in a channel,
MENTION_EVERYONE = 0x0000020000
# and the @here tag to notify all online users in a channel
# Allows the usage of custom emojis from other servers
USE_EXTERNAL_EMOJIS = 0x0000040000
VIEW_GUILD_INSIGHTS = 0x0000080000  # Allows for viewing guild insights
CONNECT = 0x0000100000  # Allows for joining of a voice channel
SPEAK = 0x0000200000  # Allows for speaking in a voice channel
MUTE_MEMBERS = 0x0000400000  # Allows for muting members in a voice channel
DEAFEN_MEMBERS = 0x0000800000  # Allows for deafening of members in a voice channel
MOVE_MEMBERS = 0x0001000000  # Allows for moving of members between voice channels
USE_VAD = 0x0002000000  # Allows for using voice-activity-detection in a voice channel
CHANGE_NICKNAME = 0x0004000000  # Allows for modification of own nickname
MANAGE_NICKNAMES = 0x0008000000  # Allows for modification of other users nicknames
MANAGE_ROLES = 0x0010000000  # Allows management and editing of roles
MANAGE_WEBHOOKS = 0x0020000000  # Allows management and editing of webhooks
MANAGE_EMOJIS = 0x0040000000  # Allows management and editing of emojis
# Allows members to use slash commands in text channels
USE_SLASH_COMMANDS = 0x0080000000
# Allows for requesting to speak in stage channels.
REQUEST_TO_SPEAK = 0x0100000000
# (This permission is under active development and may be changed or removed.)
# Allows for deleting and archiving threads, and viewing all private threads
MANAGE_THREADS = 0x0400000000
# Allows for creating and participating in threads
USE_PUBLIC_THREADS = 0x0800000000
# Allows for creating and participating in private threads
USE_PRIVATE_THREADS = 0x1000000000
 
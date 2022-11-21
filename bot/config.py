from bot.get_cfg import get_config
class Config(object):
    SESSION_NAME = get_config("SESSION_NAME", "AHCompressorBot")
    FFMPEG = get_config("FFMPEG", "ffmpeg -hide_banner -loglevel quiet -progress '''{}''' -i '''{}'''  -i 'https://te.legra.ph/file/e9408e71281cdcb017874.png' -map 0 -filter_complex 'overlay =main_w-(overlay_w+10):main_h-(overlay_h+10)'  -c:v libx265 -crf 27.5 -c:s copy? -s 1280x720 -preset superfast -metadata title='Visit For More Movies [t.me/AniXpo]'  -metadata:s:v title='Visit Website[Anixpo] t.me/AniXpo] - 720p - HEVC - 8bit'  -metadata:s:a title='[Visit t.me/AniXpo] - Opus - 96 kbps' -metadata:s:s title='[AniXpo Substations Alpha]' -c:a libopus -ab 96k -vbr 2 -ac 2 -level 3.1 '''{}''' -y")
    APP_ID = get_config("APP_ID", "8978848")
    API_HASH = get_config("API_HASH", "24ce3cff2d32cf529df1c0018e28d6cf")
    LOG_CHANNEL = get_config("LOG_CHANNEL", "zubEncoderLog")
    LOGZ = get_config("LOGZ" "zubEncoderLog")
    UPDATES_CHANNEL = get_config("UPDATES_CHANNEL", None)
    AUTH_USERS = set(
        int(x) for x in get_config(
            "AUTH_USERS", "1482769753 1995886602 -1001816242004"
        ).split()
    )
    TG_BOT_TOKEN = get_config("TG_BOT_TOKEN", "2023958354:AAFezUBfrPUmpDNus6vhVlwUHqvMuxXRXDA")
    DOWNLOAD_LOCATION = get_config("DOWNLOAD_LOCATION", "/app/downloads")
    BOT_USERNAME = get_config("BOT_USERNAME", "X04compress_bot")
    MAX_FILE_SIZE = 2097152000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 2097152000
    DEF_THUMB_NAIL_VID_S = get_config("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    HTTP_PROXY = get_config("HTTP_PROXY", None)
    MAX_MESSAGE_LENGTH = 4096
    FINISHED_PROGRESS_STR = get_config("FINISHED_PROGRESS_STR", "■")
    UN_FINISHED_PROGRESS_STR = get_config("UN_FINISHED_PROGRESS_STR", "□")
    LOG_FILE_ZZGEVC = get_config("LOG_FILE_ZZGEVC", "Log.txt")
    SHOULD_USE_BUTTONS = get_config("SHOULD_USE_BUTTONS", False)

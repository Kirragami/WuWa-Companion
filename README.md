Discord Bot for convenience features while playing Wuthering Waves.

Current features- <br />
1. Union Level Calculator : Calculates how many days to reach a target union level. <br />
    Command : !!union current_level current_xp target_level (Ex. !!union 57 12500 60)<br />

2. Pity Counter : Shows where your pity stands currently on limited banners.<br />
    Command : !!pity<br />

You need to first setup these in environment variables along with the bot TOKEN<br />
PLAYER_ID_DICT = '{"discord tag" : "wuwa player id"}'<br />
PLAYER_RECORD_ID = '{"discord tag" : "your pull record id"}'<br />

You can obtain player id and record id from debug.log file in the game path : WutheringWavesj3oFh\Wuthering Waves Game\Client\Binaries\Win64\ThirdParty\KrPcSdk_Global\KRSDKRes

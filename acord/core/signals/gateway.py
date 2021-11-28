DISPATCH        = 0
HEARTBEAT       = 1
IDENTIFY        = 2
PRESENCE        = 3
VOICE           = 4
RESUME          = 6
RECONNECT       = 7
GUILDMEMBERS    = 8
INVALIDSESSION  = 9
HELLO           = 10
HEARTBEATACK    = 11

# Error Codes
UNKNOWN             = 4000
UNKNOWN_OP          = 4001
DECODE_ERROR        = 4002
FORBIDDEN           = 4003
AUTH_FAILED         = 4004
AUTH_COMPLETED      = 4005
FAILED_SEQUENCE     = 4007
RATELIMIT           = 4008
SESSION_TIMED_OUT   = 4009
INVALID_SHARD       = 4010
SHARD_REQUIRED      = 4011
INVALID_GATEWAY_VER = 4012
INVALID_INTENTS     = 4013
DISALLOWED_INTENT   = 4014

# GLOBAL STORES
SEQUENCE            = None

def heartbeatPacket():
    return {
        "op": HEARTBEAT,
        "d": SEQUENCE
    }

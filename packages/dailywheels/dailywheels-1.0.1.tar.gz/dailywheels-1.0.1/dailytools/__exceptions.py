class OfflineTTSError(Exception):
        pass

class OnlineTTSError(Exception):
        pass
    
class OptionsError(Exception):
        pass
    
class DBInsertError(Exception):
        pass
    
class DBSearchError(Exception):
        pass
    
class SynthesizeError(Exception):
    pass

class NetConfigError(Exception):
    pass

class ConfigNotFoundError(Exception):
    pass

class NetConnectError(Exception):
    pass

class BotInitError(Exception):
    pass

class FormatNotSupport(Exception):
    pass
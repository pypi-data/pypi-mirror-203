class App:
    from functools import cached_property as _cached_property
    _setupCalled = False
    _instance = None #type: App

    def __init__(self, appName:str, appCompany:str=None, extraIdentifier:str=None) -> None:
        import os
        import simpleworkspace.io.directory
        import simpleworkspace.io.path
        from simpleworkspace.logproviders import RotatingFileLogger
        from simpleworkspace.settingsproviders import SettingsManager_JSON

        if(not self._setupCalled):
            raise TypeError("Class initialized incorrectly, use Setup()...")

        self.appName = appName
        self.appCompany = appCompany
        self.extraIdentifier = extraIdentifier

        self.path_AppData = simpleworkspace.io.path.GetAppdataPath(appName, appCompany)
        ''''C:\\Users\\username\\AppData\\Roaming\\AppCompany\\AppName'''
        self.path_AppData_Storage = os.path.join(self.path_AppData, "storage")
        '''windows example: 'C:\\Users\\username\\AppData\\Roaming\\AppCompany\\AppName\\Storage'''
        simpleworkspace.io.directory.Create(self.path_AppData_Storage) # creates parent folders aswell
        
        self._path_LogFile = os.path.join(self.path_AppData, "App.log")
        self.logger = RotatingFileLogger.GetLogger(self._path_LogFile)

        self._path_AppSettingsFile = os.path.join(self.path_AppData, "AppConfig.json")
        self.settingsManager = SettingsManager_JSON(os.path.join(self.path_AppData, "AppConfig.json"))
        self.settingsManager.LoadSettings()
        return
    
    @_cached_property
    def appTitle(self):
        '''example: "appname - appcompany"'''
        return self.appName if self.appCompany is None else f"{self.appTitle} - {self.appCompany}"
    
    @_cached_property
    def appHash(self):
        '''appname + appcompany + extraidentifier hashed together, numeric hash'''
        return hash((self.appName, self.appCompany, self.extraIdentifier))

    @classmethod
    def Current(cls):
        if(cls._instance is None):
            raise ValueError("No application has been setup yet")
        return cls._instance
    
    @classmethod
    def Setup(cls, appName:str, appCompany:str=None, extraIdentifier:str=None):
        '''
        :param extraIdentifier: used for creating a more unique apphash to identify this program, will be bundled with appName and appCompany
        '''

        cls._setupCalled = True
        cls._instance = cls(appName, appCompany=appCompany, extraIdentifier=extraIdentifier)
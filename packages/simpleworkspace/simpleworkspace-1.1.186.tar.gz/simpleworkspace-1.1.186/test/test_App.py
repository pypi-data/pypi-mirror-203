import json
import simpleworkspace as sw
from basetestcase import BaseTestCase
from simpleworkspace.types.time import TimeEnum


class AppTest(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        sw.App.Setup(self.testAppName, self.testAppCompany)

    def tearDown(self) -> None:
        super().tearDown()
        app = sw.App.Current()
        if self.testAppName in app.path_AppData and self.testAppCompany in app.path_AppData:
            sw.io.directory.Remove(app.path_AppData)
        else:
            raise LookupError("Could not find appcompany and appname in filepath, not removing them for safety precaution")

    def test_settings_json(self):
        application = sw.App.Current()
        application.settingsManager.LoadSettings()
        application.settingsManager.Settings["test1"] = 10
        application.settingsManager.Settings["test2"] = 20
        application.settingsManager.SaveSettings()
        savedSettingData = sw.io.file.Read(application._path_AppSettingsFile)
        obj = json.loads(savedSettingData)
        self.assertEqual(obj, {"test1": 10, "test2": 20})

    def test_appdata_logging(self):
        app = sw.App.Current()
        app.logger.debug("test log 1")
        app.logger.debug("test log 2")
        app.logger.debug("test log 3")
        for handler in app.logger.handlers:
            handler.flush()
        logData = sw.io.file.Read(app._path_LogFile)
        result = sw.utility.regex.Match(f"/(.*?) (\w+?) <(.*?)>: (.*)/i", logData)
        
        self.assertEqual(len(result),  3)
        self.assertEqual(result[0][4],  "test log 1")
        self.assertEqual(result[1][4],  "test log 2")
        self.assertEqual(result[2][4],  "test log 3")
        pass

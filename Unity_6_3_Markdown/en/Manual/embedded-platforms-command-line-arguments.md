* [Platform development](PlatformSpecific.html)
* [Embedded systems](embedded-systems.html)
* [Logging in embedded platforms](embedded-platforms-logging.html)
* Command line arguments for logging

Configure a logging plug-in

Create a minimal URP setup for embedded platforms

# Command line arguments for logging

Use the following command line arguments to configure the standard log output and logging **plug-in**A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#plug-in) for embedded platforms.

| **Argument** | **Description** | **Use with** |
| --- | --- | --- |
| `-nolog` | Disables the log output completely. | standard log output |
| `-logfile [path/to/logfile]` | Routes the Player log output including `stderr` to the specified log file. You can use this parameter to get trace information when the logging plug-in initializes. The log file path set using this argument has a precedence over the path set using `-platform-hmi-player-datapath`.  **Note:** If the specified file path has write restrictions, the Unity Player exits with an error code. | standard log output and logging plug-in |
| `-logfile -` | Forces the Player to route the log output including `stderr` to the console through `stdout` instead of writing to the specified file. You can use this parameter to get trace information when the logging plug-in initializes. | standard log output and logging plug-in |
| `-logflush` | Synchronizes the log output with every log event, which can be helpful in crash investigations. | standard log output |
| `-platform-hmi-log-plugin [plugin.so]` | Specifies the logging plug-in’s shared library. Needs to be located in the Plugins folder. | logging plug-in |
| `-platform-hmi-log-plugin [" "]` | Disables the configured logging plug-in temporarily. | logging plug-in |
| `-platform-hmi-log-disable-on-plugin-failure` | Disables the log output when the logging plug-in fails to initialize. | logging plug-in |
| `-platform-hmi-player-datapath [path/to/writable/folder]` | Specifies the path where the Player log output is saved as persistent data. By default, Unity uses the value of `HOME` environment variable to set this path to your system’s home directory. You can configure this path through **Player Settings** > **Other Settings** > **Configuration** > **Player Data path**. | standard log output |

## Additional resources

* [Standard log output overview](embedded-platforms-standard-logoutput.html)
* [Configure a logging plug-in](embedded-platforms-configure-logging-plugin.html)

Configure a logging plug-in

Create a minimal URP setup for embedded platforms

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
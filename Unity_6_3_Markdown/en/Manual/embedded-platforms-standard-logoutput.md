* [Platform development](PlatformSpecific.html)
* [Embedded systems](embedded-systems.html)
* [Logging in embedded platforms](embedded-platforms-logging.html)
* Standard log output overview

Logging in embedded platforms

Configure a logging plug-in

# Standard log output overview

The log output is stored in a file or can be displayed in the console. When the Unity Player initializes, any initial errors are logged in the console through [`stderr`](https://learn.microsoft.com/en-us/cpp/c-runtime-library/stdin-stdout-stderr?view=msvc-170). If any initialization error occurs, Unity Player stops running with an error exit code.

By default, Unity writes standard log output into a log file located in your current home directory at `~/.config/unity3d/CompanyName/ProductName/Player.log`. You can customize this path via the [Player Data Path](embedded-linux-player-settings.html) setting (menu: **Player Settings** > **Other Settings** > **Configuration** > **Player Data path)** or using the [command line arguments](embedded-platforms-command-line-arguments.html).

If the standard log output fails to initialize, Unity writes the log output to the console.

## Additional resources

* [Configure a logging plug-in](embedded-platforms-configure-logging-plugin.html)
* [Command line arguments for logging](embedded-platforms-command-line-arguments.html)

Logging in embedded platforms

Configure a logging plug-in

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
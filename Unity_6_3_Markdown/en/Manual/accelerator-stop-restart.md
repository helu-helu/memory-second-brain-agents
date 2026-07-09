* [Assets and media](assets-and-media.html)
* [Caching assets](importing-caching-assets.html)
* Stop and restart Unity Accelerator

Configure Unity Accelerator in the Editor

Monitor Unity Accelerator

# Stop and restart Unity Accelerator

Unity **Accelerator**The Unity Accelerator is an external tool that provides an asset cache that keeps copies of a team’s imported assets. The goal of the Accelerator is to speed up teamwork and reduce iteration time by coordinating asset sharing so that you don’t need to reimport portions of your project. [More info](UnityAccelerator.html)  
See in [Glossary](Glossary.html#Accelerator) runs as a background process for each platform. To stop or restart Unity Accelerator for each platform, perform the following steps:

## Windows

1. Open the **Services Panel** by searching for the term `Services` in the Settings menu, or running `services.msc` in the **Run** dialog (**Win** + **R**).
2. Locate the `Unity Accelerator` service in the list. The option to **Stop the service** or **Restart the service** appears on the left panel.

Alternatively you can use the `net stop` and `net start` console commands from a terminal to stop and start the service.
Examples:
`C:\> net stop "Unity Accelerator" # Stops the service
C:\> net start "Unity Accelerator" # Starts the service`

## macOS

Run the `launchctl` command from the terminal to control the `com.unity3d.accelerator` service from the LaunchControl utility. For more information, refer to <https://www.launchd.info/>.

Examples:

```
$ sudo launchctl bootout system /Library/LaunchDaemons/com.unity3d.accelerator.plist    # Stops the service
$ sudo launchctl bootstrap system /Library/LaunchDaemons/com.unity3d.accelerator.plist  # Starts the service
$ sudo launchctl kickstart -k system/com.unity3d.accelerator                            # Restarts the service
```

## Linux

Use the `systemctl` console utility to control the `unity-accelerator` service. For more information, refer to <https://manpages.ubuntu.com/manpages/bionic/en/man1/systemctl.1.html>.

Examples:

```
$ sudo systemctl stop unity-accelerator.service     # Stops the service
$ sudo systemctl start unity-accelerator.service    # Starts the service
$ sudo systemctl restart unity-accelerator.service  # Restarts the service
```

## Additional resources

* [Monitor Unity Accelerator](accelerator-monitor.html)
* [Use Unity Accelerator on the command line](accelerator-command-line.html)
* [Command line arguments reference](EditorCommandLineArguments.html#accelerator)

Configure Unity Accelerator in the Editor

Monitor Unity Accelerator

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
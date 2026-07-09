* [Platform development](PlatformSpecific.html)
* [Dedicated Server](dedicated-server.html)
* Build your application for Dedicated Server

Dedicated Server optimizations

Dedicated Server AssetBundles

# Build your application for Dedicated Server

You can create a Dedicated Server build in either of the following ways:

* [Unity Editor](#unity-editor)
* [Scripting](#scripting)
* [Command line](#command-line)

## Unity Editor

To create a Dedicated Server build in the Unity Editor, use the following steps:

1. Open the [Build Profiles](BuildSettings.html)A set of customizable configuration settings to use when creating a build for your target platform. [More info](build-profiles.html)  
   See in [Glossary](Glossary.html#buildprofile) window from **File** > **Build Profiles**.
2. Select **Add Build Profile** to open the **Platform Browser** window.
3. Select the type of server to build from the list of available platforms. For example, select **Linux Server** to build a Linux server.
4. If the server type isn’t available, select **Install with Unity Hub** and follow the installation instructions. For information on how to install modules, refer to [Add modules](https://docs.unity.com/hub/add-modules.html).
5. Select **Switch Profile** to set the new build profile as the active profile.
6. Click **Build**.

**Tip**: You can further configure the Dedicated Server build in the [Player settings](dedicated-server-player-settings.html)Settings that let you set various player-specific options for the final game built by Unity. [More info](class-PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings).

## Scripting

To create a Dedicated Server build using a script, set `buildPlayerOptions.subtarget` to `(int)StandaloneBuildSubtarget.Server`.

```
buildPlayerOptions.target = BuildTarget.StandaloneWindows;
// SubTarget expects an integer.
buildPlayerOptions.subtarget = (int)StandaloneBuildSubtarget.Server;
```

Unity defines the `UNITY_SERVER` scripting symbol when you build for the Dedicated Server platform. You can use this symbol in your **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) to compile code for the server. For more information, refer to [Scripting symbol reference](scripting-symbol-reference.html).

## Command line

To create a Dedicated Server build through the command line, use the `-standaloneBuildSubtarget Server` [argument](CommandLineArguments.html).

```
-buildTarget Linux64 -standaloneBuildSubtarget Server
```

A Dedicated Server build is a headless executable with no graphical interface. To interact with and configure your server application at runtime, use the [Unity Player command line arguments](PlayerCommandLineArguments.html) and the [DedicatedServer.Arguments API](../ScriptReference/DedicatedServer.Arguments.html).

## Code sign macOS Dedicated Server builds

Dedicated Server builds that aren’t code signed might display security warnings when deployed on macOS systems. To avoid such warnings, make sure you code sign the build before distribution. For more information, refer to the documentation on [Code sign and notarize your macOS application](macos-building-notarization.html).

## Additional resources

* [macOS build settings reference](macosbuildsettings.html)
* [Windows build settings reference](WindowsStandaloneBinaries.html)
* [Linux build settings reference](Buildsettings-linux.html)
* [Creating and Using Scripts](creating-scripts.html)
* [Scripting symbol reference](scripting-symbol-reference.html)

Dedicated Server optimizations

Dedicated Server AssetBundles

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
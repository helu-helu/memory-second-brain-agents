* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Developing for Android](android-developing.html)
* [Android application size restrictions](android-application-size-restrictions.html)
* APK expansion files

Introduction to asset splitting

APK expansion files in Unity

# APK expansion files

APK expansion files are the asset splitting solution for the **APK**The Android Package format output by Unity. An APK is automatically deployed to your device when you select File > Build & Run. [More info](android-BuildProcess.html)  
See in [Glossary](Glossary.html#APK) publishing format. They enable an application to split its assets into:

* Core assets like **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
  See in [Glossary](Glossary.html#Scripts), **plug-ins**A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)  
  See in [Glossary](Glossary.html#plug-in), and assets that the application requires for the first **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
  See in [Glossary](Glossary.html#Scene).
* Additional assets like [Streaming Assets](StreamingAssets.html) and assets that the application requires for additional scenes.

The core assets go in the main APK file and the additional assets go in APK expansion files.

[Digital distribution services](android-distribution.html) often have an application size limit. This makes it necessary for APK applications that are larger than the size limit to use APK expansion files. For example, Google Play requires applications that are larger than 100MB to use APK expansion files. It allows you to use two APK expansion files, the main APK expansion file, and the patch APK expansion file, which can be up to 2GB each. For more information, see [APK Expansion Files](https://developer.android.com/google/play/expansion-files.html).

Refer to the following sections to learn about APK expansion files and how to work with them in Unity.

| **Topic** | **Description** |
| --- | --- |
| [APK expansion files in Unity](android-apk-expansion-files-in-unity.html) | Learn how APK expansion files work in Unity and how you can create main and optional patch APK expansion files for your application. |
| [Create the main APK expansion file](android-apk-expansion-files-in-unity.html#CreateMainAPK) | Split your application into the APK and the main APK expansion file. |
| [Create the patch APK expansion file](android-apk-expansion-files-in-unity.html#CreatePatchAPK) | Create the optional patch APK expansion file. |
| [Manually install an APK expansion file](android-apk-expansion-files-install.html) | Manually install an APK expansion file on a device for local testing. |
| [Host APK expansion files](android-apk-expansion-files-host.html) | Learn how to host APK expansion files for your application. |

Introduction to asset splitting

APK expansion files in Unity

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
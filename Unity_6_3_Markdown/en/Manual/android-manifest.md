* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Introducing Android](android-introducing.html)
* Android App Manifest

Troubleshooting Gradle build issues for Android

Unity Launcher Manifest

# Android App Manifest

The Android App Manifest contains information about an Android application. Each application has a single Android App Manifest [XML](https://en.wikipedia.org/wiki/XML) file at the root of the [source set](https://developer.android.com/studio/build#sourcesets) called `AndroidManifest.xml`. The Android operating system and digital distribution services (for example, Google Play) use Android App Manifests to find information, such as the application’s name, the application’s [entry point](https://developer.android.com/guide/components/activities/intro-activities), Android version support, hardware features support, and application permissions. For more information about the Android App Manifest file, and for a list of settings that it configures, see the Android Developer documentation on [Android App Manifests](https://developer.android.com/guide/topics/manifest/manifest-intro.html).

To generate an Android App Manifest to represent an application, Gradle merges manifest files from a variety of sources. This includes:

* **Unity Library Manifest**: A manifest file that Unity produces which configures Unity Player activities. For more information, see [Unity Library Manifest](android-library-manifest.html).
* **Unity Launcher Manifest**: A manifest file that Unity produces which configures the application that wraps the Unity library. For more information, see [Unity Launcher Manifest](android-launcher-manifest.html).
* ****Plug-in**A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)  
  See in [Glossary](Glossary.html#plug-in) manifests**: Manifest files that represent plug-ins such as Android Archives (AAR) or Android Library plug-ins.

For information on how Unity uses these manifest files to generate an Android App Manifest, see [Generating an Android App Manifest](#generating-an-android-manifest).

## Generating an Android App Manifest

The [Android application build process](how-unity-builds-android-applications.html) generate an Android App Manifest file for the application. To do this:

1. Unity uses the Unity Library Manifest as a template for the Android App Manifest. If you [override the Unity Library Manifest](android-modify-gradle-project-files-templates.html), Unity uses the file you specify as the template.
2. Unity updates the Unity Library Manifest and Unity Launcher Manifest files with information such as [permissions](#permissions), configuration options, and the features that the application uses.
3. [Gradle](android-gradle-overview.html)An Android build system that automates several build processes. This automation means that many common build errors are less likely to occur. [More info](android-gradle-overview.html)  
   See in [Glossary](Glossary.html#Gradle) merges the Unity Library Manifest, Unity Launcher Manifest, and plug-in manifests into one Android App Manifest file.

You can view the Android App Manifest file inside the output Android App Bundle (AAB) or Android Package (APK) using the [Android Studio APK Analyzer](https://developer.android.com/studio/build/apk-analyzer.html), or another third-party tool such as [Apktool](https://ibotpeaches.github.io/Apktool/).

**Important**: You cannot edit the Android App Manifest file in the **APK**The Android Package format output by Unity. An APK is automatically deployed to your device when you select File > Build & Run. [More info](android-BuildProcess.html)  
See in [Glossary](Glossary.html#APK) or AAB. For information on how to override the contents of an Android App Manifest, refer to [Modify Gradle project files](android-modify-gradle-project-files.html).

## Permissions

Unity automatically adds the necessary permissions to the manifest based on the [Android Player Settings](class-PlayerSettingsAndroid.html) and Unity APIs that your application calls from C# **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts). For example:

* The following classes, packages, and Player setting add the `INTERNET` permission.
  + Setting **Internet Access** to **Require** in [Android Player settings](class-PlayerSettingsAndroid.html#Configuration) for **development builds**A development build includes debug symbols and enables the Profiler. [More info](building-introduction.html)  
    See in [Glossary](Glossary.html#developmentbuild).
  + [UnityWebRequest](../ScriptReference/Networking.UnityWebRequest.html) and [Ping](../ScriptReference/Ping.html) classes
  + [System.Net.Sockets](https://learn.microsoft.com/en-us/dotnet/api/system.net.sockets.socket?view=net-8.0)  API
  + [Unity Analytics](https://docs.unity.com/ugs/manual/analytics/manual/overview)A data platform that provides analytics for your Unity game. [More info](https://docs.unity.com/ugs/en-us/manual/analytics/manual/overview)  
    See in [Glossary](Glossary.html#UnityAnalytics) package and **Crash and Exception Reporting** in the [Cloud Diagnostics package](https://docs.unity.com/ugs/manual/cloud-diagnostics/manual/CloudDiagnostics/WelcometoCloudDiagnostics).
* Using vibration (such as [Handheld.Vibrate](../ScriptReference/Handheld.Vibrate.html)) adds `VIBRATE`.
* The [InternetReachability](../ScriptReference/Application-internetReachability.html) property adds `ACCESS_NETWORK_STATE`.
* Location APIs (such as [LocationService](../ScriptReference/LocationService.html)) adds `ACCESS_FINE_LOCATION`
* [WebCamTexture](../ScriptReference/WebCamTexture.html) APIs add `CAMERA`.
* The [Microphone](../ScriptReference/Microphone.html) class adds `RECORD_AUDIO`.

If a plug-in requires a permission that is declared in its manifest, Unity automatically adds the permission to the final Android App Manifest during the Gradle merge stage. Note that Unity includes all Unity APIs that the plug-ins use in the permissions list.

To [request permissions at runtime](android-RequestingPermissions.html) using the Android runtime permission system, you must first declare the permission in the Android App Manifest. For more information, refer to the Android documentation on [Request runtime permissions](https://developer.android.com/training/permissions/requesting.html).

## Additional resources

* [Declare permissions for an application](android-permissions-declare.html)
* [Android App Manifest Permissions](https://developer.android.com/guide/topics/manifest/manifest-intro.html#perms)
* [Add a Network Security Configuration file](https://developer.android.com/privacy-and-security/security-config#manifest)

Troubleshooting Gradle build issues for Android

Unity Launcher Manifest

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Developing for Android](android-developing.html)
* [Testing and debugging](android-testing-and-debugging.html)
* Troubleshooting for Android

Application patching

Optimization for Android

# Troubleshooting for Android

Learn how to resolve common issues when developing Android applications using Unity.

## Android manifest file contains unexpected permissions

When building a Unity Android application, the final application manifest might contain permissions that you didn’t explicitly add to your project. Such unexpected permissions might cause issues when you want to distribute your application through distribution services, such as the Play Store.

### Symptom

The application manifest contains unexpected permission entries that aren’t part of your project’s manifest files.

### Cause

When building a Unity Android application, **Gradle**An Android build system that automates several build processes. This automation means that many common build errors are less likely to occur. [More info](android-gradle-overview.html)  
See in [Glossary](Glossary.html#Gradle) generates the final application manifest by merging manifest files from various sources including **plug-ins**A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#plug-in) and packages. This process might automatically include certain unexpected permissions in the manifest based on the dependencies and the target SDK version.

### Resolution

To identify and resolve such unexpected permissions, use the manifest merger log file that Gradle generates when you [build your Android application](android-BuildProcess.html). This log file provides information on how and why Gradle adds each manifest element. Follow these steps:

1. Build your application in `.apk` or `.aab` format.
2. Go to the `logs` directory under `<your_project>/Library/Bee/Android/Prj/IL2CPP/Gradle/launcher/build/outputs`.
3. Open the appropriate log file based on the build type.

   * **Release build**: `manifest-merger-release-report.txt`
   * ****Development build**A development build includes debug symbols and enables the Profiler. [More info](building-introduction.html)  
     See in [Glossary](Glossary.html#developmentbuild)**: `manifest-merger-debug-report.txt`
4. Look for log entries that start with `IMPLIED` to identify unexpected permissions. The log file displays information as follows:

   ```
   IMPLIED from D:\MyProject\Library\Bee\Android\Prj\IL2CPP\Gradle\launcher\src\main\AndroidManifest.xml:2:1-5:12 reason: com.test.package has a targetSdkVersion < 4
   uses-permission#android.permission.READ_PHONE_STATE
   ```
5. Check the `reason` field to identify the cause of the unexpected permission. In this example, the log entry indicates that Gradle added the `uses-permission#android.permission.READ_PHONE_STATE` permission because the `targetSdkVersion` of the `com.test.package` is lower than `4`.
6. Contact the owner of the package to request updating the target SDK version to match your project’s target SDK version.

## Additional resources

* [Debug on Android devices](android-debugging-on-an-android-device.html)
* [Android App Manifest](android-manifest.html)
* [Troubleshooting Gradle build issues for Android](android-gradle-troubleshooting.html)

Application patching

Optimization for Android

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
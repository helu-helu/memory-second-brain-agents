* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Introducing Android](android-introducing.html)
* How Unity builds Android applications

Unity Library Manifest

Getting started with Android

# How Unity builds Android applications

Unity uses [Gradle](android-gradle-overview.html)An Android build system that automates several build processes. This automation means that many common build errors are less likely to occur. [More info](android-gradle-overview.html)  
See in [Glossary](Glossary.html#Gradle) to build Android applications so it’s useful to understand the build process and how Unity interacts with Gradle. Gradle lets you use [Player Settings](class-PlayerSettingsAndroid.html)Settings that let you set various player-specific options for the final game built by Unity. [More info](class-PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings) and other Unity windows to configure most aspects of the final build, however for more control, you must overwrite [manifest](android-manifest.html)There are two types of manifest files: **project manifest****s** and **package manifest****s**.  
See in [Glossary](Glossary.html#manifest) and [template](android-gradle-overview.html) files, or export your project and edit it in [Android Studio](https://developer.android.com/studio/index.html).

## The build process

To build Android applications:

1. Unity calls [AndroidProjectFilesModifier.Setup](../ScriptReference/Android.AndroidProjectFilesModifier.Setup.html) for all [AndroidProjectFilesModifier](../ScriptReference/Android.AndroidProjectFilesModifier.html) interfaces. You can use this callback to set up prerequisites for modifying custom Android Gradle project files. For more information, refer to [AndroidProjectFilesModifier.Setup](../ScriptReference/Android.AndroidProjectFilesModifier.Setup.html).
2. Unity collects project resources, code libraries, **plug-ins**A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)  
   See in [Glossary](Glossary.html#plug-in), Gradle templates, and manifest templates from your Unity project and uses them to create a valid Gradle project.
3. Unity adds and updates values inside Gradle templates and manifest files based on the Unity project’s Player settings and build settings.
4. If you chose to export the project and not build it, and use the **IL2CPP**A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](./scripting-backends-il2cpp.html)  
   See in [Glossary](Glossary.html#IL2CPP) [scripting backend](scripting-backends.html)A framework that powers scripting in Unity. Unity supports three different scripting backends depending on target platform: Mono, .NET and IL2CPP. Universal Windows Platform, however, supports only two: .NET and IL2CPP. [More info](scripting-backends.html)  
   See in [Glossary](Glossary.html#ScriptingBackend), Unity places C++ source files produced from your C# **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
   See in [Glossary](Glossary.html#Scripts) into the Gradle project. Otherwise, if you chose to build the project, Unity places the `libil2cpp.so` library into the Gradle project.
5. Unity calls [OnModifyAndroidProjectFiles](../ScriptReference/Android.AndroidProjectFilesModifier.OnModifyAndroidProjectFiles.html) for all [AndroidProjectFilesModifier](../ScriptReference/Android.AndroidProjectFilesModifier.html) interfaces. You can use this callback to modify Gradle project file values. For more information, refer to [Modify Gradle project files with the Android Project Configuration Manager](android-modify-gradle-project-files-agp.html).  
   **Note**: You can modify Android Gradle project files in custom modules only.
6. Unity calls [OnPostGenerateGradleAndroidProject](../ScriptReference/Android.IPostGenerateGradleAndroidProject.OnPostGenerateGradleAndroidProject.html) for all [IPostGenerateGradleAndroidProject](../ScriptReference/Android.IPostGenerateGradleAndroidProject.html) interfaces. You can use this callback to modify or move files before Gradle builds the application.
7. Unity runs Gradle to build the application from the Gradle project. Gradle merges the Unity Library Manifest, Unity Launcher Manifest, and plug-in manifests into one [Android App Manifest](android-manifest.html) file.

## Incremental build pipeline

Unity uses the [incremental build pipeline](building-introduction.html#incremental-build-pipeline) when it builds the Player for Android. See the following Android-specific incremental build pipeline behaviors:

* Unity incrementally builds/generates:
  + [Gradle files](android-gradle-overview.html)
  + [Manifest files](android-manifest.html)
  + [Assets packs](play-asset-delivery.html)
  + [APK expansion files (obbs)](android-OBBsupport.html)
  + Uncompressed asset splits
  + [Android symbols zip files](android-symbols.html)
* Unity incrementally copies:
  + Player binaries
  + Gradle resources
* The last step in the [build process](#the-build-process) is to run Gradle. From this point, the build process doesn’t use the incremental build pipeline and it’s up to Gradle to track dependencies.

If you implement [IPostGenerateGradleAndroidProject](../ScriptReference/Android.IPostGenerateGradleAndroidProject.html) and modify or move any Android file or asset that the incremental build pipeline uses, it can cause issues when you build your project. If you only want to [modify Gradle project files](android-modify-gradle-project-files.html), it’s best practice to use the [Android Project Configuration Manager](android-modify-gradle-project-files-methods.html#agp) instead of `IPostGenerateGradleAndroidProject`. If you must use `IPostGenerateGradleAndroidProject` for your use case and need to work around incremental build pipeline issues, refer to [Creating clean builds](build-clean-build.html).  
**Note**: You can use Android Project Configuration Manager to modify Android Gradle project files in custom modules only.

## Additional resources

* [Build your application for Android](android-BuildProcess.html)

Unity Library Manifest

Getting started with Android

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
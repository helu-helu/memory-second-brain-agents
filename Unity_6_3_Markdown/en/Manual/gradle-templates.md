* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Building and delivering for Android](android-building-and-delivering.html)
* Gradle templates

Building and delivering for Android

Gradle template variables

# Gradle templates

Gradle templates configure how to build an Android application using [Gradle](android-gradle-overview.html)An Android build system that automates several build processes. This automation means that many common build errors are less likely to occur. [More info](android-gradle-overview.html)  
See in [Glossary](Glossary.html#Gradle). Each Gradle template represents a single Gradle project. Gradle projects can include, and depend on, other Gradle projects.

## Gradle template files

A Gradle template consists of the following files:

| File | Location | Contains |
| --- | --- | --- |
| `baseProjectTemplate.gradle` | In the exported project, `root/build.gradle` folder | Configuration information that affects all modules in the final Gradle project. It specifies which Android Gradle Plugin version to use and locations of java plugins. The locations are a combination of online repositories and java plugins inside of this project. |
| `launcherTemplate.gradle` | In the exported project, `root/launcher/build.gradle` folder | Instructions on how to build the Android application. This includes bundling, signing, and whether to split the **apk**The Android Package format output by Unity. An APK is automatically deployed to your device when you select File > Build & Run. [More info](android-BuildProcess.html) See in [Glossary](Glossary.html#APK). It depends on the unityLibrary project and outputs either an .apk file or an app bundle. |
| `mainTemplate.gradle` | In the exported project, `root/unityLibrary/build.gradle` folder | Instructions on how to build Unity as a Library. This outputs an .aar file. You can override the Unity template with a custom template in the Unity Editor. Refer to the Providing a custom Gradle build template section on this page for more details. |
| `libTemplate.gradle` | Varies | If an [Android Library](AndroidAARPlugins.html) **plug-in**A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html) See in [Glossary](Glossary.html#plug-in) doesn’t include a `build.gradle` file, Unity uses the `libTemplate.gradle` file as a template to generate one. After Unity generates the `build.gradle` file, or if one already exists in the plug-in’s directory, Unity copies the plug-in into the Gradle project. |
| `settingsTemplate.gradle` | In the exported project, `root/settings.gradle` file | Specifies the names of modules that the Gradle build system should include when it builds the project. You can override the Unity template with a custom template in the Unity Editor. Refer to the Providing a custom Gradle build template section on this page for more details. |
| `gradleTemplate.properties` | In the exported project, `root/gradle.properties` file | Configures the Gradle build system and specifies properties such as the size of the [Java virtual machine (JVM) heap](https://www.ibm.com/docs/en/integration-bus/10.0?topic=development-jvm-heap-sizing) |

To have more control over the Gradle project files that Unity produces, you can override Unity’s default Gradle template files. For information on how to do this, refer to [Modify Gradle project files with Gradle template files](android-modify-gradle-project-files-templates.html).

## Modifying the exported Gradle project using C#

To modify the Gradle project after Unity assembles it, create a class that inherits from [IPostGenerateGradleAndroidProject](../ScriptReference/Android.IPostGenerateGradleAndroidProject.html) and override the [OnPostGenerateGradleAndroidProject](../ScriptReference/Android.IPostGenerateGradleAndroidProject.OnPostGenerateGradleAndroidProject.html) function. This function receives the path to the unityLibrary module as a parameter and you can use it to reach the application’s manifest and resources through C# scripting.

Building and delivering for Android

Gradle template variables

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
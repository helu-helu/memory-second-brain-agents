* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Introducing Android](android-introducing.html)
* [Gradle for Android](android-gradle-overview.html)
* Unity specific properties in gradle.properties file

Gradle project structure

Troubleshooting Gradle build issues for Android

# Unity specific properties in gradle.properties file

The `gradle.properties` file includes the following properties that are specific to Unity’s Android build process:

| **Property** | **Description** |
| --- | --- |
| **unityStreamingAssets** | Indicates the names of assets inside the [Streaming Assets](StreamingAssets.html) directory. Unity specifies that these assets are included in the final application and **Gradle**An Android build system that automates several build processes. This automation means that many common build errors are less likely to occur. [More info](android-gradle-overview.html) See in [Glossary](Glossary.html#Gradle) doesn’t compress them. |
| **unityTemplateVersion** | The version of the Gradle template file that Unity uses. If your project’s Gradle template version differs from the specified one, Unity throws an error to inform you to update your Gradle files and build your project in an empty folder. |
| **unity.projectPath** | The path to your Unity project. |
| **unity.debugSymbolLevel** | The debug symbol level used by Unity. |
| **unity.buildToolsVersion** | The build tools version used by Unity. |
| **unity.minSdkVersion** | The minimum API level used by Unity. |
| **unity.targetSdkVersion** | The target API level used by Unity. |
| **unity.compileSdkVersion** | The compile SDK version of the Android SDK that’s used to compile your application during the build process. |
| **unity.applicationId** | The application ID used by Unity. For example, `com.MyCompany.MyApp`. |
| **unity.abiFilters** | The Application Binary Interface (ABI) configurations included in the application used by Unity and are separated by commas. For example, armeabi-v7a, arm64-v8a. |
| **unity.versionCode** | The internal version number for the application. It’s used to indicate how recent the application version is, where higher number denotes a more recent version. |
| **unity.versionName** | The application version number expressed as a string. This version number is visible to the users. |
| **unity.namespace** | The application namespace used by Unity. For example, `com.MyCompany.MyApp`. |
| **unity.agpVersion** | The Android Gradle Plugin (AGP) version used by Unity. |
| **unity.androidSdkPath** | The Android Software Development Kit (SDK) installation folder path set in the **Android** section of **External Tools**, menu: **Edit** > **Preferences** > **External Tools** (macOS: **Unity** > **Settings** > **External Tools**). |
| **unity.androidNdkPath** | The Android Native Development Kit (NDK) installation folder path set in the **Android** section of **External Tools**, menu: **Edit** > **Preferences** > **External Tools** (macOS: **Unity** > **Settings** > **External Tools**). |
| **unity.androidNdkVersion** | The Android Native Development Kit (NDK) version set in the **Android** section of **External Tools**, menu: **Edit** > **Preferences** > **External Tools** (macOS: **Unity** > **Settings** > **External Tools**). |
| **unity.jdkPath** | The Java Development Kit (JDK) installation folder path set in the **Android** section of **External Tools**, menu: **Edit** > **Preferences** > **External Tools** (macOS: **Unity** > **Settings** > **External Tools**). |
| **unity.javaCompatabilityVersion** | The Java compatibility version used by Unity. |

## Additional resources

* [Gradle project files](android-gradle-project-files.html)
* [Gradle project structure](android-gradle-project-structure.html)

Gradle project structure

Troubleshooting Gradle build issues for Android

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Getting started with Android](android-getting-started.html)
* [Android environment setup](android-sdksetup.html)
* Android External Tools reference

Customize dependencies

Set up the Android SDK Target API

# Android External Tools reference

Learn how to configure Android development tools using **External Tools** window.

The **Android** section in **External Tools** panel allows you to configure Android development tools used to set up Unity projects. To access this section, go to **Edit** > **Preferences** (macOS: **Unity** > **Settings**) and then navigate to **External Tools** > **Android**.

## Android External Tools window

![External Tools for Android](../uploads/Main/PreferenceesExternalToolsAndroid.png)


External Tools for Android

Use the following settings to configure Android development tools for your project.

| **Setting** | **Description** |
| --- | --- |
| **JDK installed with Unity(recommended)** | Indicates whether to use the recommended version of Java Development Kit (JDK) installed with Unity or the custom JDK installation. If enabled, the setting displays the path to the JDK installation folder. To use the custom JDK version, disable this option and select **Browse** to set the custom JDK installation folder path. |
| **Android SDK tools installed with Unity(recommended)** | Indicates whether to use the recommended versions of Android SDK tools installed with Unity or the custom SDK tools installation. If enabled, the setting displays the path to the SDK tools installation folder. To use the custom SDK tools version, disable this option and select **Browse** to set the custom SDK tools installation folder path. |
| **Android NDK installed with Unity(recommended)** | Indicates whether to use the recommended version of Android Native Development Kit (NDK) installed with Unity or the custom NDK installation. If enabled, the setting displays the path to the NDK installation folder. To use the custom NDK version, disable this option and select **Browse** to set the custom NDK installation folder path. |
| ****Gradle**An Android build system that automates several build processes. This automation means that many common build errors are less likely to occur. [More info](android-gradle-overview.html) See in [Glossary](Glossary.html#Gradle) installed with Unity(recommended)** | Indicates whether to use the recommended version of Android Gradle installed with Unity or the custom Gradle installation. If enabled, the setting displays the path to the Gradle installation folder. To use the custom Gradle version, disable this option and select **Browse** to set the custom Gradle installation folder path. |
| **Stop Gradle daemons on exit** | Indicates whether to stop Gradle daemons when the Unity Editor exits. This option is enabled by default and it might help to free up resources on your computer. |
| **User Home** | Specifies the path to the Gradle User Home directory. If no path is specified, the Gradle User Home directory is located in the `.gradle` folder of your system’s home directory. For example, `/home/USERNAME/.gradle` on macOS or `C:\Users\USERNAME\.gradle` on Windows.   If your username contains non-ASCII characters that Gradle might not process correctly, specify a custom location for your Gradle User Home directory instead of changing your username. |
| **Kill **ADB**An Android Debug Bridge (ADB). You can use an ADB to deploy an Android package (APK) manually after building. [More info](https://developer.android.com/studio/command-line/adb.html) See in [Glossary](Glossary.html#ADB) server on exit** | Indicates whether to terminate Android Debug Bridge (adb) server when the Unity Editor exits. This option is enabled by default and it might help to free up resources on your computer. |
| **Kill external ADB instances** | Indicates whether to terminate external Android Debug Bridge (ADB) instances. These are separate instances that don’t belong to the Android SDK set from **Android SDK tools installed with Unity(recommended)** . Multiple ADB instances can conflict with each other and might cause issues when using the Android SDK. For example, when updating the API or during application launches.     **Note**: This option is enabled by default to prevent collision between different ADB instances. |
| **Maximum JVM heap size, Mbyte** | Specifies the maximum Java heap size that can be allocated during the Android build process. The value is specified in megabytes and the default value is 4096. You can increase or decrease this value based on your project requirement. Increase this value if you experience heap space errors. |
| **Keystores Dedicated Location** | Specifies the folder path to your **Android keystores**An Android system that lets you store cryptographic key entries for enhanced device security. [More info](class-PlayerSettingsAndroid.html#projectkeystore) See in [Glossary](Glossary.html#AndroidKeystore). Unity uses this path when signing your Android application during the build process. To set a new path for your application, select **Browse** and navigate to the folder where you want to store your Android keystores. For more information, refer to [Choose the keystore location](android-keystore-create.html#choose-the-keystore-location). |

## Additional resources

* [Preferences](Preferences.html)
* [Customize dependencies](android-customize-dependencies.html)
* [Gradle Daemons](https://docs.gradle.org/current/userguide/gradle_daemon.html)

Customize dependencies

Set up the Android SDK Target API

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
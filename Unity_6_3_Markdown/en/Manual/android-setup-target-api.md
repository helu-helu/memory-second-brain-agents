* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Getting started with Android](android-getting-started.html)
* [Android environment setup](android-sdksetup.html)
* Set up the Android SDK Target API

Android External Tools reference

Android Player settings

# Set up the Android SDK Target API

Configure the Android SDK Target API level for your application.

The Unity Hub installs the latest version of the Android SDK Target API that Google Play requires. If you need to use a more recent version, you can change it in the [Android Player Settings](class-PlayerSettingsAndroid.html).

## Configure Target API version

To configure the Android SDK Target API version in **Android **Player settings**Settings that let you set various player-specific options for the final game built by Unity. [More info](class-PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings)**, follow these steps:

1. Open **Android Player Settings** (menu: **Edit** > **Project Settings** > **Player**).
2. In the **Other Settings** section, change the **Target API Level**.

![Android Player Settings with the Target API Level dropdown selected.](../uploads/Main/android-sdk-target-api.png)


Android Player Settings with the Target API Level dropdown selected.

### Newer Target API version

If you select a Target API version newer than the latest installed version, the Unity Android SDK Updater can automatically download and install the new version. Unity displays a prompt and you can choose to either:

* Automatically download and install the new version of the Android SDK.
* Continue to use the highest installed version of the Android SDK.

### Older Target API version

If you select a target API version that’s not installed and is older than the latest installed version, the Unity Android SDK Updater can’t perform the update and Unity displays an error message.

In this case, to update the Android SDK Target API, you must use the Android [sdkmanager](https://developer.android.com/studio/command-line/sdkmanager) from either [Android Studio](https://developer.android.com/studio) or the [command-line tool](https://developer.android.com/studio/command-line/sdkmanager). Regardless of the method you choose, make sure to select the correct Android SDK folder for Unity in the **Android External Tools** section.

**Important**: On Windows, if you installed the Unity Editor in the default folder (`/Program Files/`), you must run the `sdkmanager` with elevated privileges (**Run as Administrator**) to perform the update.

## Additional resources

* [Install Android dependencies](android-install-dependencies.html)
* [Android External Tools reference](android-external-tools-reference.html)

Android External Tools reference

Android Player settings

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
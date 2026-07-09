* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Developing for Android](android-developing.html)
* [Android application entry points](android-application-entries.html)
* The GameActivity application entry point

Specify Android Player command-line arguments

GameActivity requirements and compatibility

# The GameActivity application entry point

The [GameActivity](https://developer.android.com/games/agdk/game-activity) application entry point is an extension of the [Activity](android-application-entries-activity.html) application entry point and is the default application entry point for new Unity projects. It provides more control over the interaction between Android and your application than the Activity application entry point. To provide this control, the GameActivity library does the following:

* It doesn’t directly map to a specific Unity version which means you can update the GameActivity library separately to Unity.
* It uses a customizable [glue library](https://developer.android.com/reference/games/game-activity/group/android-native-app-glue) as a bridge between itself and Unity. This means you can modify the bridge code to make changes and extend functionality.

| **Topic** | **Description** |
| --- | --- |
| [GameActivity requirements and compatibility](android-application-entries-game-activity-requirements.html) | Understand the system requirements and feature compatibility of the GameActivity application entry point. |
| [Modify GameActivity bridge code](android-application-entries-game-activity-modify-bridge.html) | Make changes to the code that connects the Unity runtime to the GameActivity library. |
| [Update the GameActivity library](android-application-entries-game-activity-update-library.html) | Change which version of the GameActivity library your application uses. |

## Additional resources

* [Set the application entry point for your Android application](android-application-entries-set.html)

Specify Android Player command-line arguments

GameActivity requirements and compatibility

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
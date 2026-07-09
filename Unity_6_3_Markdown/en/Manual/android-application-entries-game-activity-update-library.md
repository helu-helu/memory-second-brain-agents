* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Developing for Android](android-developing.html)
* [Android application entry points](android-application-entries.html)
* [The GameActivity application entry point](android-application-entries-game-activity.html)
* Update the GameActivity library

Modify GameActivity bridge code

Set the application entry point for your Android application

# Update the GameActivity library

The GameActivity application entry point is implemented as a library separate from the Unity Editor which means that you can update the library independently. This is useful if Google provides bug fixes that your project requires because you can acquire the fixes via a GameActivity library version update.

**Note**: By default, Unity uses a specific GameActivity library version for each Unity version. For the recommended GameActivity library version per Unity version, refer to [GameActivity requirements and compatibility](android-application-entries-game-activity-requirements.html). Unity doesn’t test all combinations of Unity version and GameActivity library version. Changing the GameActivity library version, particularly across major versions, can cause incompatibilities with the Unity runtime. Change the version only if you have a critical requirement that the recommended version doesn’t meet and test your application thoroughly after any change.

To update the GameActivity library version, change the value of the `androidx.games:games-activity` dependency in `build.gradle`. For information on the possible methods to do this, refer to [Modify Gradle project files](android-modify-gradle-project-files.html).

**Note**: Make sure that the other AndroidX dependencies support the GameActivity version that you want to use. If they don’t, you must update them too. For more information, refer to [Declaring dependencies](https://developer.android.com/jetpack/androidx/releases/games#declaring-dependencies).

## Additional resources

* [Modify GameActivity bridge code](android-application-entries-game-activity-modify-bridge.html)

Modify GameActivity bridge code

Set the application entry point for your Android application

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
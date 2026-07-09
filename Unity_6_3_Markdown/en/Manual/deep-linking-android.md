* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Developing for Android](android-developing.html)
* Deep linking on Android

Set the application entry point for your Android application

Device features and permissions

# Deep linking on Android

Deep links are hyperlinks outside of your application that take a user to a specific location within the application rather than a website. When a user clicks a deep link, the application opens from the designated location, such as a specific **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) in a Unity application. For more information about deep links and how to use them, refer to [Deep linking](deep-linking.html).

## Enable deep linking for Android applications

Use an [intent filter](https://developer.android.com/guide/components/intents-filters) to enable deep linking for Android applications. An intent filter overrides the standard [Android App Manifest](android-manifest.html) to include a specific intent filter section for [Activity](https://developer.android.com/reference/android/app/Activity).

To set up an intent filter, use the following steps:

1. Navigate to **Edit** > **Project Settings** > **Player**.
2. In the **Android settings** tab, expand the **Publishing Settings** section.
3. In the **Build** section, enable **Custom Main Manifest**. This creates a new file called `AndroidManifest.xml` in `Assets/Plugins/Android`.
4. In the Project window, go to **Assets** > **Plugins** > **Android** and open the `AndroidManifest.xml` file.
5. Add the following code sample inside the Unity`<activity>` element, named `com.unity3d.player.UnityPlayerGameActivity` or `com.unity3d.player.UnityPlayerActivity`, and save the file.

```
<intent-filter>
  <action android:name="android.intent.action.VIEW" />
  <category android:name="android.intent.category.DEFAULT" />
  <category android:name="android.intent.category.BROWSABLE" />
  <data android:scheme="unitydl" android:host="mylink" />
</intent-filter>
```

The built application now opens when the device processes any link that starts with `unitydl://`.

## Use deep linking on Android

After you enable deep links for Android, the way that you use them is platform-agnostic. For information on how to handle deep links when your application opens, refer to [Using deep links](deep-linking.html#using-deep-links).

Set the application entry point for your Android application

Device features and permissions

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
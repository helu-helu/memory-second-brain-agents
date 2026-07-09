* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Building and delivering for Android](android-building-and-delivering.html)
* [Deliver Android applications on Google Play](android-distribution.html)
* Google Play delivery considerations

Google Play delivery requirements

Dedicated Server

# Google Play delivery considerations

Consider the following key points and best practices before you publish an application to Google Play.

## Best practice checklist

To help launch an Android application successfully, Android provides best practices to follow. You can find these best practices in Android’s [Launch checklist](https://developer.android.com/distribute/best-practices/launch/launch-checklist) documentation.

### Public symbols

If your application crashes on a device, Google can use an [Android symbols](android-symbols.html) package to make a native stack trace human-readable on the [Android Vitals](https://developer.android.com/topic/performance/vitals) dashboard. It’s best practice to generate a [Public symbols](android-symbols.html#public-symbols) package for your application and upload it to Google Play. For information on how to do this, refer to [Generating a symbols package](android-symbols.html#generating-a-symbols-package).

### Deobfuscation file

Similar to symbol files, Unity can produce a deobfuscation file if you apply minification to your application build. For more information on applying minification, refer to [Android Player Settings](class-PlayerSettingsAndroid.html#minify). A deobfuscation file is automatically generated as a mapping file in the same location as your application build.

If you apply minification, it’s best practice to upload the deobfuscation file when publishing your application on Google Play. A deobfuscation file deciphers the method names in the stack trace, allowing you to identify and resolve the exact cause of the application crashes. For more information, refer to Google’s documentation on [Deobfuscate or symbolicate crash stack traces](https://support.google.com/googleplay/android-developer/answer/9848633)

## Additional resources

* [Google Play delivery requirements](android-distribution-google-play.html)

Google Play delivery requirements

Dedicated Server

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
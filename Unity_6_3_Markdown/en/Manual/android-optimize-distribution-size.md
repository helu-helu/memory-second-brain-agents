* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Building and delivering for Android](android-building-and-delivering.html)
* Optimize distribution size

Export an Android project

Deliver Android applications on Google Play

# Optimize distribution size

Some digital distribution services have a limit on the initial install size of your application. Unity includes the following methods to help you to optimize the install size:

* [Split APKs by target architecture](#splitting-apks).
* [Split the application binary](#splitting-the-application-binary).
* [Compression](#compression)A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](texture-choose-format-by-platform.html), [Animation Compression](class-AnimationClip.html#AssetProperties), [Audio Compression](class-AudioClip.html), [Build Compression](ReducingFilesize.html).  
  See in [Glossary](Glossary.html#compression)
* [Minification](#minification).

## Split APKs by target architecture

If your output application uses **APK**The Android Package format output by Unity. An APK is automatically deployed to your device when you select File > Build & Run. [More info](android-BuildProcess.html)  
See in [Glossary](Glossary.html#APK) format, the **Split APKs by target architecture** [Player Setting](class-PlayerSettingsAndroid.html) optimizes the application download and installation size. Instead of producing one APK that contains binaries for every target CPU architecture selected in the **Target Architectures** Player Setting, Unity creates a separate APK for each CPU architecture. You can upload this set of APKs to [digital distribution services](android-distribution.html) which serve the APK with the correct target CPU architecture to each device that downloads your application.

This is primarily a Google Play feature and may not work for other digital distribution services. For more information, see [Multiple APK support](https://developer.android.com/google/play/publishing/multiple-apks.html).

**Note**: Google Play requires new applications to be AABs and not APKs. When you upload an AAB, Google Play automatically generates and serves optimized APKs for each device configuration.

## Split the application binary

You can split your output application to make the initial install size smaller. The device can install a lighter version of your application and then download assets separately. If your output application uses APK format, Unity can split the application into a main APK and an expansion file (OBB). For more information see [APK expansion files](android-OBBsupport.html). If your output application uses AAB format, Unity can split the application into a [base module](https://developer.android.com/guide/app-bundle/configure-base) and asset packs. For more information, see [Play Asset Delivery](play-asset-delivery.html).

To split the application binary:

1. Select **Edit** > **Project Settings**.
2. In the **Project settings**A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](comp-ManagerGroup.html)  
   See in [Glossary](Glossary.html#ProjectSettings) window, select the **Player** tab, then open [Android Player Settings](class-PlayerSettingsAndroid.html).
3. In the **Publishing Settings** section, enable **Split Application Binary**.

## Compression

You can change the method Unity uses to compress resource files for the application. This can reduce the size of the application but can increase loading times if the method means data takes longer to decompress.

For more information, see [Compression Method](android-build-settings.html#compression-method).

## Minification

You can use [ProGuard](https://www.guardsquare.com/proguard) minification to decrease the size of the application and improve performance.

To enable ProGuard minification:

1. Select **Edit** > **Project Settings**.
2. In the Project settings window, select the **Player** tab, then open [Android Player Settings](class-PlayerSettingsAndroid.html).
3. In the **Publishing Settings** section, under **Minify** enable either **Release**, **Debug**, or both depending on the type of build you want to minify.

**Note**: ProGuard might strip out important code that your application relies on, so check any builds that you minify.

For more control over the minification process, generate a custom `proguard.txt` file and configure it to specify what not to strip. To generate the file, select **Custom Proguard File** in the **Publishing Settings** section. This generates the `proguard.txt` file in your project’s `Assets/Plugins/Android` folder. For information on how to configure ProGuard minification, see the [ProGuard documentation](https://www.guardsquare.com/manual/configuration/usage).

Export an Android project

Deliver Android applications on Google Play

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
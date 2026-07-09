* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Building and delivering for Android](android-building-and-delivering.html)
* [Deliver Android applications on Google Play](android-distribution.html)
* Google Play delivery requirements

Deliver Android applications on Google Play

Google Play delivery considerations

# Google Play delivery requirements

Google Play has specific requirements that an application must meet before you publish it. Familiarize yourself with these requirements and understand how to fulfill them before you publish an application to Google Play.

For information on how to publish your application on Google Play, refer to [Google Play](https://developer.android.com/distribute/google-play).

### Android App Bundle

Google Play requires new applications to be an [Android App Bundle](https://developer.android.com/guide/app-bundle) (AAB) instead of an **APK**The Android Package format output by Unity. An APK is automatically deployed to your device when you select File > Build & Run. [More info](android-BuildProcess.html)  
See in [Glossary](Glossary.html#APK). For information on why, refer to [The future of Android App Bundles is here](https://android-developers.googleblog.com/2021/06/the-future-of-android-app-bundles-is.html) (Android developer blog).

To configure an application to be an AAB:

1. Open the **Build Profiles** window (menu: **File** > **Build Profiles**).
2. From the list of platforms in the **Platforms** panel, select **Android**.
3. Select [Player Settings](class-PlayerSettingsAndroid.html)Settings that let you set various player-specific options for the final game built by Unity. [More info](class-PlayerSettings.html)  
   See in [Glossary](Glossary.html#PlayerSettings) for Android.
4. In the **Publishing Settings** section, enable **Split Application Binary**.
5. On the **Build Profiles** window, under **Platform Settings** section, enable **Build App Bundle (Google Play)**. If you want to [export the project](android-export-process.html) and build it in Android Studio, enable **Export Project** then enable **Export for App Bundle**.

   **Notes**:

   * **Build App Bundle (Google Play)** setting is visible only if you disable **Export Project** setting.
   * Make sure ****Development Build**A development build includes debug symbols and enables the Profiler. [More info](building-introduction.html)  
     See in [Glossary](Glossary.html#developmentbuild)** setting is disabled as otherwise the application upload might fail.

When you [Build the application](android-BuildProcess.html#building), Unity builds the application as an AAB.

### Application size

Google Play limits the install size of applications. The following table describes the size limitations Google Play has for each application type:

| **Application type** | **Size limitation** |
| --- | --- |
| **APK** | If you [split the application binary](android-optimize-distribution-size.html#splitting-the-application-binary) or use a custom [expansion file](android-OBBsupport.html), the APK must be smaller than 100 MB and the expansion file must be smaller than 2 GB. Otherwise, the APK must be smaller than 100 MB. |
| **AAB** | If you split the application binary or use custom [asset packs](play-asset-delivery.html), the base module inside the AAB must be smaller than 200 MB and the asset packs must fit the file sizes described in the [Google Play maximum size limits](https://support.google.com/googleplay/android-developer/answer/9859372#size_limits) documentation. Otherwise, the AAB must be smaller than 200 MB. |

For information on how to optimize the install size of your application, refer to [Optimize distribution size](android-optimize-distribution-size.html).

### Symbols file size

Google Play limits the size of the symbols package or the embedded symbols within an Android App Bundle. The symbols files might be rejected if their file size exceeds this limit. Unity displays a warning if your symbols package exceeds the size limit specified in the **Symbols size threshold** in the [Android Player settings](class-PlayerSettingsAndroid.html) > **Other Settings** > **Configuration**.

### Texture **compression**A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](texture-choose-format-by-platform.html), [Animation Compression](class-AnimationClip.html#AssetProperties), [Audio Compression](class-AudioClip.html), [Build Compression](ReducingFilesize.html). See in [Glossary](Glossary.html#compression) targeting

[Texture compression targeting](https://developer.android.com/guide/playcore/asset-delivery/texture-compression) is a feature of Android App Bundles that helps Google Play to generate and serve optimized APKs for different devices. If you enable it, Unity includes texture assets formatted with different compression formats in any Android App Bundles that it builds. When a device installs the application from Google Play, the APKs that the device receives contain texture assets that use the optimal **texture compression**3D Graphics hardware requires Textures to be compressed in specialized formats which are optimized for fast Texture sampling. [More info](texture-choose-format-by-platform.html)  
See in [Glossary](Glossary.html#texturecompression) format for the device.

Texture compression targeting also automatically enables the [split application binary](android-optimize-distribution-size.html#splitting-the-application-binary) feature and generates an [install-time asset pack](android-asset-packs-in-unity.html#generated-asset-packs) called **UnityTextureCompressionsAssetPack**. This asset pack contains common resources and assets required by the first **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). When you disable texture compression targeting, Unity packs these assets into the [base module](android-asset-packs-in-unity.html). This means that enabling texture compression targeting reduces the size of the base module. This can be important because the base module has a size limit of 200 MB. For more information on how Unity configures asset packs, refer to [Asset packs in Unity](android-asset-packs-in-unity.html).

To enable texture compression targeting:

1. Enable [Android App Bundles](#android-app-bundle).
2. Open the [Build Profiles](BuildSettings.html)A set of customizable configuration settings to use when creating a build for your target platform. [More info](build-profiles.html)  
   See in [Glossary](Glossary.html#buildprofile) window.
3. Select [Player Settings](class-PlayerSettingsAndroid.html) for the Android platform.
4. In the **Other Settings** > **Rendering** section, find **Texture Compression Formats** and add all required texture compression formats to it. The first texture compression format in this list is the [default format](https://developer.android.com/guide/playcore/asset-delivery/texture-compression#select-default-format).  
   **Note**: You can also use the `PlayerSettings.Android.textureCompressionFormats` API to assign the required texture compression formats.
5. On the **Build Profiles** window, select **Asset Import Overrides** and set **Texture Compression** to a value other than **Force Uncompressed**.

**Note**: When Texture compression targeting is enabled, Unity disables and ignores the **Texture Compression** [Android build setting](android-build-settings.html) which means you can’t use this setting to override the texture compression format for a build.

If you don’t enable Android App Bundles and [export](android-export-process.html) or build your application as an APK, Unity only uses the first texture compression format in the **Texture Compression Formats** list.

If you want some texture assets to use specific texture compression formats, you can override their texture compression format. The value you set for an individual **texture overrides**Platform-specific settings that allow you to set the resolution, file size with associated memory size requirements, pixel dimensions, and quality of your textures for each target platform. [More info](texture-choose-format-by-platform.html)  
See in [Glossary](Glossary.html#textureoverrides) the default texture compression format and the optimal format that Google Play would select for specific target devices. For information on how to change the **texture format**A file format for handling textures during real-time rendering by 3D graphics hardware, such as a graphics card or mobile device. [More info](texture-choose-format-by-platform.html)  
See in [Glossary](Glossary.html#textureformat) of individual textures, refer to the documentation on [Texture Import Settings window reference](class-TextureImporter.html).

### 64-bit Architecture

Google Play requires applications to support 64-bit architecture. For more information, refer to [Support 64-bit architectures](https://developer.android.com/distribute/best-practices/develop/64-bit).

To make your application support 64-bit architecture, follow these steps:

1. Open the **Build Profiles** window (menu: **File** > **Build Profiles**).
2. From the list of platforms in the **Platforms** panel, select **Android** or [create a build profile](create-build-profile.html) for the **Android** platform.
3. Select [Player Settings](class-PlayerSettingsAndroid.html).
4. In the **Other Settings** > **Configuration** section, enable **ARM64**.   
   **Note**: You can enable this setting only if you set your project’s [Scripting back end](scripting-backends.html) to [IL2CPP](./scripting-backends-il2cpp.html)A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](./scripting-backends-il2cpp.html)  
   See in [Glossary](Glossary.html#IL2CPP).

### Target API

Google Play requires applications to support a minimum target API. For information on what the current minimum target API is, refer to [Meet Google Play’s target API level requirement](https://developer.android.com/distribute/best-practices/develop/target-sdk).

To change your application’s target API:

1. Open **Build Profiles** window (menu: **File** > **Build Profiles**).
2. From the list of platforms in the **Platforms** pane, select **Android**.
3. Select [Player Settings](class-PlayerSettingsAndroid.html).
4. In the **Other Settings** > **Identification** section, set **Target API Level** to at least the target API level that Google Play requires.

### Report application dependencies

Google Play can check the Package Manager and **Asset Store**A growing library of free and commercial assets created by Unity and members of the community. Offers a wide variety of assets, from textures, models and animations to whole project examples, tutorials and Editor extensions. [More info](AssetStore.html)  
See in [Glossary](Glossary.html#AssetStore) packages that your application uses for known certification failures. It does this automatically after you upload your application to the Play Store and before the main certification process begins. This helps to identify issues with your application’s dependencies quickly without running the full certification process. If Google Play finds issues, it reports them to you via the Play Store Console along with details about the issues and how you can fix them before you submit the application again.

To report dependencies, follow these steps:

1. Open **Build Profiles** window (menu: **File** > **Build Profiles**).
2. From the list of platforms in the **Platforms** pane, select **Android**.
3. Select [Player Settings](class-PlayerSettingsAndroid.html).
4. In the **Publishing Settings** section, enable **Report Dependencies in App Bundle** to enable collection and reporting of dependencies to Google Play.

### App signature

Google Play requires applications to be signed. For information on how to sign your application, refer to [Android Keystore Manager](android-keystore-manager.html).

## Additional resources

* [Google Play delivery considerations](google-play-delivery-considerations.html)

Deliver Android applications on Google Play

Google Play delivery considerations

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
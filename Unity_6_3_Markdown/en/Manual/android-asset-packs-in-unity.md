* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Developing for Android](android-developing.html)
* [Android application size restrictions](android-application-size-restrictions.html)
* [Play Asset Delivery](play-asset-delivery.html)
* Asset packs in Unity

Play Asset Delivery

Set up Play Asset Delivery

# Asset packs in Unity

This page describes how asset packs work in the context of a Unity Android application that uses [Play Asset Delivery](play-asset-delivery.html).

You can configure Unity to generate an [Android App Bundle](https://developer.android.com/guide/app-bundle) (AAB) that includes your application split into a [base module](https://developer.android.com/guide/app-bundle/configure-base) and asset packs:

* **Base module**: Contains the executables (Java and native), **plug-ins**A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)  
  See in [Glossary](Glossary.html#plug-in), and assets in the first **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
  See in [Glossary](Glossary.html#Scene). The first scene is the scene that has a [build index](../ScriptReference/SceneManagement.Scene-buildIndex.html) of 0.
* **Asset packs**: Contains everything else, including the remaining scenes, resources, and [Streaming Assets](StreamingAssets.html). For more information about the asset packs that Unity generates at build time, refer to [Generated asset packs](#generated-asset-packs).

Alongside the asset packs that Unity generates automatically, you can also create your own custom asset packs. This helps you to control which assets an asset pack contains. Unity adds your custom asset packs to the final AAB. For more information, refer to [Custom asset packs](#custom-asset-packs).

## Generated asset packs

Asset packs have [download size limits](https://support.google.com/googleplay/android-developer/answer/9859372#size_limits). To account for this, Unity changes how it generates asset packs depending on the size of your additional assets:

* If the additional assets take less than 1.5GB of storage, Unity packs everything into a single asset pack that uses the `install-time` [delivery mode](https://developer.android.com/guide/playcore/asset-delivery#delivery-modes) and is called **UnityDataAssetPack**. If you don’t create any [custom asset packs](#custom-asset-packs), this means that the device downloads the asset pack as part of the application installation and, when the user first launches the application, all assets are available.
* If the additional assets take more than 1.5GB of storage, Unity adds Streaming Assets into one asset pack called **UnityStreamingAssetPack** and adds all other assets into the **UnityDataAssetPack** asset pack. These both asset packs use the `install-time` [delivery mode](https://developer.android.com/guide/playcore/asset-delivery#delivery-modes).
* If you enable [texture compression targeting](android-distribution-google-play.html#texture-compression-targeting), Unity generates an additional `install-time` asset pack called **UnityTextureCompressionsAssetPack** which includes common assets and the assets required by the first scene. Texture **compression**A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](texture-choose-format-by-platform.html), [Animation Compression](class-AnimationClip.html#AssetProperties), [Audio Compression](class-AudioClip.html), [Build Compression](ReducingFilesize.html).  
  See in [Glossary](Glossary.html#compression) targeting doesn’t affect Streaming Assets so if you use Streaming Assets and enable **texture compression**3D Graphics hardware requires Textures to be compressed in specialized formats which are optimized for fast Texture sampling. [More info](texture-choose-format-by-platform.html)  
  See in [Glossary](Glossary.html#texturecompression) targeting, Unity always packs Streaming Assets into a separate asset pack called **UnityStreamingAssetPack**. Unity does this regardless of whether your additional assets are over 1.5GB or not.

For asset packs that Unity automatically generates, Unity doesn’t support changing the [delivery mode](https://developer.android.com/guide/playcore/asset-delivery#delivery-modes). If you want to change the delivery mode of an asset pack, create custom asset packs with your assets.

**Important**: If either of these asset packs is larger than 1.5GB, Unity displays a warning but doesn’t fail the build. During the build process, Unity checks the sizes of Unity-generated asset packs individually, so ensure that the total size of such packs and the base module is less than the limit set by Google Play Store (4GB). Also, Unity doesn’t perform size verification for custom asset packs. This means that, if Unity-generated asset packs fit within the Google Play Store limits but their combination with custom asset packs is too large for the Google Play Store, Unity doesn’t display a warning or error. However if you enable **Warn about App Bundle size** in [Android Player settings](class-PlayerSettingsAndroid.html), it’s possible to perform the full size validation for the generated release App Bundle according to [Google Play maximum size limits](https://support.google.com/googleplay/android-developer/answer/9859372#size_limits).

## Custom asset packs

If you want to control which non-code resources are in a particular asset pack, you can create a custom asset pack. Unlike Unity-generated asset packs, you can set the delivery mode for custom asset packs. If you create a custom asset pack, be aware that the Google Play Store has size and quantity limits for asset packs. For information on the limits, refer to [Google Play maximum size limits](https://support.google.com/googleplay/android-developer/answer/9859372#size_limits).

To use custom asset packs with [Addressables](https://docs.unity3d.com/Packages/com.unity.addressables@latest/index.html), you can use [Addressables for Android](https://docs.unity3d.com/Packages/com.unity.addressables.android@latest/index.html) package.

## Additional resources

* [Set up Play Asset delivery](android-asset-packs-set-up.html)
* [Create a custom asset pack](android-asset-packs-create-custom.html)

Play Asset Delivery

Set up Play Asset Delivery

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
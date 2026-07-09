* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Developing for Android](android-developing.html)
* [Android application size restrictions](android-application-size-restrictions.html)
* [Play Asset Delivery](play-asset-delivery.html)
* Create a custom asset pack

Set up Play Asset Delivery

Manage asset packs at runtime

# Create a custom asset pack

To create a custom asset pack, create a directory with a name that ends with `.androidpack`. You can place this directory anywhere in your project’s Assets directory, or any subdirectory.

**Important**: Unity doesn’t import assets from `.androidpack` directories, so you can’t use assets in custom asset packs directly in Unity **scenes**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). To use assets from custom asset packs, you must manually access and load them dynamically at runtime. For information on how to do this, refer to [Manage asset packs at runtime](android-asset-packs-manage.html).

The following steps explain how to create a custom asset pack named **MyAssets1**:

1. Go to the directory you want to create the asset pack in. This can be directly in **Assets** or a subdirectory like **Assets/CustomAssetPacks**.
2. Create a new directory and call it `MyAssets1.androidpack`. This is the root folder of your new asset pack. The contents of the asset pack must match the structure that Android Studio expects or builds of your project will fail. For information on the expected structure, refer to [Integrate asset delivery](https://developer.android.com/guide/playcore/asset-delivery/integrate-java). The only exception is that you don’t need to add a `build.gradle` file.  
   **Note**: Asset pack names must begin with a letter and consist of English alphanumeric characters or an underscore. If you’re creating more than one custom asset pack, make sure you choose a unique name for each asset pack. Asset pack names that are similar, such as `Assets1.androidpack` and `MyAssets1.androidpack`, cause Android App Bundle (AAB) build failure.
3. To add assets to the asset pack, place them at the following folder path within the asset pack: `src/main/assets`.
4. By default, the delivery mode is `on-demand`, which means that if you don’t change the delivery mode, you need to manually download the asset pack at runtime. For information on how to do this, refer to [Manage asset packs at runtime](android-asset-packs-manage.html).
5. To use a different delivery mode, create a file called `build.gradle` inside the custom asset pack directory. Paste the following into the file:

```
apply plugin: 'com.android.asset-pack'
assetPack {
    packName = "MyAssets1"
    dynamicDelivery {
        deliveryType = "fast-follow"
    }
}
```

This sets the delivery mode to `fast-follow`, which means Google Play automatically downloads the asset pack after it installs the application. For information on the format of this file, refer to [Integrate asset delivery](https://developer.android.com/guide/playcore/asset-delivery/integrate-java).

**Note**: The `packName` you specify in the `build.gradle` file must match the asset pack directory name you set without the `.androidpack` extension.

## Additional resources

* [Asset packs in Unity](android-asset-packs-in-unity.html)
* [Manage asset packs at runtime](android-asset-packs-manage.html)

Set up Play Asset Delivery

Manage asset packs at runtime

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
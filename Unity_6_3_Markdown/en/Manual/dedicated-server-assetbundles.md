* [Platform development](PlatformSpecific.html)
* [Dedicated Server](dedicated-server.html)
* Dedicated Server AssetBundles

Build your application for Dedicated Server

Desktop headless mode

# Dedicated Server AssetBundles

You can apply the Dedicated Server optimizations to AssetBundles starting in Unity Editor version **2023.1.0a21**. You can build an AssetBundle through scripting. Refer to the section on [AssetBundle](AssetBundlesIntro.html) for more information on building AssetBundles in general.

To build an AssetBundle to undergo the same Dedicated Server optimizations as discussed for the Player, specify the `subtarget` field in the `BuildAssetBundlesParameters` struct to be `StandaloneBuildSubtarget.Server` when calling the `BuildAssetBundle` method. Refer to the following example:

```
BuildAssetBundlesParameters serverAssetBundleParameters =
{
    outputPath = /*some example asset path here, not entirely relevant*/,
    options = BuildAssetBundleOptions.None,
    targetPlatform = BuildTarget.StandaloneWindows64,  //alternately, the MacOS or Linux build targets, any desktop platform
    subtarget = StandaloneBuildSubtarget.Server
};
BuildPipeline.BuildAssetBundles(serverAssetBundleParameters);
```

After you build the AssetBundle, you can load it by a Player at runtime. Refer to [Using AssetBundles Natively](AssetBundles-Native.html).

**Warning**: While the AssetBundle loading process checks if the AssetBundle target platform matches the target platform of the player, it doesn’t check the AssetBundle subtarget. Make sure to not load an AssetBundle that was built for a non-server standalone player. Don’t try to load an AssetBundle that targets the Dedicated Server subtarget (or vice-versa).

Build your application for Dedicated Server

Desktop headless mode

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
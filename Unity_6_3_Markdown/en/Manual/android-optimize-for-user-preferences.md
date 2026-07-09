* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Developing for Android](android-developing.html)
* [Optimization for Android](android-optimization.html)
* Optimize for user preferences

Game state hinting

Large screen and foldable device support

# Optimize for user preferences

Android’s [game mode](https://developer.android.com/games/optimize/adpf/gamemode/about-API-and-interventions) feature indicates how the user wants to optimize your application. It enables users to say whether they want your application to run normally, optimize for battery life, or optimize for best performance.

## Requirements and compatibility

Android’s game mode feature requires Android version 13.

## Use game mode in Unity

Unity provides the [AndroidGame.GameMode](../ScriptReference/Android.AndroidGame.GameMode.html) property that you can use to retrieve the current game mode for your application.

Depending on the current game mode, you should adapt your Unity application to accommodate the user’s preference. For example, if the game mode is [battery saving](../ScriptReference/Android.AndroidGameMode.Battery.html), the user expects your application to run for as long as possible. In this case, you should reduce the resource intensity of effects and calculations to reduce the impact your application has on the device’s battery life. This includes things like:

* Decrease the frame rate or resolution of the application.
* Reduce the **LOD**The *Level Of Detail* (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](LevelOfDetail.html)  
  See in [Glossary](Glossary.html#LOD) bias to make Unity display lower detail LODs closer to the **camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
  See in [Glossary](Glossary.html#Camera).
* Reduce the cull distance of particular layers.
* Reduce or possible batch network calls and/or sensor usage.

If the game mode is set to [maximize performance](../ScriptReference/Android.AndroidGameMode.Performance.html), the user expects your application to look and play as well as possible. In this case, you can enable more effects and not be as wary of battery consumption.

**Tip**: If your application is resource intensive and you want to enhance its overall performance, consider using [Adaptive Performance](adaptive-performance/adaptive-performance.html). It provides feedback about the thermal and power state of a mobile device and enables you to react appropriately to prevent thermal throttling or excessive battery consumption.

Game state hinting

Large screen and foldable device support

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
* [Assets and media](assets-and-media.html)
* [Managing assets at runtime](assets-managing-runtime.html)
* Avoiding asset duplication

Analyzing AssetBundles

Modify source assets from code

# Avoiding asset duplication

Asset duplication happens when Unity recursively follows [direct references](assets-direct-reference.html) to make sure that all required objects are included in the build. Assets and **scenes**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) aren’t shared between different builds, so the same content might be duplicated both in the Player build and a content-only build that you make using [AssetBundles](AssetBundles-Building.html) or [Addressables](https://docs.unity3d.com/Packages/com.unity.addressables@latest). For small objects this might not be a problem, but for large assets such as textures or meshes this can lead to large build sizes.

## Use AssetBundles or Addressables to minimize asset duplication

To avoid or minimize asset duplication, you can minimize the amount of content that goes into the Player build and put all the content into [AssetBundles](AssetBundlesIntro.html) or [Addressables](https://docs.unity3d.com/Packages/com.unity.addressables@latest) instead.

To create a minimal Player build, include only a single starting scene containing a MonoBehavior that bootstraps the rest of the content loading using the AssetBundle or Addressable APIs. You should also avoid putting any assets into [Resources folders](assets-resources-system.html) that are also referenced by a content-only build. You can ship the output of the AssetBundle or Addressable builds with the Player build, using the [StreamingAssets](StreamingAssets.html) folder, or hosted on a CDN.

## Duplication of assets in AssetBundles

Unity uses the [Asset Database](AssetDatabase.html) to discover all dependencies of an object when it’s built into an AssetBundle. Unity uses this dependency information to determine the set of objects to include in an AssetBundle.

AssetBundle assignment happens at the asset level. Objects in an asset explicitly assigned to an AssetBundle are included only in that specific AssetBundle. Depending on the [`BuildPipeline.BuildAssetBundles`](../ScriptReference/BuildPipeline.BuildAssetBundles.html) method used, an asset is explicitly assigned either by setting its [`AssetImporter.assetBundleName`](../ScriptReference/AssetImporter.assetBundleName.html) property to a non-empty string, or by listing it in [`AssetBundleBuild.assetNames`](../ScriptReference/AssetBundleBuild.assetNames.html).

Assets can be duplicated in AssetBundles if the same asset is referenced from different AssetBundles. If that asset isn’t explicitly assigned to an AssetBundle then Unity copies its content inside each AssetBundle that references it.

For example, if two objects are assigned to separate AssetBundles but share a reference to the same dependency object, Unity duplicates the dependency object into both AssetBundles. These duplicated dependencies are also instanced, meaning the two copies are treated as distinct objects with unique identifiers. This increases the overall size of the application’s AssetBundles and results in two separate copies of the object being loaded into memory if both parent AssetBundles are loaded.

To prevent this from happening, make sure that shared assets are explicitly assigned to an AssetBundle. For more information, refer to [Handling dependencies between AssetBundles](AssetBundles-Dependencies.html). The [Build Report Inspector](https://docs.unity3d.com/Packages/com.unity.build-report-inspector@latest) is also a useful tool to identify duplication in AssetBundles.

Addressables has the same issue with duplication of implicitly referenced assets. In that case, you can avoid it by assigning [shared assets to a group](https://docs.unity3d.com/Packages/com.unity.addressables@latest/?subfolder=/manual/Groups.html). The Addressables Analyze tool helps diagnose and resolve asset duplication.

## Additional resources

* [Direct reference asset management](assets-direct-reference.html)
* [Use AssetBundles to load assets at runtime](assetbundles-section.html)
* [Use the Resources system to load assets at runtime](assets-resources-system.html)
* [StreamingAssets](StreamingAssets.html)
* [Addressables package](https://docs.unity3d.com/Packages/com.unity.addressables@latest)
* [Handling dependencies between AssetBundles](AssetBundles-Dependencies.html)

Analyzing AssetBundles

Modify source assets from code

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
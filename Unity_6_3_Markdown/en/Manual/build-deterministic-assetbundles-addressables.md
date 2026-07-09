* [Building and publishing](building-and-publishing.html)
* [Deterministic builds](build-deterministic-builds.html)
* AssetBundle and Addressables determinism

Editor script determinism

Cache location reference

# AssetBundle and Addressables determinism

[AssetBundles](AssetBundlesIntro.html) and [Addressables](https://docs.unity3d.com/Packages/com.unity.addressables@latest) have related workflows for ensuring deterministic builds.

## AssetBundle determinism best practices

When building AssetBundles, every referenced asset and dependency must remain identical. Avoid timestamps or build-date suffixes in AssetBundle names and use static identifiers or semantic versions.

By design, you must build AssetBundles deterministically, independent of whether [incremental builds](building-introduction.html#incremental-build-pipeline) are enabled.

If clearing the cache breaks AssetBundle determinism, your build process has non-deterministic elements that need to be fixed. A common way to trace this issue back is as follows:

* Use a **version control**A system for managing file changes. You can use Unity in conjunction with most common version control tools, including Perforce, Git, Mercurial and Unity Version Control (UVCS). [More info](VersionControl.html)  
  See in [Glossary](Glossary.html#versioncontrol) system to identify assets that might have been unintentionally modified.
* Use tools like [UnityDataTools](https://github.com/Unity-Technologies/UnityDataTools/tree/main/UnityDataTool) to find differences in the serialized data contained within the AssetBundles.

For more information about building AssetBundles, refer to [Build assets into an AssetBundle](AssetBundles-Building.html).

## Addressable determinism

Because the Addressables system is built on top of the `AssetBundle` API, all the determinism best practices from the previous AssetBundle section apply to Addressables. Addressable builds are deterministic when the build environment and inputs are identical.

The deterministic behavior of Addressables also depends on both the Scriptable Build Pipeline (SBP) and the [Addressable hash calculation](https://docs.unity3d.com/Packages/com.unity.addressables@latest/index.html?subfolder=/manual/build-content-catalogs.html).

Because SBP calculates the content-based hash from the build outputs, it’s more sensitive to changes compared to AssetBundle hashing, which Unity computes from the build inputs.

In AssetBundle workflows, a non-deterministic build might produce the same cache identifier, such as an input-based hash or a filename, despite generating different binary content. This can lead to reusing outdated cached AssetBundles. SBP hashes the build output to avoid this issue.

Like AssetBundles, both the Addressable assets and all their referenced dependencies must be identical across builds to ensure determinism.

Addressables uses a content hash that SBP generates for caching. The SBP hash calculation isn’t limited to the binary content of the AssetBundle. It also includes the names of all dependent AssetBundles referenced by the target AssetBundle. For more information, refer to [Addressable asset dependencies](https://docs.unity3d.com/Packages/com.unity.addressables@latest/index.html?subfolder=/manual/AssetDependencies.html).

### Editor automation scripts

If your project uses Editor automation, such as custom **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) that automatically assign assets to Addressable groups, ensure the following:

* The order of assigned Addressables and Addressable groups are deterministic.
* Each build environment has identical [Addressable Asset Settings](https://docs.unity3d.com/Packages/com.unity.addressables@latest/index.html?subfolder=/manual/AddressableAssetSettings.html).

### Identifying non-deterministic Addressable builds

Every Addressables build automatically creates a build layout report, which includes information about all the built assets in your project. For more information, refer to [Create a build report](https://docs.unity3d.com/Packages/com.unity.addressables@latest/index.html?subfolder=/manual/BuildLayoutReport.html).

For binary-level inspection, use the [UnityDataTools](https://github.com/Unity-Technologies/UnityDataTools) project which can dump or export binaries into readable databases or text files, allowing detailed comparison of serialized data down to individual component fields.

## Additional resources

* [AssetBundles introduction](AssetBundlesIntro.html)
* [Build assets into an AssetBundle](AssetBundles-Building.html)
* [Addressables documentation](https://docs.unity3d.com/Packages/com.unity.addressables@latest)
* [UnityDataTools](https://github.com/Unity-Technologies/UnityDataTools)

Editor script determinism

Cache location reference

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
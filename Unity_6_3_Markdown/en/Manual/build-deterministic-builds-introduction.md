* [Building and publishing](building-and-publishing.html)
* [Deterministic builds](build-deterministic-builds.html)
* Deterministic builds introduction

Deterministic builds

Editor script determinism

# Deterministic builds introduction

Build determinism is important if you want to be able to repeat a build process and get the same set of binary files. Creating a deterministic build enables regulatory compliance for industries requiring binary verification, and is a useful way to ensure that users don’t download unchanged content. Deterministic builds make unauthorized modifications easier to detect, and you can also track any bugs to their exact code and asset states.

## Understanding non-deterministic builds

Non-deterministic builds can happen in the following situations:

* **During asset import and conversion:** Non-deterministic builds can happen when Unity imports source assets and converts them to an [internal format](assets-supported-types.html#native-asset-importers), or when Unity converts imported assets into packaged assets such as [AssetBundles](AssetBundlesIntro.html).
* **Editor **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
  See in [Glossary](Glossary.html#Scripts) that collect or modify assets at build time:** Non-deterministic builds can happen if, for example, tools or custom postprocessors automatically gather project assets and assign them to serialized array fields inside a ScriptableObject. If the order of objects in that array isn’t explicitly sorted, the serialized data might differ between machines or consecutive builds.

## Build environment consistency

The most common cause of non-deterministic builds are mismatched environments. To ensure a consistent environment consider the following:

* **Consistent build machine environments:** Keep operating system and CPU architecture consistent across all build machines. Floating-point rounding behavior differs between architectures, which can change serialized float values especially in AnimationClips or imported **Mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
  See in [Glossary](Glossary.html#Mesh) data.
* **Consistent toolchains:** Use the same Unity Editor version, Xcode version, and toolchains across builds. Small serialization changes between Unity versions can change AssetBundle byte layouts.
* **Disable automatic new line conversion in Git:** Windows and macOS encode line endings differently, and automatic line conversion modifies file hashes and breaks determinism. To disable automatic conversion, run the following git command:

  ```
  git config --global core.autocrlf false
  ```

### Use a cache server to preserve determinism

To achieve deterministic builds in Unity, the most effective method is to force all machines to share identical imported assets via [Unity Accelerator](UnityAccelerator.html).

When multiple developers connect to the same remote **Accelerator**The Unity Accelerator is an external tool that provides an asset cache that keeps copies of a team’s imported assets. The goal of the Accelerator is to speed up teamwork and reduce iteration time by coordinating asset sharing so that you don’t need to reimport portions of your project. [More info](UnityAccelerator.html)  
See in [Glossary](Glossary.html#Accelerator), each machine reuses the same imported artifacts instead of re-importing locally.

Unity Accelerator has the following limitations:

* It only caches imported assets.
* It doesn’t cache built AssetBundles or Addressable build artifacts.
* The determinism benefit applies to import-time consistency, not AssetBundle reuse.

## Additional resources

* [Introduction to Unity Accelerator](UnityAccelerator.html)
* [Managing assets at runtime](assets-managing-runtime.html)
* [AssetBundles introduction](AssetBundlesIntro.html)
* [Customize the build pipeline](build-customize-build-pipeline.html)

Deterministic builds

Editor script determinism

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
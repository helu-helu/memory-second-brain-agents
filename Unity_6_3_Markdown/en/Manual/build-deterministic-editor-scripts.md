* [Building and publishing](building-and-publishing.html)
* [Deterministic builds](build-deterministic-builds.html)
* Editor script determinism

Deterministic builds introduction

AssetBundle and Addressables determinism

# Editor script determinism

Scripts that modify assets during import or **post-processing**A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](Glossary.html#post-processing) can unintentionally break build determinism. Before building, ensure that all generated assets are version-controlled and stable.

To prevent Unity Editor **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) from causing non-deterministic builds, follow these guidelines:

* Sort collected assets deterministically by GUID or asset path before assigning them to serialized fields.
* [`Directory.GetFiles`](https://learn.microsoft.com/en-us/dotnet/api/system.io.directory.getfiles?view=net-9.0) and [`AssetDatabase.FindAssets`](../ScriptReference/AssetDatabase.FindAssets.html) don’t guarantee sorted results.
* Avoid deleting and re-importing assets before builds, because Unity generates new GUIDs for re-imported assets.

Avoid non-deterministic coding patterns such as the following:

* Postprocessor scripts that mark assets dirty and re-save them during import.
* AssetPostprocessor scripts that use random seeds or machine-specific paths.
* Random or time-based values (`Random.value`, `Guid.NewGuid`, `DateTime.Now`, noise sampling) in asset generation.
* Creating new ScriptableObject assets at build time, which generate different GUIDs per machine.
* Modifying asset serialized data during the build process, because changes can be difficult to detect.

## Pre-serialized runtime data determinism

In some workflows, tools generate pre-serialized runtime data such as Protobuf message binaries, JSON blobs, or other binary payloads during the build process and embed them into the build as assets or resources.

Even if the generated code is deterministic, the serialized data might not be. Review the official documentation or source of the serialization library to verify whether it produces deterministic output under identical inputs.

Avoid regenerating serialized data during every build. Instead, generate once, validate, and commit the data to **version control**A system for managing file changes. You can use Unity in conjunction with most common version control tools, including Perforce, Git, Mercurial and Unity Version Control (UVCS). [More info](VersionControl.html)  
See in [Glossary](Glossary.html#versioncontrol).

## Additional resources

* [`AssetDatabase` API reference](../ScriptReference/AssetDatabase.html)
* [`AssetPostprocessor` API reference](../ScriptReference/AssetPostprocessor.html)
* [ScriptableObject](class-ScriptableObject.html)
* [Customize the build pipeline](build-customize-build-pipeline.html)

Deterministic builds introduction

AssetBundle and Addressables determinism

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
* [Assets and media](assets-and-media.html)
* [Importing assets](import-assets.html)
* Asset import determinism

Managing importers with scripts

Analyze the import process

# Asset import determinism

A deterministic asset importer always produces the same output from the same input and set of dependencies. Non-determinism happens when the same asset file produces different import results, usually through cached import results.

When you download an import result from the cache, Unity assumes that the result is identical to the output of importing the asset locally. If you receive incorrect cached data, then you might experience inconsistent or failed builds, visual differences, or unexplained bugs. These issues are often subtle and difficult to debug because the source isn’t immediately clear.

## Non-deterministic asset importer code

A common cause of non-determinism is through any asset importers that you make with [scripted importers](ScriptedImporters.html), or `AssetPostprocessor` instances. Ensure that any scripted importers you write are deterministic. Register import dependencies, bump version numbers, and avoid creating non-deterministic `AssetPostprocessor` or `ScriptedImporter` code. For more information, refer to [Import dependencies and determinism](ScriptedImporters.html#import-dependencies-and-determinism).

## Non-deterministic asset types

Some Unity Editor-generated assets are non-deterministic and can produce different binary outputs when regenerated, even with identical source data and settings.

To maintain deterministic builds, avoid regenerating these assets unless the source content changes, and keep previously baked or generated data under **version control**A system for managing file changes. You can use Unity in conjunction with most common version control tools, including Perforce, Git, Mercurial and Unity Version Control (UVCS). [More info](VersionControl.html)  
See in [Glossary](Glossary.html#versioncontrol). Only rebuild **lightmaps**A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap), or other baked assets when the source content changes, and not as part of every build routine.

| **Asset type** | **Behavior** |
| --- | --- |
| **Lightmaps** | Re-baking lightmaps for every build produces different binary data, even with the same lighting setup. This is because the baking system involves not only floating-point rounding but also sampling noise that can make lightmaps non-reproducible. |
| ****NavMesh**A mesh that Unity generates to approximate the walkable areas and obstacles in your environment for path finding and AI-controlled navigation. [More info](https://docs.unity3d.com/Packages/com.unity.ai.navigation@latest/index.html?subfolder=/manual/NavInnerWorkings.html%23walkable-areas) See in [Glossary](Glossary.html#NavMesh)** | Build NavMeshes under identical input and environmental conditions. However, NavMeshes are sensitive to floating-point operations because Unity calculates the NavMesh based on the **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html) See in [Glossary](Glossary.html#Scene)’s meshes. Therefore, the NavMesh might bake differently on other architectures. |
| **Generated assets based on noise sampling** | Creating assets based on sampling noise textures or other randomness can generate assets differently each time. |

## Verify deterministic assets

Before you build assets, you can confirm whether the imported assets are deterministic with the `-consistencyCheck` command-line argument. You can also use the [Import Activity window](ImportActivityWindow.html) to inspect re-import reasons and timestamps.

You can disable automatic artifact cleanup when analyzing imports as follows:

```
EditorUserSettings.artifactGarbageCollection = false
```

This prevents Unity from deleting previous import artifacts. Deleting the [`Library` folder](default-directories.html) clears all historical import data.

### Investigate non-deterministic assets

To get more information about the non-deterministic assets in your project, inspect the Editor log file. To open the log:

1. Open the [**Console** window](Console.html) (**Window** > **General** > **Console**Abbreviation of **game console**  
   See in [Glossary](Glossary.html#console)).
2. Select the More menu (⋮) and select **Open Editor Log**.

The Editor log displays inconsistencies in the following format:

```
ConsistencyChecker - guid: <asset_guid>, dependenciesHash.value: <dep_hash_a>, importResultID: <result_id_a>, producedFiles[0].extension: , producedFiles[0].contentHash: <content_hash_a>
ConsistencyChecker - guid: <asset_guid>, dependenciesHash.value: <dep_hash_a>, importResultID: <result_id_b>, producedFiles[0].extension: , producedFiles[0].contentHash: <content_hash_b>
Importer(<importer_name>) generated inconsistent result for asset(<asset_guid>) <asset_path>
```

For more information, refer to [Check the consistency of the import process](ImporterConsistency.html#editor-log-output).

## Additional resources

* [Import Activity window](ImportActivityWindow.html)
* [Managing assets at runtime](assets-managing-runtime.html)
* [Command line arguments](CommandLineArguments.html)

Managing importers with scripts

Analyze the import process

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
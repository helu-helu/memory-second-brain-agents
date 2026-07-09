* [Assets and media](assets-and-media.html)
* [Managing assets with the Asset Database](AssetDatabase.html)
* Refreshing the Asset Database

Contents of the Asset Database

Programming with the Asset Database

# Refreshing the Asset Database

Unity refreshes the Asset Database in the following situations:

* When the Unity Editor regains focus (if you have enabled [Auto-Refresh](Preferences.html) in the Preferences window)
* When you select **Assets > Refresh** from the menu.
* When you call [`AssetDatabase.Refresh`](../ScriptReference/AssetDatabase.Refresh.html) from code. Some other `AssetDatabase` APIs trigger a refresh, but only for the assets you specify.

## Refresh process

Unity performs the following steps during an Asset Database refresh:

1. Check if any files in the `Assets` and `Packages` folders have been added, modified, or deleted since the last check and update the Asset Database accordingly.
2. Import and compile code-related files such as .dll, .asmdef, .asmref, .rsp, and .cs files.
3. Reload the [scripting domain](domain-reloading.html), if [Refresh](../ScriptReference/AssetDatabase.Refresh.html) was not invoked from a script.
4. Post-process all of the assets for the imported code-related files.
5. Import non-code-related assets and post-process all remaining imported assets.
6. [Hot reload](#hotreloading) the assets.

### Restarting the refresh process

Unity restarts the Asset Database refresh process if:

* The import of an asset fails.
* After the import, a file that the importer used has changed on disk.
* In [`OnPostProcessAllAssets`](../ScriptReference/AssetPostprocessor.OnPostprocessAllAssets.html), you call any of the following:
  + [`ForceReserializeAssets`](../ScriptReference/AssetDatabase.ForceReserializeAssets.html)
  + [`AssetImporter.SaveAndReimport`](../ScriptReference/AssetImporter.SaveAndReimport.html)
  + Any `AssetDatabase` API that queues an additional refresh, such as MoveAsset, CreateAsset and ImportAsset.
* The last modified timestamp of the file being imported changes while it’s being imported. This can happen if you start pulling files from a **version control**A system for managing file changes. You can use Unity in conjunction with most common version control tools, including Perforce, Git, Mercurial and Unity Version Control (UVCS). [More info](VersionControl.html)  
  See in [Glossary](Glossary.html#versioncontrol) system while the Editor has focus.
* An importer creates a file in the middle of an import. For example, FBX models can restart a refresh by extracting their Textures from the model.
* An assembly reload happens after compiling **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
  See in [Glossary](Glossary.html#Scripts). If you generate a C# file during the refresh process, that new file must then be compiled.
* You save an asset as **Text only** but the asset must be serialized as binary. For example, **Scenes**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
  See in [Glossary](Glossary.html#Scene) with Terrains in them must be serialized as Binary, since the **terrain**The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](terrain-UsingTerrains.html)  
  See in [Glossary](Glossary.html#Terrain) data would be unwieldy if viewed as an array of characters in a text file.

## Dependency tracking

The Asset Database keeps track of two types of Asset dependencies: **static dependencies** and **dynamic dependencies**. If any dependency of an asset changes, then Unity reimports the asset.

### Static dependencies

A static dependency is a value, setting, or property that an importer depends on. Static dependencies are known before the asset is imported, and are not affected by the behavior of the importer during the import process. If any of an asset’s static dependencies change, then Unity re-imports the asset.

Static dependencies include:

* The name of the asset.
* ID of the importer associated with the asset.
* The version of the importer.
* The currently selected build target platform.

### Dynamic dependencies

Dynamic dependencies are defined by the content of the source asset and are usually discovered during the import process. For example, a **shader**A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#shader) might reference another shader, and a **prefab**An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](Prefabs.html)  
See in [Glossary](Glossary.html#prefab) might depend on other prefabs.

The importer might also use a global state conditionally based on the content of the source asset, in which case it also becomes a dynamic dependency. Examples of this are the target platform, the project’s color space, the graphics API, the scripting runtime version, or the Texture **compression**A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](texture-choose-format-by-platform.html), [Animation Compression](class-AnimationClip.html#AssetProperties), [Audio Compression](class-AudioClip.html), [Build Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) state.

Unity stores dynamic dependencies of an asset in an [`AssetImportContext`](../ScriptReference/AssetImporters.AssetImportContext.html).

## Import and compile code-related files

In the list of changed or added files, Unity gathers the ones that relate to code, and sends them to the script compilation pipeline. The compiler generates assemblies from the script files and assembly definition files in your project. For more information on this step, refer to [Organizing scripts into assemblies](assembly-definition-files.html).

## Import non-code-related assets

Each asset’s importer processes that type of asset, and identifies files to import based on the file extensions. For example, the TextureImporter is responsible for importing .jpg, .png and .psd files, among others.

There are two types of importers:

* Native importers: Unity’s [built-in importers](assets-supported-types.html#asset-importers).
* [Scripted importers](ScriptedImporters.html): Custom importers that extend Unity’s import capabilities. These are written in C#.

Unity processes all native importers first, and then all scripted importers in a separate phase.

## Preprocessing and postprocessing

The `AssetPostprocessor` class provides a range of callbacks which allow you to perform work before (preprocessing) and after (postprocessing) import for different asset types. For the details of these callbacks and usage examples, refer to the [`AssetPostprocessor`](../ScriptReference/AssetPostprocessor.OnPreprocessAsset.html) API reference.

## Hot reloading

Hot reloading is the process of applying changes to scripts and assets while the Editor is open. This might happen while the Editor is in Play mode or Edit mode and requires no restart of the Editor for changes to take effect.

When you change and save a script, Unity hot-reloads all of the project’s script data. It first stores the values of [serializable variables](script-serialization-rules.html) in all loaded scripts, reloads the scripts, then restores the values. Data stored in non-serializable variables is lost.

This affects all Editor windows and all MonoBehaviour scripts in the project. Unlike other cases of serialization, Unity serializes private fields by default when reloading, even if they don’t have the [SerializeField](../ScriptReference/SerializeField.html) attribute.

## Additional resources

* [Contents of the Asset Database](asset-database-contents.html)
* [Programming with the Asset Database](AssetDatabaseCustomizingWorkflow.html)

Contents of the Asset Database

Programming with the Asset Database

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
* [Building and publishing](building-and-publishing.html)
* Content output of a build

Introduction to building

Create a build from the Editor

# Content output of a build

When you create a build of your Unity project, the `Data` folder (or equivalent on target platforms) contains the serialized files that make up the content of your application. The primary files in the build’s `Data` folder related to asset loading are:

* `globalgamemanager`: Contains core engine data, global **project settings**A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](comp-ManagerGroup.html)  
  See in [Glossary](Glossary.html#ProjectSettings) (like Quality Settings, Graphics Settings Physics settings, Tags, and Layers).
* `globalgamemanager.assets`: Contains assets referenced from the `globalgamemanager` file. This can include ScriptableObjects, such as HDRP or URP settings, and other assets referenced from those settings.
* `resources.assets`: Contains all assets located within any folder named [`Resources` in your project](LoadingResourcesatRuntime.html). These assets are always included in the build, regardless of whether they’re directly referenced by any **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
  See in [Glossary](Glossary.html#Scene), and can be loaded with [`Resources.Load`](../ScriptReference/Resources.Load.html).
* `level` files appended with a number, for example, `level0`, `level1`: Each `level` file corresponds to the [**Scene List**](build-profile-scene-list.html) in ****Build Profiles**A set of customizable configuration settings to use when creating a build for your target platform. [More info](build-profiles.html)  
  See in [Glossary](Glossary.html#buildprofile)**, in the order they appear. These files contain **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
  See in [Glossary](Glossary.html#GameObject) and components specific to that scene.
* `sharedassets` files appended with a number, for example, `sharedassets0`, `sharedassets1`: These files contain assets referenced by a scene reference. Their numbering corresponds to the scene in the scene build order that references them first.
* `Resources/unity_builtin_extra` : Contains built-in **shaders**A program that runs on the GPU. [More info](Shaders.html)  
  See in [Glossary](Glossary.html#shader) if they’re referenced by the build.
* `Resources/unity default resources`: Contains built-in assets that are always included in the build, such as default materials and fonts. This file is pre-built for each target platform, and distributed as part of the Unity Editor installation. Unity copies the file into the output as part of the build process.

**Important**: The exact layout and file formats that Unity uses might change between versions, so don’t write code that depends on the specific naming convention for the output files.

## Binary data

Each serialized file in the build can be accompanied by a .resS file which contains texture or **mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) data. For example `level0` might be accompanied by `level0.resS` and `sharedassets0` might be accompanied by `sharedassets0.assets.resS`.`

Similarly any serialized file that contains AudioClip or VideoClip objects will have an accompanying `.resource` file that contains the binary data for those objects. For example `level0.resource` or `sharedassets1.resource`.

Unity stores the binary data in separate files to reduce memory usage when loading assets at runtime and to aid in efficient transfer to the GPU for certain data types.

## Shared asset grouping

The order of the scenes in the [**Scene List**](build-profile-scene-list.html) in your project determines the way that Unity packs together shared assets as follows:

1. Unity processes scenes in the exact order listed in **File > Build Profiles > Scene List**.
2. Unity saves each object in the scene file to the corresponding `level` file, unless it’s an object that’s stripped out (for example an Editor-only component).
3. For each reference from a scene object to an object in an asset, Unity uses the direct reference graph to pull all required objects into the build. If a discovered object isn’t assigned to a `sharedasset` file then it’s assigned to the `sharedasset` file corresponding to the scene currently being processed. For example, `level2` populates `sharedassets2`, but it can also reference objects in `sharedassets0`, `sharedassets1`, `globalgamemanagers.assets`, `resources.assets`, and `unity_default_resources`.

This algorithm ensures that objects are only built once, rather than duplicating the assets across multiple scenes. It prioritizes efficiency of the first scenes in the scene list at the expense of later scenes. For example, `level0` has the least references of other files and can only reference `sharedassets0`, `globalgamemanagers.assets`, and `unity_default_resources`. In contrast, `level99` might reference objects spread over 100 `sharedasset` files, `globalgamemanagers.assets`, `resources.assets`, and `unity_default_resource`.

The algorithm gives specific preference to the first scene, because it’s the first to load when the application starts.

## Player data compression options

You can optionally compress Player data into an LZ4 ArchiveFile, by specifying [`BuildOptions.CompressWithLz4`](../ScriptReference/BuildOptions.CompressWithLz4.html). This is the same file format that Unity uses to archive AssetBundles.

The compressed file for Player builds is always called `data.unity3d` and contains the global game managers (`globalgamemanagers`) serialized files, scene serialized files (`level` and `sharedassets` files), Resources serialized files (`resources.assets`), and shader serialized files (`Resources/unity_builtin_extra`).

It doesn’t contain `Resources/unity default resources`, because the content build doesn’t generate that file.

It also doesn’t contain any `.resource` files that contain video and audio content, which are left outside the `data.unity3d` file.

## AssetBundle content output

If you use AssetBundles to build content, then the way Unity assigns objects to files, and the file naming conventions, are different. For more information, refer to [AssetBundle build output](assetbundles-file-format.html).

## Additional resources

* [Introduction to asset management](assets-managing-introduction.html)
* [Include additional files in a build](StreamingAssets.html)
* [Reducing the file size of a build](ReducingFilesize.html)

Introduction to building

Create a build from the Editor

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
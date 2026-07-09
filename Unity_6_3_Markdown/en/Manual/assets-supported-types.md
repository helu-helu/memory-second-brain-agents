* [Assets and media](assets-and-media.html)
* [Types of assets](AssetTypes.html)
* Supported asset type reference

Types of assets

Models

# Supported asset type reference

Unity supports many different types of assets and most common image file types. It uses [asset importers](#asset-importers) to process and convert external files into assets you can use in your project.

Unity supports the following kinds of files:

* **3D model files**: Unity supports standard and proprietary **model file**A file containing a 3D data, which may include definitions for meshes, bones, animation, materials and textures. [More info](3D-formats.html)  
  See in [Glossary](Glossary.html#modelfile) formats. Internally, Unity uses the FBX file format as its importing chain. For a list of supported files, refer to [3D model importers](#3d-model-importers).
* **Image files**: Unity imports image files as textures and supports most common image file types. For a list of supported files, refer to [Image importers](#image-importers).
* **Audio and video files**: Unity supports many audio and video file formats. For a list of supported files, refer to [Audio and video importers](#audio-and-video-importers).
* ****Shader**A program that runs on the GPU. [More info](Shaders.html)  
  See in [Glossary](Glossary.html#shader) files**: Unity supports different shader file types depending on the graphics pipeline you’re using. For a list of supported files, refer to [Shader importers](#shader-importers).
* **Text and arbitrary data**: Unity can import arbitrary data from files such as .html, .xml, .json files, which you can use to store and use data from external sources. For a list of supported files, refer to [Text and arbitrary data importers](#text-and-arbitrary-data-importers).
* **Plug-ins and code related assets**: You can add managed and native [plug-ins](plug-ins.html)A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)  
  See in [Glossary](Glossary.html#plug-in) files into your project to expand the functionality of your application, and [assembly definitions](assembly-definition-files.html) to create and organize your **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
  See in [Glossary](Glossary.html#Scripts) into assemblies. For a list of supported files, refer to [Plug-ins and code importers](#plug-ins-and-code-importers)
* **Native assets**: There are a range of asset types that are native to the Unity Editor. For a list of supported files, refer to [Native asset importers](#native-asset-importers).

## Asset importers

Unity uses importers to process and convert external files into assets that can be used in your project. Each file type has a corresponding importer that handles its specific requirements.

Unity supports many asset file types via its collection of built-in importers. Most of these importers are implemented in the Unity Editor’s native code. They provide the import functionality for most of Unity’s basic asset types, such as 3D models, textures, and audio files.

Most importers have a corresponding class in the `UnityEditor` namespace that exposes the same configurable import settings as the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window for the asset type. They also have corresponding pre-process and post-process callbacks on the [`AssetPostprocessor`](../ScriptReference/AssetPostprocessor.html) class so you can define custom behavior to run before or after asset import. For example, the import settings for the `AudioImporter` are configurable in the [Audio Clip Inspector window](class-AudioClip.html) or from code with the [`AudioImporter` class](../ScriptReference/AudioImporter.html). You can also create custom pre-import or post-import behavior for audio assets with [`AssetPostprocessor.OnPreprocessorAudio`](../ScriptReference/AssetPostprocessor.OnPreprocessAudio.html) and [`AssetPostprocessor.OnPostprocessAudio`](../ScriptReference/AssetPostprocessor.OnPostprocessAudio.html) respectively. This pattern applies for most major asset types.

### 3D model importers

Unity uses the FBX file format as its importing chain. For a list of 3D modeling software that Unity supports, refer to [Model file formats](3D-formats.html).

| **Importer** | **Description** | **Supported file formats** |
| --- | --- | --- |
| **FBXImporter** | Imports 3D model files. For more information, refer to [Importing a model](ImportingModelFiles.html). | * `.blend` * `.c4d` * `.dae` * `.dxf` * `.fbx` * `.jas` * `.lxo` * `.ma` * `.mb` * `.max` * `.obj` |
| **Mesh3DSImporter** | Imports 3D Studio Max files. For more information, refer to [Importing a model](ImportingModelFiles.html). | `.3ds` |
| **SketchUpImporter** | Imports SketchUp files. For more information, refer to [SketchUp Import Settings](class-SketchUpImporter.html) and [`SketchUpImporter`](../ScriptReference/SketchUpImporter.html). | `.skp` |
| **SpeedTreeImporter** | Imports SpeedTree files. For more information, refer to [SpeedTree Import Settings window](class-SpeedTreeImporter.html) and [`SpeedTreeImporter`](../ScriptReference/SpeedTreeImporter.html). | * `.spm` * `.st` |
| **SubstanceImporter** | Imports Substance files. | `.sbsar` |

### Audio and video importers

| **Importer** | **Description** | **Supported file formats** |
| --- | --- | --- |
| **AudioImporter** | Imports audio files. For more information, refer to [Audio files](AudioFiles.html) and [`AudioImporter`](../ScriptReference/AudioImporter.html). | * `.aif` * `.aiff` * `.flac` * `.it` * `.mod` * `.mp3` * `.ogg` * `.s3m` * `.wav` * `.xm` |
| **VideoClipImporter** | Imports video files. For more information, refer to [Video sources](video-sources.html) and [`VideoClipImporter`](../ScriptReference/VideoClipImporter.html). | * `.asf` * `.avi` * `.dv` * `.m4v` * `.mov` * `.mp4` * `.mpg` * `.mpeg` * `.ogv` * `.vp8` * `.webm` * `.wmv` |

### Image importers

Unity imports image files as textures. Unity supports most common image file types, such as `.bmp`, `.tif`, `.tga`, `.jpg`, `.svg`, and `.psd`. For more information, refer to [Import a texture](ImportingTextures.html).

| **Importer** | **Description** | **Supported file formats** |
| --- | --- | --- |
| **IHVImageFormatImporter** | Imports specialized image formats. For more information, refer to [`IHVImageFormatImporter`](../ScriptReference/IHVImageFormatImporter.html). | * `.astc` * `.dds` * `.ktx` * `.pvr` |
| **TextureImporter** | Imports texture files. For more information, refer to [Import a texture](ImportingTextures.html) and [`TextureImporter`](../ScriptReference/TextureImporter.html). | * `.bmp` * `.exr` * `.gif` * `.hdr` * `.iff` * `.jpeg` * `.jpg` * `.pct` * `.pic` * `.pict` * `.png` * `.psd` * `.tga` * `.tif` * `.tiff` * `.svg` |

### Native asset importers

There are a range of asset types that are native to the Unity Editor. You can create assets of these types using Editor features. When you create these, Unity saves the files which represent them as asset files in the `Assets` folder of your project. These include [animations](animeditor-CreatingANewAnimationClip.html), [curves](EditingCurves.html), [gradients](PartSysUsage.html), [masks](class-AvatarMask.html)Can refer to a Sprite Mask, a UI Mask, or a Layer Mask [More info](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/script-Mask.html)  
See in [Glossary](Glossary.html#mask), [materials](Materials.html)An asset that defines how a surface should be rendered. [More info](class-Material.html)  
See in [Glossary](Glossary.html#Material), and [presets](Presets.html).

| **Importer** | **Description** | **Supported file formats** |
| --- | --- | --- |
| **NativeFormatImporter** | Imports Unity’s native asset formats. | * `.anim` * `.asset` * `.blendtree` * `.brush` * `.buildreport` * `.colors` * `.controller` * `.cubemap` * `.curves` * `.curvesNormalized` * `.flare` * `.fontsettings` * `.giparams` * `.gradients` * `.guiskin` * `.ht` * `.mask` * `.mat` * `.mesh` * `.mixer` * `.overrideController` * `.particleCurves` * `.particleCurvesSigned` * `.particleDoubleCurves` * `.particleDoubleCurvesSigned` * `.physicMaterial` * `.physicsMaterial2D` * `.playable` * `.preset` * `.renderTexture` * `.shadervariants` * `.signal` * `.spriteatlas` * `.state` * `.statemachine` * `.terrainlayer` * `.texture2D` * `.transition` * `.webCamTexture` |
| **PrefabImporter** | Imports **prefab**An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](Prefabs.html) See in [Glossary](Glossary.html#prefab) files. For more information, refer to [Creating prefabs](CreatingPrefabs.html). | `.prefab` |
| **VisualEffectImporter** | Imports visual effect files. | * `.vfx` * `.vfxblock` * `.vfxoperator` |

### Plug-ins and code importers

You can add managed and native [plug-ins](plug-ins.html) such as `.dll` files into your project to expand the functionality of your application. Unity also supports [assembly definitions](assembly-definition-files.html) to help you create and organize your scripts into assemblies.

| **Importer** | **Description** | **Supported file formats** |
| --- | --- | --- |
| **AssemblyDefinitionImporter** | Imports assembly definition files. For more information, refer to [Introduction to assemblies in Unity](assembly-definitions-intro.html). | `.asmdef` |
| **AssemblyDefinitionReferenceImporter** | Imports assembly definition reference files. For more information, refer to [Introduction to assemblies in Unity](assembly-definitions-intro.html). | `.asmref` |
| **DefaultImporter** | Imports system files. | * `.rsp` * `.unity` |
| **PackageManifestImporter** | Imports package manifest files. For more information, refer to [Package manifest](upm-manifestPkg.html)Each package has a *manifest*, which provides information about the package to the Package Manager. The manifest contains information such as the name of the package, its version, a description for users, dependencies on other packages (if any), and other details. [More info](upm-manifestPkg.html) See in [Glossary](Glossary.html#packagemanifest). | `.json` |
| **PluginImporter** | Imports plug-in files. For more information, refer to [Import and configure plug-ins](plug-in-inspector.html) and [`PluginImporter`](../ScriptReference/PluginImporter.html). | * `.a` * `.aar` * `.bc` * `.bundle` * `.c` * `.cc` * `.config` * `.cpp` * `.dylib` * `.h` * `.jar` * `.java` * `.jslib` * `.jspre` * `.kt` * `.m` * `.mm` * `.prx` * `.rpl` * `.so` * `.suprx` * `.swift` * `.winmd` * `.xib` |

### Shader importers

| **Importer** | **Description** | **Supported file formats** |
| --- | --- | --- |
| **ComputeShaderImporter** | Imports compute shader files. For more information, refer to [Writing compute shaders](class-ComputeShader.html) and [`ComputeShader`](../ScriptReference/ComputeShaderImporter.html). | `.compute` |
| **RayTracingShaderImporter** | Imports **ray tracing**The process of generating an image by tracing out rays from the Camera through each pixel and recording the color contribution at the hit point. This is an alternative to rasterization. raytracing See in [Glossary](Glossary.html#raytracing) shader files. For more information, refer to [Introduction to shaders](shader-introduction.html). | `.raytrace` |
| **ShaderImporter** | Imports shader files. For more information, refer to [Introduction to shaders](shader-introduction.html) and [`ShaderImporter`](../ScriptReference/ShaderImporter.html). | * `.cg` * `.cginc` * `.glslinc` * `.hlsl` * `.shader` |

### Text and arbitrary data importers

| **Importer** | **Description** | **Supported file formats** |
| --- | --- | --- |
| **LocalizationImporter** | Imports localization files. | `.po` |
| **TextScriptImporter** | Imports text and script files. For more information, refer to [Text assets](class-TextAsset.html). | * `.boo` * `.bytes` * `.csv` * `.fnt` * `.htm` * `.html` * `.js` * `.json` * `.manifest` * `.md` * `.rsp` * `.txt` * `.xml` * `.yaml` |
| **TrueTypeFontImporter** | Imports font files. For more information, refer to [Font assets](UIE-font-asset-landing.html) and [`TrueTypeFontImporter`](../ScriptReference/TrueTypeFontImporter.html). | * `.dfont` * `.otf` * `.ttc` * `.ttf` |

### Built-in scripted importers

[Scripted importers](ScriptedImporters.html) allow you to write your own custom importers for formats that Unity doesn’t natively support. Some of Unity’s own built-in importers are implemented as scripted importers because they are written in C# in core packages, rather than within the Unity Editor’s native code itself. Unity imports scripted importer assets after native importer assets.

| **Importer** | **Description** | **File formats** |
| --- | --- | --- |
| **SpeedTree9Importer** | Imports SpeedTree 9 files. For more information, refer to [`SpeedTree9Importer`](../ScriptReference/SpeedTree.Importer.SpeedTree9Importer.html). | `.st9` |
| **StyleSheetImporter** | Imports Unity style sheet files. For more information, refer to [Introduction to USS](UIE-about-uss.html). | `.uss` |
| **UIElementsViewImporter** | Imports Unity XML files. For more information, refer to [Structure UI with UXML](UIE-UXML.html). | `.uxml` |

## Additional resources

* [Scripted importers](ScriptedImporters.html)
* [Introduction to importing assets](ImportingAssets.html)
* [Asset metadata](AssetMetadata.html)
* [`AssetPostprocessor` API reference](../ScriptReference/AssetPostprocessor.html)

Types of assets

Models

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
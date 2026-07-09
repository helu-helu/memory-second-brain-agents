* [Assets and media](assets-and-media.html)
* [Importing assets](import-assets.html)
* Introduction to importing assets

Importing assets

Asset metadata

# Introduction to importing assets

When you create a Unity project, Unity creates a folder for your project which contains an `Assets` subfolder. You can use this folder to store assets created outside of Unity to then use in your project.

**Important:** Using cloud-based storage methods to store your project is an unsupported workflow. It can cause synchronization issues which corrupt your project. Use [version control](VersionControl.html)A system for managing file changes. You can use Unity in conjunction with most common version control tools, including Perforce, Git, Mercurial and Unity Version Control (UVCS). [More info](VersionControl.html)  
See in [Glossary](Glossary.html#versioncontrol) to manage your project.

## Using the Assets folder

You can either export the asset file directly into the `Assets` folder, or copy it into the folder. For many common formats, you can save the source file directly into your project’s `Assets` folder and Unity can read it. Unity also detects when you save new changes to the file and re-imports files as necessary.

For a list of supported asset types, refer to [Supported asset type reference](assets-supported-types.html).

### Managing assets in the Project window

Use the [Project window](ProjectView.html)A window that shows the contents of your `Assets` folder (Project tab) [More info](ProjectView.html)  
See in [Glossary](Glossary.html#Projectwindow) to view the contents of your `Assets` folder. Whenever you save or copy a file to your `Assets` folder, Unity imports it and it then appears in your Project window. If you drag a file from your computer’s file browser into Unity’s Project window, Unity makes a copy and places it into your `Assets` folder. You can then access this copy from the Project window.

**Warning:** Usually, the items that appear in your Project window represent actual files on your computer. If you delete them in the Project window, you also delete them from your computer.

![The Project window with the Assets folder opened, containing food related models.](../uploads/Main/importing-project-window.png)


The Project window with the Assets folder opened, containing food related models.

### Modifying asset files

When you modify a file in Unity, Unity doesn’t modify your original source file. Instead, the import process reads your source file, and creates a representation of your asset internally, which matches your chosen [import settings](#asset-import-settings). If you modify the import settings for an asset, or make a change to the source file in the `Assets` folder, Unity re-imports the asset again to reflect your changes.

If you want to move or rename assets in your project, it’s best practice to do it in the Project window. Unity then automatically moves or renames the asset’s corresponding `.meta` file. For more information on .meta files, refer to [Asset metadata](AssetMetadata.html).

If you drag a file from your computer’s file browser into Unity’s Project window, Unity makes a copy and places it into your `Assets` folder. You can then access this copy from the Project window.

### Complex assets

If you import a single asset file that contains complex information, Unity might create multiple assets from it. For example:

* If a 3D file (such as an FBX file) defines materials or contains embedded textures, Unity extracts the [materials and embedded textures](FBXImporter-Materials.html) as separate assets.
* If you want to import an image file as multiple 2D sprites. Use the 2D **Sprite**A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](sprite/sprite-landing.html)  
  See in [Glossary](Glossary.html#Sprite) Editor to define multiple sprites from a single graphic image and Unity displays each sprite as a separate sprite asset in the Project window. For more information, refer to [Create sprites from a texture](sprite/sprite-editor/use-editor.html).
* If a 3D file contains multiple animation timelines or multiple clips, Unity automatically defines separate animation timelines or clips based on its [animation import settings](Splittinganimations.html). The resulting multiple animation clips appear as separate **Animation Clip**Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](class-AnimationClip.html)  
  See in [Glossary](Glossary.html#AnimationClip) assets in the Project window.

## Asset processing

Unity reads and processes any files that you add to the `Assets` folder and converts the contents of the file to internal data that’s correctly formatted for your application’s target platform. The source asset files remain unchanged, and Unity stores the internal data in the project’s `Library` folder. This data is part of Unity’s [Asset Database](AssetDatabase.html).

Unity uses internal formats for assets so it can use versions of your assets at runtime in the Unity Editor, and can keep your unmodified source files in the `Assets` folder. This system means that you can edit an asset file and the Editor picks up the changes automatically. For example, hardware such as mobile devices can’t convert `.psd` files directly to render them as textures. When you place a `.psd` file in the `Assets` folder, Unity converts the file to an internal version that mobile devices can process.

Unity stores the internal representation of your assets in the `Library` folder, which behaves like a cache folder. You don’t need to ever alter the `Library` folder manually, and if you do, you might negatively affect your project. This also means that you don’t need to include the `Library` folder under version control.

**Tip:** If your project isn’t open, you can safely delete the `Library` folder, because Unity can regenerate all its data from the `Assets` and `ProjectSettings` folders the next time you launch your project.

## Asset import settings

Each type of asset that Unity supports has a set of import settings, which affect how the asset appears or behaves. To view an asset’s import settings, select the asset in the Project window. The import settings for the selected asset appear in the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector). The options that appear vary depending on the type of asset selected.

![A selected models Inspector window with its Import Settings displayed.](../uploads/Main/importing-model-import-settings.png)


A selected model’s Inspector window with its Import Settings displayed.

For more information, refer to the documentation on the following Import Settings:

* [Model Import Settings](class-FBXImporter.html)
* [SketchUp Import Settings](class-SketchUpImporter.html)
* [SpeedTree Import Settings](class-SpeedTreeImporter.html)
* [Texture Import Settings](class-TextureImporter.html)
* [Cubemap texture Import Settings](texture-type-cubemap.html)
* [Animation Import Settings](class-AnimationClip.html)
* [Assembly Definition Import Settings](class-AssemblyDefinitionImporter.html)
* [Audio Import Settings](class-AudioClip.html)

If you’re developing a cross-platform project, you can override the default settings and assign different import settings on a per-platform basis.

## Reusing assets between projects

As you build your application, [Unity stores metadata](AssetMetadata.html) about your assets, such as import settings and links to other assets, among other information. If you want to transfer your assets into a different project and preserve all this information, you can export your assets into one of the following containers:

* An [asset package](AssetPackages.html)A collection of files and data from Unity projects, or elements of projects, which are compressed and stored in one file, similar to Zip files, with the `.unitypackage` extension. Asset packages are a handy way of sharing and re-using Unity projects and collections of assets. [More info](AssetPackages.html)  
  See in [Glossary](Glossary.html#assetpackage), which you can create directly in the Editor.
* A [custom package](CustomPackages.html), which you can access and manage inside the [Package Manager](Packages.html).

## Additional resources

* [Asset packages](AssetPackages.html)
* [Materials and shaders](Materials.html)
* [Textures and videos](Textures.html)
* [Import a sprite or spritesheet texture](sprite/import-images-sprites/import-images-sprites-landing.html)
* [Audio files](AudioFiles.html)

Importing assets

Asset metadata

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
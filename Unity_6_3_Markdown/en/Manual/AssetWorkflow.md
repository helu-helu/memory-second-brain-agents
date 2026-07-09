* [Assets and media](assets-and-media.html)
* Introduction to assets in Unity

Assets and media

Types of assets

# Introduction to assets in Unity

An asset is any item that you use in your Unity project to create your application, such as textures, 3D models, or sound files. Assets can include:

* ****Visual elements**A node of a visual tree that instantiates or derives from the C# [`VisualElement`](../ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](UIE-VisualTree.html)  
  See in [Glossary](Glossary.html#visualelement)**: 3D models, textures, or **sprites**A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](sprite/sprite-landing.html)  
  See in [Glossary](Glossary.html#Sprite).
* **Audio elements**: Sound effects or music.
* **Abstract items**: Color gradients, animation masks, arbitrary text, or numeric data.

## Importing assets

To use assets in Unity, you must [import them into your project](import-assets.html). You can [add assets to the `Assets` folder](ImportingAssets.html) of your project, or [use scripts](ScriptedImporters.html) to import assets automatically.

**Important:** Using cloud-based storage methods to store your project is an unsupported workflow. It can cause synchronization issues which corrupt your project. Use [version control](VersionControl.html)A system for managing file changes. You can use Unity in conjunction with most common version control tools, including Perforce, Git, Mercurial and Unity Version Control (UVCS). [More info](VersionControl.html)  
See in [Glossary](Glossary.html#versioncontrol) to manage your project.

Unity supports a wide range of asset formats. For more information, refer to [Supported asset type reference](assets-supported-types.html).

If you’re working on a complex project with a large team of people, you can use the [Unity Accelerator](UnityAccelerator.html) cache server to speed up asset management.

## How Unity manages assets

Unity uses the [Asset Database](AssetDatabase.html) to store the assets in your project and maintain consistency between the original source files and their imported versions used by your application at runtime. You can use the [Import Activity window](ImportActivityWindow.html) to inspect how Unity imports the assets in your project.

## Grouping assets together

You can use [AssetBundles](assetbundles-section.html) to group together assets in an archive file format, which you can then use to update assets remotely, or provide DLC content for your application.

You can also use [asset packages](AssetPackages.html)A collection of files and data from Unity projects, or elements of projects, which are compressed and stored in one file, similar to Zip files, with the `.unitypackage` extension. Asset packages are a handy way of sharing and re-using Unity projects and collections of assets. [More info](AssetPackages.html)  
See in [Glossary](Glossary.html#assetpackage) to package assets together to share between other Unity projects.

## Managing assets through scripts

You can perform many of the loading, importing, and unloading operations that Unity does with the [Asset Database APIs](AssetDatabaseCustomizingWorkflow.html).

An alternative method of managing loading assets is with the [Resources system](LoadingResourcesatRuntime.html), but it can impact on the performance of your application.

The [Addressables package](https://docs.unity3d.com/Packages/com.unity.addressables@latest) provides a streamlined workflow for managing asset loading at runtime and is the recommended system for organizing assets in Unity projects.

## Additional resources

* [Supported asset type reference](assets-supported-types.html)
* [Introduction to Unity Accelerator](UnityAccelerator.html)
* [Programming with the Asset Database](AssetDatabaseCustomizingWorkflow.html)
* [Introduction to AssetBundles](AssetBundlesIntro.html)

Assets and media

Types of assets

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
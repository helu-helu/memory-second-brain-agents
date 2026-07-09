* [Assets and media](assets-and-media.html)
* [Importing assets](import-assets.html)
* Asset metadata

Introduction to importing assets

Import assets simultaneously

# Asset metadata

As part of the [importing process](ImportingAssets.html), Unity creates metadata about any assets you import into your project. The metadata contains information such as the asset’s [import settings](ImportingAssets.html#asset-import-settings), and where your project uses the asset. When you import an asset, Unity does the following:

* [Assigns the asset a unique ID](#asset-ids).
* [Creates a `.meta` file for the asset](#meta-files).
* [Processes the asset](ImportingAssets.html#asset-processing).

## Asset IDs

The Unity Editor frequently checks the contents of the `Assets` folder against the list of assets it already knows about. When you place an asset in the `Assets` folder, Unity detects that you have added a new file and assigns a unique ID to the asset. This is an ID that Unity uses internally to reference the asset, so that it can move or rename the asset without breaking anything. You can use the [Import Activity window](ImportActivityWindow.html) to view the ID of an asset.

## Meta files

Unity creates `.meta` files for each folder and file in your project’s `Assets` folder and stores the `.meta` file in the same location as the asset file. These files are hidden in the [Project window](ProjectView.html)A window that shows the contents of your `Assets` folder (Project tab) [More info](ProjectView.html)  
See in [Glossary](Glossary.html#Projectwindow), and are considered a hidden file by your operating system, so might be hidden by default in your file browser.

The `.meta` files contain the unique ID assigned to the asset, and values for all the asset’s [import settings](ImportingAssets.html#asset-import-settings). If you change the import settings for an asset, Unity saves those new settings to the `.meta` file that accompanies the asset. Unity then re-imports the asset according to your updated settings, and updates the corresponding imported data in the project’s `Library` folder.

### Moving and renaming assets

Meta files contain important information about how the asset is used in your project, and they must stay with the asset file they relate to. If you move or rename an asset within the Project window, Unity automatically moves or renames the corresponding `.meta` file. However, if you move or rename an asset outside of Unity, you must move or rename the `.meta` file to match.

If an asset loses its `.meta` file, any reference to that asset is broken in your project. In this situation, Unity generates a new `.meta` file for the moved or renamed asset as if it’s a brand new asset, and deletes the old `.meta` file. When Unity deletes the old `.meta` file it might cause significant issues such as the following:

* If a texture asset loses its `.meta` file, any materials that use that texture lose their reference to that texture. To fix it, you must manually re-assign that texture to any materials which require it.
* If a script asset loses its `.meta` file, any **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
  See in [Glossary](Glossary.html#GameObject) or **Prefabs**An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](Prefabs.html)  
  See in [Glossary](Glossary.html#prefab) that have that script assigned instead have an unassigned script component, and lose their functionality. To fix it, you must manually re-assign that script to any GameObjects which require it.

### Empty folders and version control

Unity assigns each folder in your project’s `Assets` folder its own `.meta` file. However, some **version control**A system for managing file changes. You can use Unity in conjunction with most common version control tools, including Perforce, Git, Mercurial and Unity Version Control (UVCS). [More info](VersionControl.html)  
See in [Glossary](Glossary.html#versioncontrol) systems (VCS) can’t store empty folders. When you add or delete an empty folder from your project, the VCS stores the `.meta` file as added or removed, but doesn’t store the change of adding or removing the folder itself. To help resolve this issue, Unity behaves in the following ways relating to empty folders:

* If Unity detects an empty folder that no longer has a corresponding `.meta` file, it assumes another user in your VCS deleted the folder and removed the meta file, so deletes the empty folder locally.
* If Unity detects a new `.meta` file for a folder, but that folder doesn’t exist locally, it assumes another user in your VCS created a new folder, and then creates a new unversioned meta file for empty folders.

## Additional resources

* [Importing assets introduction](ImportingAssets.html)
* [Asset workflow](AssetWorkflow.html)

Introduction to importing assets

Import assets simultaneously

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
* [Get started](get-started.html)
* [Project configuration](project-configuration.html)
* Default project directories

Diff tool support

Reserved folder name reference

# Default project directories

When you create a project, Unity creates a project folder which contains default subfolders. These default subfolders each have a specific role in organizing your project’s files, settings, and data.

**Important:** Using cloud-based storage methods to store your project is an unsupported workflow. It can cause synchronization issues which corrupt your project. Use [version control](VersionControl.html)A system for managing file changes. You can use Unity in conjunction with most common version control tools, including Perforce, Git, Mercurial and Unity Version Control (UVCS). [More info](VersionControl.html)  
See in [Glossary](Glossary.html#versioncontrol) to manage your project.

The default directories that Unity creates are as follows:

## Assets

Use the `Assets`folder to store all asset files related to your project, including **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts), textures, models, audio files, and [scenes](working-with-scenes.html)A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). For more information, refer to [Introduction to importing assets](ImportingAssets.html).

The folder contains the following files and subfolders:

| **File or folder** | **Description** |
| --- | --- |
| `InputSystem_Actions` | A default input action asset. For more information, refer to [Input action assets](https://docs.unity3d.com/Packages/com.unity.inputsystem@latest?subfolder=/manual/ActionAssets.html). |
| `Scenes` | Contains a default [scene](scenes-working-with.html) called `SampleScene`. |
| `Settings` | Contains asset setting files that determine how Unity handles certain assets in your project by default. The default settings Unity creates depend on [the template](https://docs.unity.com/hub/project-create#template-categories.html) you used to create your project. Examples include default settings for [the volumes](urp/Volumes.html) in your project, and default [Universal renderer assets](urp/urp-universal-renderer.html) and [Universal Render Pipeline assets](urp/universalrp-asset.html) for mobile and desktop. |
| `TutorialInfo` | Files related to the in-Editor tutorials. |

## Library

The `Library` folder contains a local cache of imported assets and metadata. Exclude the `Library` folder from version control, because it’s unique to your computer and is a working directory for your project. It also doesn’t display in the [Project window](ProjectView.html)A window that shows the contents of your `Assets` folder (Project tab) [More info](ProjectView.html)  
See in [Glossary](Glossary.html#Projectwindow) of the Unity Editor.

You can delete the `Library` folder to troubleshoot unexplained issues or a corrupted project. Unity regenerates the folder the next time you open the project. However, only delete the `Library` folder as a last-resort measure for critical, unrecoverable errors. Deleting it forces Unity to recompile all project code and reimport all assets, which can take a significant amount of time.

**Warning:** Don’t edit the contents of the `Library` folder. It contains data that might corrupt your project if you edit it. The following information is provided for reference only.

| **Folder** | **Description** |
| --- | --- |
| `APIUpdater` | Contains files related to the [API updater](APIUpdater.html) process. |
| `Artifacts` | Contains files related to asset processing and compilation. |
| `Bee` | Contains data related to Unity’s build process. |
| `BuildPlayerData` | Contains cached type data from the most recent Player or content-only build. |
| `BuildProfiles` | Contains files related to [build profiles](build-profiles.html)A set of customizable configuration settings to use when creating a build for your target platform. [More info](build-profiles.html) See in [Glossary](Glossary.html#buildprofile). |
| `BurstCache` | Contains cache data for the [Burst compiler](https://docs.unity3d.com/Packages/com.unity.burst@latest). |
| `PackageCache` | Contains the installed packages in your project. |
| `PackageManager` | Contains data related to the [Package Manager](PackagesList.html). |
| `PlayerDataCache` | Contains cached data from the most recent Player build. |
| `PlayerScriptAssemblies` | Contains assemblies compiled for the target platform. Used during content-only builds. |
| `ScriptAssemblies` | Contains files related to [Unity’s scripting processes](overview-of-dot-net-in-unity.html). |
| `Search` | Contains data related to [Unity Search](search-overview.html). |
| `ShaderCache` | Contains cache data related to the **shaders**A program that runs on the GPU. [More info](Shaders.html) See in [Glossary](Glossary.html#shader) in your project. |
| `StateCache` | Contains cache data related to the current Editor session, including the state of the Hierarchy window and **Scene view**An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](UsingTheSceneView.html) See in [Glossary](Glossary.html#SceneView). |
| `TempArtifacts` | A folder that Unity uses to store temporary import data, before moving it to the `Artifacts` folder. |

## Logs

Contains log files related to import operations and other Editor processes. For more information, refer to [Log files reference](log-files.html).

## Packages

Contains a [`manifest.json`](upm-manifestPrj.html) file which defines the packages to use in your project.

## ProjectSettings

Contains project-specific settings files, such as settings for building, graphics, and memory, and managers for input, tags, and presets.

## Temp

A folder for temporary data, which gets cleared every time you close Unity. Exclude this folder from version control.

## UserSettings

Contains settings for your local version of the project, such as specific [user preferences](Preferences.html), and your preferred [Editor layout](CustomizingYourWorkspace.html). Exclude from version control to avoid overwriting your teammates’ personal Unity preferences.

## Additional resources

* [Introduction to importing assets](ImportingAssets.html)
* [Log files reference](log-files.html)

Diff tool support

Reserved folder name reference

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
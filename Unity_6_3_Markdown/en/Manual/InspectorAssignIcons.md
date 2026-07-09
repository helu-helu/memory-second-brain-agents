* [Unity Editor interface](unity-editor.html)
* [Unity Editor windows and views reference](editor-windows-views-reference.html)
* [Inspector window reference](UsingTheInspector.html)
* Assign icons to inspected items

Focus an Inspector window

Project window reference

# Assign icons to inspected items

Use the ****Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector)** window to assign an icon to the item you’re inspecting. The icon appears in the ****Scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene)** view, making it easier to identify the item.

The icon’s behavior in the [Scene view](UsingTheSceneView.html)An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView) depends on the item type:

* **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
  See in [Glossary](Glossary.html#GameObject): The icon appears over that GameObject, and any duplicates.
* **Prefab**An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](Prefabs.html)  
  See in [Glossary](Glossary.html#prefab): The icon appears over any instances of that prefab.
* Script: The icon appears over any GameObject that has the script attached.

To control how Unity draws custom icons in the **Scene** view, use the [Gizmos menu](GizmosMenu.html).

**Note:** When you change an asset’s icon, Unity marks the asset as modified, and **version control**A system for managing file changes. You can use Unity in conjunction with most common version control tools, including Perforce, Git, Mercurial and Unity Version Control (UVCS). [More info](VersionControl.html)  
See in [Glossary](Glossary.html#versioncontrol) systems register the change.

### Icon types

The Unity Editor supports three icons types.

| **Icon type** | **Description** |
| --- | --- |
| **Label icons** | Colored capsules that show the item’s name. |
| **Image only icons** | Colored circles. They’re useful for objects that don’t have a visual representation such as waypoints. |
| **Custom icons** (other) | An icon based on an asset in the project. For example, use a skull and crossbones icon to indicate danger areas in a game level. |

## Manage icons in the **Inspector** window

To add icons, in the **Inspector** window, select **Select icon**. Then:

* To assign an icon to a GameObject or a script, do one of the following:
  + To assign a label or image icon, click any icon from the list.
  + To assign a custom icon, select **Other…** and select a texture.
* To assign an icon to a prefab, open the prefab in [prefab editing mode](EditingInPrefabMode.html).

To replace or remove icons, in the **Inspector** window, select **Select icon**. Then:

* To replace the icon, select any other icon from the list.
* To remove the icon, select **None**. The item’s icon reverts to the default Unity icon.

## Additional resources

* [Using the Scene view](UsingTheSceneView.html)
* [Gizmos menu](GizmosMenu.html)
* [Edit prefab assets](EditingInPrefabMode.html)

Focus an Inspector window

Project window reference

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
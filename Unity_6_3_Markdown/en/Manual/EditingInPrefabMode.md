* [GameObjects](working-with-gameobjects.html)
* [Prefabs](Prefabs.html)
* Edit prefab assets

Create prefabs

Nest prefab instances in other prefabs

# Edit prefab assets

To edit **prefab**An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](Prefabs.html)  
See in [Glossary](Glossary.html#prefab) assets, you can open them in an isolated editing mode which allows you to view and edit the contents of the prefab asset separately from any other **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) in the **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). Changes that you make in prefab editing mode affect all instances of that prefab.

## Open a prefab asset in prefab editing mode

You can open a prefab asset in prefab editing mode in the following ways:

* **In isolation:** Unity hides the rest of the current working scene, and displays only the GameObjects that relate to the prefab asset in the Hierarchy.
* **In context:** The rest of the current working scene remains visible, but locked for editing. The Hierarchy displays only the GameObjects that relate to the prefab asset.

When you open prefab editing mode either in context or in isolation, the **Scene view**An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView) displays only the contents of that prefab. At the top of the Scene view, a breadcrumb bar displays the name of the open prefab asset. You can use this bar to navigate back to the main scene or other prefab assets you might have open.

The Hierarchy window displays a bar at the top which shows the currently open prefab. You can use the back arrow in the header bar to navigate back one step, which is equivalent to clicking the previous breadcrumb in the bar in the Scene view.

![The Scene view and Hierarchy, with prefab editing mode in isolation. The prefab breadcrumb bar is highlighted.](../uploads/Main/prefabs-isolation-mode.png)


The Scene view and Hierarchy, with prefab editing mode in isolation. The prefab breadcrumb bar is highlighted.

### Open in isolation

To open a prefab asset and edit it in isolation, perform one of the following actions:

* Double-click the prefab asset in the **Project window**A window that shows the contents of your `Assets` folder (Project tab) [More info](ProjectView.html)  
  See in [Glossary](Glossary.html#Projectwindow).
* Select a prefab asset in the Project window. Select **Open** in the top right of the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
  See in [Glossary](Glossary.html#Inspector) window.

Unity then opens the prefab asset in isolation in prefab editing mode.

### Open in context

To open a prefab asset and edit it in context, perform one of the following actions:

* Select a prefab instance in the Hierarchy window. Select **Open** in the top right of the Inspector window.
* Select a prefab instance in the Hierarchy window and press **P** on the keyboard. This is the default [keyboard binding](ShortcutsManager.html).
* Select the arrow next to the prefab instance in the Hierarchy window.

Unity then opens the prefab asset in context in prefab editing mode.

By default, Unity opens prefab instances in context when you select **Open** from the Inspector. To open the prefab instance in isolation, hold down **Alt** (macOS: **Option**) and select **Open**.

To change the default behavior, perform the following steps:

1. Open the Preferences window: **Edit** > **Preferences** (macOS: **Unity** > **Settings**).
2. Go to **General** > **Hierarchy window** > **Default Prefab Mode**, and change the setting to **In Isolation**.

To open the prefab asset in context after adjusting the default behavior, select the prefab instance and press **P**. You can also set up custom shortcuts for editing prefabs in the [Shortcuts window](ShortcutsManager.html).

## Edit a prefab asset in isolation

By default, when you edit a prefab asset in isolation mode, Unity displays it in the default **skybox**A special type of Material used to represent skies. Usually six-sided. [More info](sky-landing.html)  
See in [Glossary](Glossary.html#Skybox), out of context of the scenes in your project. You can assign a scene as an editing environment if you prefer to edit prefab assets against a background related to your project. To change the default environment, perform the following steps:

1. Open the Editor Project Settings: **Edit** > **Project Settings** > **Editor**.
2. Under **Prefab Mode** > **Editing Environments**, select a scene for regular prefabs and UI prefabs. UI prefabs are defined as prefabs which have a [Rect Transform](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/class-RectTransform.html) component on the root, rather than a regular Transform component.

Unity only uses this editing environment when you open prefab editing mode in isolation.

## Edit a prefab asset in context

When you [open prefab editing mode in context](#open-in-context), by default Unity grays out the rest of the context of the scene.

![The Scene view and Hierarchy with prefab editing mode in context, and the Context set to Gray. The prefab options are highlighted.](../uploads/Main/prefab-mode-context-grey.png)


The Scene view and Hierarchy with prefab editing mode in context, and the **Context** set to **Gray**. The prefab options are highlighted.

To change this view, select one of the **Context** options in the bar at the top of the Scene view:

* **Normal**: Displays the prefab in context with the rest of the scene in its regular colors.
* **Gray**: Displays the prefab in context with the rest of the scene in gray.
* **Hidden**: Displays the prefab in context with the rest of the scene hidden.

You can’t select any other GameObjects that are in the rest of the scene, so you can only focus on editing the prefab. When **Context** is set to anything other than **Hidden**, you can continue to use Unity’s snapping features to snap any GameObjects that are part of the prefab to the scene.

### Editing prefab properties

Unity displays the prefab contents at a position that matches that of the prefab instance it was opened through. This means that you might preview the **root transform**The Transform at the top of a hierarchy of Transforms. In a Prefab, the Root Transform is the topmost Transform in the Prefab. In an animated humanoid character, the Root Transform is a projection on the Y plane of the Body Transform and is computed at run time. At every frame, a change in the Root Transform is computed, and then this is applied to the GameObject to make it move. [More info](RootMotion.html)  
See in [Glossary](Glossary.html#RootTransform) of the prefab contents with different position and rotation values than the prefab asset actually has.

**Important**: You can’t edit the **Transform** values while prefab editing mode is open in context. You must [open the prefab in isolation](#open-in-isolation) to edit these values.

To visualize the [overrides on the main prefab asset](PrefabInstanceOverrides.html), select the **Show Overrides** setting in the top bar of the Scene view. Disable this option to view the default properties of the prefab asset.

## Automatically save edits to the prefab asset

To automatically save any changes you make to the prefab asset, select **Auto Save** in the top right of the Scene view, while in prefab editing mode. You can disable this option if editing a complex prefab is slow. Unity then displays a dialog asking if you want to save the prefab asset when you exit prefab editing mode.

You can disable **Auto Save** completely and remove the option from prefab editing mode. To do this:

1. Open the Editor Project Settings: **Edit** > **Project Settings** > **Editor**.
2. Under **Prefab Mode**, disable the **Allow Auto Save** setting.

## Additional resources

* [Create prefabs](CreatingPrefabs.html)
* [Create variations of prefabs](PrefabVariants.html)
* [Override prefab instances](PrefabInstanceOverrides.html)

Create prefabs

Nest prefab instances in other prefabs

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
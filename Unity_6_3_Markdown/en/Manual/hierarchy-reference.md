* [Unity Editor interface](unity-editor.html)
* [Unity Editor windows and views reference](editor-windows-views-reference.html)
* [The Hierarchy window](hierarchy-window.html)
* Hierarchy window reference

Manage GameObjects in the Hierarchy window

Scene view reference

# Hierarchy window reference

Explore the settings and functions in the Hierarchy window to view and organize objects in your **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).

The Hierarchy window displays every [GameObject](GameObjects.html)The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) in a scene, including models, cameras, and [prefabs](Prefabs.html)An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](Prefabs.html)  
See in [Glossary](Glossary.html#prefab). You can use the Hierarchy window to manage and group the GameObjects you use in a scene. When you add or remove GameObjects in the Scene view, you also add or remove them from the Hierarchy window.

For more information about creating and organizing items in the Hierarchy window, refer to [Manage GameObjects in the Hierarchy window](Hierachy).

## Icons in the Hierarchy window

Icons in the Hierarchy window indicate the type, visibility, and pickability of items in your scene.

### GameObject icons in the Hierarchy

The icons next to the GameObject name indicate whether the item is a basic GameObject or a prefab, and whether a prefab has been modified from its original values.

You can identify the following types of items using the icons in the Hierarchy window.

| Item | Icon | Description |
| --- | --- | --- |
| GameObject | The icon for a GameObject is an outline of a cube. | The foundational building blocks of all items in a scene. GameObjects are containers for components, which provide functionality.   For more information, refer to [Introduction to GameObjects](GameObjects.html) |
| Prefab | The icon for a prefab is a blue cube. | Prefabs are assets that act as a template for specific items in your scene. When you edit a prefab asset, updates are applied to all instances of that asset that appear in your scene.   For more information, refer to [Introduction to prefabs](Prefabs.html). |
| Prefab variant | The icon for a prefab variant is a blue cube with one side shaded gray. | A prefab variant is a prefab asset that inherits some properties from a different prefab asset, while others properties have new values. Essentially, it’s a new prefab that’s based on an original, base prefab with some changes, or overrides. Editing the base prefab also edits the variant, except for properties that are already changed in the variant.   For more information, refer to [Create variations of prefabs](PrefabVariants.html). |
| Prefab model | The icon for a prefab model is a blue cube with one side gray and a line cut into the top. | Prefab models are prefabs that are imported from other digital content creation (DCC) software. Prefab models can contain skeletons, materials, meshes, animations, and more. |

### Scene visibility icons

The scene visibility status controls whether the GameObject is hidden or displayed in the **Scene view**An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView). You can toggle visibility on and off using the status indicator at the edge of the Hierarchy window. For more information, refer to [Scene visibility](SceneVisibility.html).

The following visibility states are available.

| State | Icon | Description |
| --- | --- | --- |
| Visible | The icon for a visible GameObject is an eye. | The GameObject and all its children are visible in the scene. This is the default status for a new GameObject. This status icon is visible only when you hover over the GameObject. |
| Hidden | The icon for a hidden GameObject is an eye with a strikethrough. | The GameObject and all its children are hidden in the scene. |
| Visible parent | The icon for a visible parent GameObject is an eye with a dot underneath the right corner. | The GameObject is visible in the scene, but one of more of its children are hidden. |
| Hidden parent | The icon for a hidden parent GameObject is an eye with a dot underneath the right corner and a strikethrough. | The GameObject is hidden in the scene, but one of more of its children are visible. |

### Scene pickability icons

The scene pickability status controls whether you can select the GameObject in the Scene view. You can toggle pickability on and off using the status indicator at the edge of the Hierarchy window. For more information, refer to [Scene picking controls](ScenePickingControls.html).

The following pickability states are available.

| State | Icon | Description |
| --- | --- | --- |
| Pickable | The icon for a pickable GameObject is a hand with pointing finger. | You can select the GameObject, and any of its children, in the Scene view. This is the default status for a new GameObject. This status icon is visible only when you hover over the GameObject. |
| Not pickable | The icon for a not pickable GameObject is hand with pointing finger with a strikethrough. | You can’t select the GameObject, or any of its children, in the Scene view. |
| Pickable parent | The icon for a pickable parent GameObject is hand with pointing finger with a dot underneath the right corner. | You can select the GameObject in the Scene view, but you can’t select one or more of its children. |
| Not pickable parent | The icon for a not pickable parent GameObject is a hand with pointing finger with a dot underneath the right corner and a strikethrough. | You can’t select the GameObject in the Scene view, but you can select one or more of its children. |

## New Hierarchy

Enable the [**New Hierarchy** setting](preferences-general.html) in the Preferences window (**Edit** > **Preferences** (macOS: **Unity > Settings**) > **General**) to change the view of the Hierarchy window. This view displays extra information about the GameObjects in your scene such as their [layers](Layers.html)Layers in Unity can be used to selectively opt groups of GameObjects in or out of certain processes or calculations. This includes camera rendering, lighting, physics collisions, or custom calculations in your own code. [More info](Layers.html)  
See in [Glossary](Glossary.html#layer) and [tags](Tags.html)  
See in [Glossary](Glossary.html#tag), and optionally highlights each alternate row for easier navigation of items.

**Important**: The **New Hierarchy** setting is in preview and might change in future versions of Unity.

![New Hierarchy window setting enabled. The Hierarchy window has columns with additional information about the objects in the scene.](../uploads/Main/hierarchy-window-new.png)


New Hierarchy window setting enabled. The Hierarchy window has columns with additional information about the objects in the scene.

Right-click on the header row of the Hierarchy window to customize the information displayed:

| **Option** | **Description** |
| --- | --- |
| **Resize to Fit** | Resizes the columns to fit the width of the Hierarchy window. |
| **Visibility** | Displays a column to control the [scene visibility status](#scene-visibility-icons) of the GameObject. |
| **Picking** | Displays a column to control the [scene pickability status](#scene-pickability-icons) of the GameObject. |
| **Active** | Displays a column to control the [active status](class-GameObject.html#active-status) of the GameObject. |
| **Static** | Displays a column to control the [static status](class-GameObject.html#static-status) of the GameObject. |
| **Layer** | Displays a column to view and control the [layer](Layers.html) assigned to the GameObject. Use the dropdown menu to assign a new layer to the GameObject. |
| **Tag** | Displays a column to view and control the [tags](Tags.html) assigned to the GameObject. Use the dropdown menu to assign a new tag to the GameObject. |
| **Reset Columns** | Resets the Hierarchy window to the default columns, which are **Picking**, **Active**, and **Name**. |

Unity displays only the values that are different from the default in each column.

## Override indicators

When you edit a prefab instance in a scene, Unity displays an indicator next to the parent GameObject in the Hierarchy window. This indicator highlights any prefab that has non-default override values in any of its child GameObjects. To open the [Overrides dropdown](prefab-instance-inspector-reference.html) directly from the Hierarchy window, select the override indicator. The override indicator appears as a blue line in the left side of the margin and is identical to the instance override in the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window. For more information, refer to [Override prefab instances](PrefabInstanceOverrides.html).

![The override indicator is displayed next to prefab A when its child, GameObject C, has a value in a non-default state.](../uploads/Main/hierarchy-override-indicator.png)


The override indicator is displayed next to prefab A when its child, GameObject C, has a value in a non-default state.

Any objects that are added to the instance have a plus badge on their icons.

![The Hierarchy window showing a Prefab instance with a child prefab instance called Banana added as an override.](../uploads/Main/prefab-instance-hierarchy-override.png)


The Hierarchy window showing a Prefab instance with a child prefab instance called Banana added as an override.

## Additional resources

* [Manage GameObjects in the Hierarchy window](Hierarchy.html)
* [Scene visibility](SceneVisibility.html)
* [Scene picking controls](ScenePickingControls.html)
* [Override prefab instances](PrefabInstanceOverrides.html)

Manage GameObjects in the Hierarchy window

Scene view reference

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
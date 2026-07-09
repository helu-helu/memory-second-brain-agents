* [Unity Editor interface](unity-editor.html)
* [Unity Editor windows and views reference](editor-windows-views-reference.html)
* [Gizmos and handles](gizmos-and-handles.html)
* Gizmos introduction

Gizmos and handles

Gizmos menu reference

# Gizmos introduction

Gizmos are graphics associated with GameObjects in the **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). Some **gizmos**A graphic overlay associated with a GameObject in a Scene, and displayed in the Scene View. Built-in scene tools such as the move tool are Gizmos, and you can create custom Gizmos using textures or scripting. Some Gizmos are only drawn when the GameObject is selected, while other Gizmos are drawn by the Editor regardless of which GameObjects are selected. [More info](GizmosMenu.html#GizmosIcons)  
See in [Glossary](Glossary.html#Gizmo) are only drawn when the **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) is selected, while other gizmos are drawn by the Unity Editor regardless of which GameObjects are selected. They are usually wireframes, drawn with code rather than bitmap graphics, and can be interactive.

The ****Camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera)** gizmo and **Light direction** gizmo are both examples of built-in gizmos. You can also create your own Gizmos using script. Refer to [Introduction to the camera view](UnderstandingFrustum.html) for more information about the camera.

Some gizmos are passive graphical overlays, shown for reference (such as the **Light direction** gizmo, which shows the direction of the light). Other gizmos are interactive, such as the [audio source](class-AudioSource.html)A component which plays back an Audio Clip in the scene to an audio listener or through an audio mixer. [More info](class-AudioSource.html)  
See in [Glossary](Glossary.html#AudioSource) **spherical range** gizmo, which you can click and drag to adjust the maximum range of the audio source.

The **Move**, **Scale**, **Rotate** and **Transform** tools are also interactive gizmos. Refer to [Positioning GameObjects](PositioningGameObjects.html) to learn more about these tools.

![The camera gizmo and a light gizmo. These gizmos are only visible when they are selected.](../uploads/Main/IconAndGizmoForLightAndCamera.png)


The camera gizmo and a light gizmo. These gizmos are only visible when they are selected.

Refer to the [`OnDrawGizmos`](../ScriptReference/MonoBehaviour.OnDrawGizmos.html) method for further information about implementing custom Gizmos in your **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts).

## Icons

You can display icons in the Game view or **Scene view**An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView) as flat, billboard-style overlays. These help indicate a GameObject’s position while you work on your game. The Camera icon and Light icon are examples of built-in icons. You can also assign custom icons to GameObjects or individual scripts. For more information, refer to [Assigning Icons](InspectorAssignIcons.html).

![The built-in icons for a Camera and a Light](../uploads/Main/GizmosMenu2.png)


The built-in icons for a Camera and a Light


![Left: icons in 3D mode. Right: icons in 2D mode.](../uploads/Main/GizmoMenu2Dvs3Dicons.png)


**Left**: icons in 3D mode. **Right**: icons in 2D mode.

## Selection wireframes

Unity provides visual feedback when you select GameObjects in the Scene view through selection outlines and wireframes. These visual indicators help you identify selected objects and understand their hierarchy relationships at a glance.

### Selection Outline

When **Selection Outline** is enabled, an outline appears around selected GameObjects and their child GameObjects. By default, Unity outlines selected GameObjects in orange, and child GameObjects in blue. You can change these colors in the [Unity Preferences window](#SelectionColors).

![Selecting a GameObject (the far left box) outlines it in orange, and outlines its child GameObjects (the middle and right boxes) in blue.](../uploads/Main/GameObjectSelectedOutline.jpg)


Selecting a GameObject (the far left box) outlines it in orange, and outlines its child GameObjects (the middle and right boxes) in blue.

When you select a GameObject, Unity outlines all its child GameObjects (and their child GameObjects), but doesn’t outline parent GameObjects (or their parent GameObjects).

![Selecting the middle box highlights it in orange, and highlights its child GameObject (the far right box) in blue, but doesnt highlight its parent GameObject (the far left box).](../uploads/Main/GameObjectSelectedOutlineParentChild.jpg)


Selecting the middle box highlights it in orange, and highlights its child GameObject (the far right box) in blue, but doesn’t highlight its parent GameObject (the far left box).

If selected GameObjects extend beyond the edges of the Scene view, the selection outline runs along the edge of the window:

![The selection outline along the edge of the window, when the GameObject you selected extends beyond the Scene view](../uploads/Main/GameObjectSelectedBeyondEdges.png)


The selection outline along the edge of the window, when the GameObject you selected extends beyond the Scene view

### Selection Wire

When **Selection Wire** is enabled, then when you select a GameObject in the Scene view or Hierarchy window, the wireframe **Mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) for that GameObject is made visible in the Scene view:

![The wireframe visible on a mesh](../uploads/Main/GameObjectSelectedWire.png)


The wireframe visible on a mesh

### Selection colors

You can set custom colors for selection wireframes.

1. Go to **Unity** > **Settings** (macOS) or **Edit** > **Preferences** (Windows) to open the [Preferences](Preferences.html) window.
2. On the colors tab, change one or more of the following colors:
   * **Selected Children Outline**: outline color for selected GameObjects’ children.
   * **Selected Outline**: outline color for selected GameObjects.
   * **Wireframe Selected**: outline color for selected GameObjects’ wireframes.

## Built-in components, scripts, and recently changed items

Use the list in the **Gizmos** menu to control the visibility of icons and gizmos for various components. The list is divided into sections:

![The Gizmos menu, displaying items with custom icons and some recently modified items](../uploads/Main/GizmosMenuAll.png)


The Gizmos menu, displaying items with custom icons and some recently modified items

### Recently Changed

The **Recently Changed** section controls the visibility of the icons and gizmos for items that you’ve modified recently. It appears the first time you change one or more items. Unity updates the list after subsequent changes.

### Scripts

The **Scripts** section controls the visibility of the icons and gizmos for scripts that:

* Have an icon assigned to them (see documentation on [Assigning Icons](InspectorAssignIcons.html)).
* Implement the [OnDrawGizmos](../ScriptReference/MonoBehaviour.OnDrawGizmos.html) function.
* Implement the [OnDrawGizmosSelected](../ScriptReference/MonoBehaviour.OnDrawGizmosSelected.html) function.

This section appears when your Scene contains one or more scripts that meet the above criteria.

### Built-in Components

The **Built-in Components** section controls the visibility of the icons and gizmos for all component types that have an icon or gizmo.

Built-in component types that do not have an icon or gizmo shown in the Scene view (for example, Rigidbody) are not listed here.

### Toggling icon visibility

The **icon** column shows or hides the icons for each component type. Full-color icons are displayed in the main Scene view window, faded icons are not.

![The Light icon is faded, indicating that the Editor does not display light icons in the Scene view. The Camera icon is full-color, indicating that the Editor does display camera icons in the Scene view.](../uploads/Main/gizmos-icon.png)


The **Light** icon is faded, indicating that the Editor does not display light icons in the Scene view. The **Camera** icon is full-color, indicating that the Editor does display camera icons in the Scene view.

To toggle an icon’s visibility in the Scene view, click any icon in the **icon** column.

**Note:** If an item in the list has a gizmo but no icon, the **icon** column for that item is empty.

### Changing script icons

Scripts with custom icons show a small drop-down menu arrow in the **icon** column. To change a custom icon, click the arrow to open the [Select Icon](InspectorAssignIcons.html) menu.

![The Select Icon menu for script](../uploads/Main/GizmosMenuIconsMenu.png)


The Select Icon menu for script

### Toggling gizmo visibility

To control whether the Editor draws gizmo graphics for a particular component type (for example, a **Collider’s** wireframe gizmo or a **Camera’s** [view frustum](UnderstandingFrustum.html) gizmo) or script, use the checkboxes in the **Gizmo** column.

* When a checkbox is checked, the Editor draws gizmos for that component type.
* When a checkbox is cleared, the Editor does not draw gizmos for that component type.

**Note:** If an item in the list has an icon but no gizmo, the **Gizmo** column for that item is empty.

To toggle gizmo visibility for an entire section (all **Built-in Components**, all **Scripts**, and so on), use the checkboxes next to the section names.

The **Built-in Components** checkbox toggles gizmo visibility for every type of component listed in that section

When the checkbox is toggled on, gizmo visibility is toggled on for one or more item types in the section.

## Additional resources

* [Programming with gizmos and handles](gizmos-handles-programming.html)
* [Gizmos menu reference](GizmosMenu.html)

Gizmos and handles

Gizmos menu reference

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
* [GameObjects](working-with-gameobjects.html)
* [Prefabs](Prefabs.html)
* Create prefabs

Introduction to prefabs

Edit prefab assets

# Create prefabs

To create and use **prefabs**An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](Prefabs.html)  
See in [Glossary](Glossary.html#prefab) in your project, you must do the following:

1. [Create a prefab asset](#create-a-prefab-asset).
2. [Create an instance of the prefab asset](#create-an-instance-of-a-prefab).

## Create a prefab asset

To create a prefab asset, perform the following steps:

1. Create a [GameObject](GameObjects.html)The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
   See in [Glossary](Glossary.html#GameObject) and configure its position, scale, rotation, components, and other properties as needed.
2. Drag the GameObject into the `Assets` folder in the [Project window](ProjectView.html)A window that shows the contents of your `Assets` folder (Project tab) [More info](ProjectView.html)  
   See in [Glossary](Glossary.html#Projectwindow). You can optionally select more than one GameObject to create multiple prefab assets.

Unity then creates a prefab asset from the GameObject, all its components, and child GameObjects. The original GameObject becomes an instance of the newly created prefab asset.

![A GameObject named Health Pack in the left window. After dragging the GameObject into a child folder of the Assets folder, the Health Pack object is saved as a .prefab file, and the original GameObject becomes an instance of the prefab asset. The Inspector displays details of the Health Pack prefab asset.](../uploads/Main/prefab-workflow.png)


A GameObject named Health Pack in the left window. After dragging the GameObject into a child folder of the `Assets` folder, the Health Pack object is saved as a .prefab file, and the original GameObject becomes an instance of the prefab asset. The Inspector displays details of the Health Pack prefab asset.

If you drag multiple GameObjects that aren’t already prefabs into the Project window, Unity creates new prefab assets for each one without any additional steps. However, if any of the GameObjects are existing prefabs or [prefab variants](PrefabVariants.html), Unity displays a dialog which asks you to confirm whether you want to create new prefab assets or new variants from the GameObjects.

### Replace a prefab asset

You can replace a prefab asset with a GameObject or [prefab instance](#create-an-instance-of-a-prefab) that’s in the [Hierarchy window](Hierarchy.html). To replace a prefab asset:

1. Select the GameObject or prefab in the Hierarchy window.
2. Drag it on top of an existing prefab asset in the Project window.

If the contents of the GameObject or prefab instance differ from the prefab asset, then Unity displays a dialog to confirm that you intend to replace the prefab asset.

Unity tries to preserve references to the prefab and the individual parts of the prefab such as child GameObjects and components. To do this, it matches the names of GameObjects between the new prefab and the existing prefab that you’re replacing.

Because Unity performs this matching by name only, if there are multiple GameObjects with the same name in the prefab asset’s hierarchy, the matching is unpredictable. Therefore, to ensure Unity preserves the references when saving over an existing prefab, make sure all GameObjects within the prefab have unique names.

Unity behaves in a similar way if a GameObject has more than one of the same type of component attached to it.

## Create an instance of a prefab

To create an instance of a prefab asset:

1. Select the prefab asset in the Project window.
2. Drag the prefab asset into the Hierarchy or **Scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
   See in [Glossary](Glossary.html#Scene) view.

You can also create instances of prefabs at runtime using scripting. For more information, refer to [Instantiating prefabs](instantiating-prefabs.html).

### Replace a prefab instance’s prefab asset

You can replace a prefab instance’s parent prefab asset, while retaining the instance’s position, rotation, and scale. Unity merges the contents of the new prefab asset and preserves any overrides and references via name-based matching.

You can replace a prefab asset in the following ways:

* In the [Inspector for the prefab instance](prefab-instance-inspector-reference.html):
  1. Drag a prefab asset from the Project window into the **Prefab** field in the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
     See in [Glossary](Glossary.html#Inspector).
  2. If the prefab has any [overrides](prefabs-override.html), Unity displays a context menu and you can choose to either **Replace and Keep Overrides** to preserve any overrides, or **Replace** and discard any overrides.
* In the Hierarchy window:
  1. Right-click on a prefab instance or GameObject.
  2. Select **Prefab** > **Replace**, or **Replace and Keep Overrides** to preserve overrides.
  3. A **Select GameObject** window appears and you can choose the prefab asset you want to replace it with.
* In the Project window:
  1. Hold down Ctrl (macOS: Command) and drag a prefab asset onto a prefab instance or GameObject in the Hierarchy.
  2. In the context menu, select **Replace**, or **Replace and Keep Overrides** to preserve overrides.

You can also use the [`PrefabUtility.ReplacePrefabAssetOfPrefabInstance`](../ScriptReference/PrefabUtility.ReplacePrefabAssetOfPrefabInstance.html) method to control this behavior in your **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts).

## Additional resources

* [Edit prefab assets](EditingInPrefabMode.html)
* [Nest prefab instances in other prefabs](NestedPrefabs.html)
* [Create variations of prefabs](PrefabVariants.html)

Introduction to prefabs

Edit prefab assets

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
* [World building](CreatingEnvironments.html)
* [Terrain](script-Terrain.html)
* [Trees](terrain-Trees-Landing.html)
* [Import trees from SpeedTree](SpeedTree-landing.html)
* SpeedTree Import Settings

SpeedTree model import

SpeedTree Model tab reference

# SpeedTree Import Settings

[Switch to Scripting](../ScriptReference/SpeedTreeImporter.html "Go to SpeedTreeImporter page in the Scripting Reference")

When you put SpeedTree files in the Assets folder of your Unity project, the Unity Editor automatically imports and stores them as Unity assets.

SpeedTree import settings are specific to files for models created in [SpeedTree](SpeedTree.html). For information on models and animation created in other 3D modeling applications, refer to the [Model Import Settings](class-FBXImporter.html) window.

## Importing SpeedTree files to Unity

Unity recognizes and imports SpeedTree model assets in the same way it handles other assets. If you’re using SpeedTree Modeler 7, re-save your .spm files using the Unity version of the Modeler. If you’re using SpeedTree Modeler 8, 9, or 10, you can save your .st or .st9 files directly into the Unity project folder.

The SpeedTree Importer generates a **prefab**An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](Prefabs.html)  
See in [Glossary](Glossary.html#prefab) with the [LOD Group](class-LODGroup.html)A component to manage level of detail (LOD) for GameObjects. [More info](class-LODGroup.html)  
See in [Glossary](Glossary.html#LODGroup) component configured. You can instantiate the prefab in a **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) as a common prefab instance, or select the prefab as a tree prototype and then paint it across the **terrain**The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](terrain-UsingTerrains.html)  
See in [Glossary](Glossary.html#Terrain).

### Wind settings

When you import an .st9 file to the Unity Editor, you can select the correct Wind algorithm to use for the new Unity asset.

### Materials

By default, Unity imports SpeedTree model materials as sub-assets. If you want to make adjustments to the materials, you can extract them to a location of your choice or re-use existing materials with Material Remapping.

## SpeedTree Import window

You can customize import settings from the SpeedTree Import window:

![The SpeedTree Import Settings window](../uploads/Main/class-SpeedTreeImporter.png)


The SpeedTree Import Settings window

### View import settings

To view the import settings in the ****Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector)** window, select the file in the **Project** window.

### Customize how Unity imports the file

To customize how Unity imports the selected file, use the properties on the **Model**, **Materials**, and **Wind** tabs on this window.

For more information about settings you can use to customize how Unity imports a SpeedTree model, see the following topics:

| **Topic** | **Description** |
| --- | --- |
| **[Model tab](SpeedTreeImporter-Model.html)** | Understand the options in the Model tab of the SpeedTree Import Settings window. |
| **[Materials tab](SpeedTreeImporter-Materials.html)** | Understand the options in the Materials tab of the SpeedTree Import Settings window. |

SpeedTree model import

SpeedTree Model tab reference

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
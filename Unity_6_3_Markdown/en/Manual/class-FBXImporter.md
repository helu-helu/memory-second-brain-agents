* [Assets and media](assets-and-media.html)
* [Types of assets](AssetTypes.html)
* [Models](models.html)
* [Importing models into Unity](models-importing.html)
* Model Import Settings reference

Importing a model with non-humanoid (generic) animations

Model tab Import Settings reference

# Model Import Settings reference

To open a model’s Import Settings, select the model from the [Project window](ProjectView.html)A window that shows the contents of your `Assets` folder (Project tab) [More info](ProjectView.html)  
See in [Glossary](Glossary.html#Projectwindow). The [Inspector](UsingTheInspector.html)A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) then displays the Import Settings for the selected model.

![The Import Settings window](../uploads/Main/model-import-settings.png)


The Import Settings window

**Note:** These settings are for importing models and animations created in most 3D modeling applications. However, models created in SketchUp and SpeedTree use specialized settings. For more information, refer to [SketchUp Import Settings](class-SketchUpImporter.html), and [SpeedTree Import Settings](class-SpeedTreeImporter.html).

You can customize how Unity imports the selected file by setting the properties in the following tabs:

## Model

Contains settings for 3D models, which can represent a character, a building, or a piece of furniture. In these cases, Unity creates multiple assets from a single **model file**A file containing a 3D data, which may include definitions for meshes, bones, animation, materials and textures. [More info](3D-formats.html)  
See in [Glossary](Glossary.html#modelfile). In the Project window, the main imported object is a model [prefab](Prefabs.html)An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](Prefabs.html)  
See in [Glossary](Glossary.html#prefab). Usually there are also several **mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) objects that the model prefab references.

For more information, refer to [Model Import Settings reference](FBXImporter-Model.html).

## Rig

Contains settings for rigs (sometimes called skeletons). A rig includes a set of deformers arranged in a hierarchy that animate a mesh (sometimes called skin) on one or more models created in a 3D modeling application such as Autodesk 3ds Max or Autodesk Maya. For humanoid and generic (non-humanoid) models, Unity creates an **avatar**An interface for retargeting animation from one rig to another. [More info](ConfiguringtheAvatar.html)  
See in [Glossary](Glossary.html#Avatar) to reconcile the imported rig with the Unity **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject).

For more information, refer to [Rig Import Settings reference](FBXImporter-Rig.html).

## Animation

Contains settings for animation clips. You can define any series of different poses that happen over a set of frames, such as walking, running, or idling as an **animation clip**Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](class-AnimationClip.html)  
See in [Glossary](Glossary.html#AnimationClip). You can reuse clips for any model that has an identical rig. Often a single file contains several different actions, each of which you can define as a specific animation clip.

For more information, refer to [Animation Import Settings reference](class-AnimationClip.html).

## Materials

Contains settings for the materials and textures in your model. You can extract materials and textures or leave them embedded within the model. You can also adjust how materials are mapped in the model.

For more information, refer to [Materials Import Settings reference](FBXImporter-Materials.html).

## Additional resources

* [Model import workflows](ImportingModelFiles.html)
* [Model file formats](3D-formats.html)

Importing a model with non-humanoid (generic) animations

Model tab Import Settings reference

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
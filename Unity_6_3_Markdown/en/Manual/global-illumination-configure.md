* [Lighting](LightingOverview.html)
* [Direct and indirect lighting](direct-and-indirect-lighting.html)
* [Precalculating surface lighting with lightmaps](Lightmapping-landing.html)
* [Configuring lightmapping](configure-lightmapping-settings.html)
* Configure lightmapping with a Lighting Settings Asset

Configuring lightmapping

Change the fade distance of lights with fall-off

# Configure lightmapping with a Lighting Settings Asset

A Lighting Settings Asset represents a saved instance of the [LightingSettings](../ScriptReference/LightingSettings.html) class, which stores data for the Baked **Global Illumination**A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](Glossary.html#globalillumination) and the **Enlighten**A lighting system by Geomerics used in Unity for Enlighten Realtime Global Illumination. [More info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)  
See in [Glossary](Glossary.html#Enlighten) Realtime Global Illumination systems. The Unity Editor uses this data when it precomputes lighting data for a **Scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) that uses one or both of these systems.

You can assign the same Lighting Settings Asset or instance of the `LightingSettings` class to more than one Scene, which makes it easy to share Global Illumination system settings across multiple Scenes.

## Creating a Lighting Settings Asset

There are two ways to create a Lighting Settings Asset in the Unity Editor.

To create a Lighting Settings Asset from the Project view:

1. In the Project view, either click the add (+) button, or open the context menu and navigate to **Create**.
2. Click **Lighting Settings**. Unity creates a new Lighting Settings Asset in the Project view.

To create and automatically assign Lighting Settings Asset from the Lighting window:

1. Open the Lighting window (menu: **Window** > **Rendering** > **Lighting**).
2. Open the **Scene** tab.
3. Select **New**. Unity creates a new Lighting Settings Asset in the Project view, and immediately assigns it to the active Scene.

Select **Clone** instead to create a duplicate of the current Lighting Settings Asset, and immediately assign it to the active Scene.

You can also create a Lighting Settings Asset from a script. To do this, create an instance of the LightingSettings class and either save it to disk, or assign it to a Scene and save that Scene. For more information and code examples, see the [LightingSettings API documentation](../ScriptReference/LightingSettings.html).

## Assigning a Lighting Settings Asset to a Scene

To assign a Lighting Settings Asset to a Scene in the Unity Editor:

1. Open the Scene that you want to assign the Lighting Settings Asset to.
2. If you have more than one Scene open, ensure that the Scene that you want to assign the Lighting Settings Asset to is the [active Scene](MultiSceneEditing.html).
3. Open the Lighting window (menu: **Window** > **Rendering** > **Lighting**).
4. Open the **Scene** tab.
5. Either drag the Lighting Settings Asset to the **Lighting Settings** field, or click the icon to the right of the **Lighting Settings** field and choose the Lighting Settings Asset from the list.

You can also assign a Lighting Settings Asset to the active Scene from a script. To do this, load the Lighting Settings Asset to obtain an instance of the `LightingSettings` class, then use the `Lightmapping.lightingSettings` API to assign that `LightingSettings` instance to the active Scene. For more information and code examples, see the [LightingSettings API documentation](../ScriptReference/LightingSettings.html).

## Viewing and editing the properties of a Lighting Settings Asset

You can view and edit the properties of Lighting Settings Asset in two places in the Unity Editor:

* In the Project view, if you select a Lighting Settings Asset, you can view and edit its properties in the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
  See in [Glossary](Glossary.html#Inspector).
* If the active Scene has a Lighting Settings Asset assigned to it, you can view and edit the properties of that Lighting Settings Asset in the Lighting Window’s Scene tab.

You can also read from or write to the properties of a Lighting Settings Asset from a script. To do this, load the Lighting Settings Asset to obtain an instance of the`LightingSettings` class, and access its properties. For more information and code examples, see the [LightingSettings API documentation](../ScriptReference/LightingSettings.html).

## Default LightingSettings data

When a Scene does not have a Lighting Settings Asset assigned to it, Unity uses the default `LightingSettings` object for that Scene. The default `LightingSettings` object is an internal, read-only instance of the `LightingSettings` class.

You cannot make any changes to the `LightingSettings` data for a Scene that uses the default `LightingSettings`, but Unity can perform a bake using its settings.

To make changes to the `LightingSettings` data for a Scene, you must use the Unity Editor to create and assign a Lighting Settings Asset, or use a script to create, configure, and assign a `LightingSettings` object. For more information and code examples, see the [LightingSettings API documentation](../ScriptReference/LightingSettings.html).

Configuring lightmapping

Change the fade distance of lights with fall-off

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
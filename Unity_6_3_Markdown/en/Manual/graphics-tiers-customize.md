* [Render pipelines](render-pipelines.html)
* [Using the Built-In Render Pipeline](built-in-render-pipeline.html)
* [Graphics quality settings in the Built-In Render Pipeline](built-in-graphics-quality-settings.html)
* Configure graphics tiers in the Built-In Render Pipeline

Graphics tiers in the Built-In Render Pipeline

Rendering paths in the Built-In Render Pipeline

# Configure graphics tiers in the Built-In Render Pipeline

## Using graphics tiers with C# scripts

Unity stores the value of the current graphics tier in [Graphics.activeTier](../ScriptReference/Graphics-activeTier.html), represented by a [GraphicsTier](../ScriptReference/Rendering.GraphicsTier.html) enum. To add custom behavior based on the current graphics tier, you can test against this value.

To override the value of `Graphics.activeTier`, set it directly. Note that you must do this before Unity loads any **shaders**A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#shader) that vary based on graphics tier. A good place to set this value is in a pre-loading **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene), before you load your main scene.

## Tier settings

In the Unity Editor, you can configure **tier settings**. Tier settings allow you to enable or disable graphics features for each tier.

Tier settings work by changing `#define` preprocessor directives in Unity’s internal shader code. These changes automatically affect prebuilt shaders for the Built-in **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#renderpipeline) (such as the [Standard Shader](shader-StandardShader.html)), and the internal shader library code for [Surface Shaders](SL-SurfaceShaders.html)A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](SL-SurfaceShaders.html)  
See in [Glossary](Glossary.html#SurfaceShader). You can also add code to your own hand-coded shaders that changes their behavior based on tier settings. For more information, see [Graphics tiers and shader variants](graphics-tiers.html#shader-variants).

The default tier settings are suitable for most use cases. You should only change them if you are experiencing performance issues, or if you want to enable features on lower-end devices that are not enabled by default.

You can configure different tier settings for each graphics tier of a given build target. You can change tier settings in the following ways:

* Use the [Graphics Settings](class-GraphicsSettings.html) window, in the **Tier Settings** section.
* Use these APIs in an Editor script:
  + [EditorGraphicsSettings](../ScriptReference/Rendering.EditorGraphicsSettings.html)
  + [TierSettings](../ScriptReference/Rendering.TierSettings.html)

You can test tier settings in the Editor. To do this, navigate to **Edit > Graphics Tier** and choose the tier that you want the Unity Editor to use.

Graphics tiers in the Built-In Render Pipeline

Rendering paths in the Built-In Render Pipeline

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
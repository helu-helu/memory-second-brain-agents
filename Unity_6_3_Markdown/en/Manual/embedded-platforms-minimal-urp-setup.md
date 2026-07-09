* [Platform development](PlatformSpecific.html)
* [Embedded systems](embedded-systems.html)
* Create a minimal URP setup for embedded platforms

Command line arguments for logging

Embedded Linux

# Create a minimal URP setup for embedded platforms

Configure the Universal **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#renderpipeline) (URP) to simplify rendering and improve performance on embedded platforms.

Unity recommends the efficient and configurable Universal Render Pipeline (URP) for embedded platforms. By default, URP enables features that enhance visual quality but can be resource-intensive. On embedded platforms, you can adjust or disable these settings to achieve a minimal yet efficient setup.

Follow these steps to create a minimal rendering configuration and verify it with the [Render Graph Viewer](urp/render-graph-view.html).

## 1. Set up Quality settings

Use the same Quality settings on desktop as on embedded platforms during development:

1. Open the [**Quality**](class-QualitySettings.html) settings window (menu: **Edit** > **Project Settings** > **Quality**).
2. Identify the Quality level you want to use for embedded platforms.
3. In the Quality level matrix for each platform, select the platform column, then select the required quality level in the **Default** level dropdown.

You can remove the quality levels that you no longer need by unchecking the corresponding checkboxes in the Quality matrix.

This ensures that the desktop build uses the same default quality level as embedded platforms, indicated by the green check mark in the matrix.

## 2. Configure the URP Asset

Select the [URP Asset](urp/universalrp-asset.html) assigned to the quality level set for embedded platforms to view it the ****Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector)**, then apply the following settings:

### Quality settings

* Set **Render Scale** to `1.0`.
* Disable ****HDR**high dynamic range  
  See in [Glossary](Glossary.html#HDR)**.

## 3. Disable post-processing on the Renderer

To remove **post-processing**A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](Glossary.html#post-processing) effects from the build, disable post-processing on the Renderer:

1. Select the URP Asset.
2. In the **Inspector** window, find the **Renderer List** section, and then click the linked Renderer asset.
3. Under **Post-processing**, disable the **Enabled** toggle.

This excludes post-processing effects such as Bloom, **Tonemapping**The process of remapping HDR values of an image into a range suitable to be displayed on screen. [More info](PostProcessingOverview.html)  
See in [Glossary](Glossary.html#tonemapping), and Vignette from the build.

For more information, refer to [Universal Renderer asset reference](urp/urp-universal-renderer.html#post-processing).

## 4. Configure camera settings

Select each **camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) used in the minimal setup to view it in the **Inspector**, then configure the following settings:

* In the **Rendering** section, disable **Render Shadows**.
* In the **Environment** section, if a **skybox**A special type of Material used to represent skies. Usually six-sided. [More info](sky-landing.html)  
  See in [Glossary](Glossary.html#Skybox) isn’t required, set the **Background Type** to **Solid Color** and choose a background color.

For more information on these settings, refer to [Camera component reference](urp/camera-component-reference.html).

## 5. Verify the setup with the Render Graph Viewer

To verify the setup:

1. Open **Window** > **Analysis** > **Render Graph Viewer**.
2. Run the **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
   See in [Glossary](Glossary.html#Scene) with the camera that uses this setup.

The render graph displays only opaque, transparent, and UI draw passes with an optional skybox pass. The following image depicts the minimal URP configuration:

![Render Graph Viewer displaying minimal URP render passes](../uploads/Main/render-graph-viewer.png)


Render Graph Viewer displaying minimal URP render passes

**Note**: URP’s default lit **shaders**A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#shader) are typically more resource-intensive than simpler alternatives. For better performance on embedded platforms, use [unlit-type shaders](urp/shading-model.html#shaders-with-no-lighting) or [simple shaders](urp/shading-model.html#simple-shading) whenever possible.

## Additional resources

* [Universal Render Pipeline asset reference](urp/universalrp-asset.html)
* [Universal Renderer asset reference](urp/urp-universal-renderer.html)
* [Analyze a render graph](urp/render-graph-view.html)
* [Render Graph Viewer window reference](urp/render-graph-viewer-reference.html)

Command line arguments for logging

Embedded Linux

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
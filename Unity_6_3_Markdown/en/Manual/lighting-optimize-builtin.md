* [Lighting](LightingOverview.html)
* Optimize lighting in the Built-In Render Pipeline

Light component Inspector window reference for the Built-In-Render-Pipeline

Troubleshooting emissive materials not rendering

# Optimize lighting in the Built-In Render Pipeline

To optimize the lights in your **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene), avoid Unity using multiple render passes to render **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject), or doing too much work to render lighting. This reduces the number of the draw calls the CPU sends, and the number of vertices and **pixels**The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) the GPU processes.

Do the following:

* Use [lightmapping](Lightmapping-landing.html) to light static objects, instead of **realtime lights**Light components whose Mode property is set to Realtime. Unity calculates and updates the lighting of Realtime Lights every frame at runtime. No Realtime Lights are precomputed. [More info](LightModes-introduction.html#realtime)  
  See in [Glossary](Glossary.html#RealtimeLights).
* Avoid combining meshes if they’re lit by different realtime per-pixel lights, because Unity calculates every light for every combined **mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
  See in [Glossary](Glossary.html#Mesh).
* Avoid lighting GameObjects with multiple per-pixel lights.

## Prioritize lights

To avoid lighting GameObjects with multiple per-pixel lights, prioritize which lights provide per-pixel lighting based on which GameObjects they light.

For example, in a driving game, prioritize the car headlights as a per-pixel light, but deprioritize the rear lights and distant lampposts.

To decrease the number of per-pixel lights, do any of the following:

* In the [Light component Inspector window](class-Light.html), set **Render Mode** to **Not important**. This sets the light as a per-vertex light or spherical harmonics (SH) light.
* In the [Quality settings window](class-QualitySettings.html), decrease **Pixel Light Count**. This excludes lights from the per-pixel light group.

To increase the number of per-pixel lights, do any of the following:

* In the [Light component Inspector window](class-Light.html), increase the **Intensity**. The brightest light is always a per-pixel light.
* In the [Light component Inspector window](class-Light.html), set **Render Mode** to **Important**. This sets the light as a per-pixel light.
* In the [Quality settings window](class-QualitySettings.html), increase **Pixel Light Count**. This includes more lights in the per-pixel light group.

## Disable per-vertex and spherical harmonics (SH) lights

To disable per-vertex and SH lights in a custom **shader**A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#shader), add the `OnlyDirectional` tag to the Pass in your **ShaderLab**Unity’s language for defining the structure of Shader objects. [More info](SL-Shader.html)  
See in [Glossary](Glossary.html#ShaderLab) code. For more information, refer to [Pass tags in ShaderLab reference](SL-PassTags.html).

## Additional resources

* [Per-vertex and per-pixel lights](PerPixelLights.html)
* [Per-vertex and per-pixel lights in the Built-In Render Pipeline](PerPixelLights-BuiltIn.html)

Light component Inspector window reference for the Built-In-Render-Pipeline

Troubleshooting emissive materials not rendering

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
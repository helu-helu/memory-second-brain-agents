* [Lighting](LightingOverview.html)
* [Lighting in the Built-In Render Pipeline](lighting-birp.html)
* [Configure a GameObject to sample more Light Probes in the Built-In Render Pipeline](LightProbeProxyVolume-landing.html)
* Introduction to Light Probe Proxy Volumes in the Built-In Render Pipeline

Configure a GameObject to sample more Light Probes in the Built-In Render Pipeline

Set a GameObject to use a Light Probe Proxy Volume in the Built-In Render Pipeline

# Introduction to Light Probe Proxy Volumes in the Built-In Render Pipeline

[Switch to Scripting](../ScriptReference/LightProbeProxyVolume.html "Go to LightProbeProxyVolume page in the Scripting Reference")

The **Light Probe Proxy Volume** (LPPV) component allows you to use more lighting information for large dynamic **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) that cannot use baked **lightmaps**A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap) (for example, large Particle Systems or skinned Meshes).

By default, a probe-lit Renderer receives lighting from a single [Light Probe](LightProbes.html)Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe) that is interpolated between the surrounding Light Probes in the **Scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). Because of this, GameObjects have constant ambient lighting across the surface. This lighting has a rotational gradient because it is using spherical harmonics, but it lacks a spatial gradient. This is more noticeable on larger GameObjects or **Particle**A small, simple image or mesh that is emitted by a particle system. A particle system can display and move particles in great numbers to represent a fluid or amorphous entity. The effect of all the particles together creates the impression of the complete entity, such as smoke. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particle) Systems. The lighting across the GameObject matches the lighting at the anchor point, and if the GameObject straddles a lighting gradient, parts of the GameObject may look incorrect.

The **Light Probe Proxy Volume** component generates a 3D grid of interpolated Light Probes inside a **Bounding Volume**A closed shape representing the edges and faces of a collider or trigger.  
See in [Glossary](Glossary.html#boundingvolume). You can specify the resolution of this grid in the UI of the component. The spherical harmonics (SH) coefficients of the interpolated Light Probes are uploaded into 3D textures. The 3D textures containing SH coefficients are then sampled at render time to compute the contribution to the diffuse ambient lighting. This adds a spatial gradient to probe-lit GameObjects.

The [Standard Shader](shader-StandardShader.html) supports this feature. To add this to a custom **shader**A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#shader), use the `ShadeSHPerPixel` function. To learn how to implement this function, see the [Particle System sample Shader](#SampleShader) code example at the bottom of this page.

## Render pipeline support

See [render pipeline feature comparison](render-pipelines-feature-comparison.html) for more information about support for the Light Probe Proxy Volume component across **render pipelines**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#renderpipeline).

## Images for comparison

1. A simple **Mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
   See in [Glossary](Glossary.html#Mesh) Renderer using a Standard Shader:

   ![With Light Probe Proxy Volume (resolution: 4x1x1)](../uploads/Main/LightProbeProxyVolumeExample1.png)


   With Light Probe Proxy Volume (resolution: 4x1x1)


   ![Without Light Probe Proxy Volume](../uploads/Main/LightProbeProxyVolumeExample2.png)


   Without Light Probe Proxy Volume
2. A skinned **Mesh Renderer**A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](class-MeshRenderer.html)  
   See in [Glossary](Glossary.html#MeshRenderer) using a Standard Shader:

   ![With Light Probe Proxy Volume (resolution: 2x2x2)](../uploads/Main/LightProbeProxyVolumeExample3.png)


   With Light Probe Proxy Volume (resolution: 2x2x2)


   ![Without Light Probe Proxy Volume](../uploads/Main/LightProbeProxyVolumeExample4.png)


   Without Light Probe Proxy Volume

## Hardware requirements

The component requires at least Shader Model 4 graphics hardware and API support, including support for 3D Textures with 32-bit or 16-bit floating-point format and linear filtering.

To work correctly, the Scene needs to contain Light Probes via **Light Probe Group**A component that enables you to add Light Probes to GameObjects in your scene. [More info](class-LightProbeGroup.html)  
See in [Glossary](Glossary.html#LightProbeGroup) components. If a requirement is not fulfilled, the Renderer or Light Probe Proxy Volume component **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) displays a warning message.

LightProbeProxyVolume

Configure a GameObject to sample more Light Probes in the Built-In Render Pipeline

Set a GameObject to use a Light Probe Proxy Volume in the Built-In Render Pipeline

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
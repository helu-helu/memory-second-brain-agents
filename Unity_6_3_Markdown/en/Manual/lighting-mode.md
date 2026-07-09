* [Lighting](LightingOverview.html)
* [Light sources](lighting-light-sources.html)
* [Light components](lighting-light-components.html)
* [Configuring Light components](lighting-light-components-configuring.html)
* [Configuring Mixed lights with Lighting Modes](lighting-mode-landing.html)
* Lighting Mode

Configuring Mixed lights with Lighting Modes

Set the Lighting Mode of a scene

# Lighting Mode

To control the behaviour of all the lights in a **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) that have a **Light Mode**A Light property that defines the use of the Light. Can be set to Realtime, Baked and Mixed. [More info](LightModes.html)  
See in [Glossary](Glossary.html#LightMode) of Mixed, set the Lighting Mode in the [Lighting Settings Asset](class-LightingSettings.html).

There are four options for Lighting Mode, in order of visual fidelity:

* Distance **Shadowmask**A shadowmask texture uses the same UV layout and resolution as its corresponding lightmap texture. [More info](lighting-mode.html#shadowmask)  
  See in [Glossary](Glossary.html#Shadowmask) mode renders realistic lighting at a long distance, but has the most performance impact. You can use this mode for open worlds on high-end or mid-range platforms.
* Shadowmask mode is similar to **Distance Shadowmask**A version of the Shadowmask lighting mode that includes high quality shadows cast from static GameObjects onto dynamic GameObjects. [More info](lighting-mode.html#shadowmask)  
  See in [Glossary](Glossary.html#DistanceShadowmask) but has fewer real-time shadows and less performance impact.
* Baked Indirect mode renders realistic lighting and [realtime shadows](shadow-realtime.html).
* Subtractive mode renders simple lighting and low-fidelity shadows, but has a low performance impact. You can use this mode for low-end hardware, simple scenes with few lights, or stylized art such as cel shading.

For information about which **render pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#renderpipeline) supports which Lighting Mode, refer to [Render pipeline feature comparison reference](render-pipelines-feature-comparison.html#lighting).

## How Unity calculates lighting

The following table shows how Unity calculates lighting from Mixed lights for each Lighting Mode.

| **Lighting from Mixed lights** | **Baked Indirect Lighting Mode** | **Shadowmask Lighting Mode** | **Distance Shadowmask Lighting Mode** | **Subtractive Lighting Mode** |
| --- | --- | --- | --- | --- |
| Direct lighting | Real-time | Real-time | Real-time | Real-time for dynamic **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html) See in [Glossary](Glossary.html#GameObject), baked for static GameObjects. |
| Indirect lighting | Baked | Baked | Baked | Baked |
| Specular highlights | Yes | Yes | Yes | Dynamic GameObjects only |
| Shadows from dynamic GameObjects, up to [**Shadow Distance**](shadow-distance.html) | Real-time | Real-time | Real-time | Real-time, from the single highest-intensity Directional Light only |
| Shadows from static GameObjects, up to [**Shadow Distance**](shadow-distance.html) | Real-time | Baked, from a maximum of 4 lights per GameObject | Real-time | Baked, from a maximum of 4 lights per GameObject |
| Shadows from static GameObjects, beyond [**Shadow Distance**](shadow-distance.html) | No shadows | Baked, from a maximum of 4 lights per GameObject | Baked, from a maximum of 4 lights per GameObject | No shadows |

## Where Unity stores lighting data

Unity stores baked indirect lighting in the following places:

* **Light Probes**Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](LightProbes.html)  
  See in [Glossary](Glossary.html#LightProbe) store indirect lighting of dynamic GameObjects.
* **Lightmap**A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](Lightmapping.html)  
  See in [Glossary](Glossary.html#Lightmap) textures store indirect lighting of static GameObjects. In Subtractive mode, lightmap textures also store direct lighting.

Unity stores shadows in the following places:

* [Shadowmap textures](shadow-mapping.html) store real-time shadows, if the Lighting Mode supports them.
* Light Probes and shadow mask textures store baked shadows from static GameObjects, if the Lighting Mode supports them. In Subtractive mode, lightmaps store them instead.

![An example of a lightmap texture with shadows. The square area with yellow lines is the baked surface lighting of a plane. The white circle is a bright spot light, and the two black areas are shadows from other objects.](../uploads/Main/lightmap-with-shadows-example.jpg)


An example of a lightmap texture with shadows. The square area with yellow lines is the baked surface lighting of a plane. The white circle is a bright spot light, and the two black areas are shadows from other objects.

In Subtractive mode, real-time and baked shadows might not blend correctly, because lightmaps don’t contain enough data to calculate blending accurately. To improve blending, adjust the **Realtime Shadow Color** setting in the [Lighting window](lighting-window.html).

### Shadow mask textures

If you select Shadowmask mode or Distance Shadowmask mode, Unity creates shadow mask textures to store baked shadows for static GameObjects. Each shadow mask texture stores occlusion information about **baked lights**Light components whose Mode property is set to Baked. Unity pre-calculates the illumination from Baked Lights before runtime, and does not include them in any runtime lighting calculations. [More info](LightModes-introduction.html#baked)  
See in [Glossary](Glossary.html#bakedlights), and has the following characteristics:

* Uses the same UV layout and resolution as its corresponding lightmap texture.
* Stores up to four lights per texel, with each light stored in an RGBA channel.

![An example of a baked shadow mask texture. The square area with yellow lines represents a plane. The two grey areas are shadows.](../uploads/Main/baked-shadow-mask-example.jpg)


An example of a baked shadow mask texture. The square area with yellow lines represents a plane. The two grey areas are shadows.

If more than four lights overlap each other at any point in space, Unity bakes the remaining lights. If you bake again, the same lights stay baked unless you change the overlapping lights. To check which lights overlap, use the **Light Overlap** [Debug Draw Mode for lighting](GIVis.html).

## Additional resources

* [Direct and indirect lighting](direct-and-indirect-lighting.html)
* [Setting a light as realtime or baked](LightModes-landing.html)
* [Enable shadows](shadow-configuration.html)

Configuring Mixed lights with Lighting Modes

Set the Lighting Mode of a scene

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
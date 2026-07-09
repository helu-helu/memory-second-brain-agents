* [Lighting](LightingOverview.html)
* [Lighting reference](lighting-reference.html)
* Debug Draw Modes for lighting reference

Lightmap Parameters Asset Inspector window reference

Materials and shaders

# Debug Draw Modes for lighting reference

The **Scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) view has several Debug Draw Modes to help you understand and debug the lighting in your scene.

Use the [Scene view View Options toolbar](overlays-reference-view-options.html) to select a Debug Draw Mode.

If you use the Universal Rendering Pipeline or the High Definition **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#renderpipeline), not all the modes appear. You can use the **Rendering Debugger** window to debug lighting in these pipelines.

## Lighting

### Contributors / Receivers

![A wooden village scene in Contributors / Receivers mode. Most of the geometry is orange and doesnt contribute to global illumination. The green rock and post receive global illumination from lightmaps, and the purple shields receive global illumination from Light Probes.](../uploads/Main/ContributorsReceiversDebugDrawMode.jpg)


A wooden village scene in **Contributors / Receivers** mode. Most of the geometry is orange and doesn’t contribute to global illumination. The green rock and post receive global illumination from lightmaps, and the purple shields receive global illumination from Light Probes.

The **Contributors / Receivers** mode displays the following colors depending on whether objects contribute to and receive **global illumination**A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](Glossary.html#globalillumination):

* Orange means the object doesn’t contribute to global illumination. To change this, use the **Contribute GI** flag in the object’s [Static Editor Flags property](StaticObjects.html).
* Green means the object receives global illumination from **lightmaps**A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](Lightmapping.html)  
  See in [Glossary](Glossary.html#Lightmap). To change this, use the **Receive Global Illumination** setting in the object’s [Mesh Renderer component](class-MeshRenderer.html).
* Blue means the object receives global illumination from **Light Probes**Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](LightProbes.html)  
  See in [Glossary](Glossary.html#LightProbe). To change this, use the **Receive Global Illumination** setting in the object’s [Mesh Renderer component](class-MeshRenderer.html).

Use the [Preferences window](preferences-colors.html) to customize the colors.

### Shadow Cascades

![A wooden village scene in Shadow Cascades mode. The closest geometry is purple to represent the first shadow cascade. Geometry thats further away, for example the rear of a house, is green. The furthest geometry, for example a hill behind the houses, is yellow.](../uploads/Main/ShadCascade4Visualization.png)


A wooden village scene in **Shadow Cascades** mode. The closest geometry is purple to represent the first shadow cascade. Geometry that’s further away, for example the rear of a house, is green. The furthest geometry, for example a hill behind the houses, is yellow.

The **Shadow Cascades** mode displays a different color for each [shadow cascade](shadow-cascades.html). The colors match the shadow cascade colors in the **Shadows** section of the [Quality Settings window](class-QualitySettings.html#Shadows).

You can use this mode to help you adjust the shadow distance, cascade count and cascade shadow splits.

This mode uses the **Scene view**An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView) far plane instead of the shadow distance. You might need to reduce the shadow distance if you want to match the in-game behavior of a **camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) with a small far plane distance.

## Global Illumination

The following modes are enabled when you use [Enlighten Realtime Global Illumination](realtime-gi-using-enlighten.html) or [Baked Global Illumination](Lightmapping.html).

### Indirect (Realtime Global Illumination only)

![A wooden village scene in Indirect mode. Each GameObject displays a checkerboard pattern representing lightmap texels.](../uploads/Main/GIVis7.png)


A wooden village scene in **Indirect** mode. Each GameObject displays a checkerboard pattern representing lightmap texels.

The **Indirect** mode displays the realtime lightmaps generated by **Enlighten**A lighting system by Geomerics used in Unity for Enlighten Realtime Global Illumination. [More info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)  
See in [Glossary](Glossary.html#Enlighten) Realtime Global Illumination.

### Directionality

![A wooden village scene in Directionality mode. Each GameObject displays a similar checkerboard pattern to Indirect mode, using a different color depending on the direction the geometry faces.](../uploads/Main/GIVis8.png)


A wooden village scene in **Directionality** mode. Each GameObject displays a similar checkerboard pattern to **Indirect** mode, using a different color depending on the direction the geometry faces.

The **Directionality** mode displays the dominant light direction as a color. Refer to [Directional Mode](LightmappingDirectional.html) for more information.

### Albedo

![A wooden village scene in Albedo mode. Each GameObject displays a similar checkerboard pattern to Indirect mode, using the albedo color of the material.](../uploads/Main/GIVis5.png)


A wooden village scene in **Albedo** mode. Each GameObject displays a similar checkerboard pattern to **Indirect** mode, using the albedo color of the material.

The **Albedo** mode displays the albedo color of materials.

### Emissive

![A wooden village scene in Emissive mode. Each GameObject displays a similar checkerboard pattern to Indirect mode, using a dark color where theres no emission.](../uploads/Main/GIVis6.png)


A wooden village scene in **Emissive** mode. Each GameObject displays a similar checkerboard pattern to **Indirect** mode, using a dark color where there’s no emission.

The **Emissive** mode displays the emissive color of [emissive materials](lighting-emissive-materials.html).

### UV Charts

![A wooden village scene in UV Charts mode. Each GameObject displays a similar checkerboard pattern to Indirect mode, using a different color for each UV chart.](../uploads/Main/GIVis3.png)


A wooden village scene in **UV Charts** mode. Each GameObject displays a similar checkerboard pattern to **Indirect** mode, using a different color for each UV chart.

The **UV Charts** mode displays a different color for each UV chart.

You can use this mode to check how lightmaps scale onto geometry. Change the scale using settings such as **Resolution** in the [Lightmap Parameters Asset](class-LightmapParameters.html), or the **Scale in Lightmap** property of individual renderers.

### Systems (Realtime Global Illumination only)

![A wooden village scene in Systems mode. Each GameObject displays a similar checkerboard pattern to Indirect mode, using a different color for each group of GameObjects.](../uploads/Main/GIVis4.png)


A wooden village scene in **Systems** mode. Each GameObject displays a similar checkerboard pattern to **Indirect** mode, using a different color for each group of GameObjects.

The **Systems** mode displays a different color for each group of clusters (systems) that Enlighten Realtime Global Illumination creates to generate realtime lightmaps.

Refer to [How Enlighten Realtime Global Illumination works](realtime-gi-using-enlighten.html#how-enlighten-realtime-global-illumination-works) for more information.

### Clustering (Realtime Global Illumination only)

![A wooden village scene in Clustering mode. Each GameObject displays a bright multicolored patchwork pattern that represents lightmap clusters.](../uploads/Main/GIVis10.png)


A wooden village scene in **Clustering** mode. Each GameObject displays a bright multicolored patchwork pattern that represents lightmap clusters.

The **Clustering** mode displays a different color for each cluster Enlighten Realtime Global Illumination creates to generate realtime lightmaps.

Large scenes might generate more clusters than Unity can store in memory. To reduce the number of clusters, use the **Cluster Resolution** setting in the [Lightmap Parameters Asset](class-LightmapParameters.html) to adjust the ratio of clusters to geometry.

Refer to [How Enlighten Realtime Global Illumination works](realtime-gi-using-enlighten.html#how-enlighten-realtime-global-illumination-works) for more information.

### Lit Clustering (Realtime Global Illumination only)

![A wooden village scene in Lit Clustering mode. Each GameObject displays a similar patchwork pattern to Clustering mode, using more muted colors that represent both different clusters and lightmap color.](../uploads/Main/GIVis11.png)


A wooden village scene in **Lit Clustering** mode. Each GameObject displays a similar patchwork pattern to **Clustering** mode, using more muted colors that represent both different clusters and lightmap color.

The **Lit Clustering** mode displays a different color for each cluster Enlighten Realtime Global Illumination creates to generate realtime lightmaps, and applies color from the realtime lightmaps.

### Texel Validity (Baked Global Illumination only)

![A wooden village scene in Texel Validity mode. Most of the scene is green to represent valid texels, but some of the edges of walls and GameObjects are red to represent invalid texels.](../uploads/Main/GIVis14.png)


A wooden village scene in **Texel Validity** mode. Most of the scene is green to represent valid texels, but some of the edges of walls and GameObjects are red to represent invalid texels.

The **Texel Validity** mode displays red on a surface if the baked lightmap texel is invalid. Unity marks a texel as invalid when the lightmapping process emits rays from the surface and hits mostly backfaces. Unity tries to interpolate a color for an invalid texel by looking at neighboring valid texels.

To adjust the threshold for marking texels as invalid, use the **Backface Tolerance** setting in the [Lightmap Parameters Asset](class-LightmapParameters.html).

### UV Overlap (Baked Global Illumination only)

![A wooden village scene in UV Overlap mode. Small red areas on the edges of a small building highlight UV overlaps.](../uploads/Main/GIVis15.png)


A wooden village scene in **UV Overlap** mode. Small red areas on the edges of a small building highlight UV overlaps.

The **UV Overlap** mode displays red if a baked lightmap texel is too close to a texel in another lightmap chart, which might cause aliasing, pixelation and other issues. Refer to [Fixing lightmap UV overlap](troubleshooting-lightmapping-artifacts.html#ProgressiveLightmapper-UVOverlap) for more information.

### Lightmap indices (Baked Global Illumination only)

![A wooden village scene in Lightmap Indices mode. Different GameObjects are different pastel colors, to represent different lightmaps.](../uploads/Main/LightmapIndicesDebugDrawMode.jpg)


A wooden village scene in **Lightmap Indices** mode. Different GameObjects are different pastel colors, to represent different lightmaps.

The **Lightmap indices** mode displays a different color for each baked lightmap.

### Light Overlap (Baked Global Illumination only)

![A wooden village scene in Light Overlap mode. Five light sources are visible. Four are white and contribute to the shadow mask textures. The fifth is red and displays a light cone, and doesnt contribute.](../uploads/Main/GIVis13.png)


A wooden village scene in **Light Overlap** mode. Five light sources are visible. Four are white and contribute to the shadow mask textures. The fifth is red and displays a light cone, and doesn’t contribute.

If you use the [Shadowmask Lighting Mode](lighting-mode.html#shadowmask), the **Light Overlap** mode displays a light volume as red if the light doesn’t contribute to the baked shadow mask textures. This means there are more than 4 light volumes that overlap, so the highlighted light has to fall back to fully baked. Refer to [Light Mode: Shadowmask](lighting-mode.html#shadowmask) for more information.

### Baked Lightmap (Baked Global Illumination only)

![A wooden village scene in Baked Lightmap mode. All the GameObjects have a dense checkerboard pattern to represent lightmap texels.](../uploads/Main/GIVis9.png)


A wooden village scene in **Baked Lightmap** mode. All the GameObjects have a dense checkerboard pattern to represent lightmap texels.

The **Baked Lightmap** mode displays the lightmaps generated by Baked Global Illumination.

### Shadowmask (Baked Global Illumination only)

![A wooden village scene in Shadowmask mode. All the GameObjects display the same dense checkerboard pattern as Baked Lightmap mode, but are now red to represent the shadow mask texture.](../uploads/Main/GIVis12.png)


A wooden village scene in **Shadowmask** mode. All the GameObjects display the same dense checkerboard pattern as **Baked Lightmap** mode, but are now red to represent the shadow mask texture.

If you use the [Shadowmask Lighting Mode](lighting-mode.html#shadowmask), the ****Shadowmask**A shadowmask texture uses the same UV layout and resolution as its corresponding lightmap texture. [More info](lighting-mode.html#shadowmask)  
See in [Glossary](Glossary.html#Shadowmask)** mode displays the baked shadow mask textures. Refer to [Light Mode: Shadowmask](lighting-mode.html#shadowmask) for more information.

## Lighting Visualization overlay reference

The properties in the Lighting Visualization overlay depend on the Debug Draw Mode you select.

| Property | Description |
| --- | --- |
| **Lighting Data** | Select whether Unity uses the current baked lightmaps in the Debug Draw Mode, or temporary lightmaps that Unity rebakes when you update the scene. Refer to [Preview lightmapping](Lightmapping-preview.html) for more information. The options are:  * **Baked**: Use the current baked lightmaps. * **Preview**: Use temporary lightmaps that Unity rebakes when you update the scene. |
| **Show Lightmap Resolution** | Use a checkerboard pattern to display the resolution of lightmaps. Each check is one **pixel**The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html) See in [Glossary](Glossary.html#pixel) in a lightmap. |
| **Highlight Back-Facing Geometry** | Display back-facing geometry as purple. Use the [Preferences window](preferences-colors.html) to change the color. |
| **Adjust Lightmap Exposure** | Raise or lower the brightness of the lightmap colors, to help make the range of colors more visible. The default value is 0. |

## Additional resources

* [Lightmapping troubleshooting guide](https://forum.unity.com/threads/lightmapping-troubleshooting-guide.1340936/) on the Unity Forums.

Lightmap Parameters Asset Inspector window reference

Materials and shaders

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
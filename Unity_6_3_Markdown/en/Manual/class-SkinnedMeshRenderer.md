* [Assets and media](assets-and-media.html)
* [Types of assets](AssetTypes.html)
* [Meshes](mesh.html)
* [Mesh components reference](mesh-components-reference.html)
* Skinned Mesh Renderer component reference

Mesh Renderer component reference

Mesh Filter component reference

# Skinned Mesh Renderer component reference

[Switch to Scripting](../ScriptReference/SkinnedMeshRenderer.html "Go to SkinnedMeshRenderer page in the Scripting Reference")

The Skinned **Mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) Renderer component renders a deformable mesh. Deformable meshes include skinned meshes (meshes that have bones and bind poses), meshes that have blend shapes, and meshes that run cloth simulation.

To render a regular mesh, use a [Mesh Renderer](class-MeshRenderer.html)A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](class-MeshRenderer.html)  
See in [Glossary](Glossary.html#MeshRenderer) and a [Mesh Filter](class-MeshFilter.html)A mesh component that takes a mesh from your assets and passes it to the Mesh Renderer for rendering on the screen. [More info](class-MeshFilter.html)  
See in [Glossary](Glossary.html#MeshFilter) instead.

When you add a deformable mesh or a model with a deformable mesh to a **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene), Unity adds a Skinned Mesh Renderer component to the resulting **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject).

In C# code, the [SkinnedMeshRenderer](../ScriptReference/SkinnedMeshRenderer.html) class represents a Skinned Mesh Renderer component. The `SkinnedMeshRenderer` class inherits much of its functionality from the [Renderer](../ScriptReference/Renderer.html) class. As such, this component has a lot in common with other components that inherit from `Renderer`, such as [Line Renderer](class-LineRenderer.html)A component that takes an array of two or more points in 3D space and draws a straight line between each one. You can use a single Line Renderer component to draw anything from a simple straight line to a complex spiral. [More info](class-LineRenderer.html)  
See in [Glossary](Glossary.html#LineRenderer), and [Trail Renderer](class-TrailRenderer.html)A visual effect that lets you to make trails behind GameObjects in the Scene as they move. [More info](class-TrailRenderer.html)  
See in [Glossary](Glossary.html#TrailRenderer).

* [Properties](#properties)
* [Materials](#materials)An asset that defines how a surface should be rendered. [More info](class-Material.html)  
  See in [Glossary](Glossary.html#Material)
* [Lighting](#Lighting)
* [Probes](#Probes)
* [Ray Tracing](#ray-tracing)The process of generating an image by tracing out rays from the Camera through each pixel and recording the color contribution at the hit point. This is an alternative to rasterization. raytracing  
  See in [Glossary](Glossary.html#raytracing)
* [Mesh LOD](#mesh-lod)
* [Additional Settings](#AdditionalSettings)

## Properties

| **Property** | **Description** |
| --- | --- |
| **Bounds** | Sets the bounding volume that Unity uses to determine when the mesh is offscreen. Unity pre-calculates the bounds when importing the mesh and animations in the Model file, and displays the bounds as a wireframe around the Model in the Scene view.  If you set Update When Offscreen to True, Unity recalculates these bounds every frame and uses those calculated values to overwrite this property.  This property corresponds to the [Mesh.Bounds](../ScriptReference/Mesh-bounds.html) API. |
| **BlendShapes** | Stores the weight values that Unity uses with the [blend shapes](BlendShapes.html) defined in the mesh. |
| **Quality** | Sets a runtime cap for the maximum number of bones that can affect a vertex.   When Unity imports a mesh, Unity can skin every vertex with a number of bones from one to 32. A higher number of influential bones improves results during movement. However, this also increases the computational resources required, and therefore might affect performance.  For performance reasons, it’s better to set the number of bones that affect a vertex on import, rather than using a runtime cap. To do this, use the Rig tab of the [Model Import Settings window](class-FBXImporter.html) and adjust the Skin Weights setting.  In addition to using this setting to set a runtime cap per-component, you can also set a global limit for your project under Edit > Project Settings > Quality > Other > Skin Weights.  This property corresponds to the [SkinnedMeshRenderer.quality](../ScriptReference/SkinnedMeshRenderer-quality.html) API.  The options are:  * **Auto**: Use the global limit set in **Quality Settings** > **Skin Weights**. **Note:** If you import a custom number of skin weights and you want to allow more than four bones of influence, you must choose this option and make sure you set **Skin Weights** to **Unlimited**. * **1 Bone**: Use only one bone per vertex. * **2 Bones**: Use up to two bones per vertex. * **4 Bones**: Use up to four bones per vertex. To allow more than four bones to influence a single vertex, use the **Auto** setting. |
| **Update When Offscreen** | Enable this option to calculate the bounding volume at every frame, even when the mesh is not visible by any Camera. Disable this option to stop skinning when the GameObject is off-screen and resume it when the GameObject is visible again.  This is disabled by default, for performance reasons.  This property corresponds to the [SkinnedMeshRenderer.updateWhenOffscreen](../ScriptReference/SkinnedMeshRenderer-updateWhenOffscreen.html) API. |
| **Mesh** | Set the mesh that this Renderer uses. The mesh should either contain a valid bind pose and skin weights, use blend shapes, or run cloth simulation. If the mesh does not use any of these techniques, consider using a Mesh Renderer and a Mesh Filter.  Corresponds to the [SkinnedMeshRenderer.sharedMesh](../ScriptReference/SkinnedMeshRenderer-sharedMesh.html) property. |
| **Root bone** | Set the transform that is the “root” of the skeleton. The bounds move along with this transform. |
| **Rendering Layer Mask** | This property determines which rendering layer Unity assigns this renderer to. You can use this property to specify an additional rendering-specific layer mask. This filters the renderers based on the mask the renderer has.  This property corresponds to the [Renderer.renderingLayerMask](../ScriptReference/Renderer-renderingLayerMask.html) API.  Unity only displays this property when you use a [Scriptable Render Pipeline](https://docs.unity3d.com/Manual/ScriptableRenderPipeline.html). |
| **Renderer Priority** | Sort renderers by priority. Lower values are rendered first and higher values are rendered last.  This property corresponds to the [Renderer.rendererPriority](../ScriptReference/Renderer-rendererPriority.html) API.  Unity only displays this property when you use the High Definition Render Pipeline. |

## Materials

The **Materials** section lists all the [materials](class-Material.html) that this component uses.

| **Property** | **Description** |
| --- | --- |
| **Size** | The number of elements in the material list.  If you decrease the number of elements, Unity deletes the elements at the end of the list. If you increase the number of elements, Unity adds new elements to the end of the list. Unity populates new elements with the same material that the element at the end of the list uses. |
| **Element** | The materials in the list. You can assign a material asset to each element.  By default, Unity orders the list alphabetically based on the name of the materials. This list is reorderable, and Unity updates the number of the elements automatically as you change their order. |

**Note:** If there are more materials than there are sub-meshes, Unity renders the last sub-mesh with each of the remaining materials, one on top of the next. If the materials are not fully opaque, you can layer different materials and create interesting visual effects. However, fully opaque materials overwrite previous layers, so any additional opaque materials that Unity applies to the last sub-mesh negatively affect performance and produce no benefit.

## Lighting

The **Lighting** section contains properties that relate to lighting.

| **Property** | **Description** |
| --- | --- |
| **Cast Shadows** | Specify if and how this Renderer casts shadows when a suitable [Light](class-Light.html) shines on it.  This property corresponds to the [Renderer.shadowCastingMode](../ScriptReference/Renderer-shadowCastingMode.html) API.  The options are:  * **On**: This Renderer casts a shadow when a shadow-casting Light shines on it. * **Off**: This Renderer does not cast shadows. * **Two-sided**: This Renderer casts two-sided shadows. This means that single-sided objects like a plane or a quad can cast shadows, even if the light source is behind the mesh. For [Baked Global Illumination](class-LightingSettings.html#MixedLighting) or Enlighten [Realtime Global Illumination](class-LightingSettings.html#RealtimeLighting) to support two-sided shadows, the material must support [Double Sided Global Illumination](https://docs.unity3d.com/Manual/class-Material.html). * **Shadows Only**: This Renderer casts shadows, but the Renderer itself isn’t visible. |
| **Receive Shadows** | Specify if Unity displays shadows cast onto this Renderer.  This property only has an effect if you enable [Baked Global Illumination](class-LightingSettings.html#MixedLighting) or Enlighten [Realtime Global Illumination](class-LightingSettings.html#RealtimeLighting) for this scene.  This property corresponds to the [Renderer.receiveShadows](../ScriptReference/Renderer-receiveShadows.html) API.  If your project uses the Universal Render Pipeline (URP), this property appears in the **Inspector** window of materials instead. For more information, refer to [Shader material Inspector window reference for URP](urp/shaders-in-universalrp-reference.html). |
| **Contribute Global Illumination** | Include this Renderer in global illumination calculations, which take place at bake time.  This property only has an effect if you enable [Baked Global Illumination](class-LightingSettings.html#MixedLighting) or Enlighten [Realtime Global Illumination](class-LightingSettings.html#RealtimeLighting) for this scene.  Enabling this property enables the Contribute GI flag in the GameObject’s [Static Editor Flags](StaticObjects.html). It corresponds to the [StaticEditorFlags.ContributeGI](../ScriptReference/StaticEditorFlags.ContributeGI.html) API. |
| **Receive Global Illumination** | Whether Unity provides global illumination data to this Renderer from baked lightmaps, or from runtime Light Probes.  This property is only editable if you enable **Contribute Global Illumination**. It only has an effect if you enable [Baked Global Illumination](class-LightingSettings.html#MixedLighting) or Enlighten [Realtime Global Illumination](class-LightingSettings.html#RealtimeLighting) for this scene.  This property corresponds to the [MeshRenderer.receiveGI](../ScriptReference/MeshRenderer-receiveGI.html) API.  The options are:  * **Lightmaps**: Unity provides global illumination data to this Renderer from lightmaps. * **Light Probes**: Unity provides global illumination data to this Renderer from [Light Probes](LightProbes.html)Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](LightProbes.html) See in [Glossary](Glossary.html#LightProbe) in the scene. |
| **Prioritize Illumination** | Enable this property to always include this Renderer in Enlighten Realtime Global Illumination calculations. This ensures that the Renderer is affected by distant emissives, even those which are normally excluded from Global Illumination calculations for performance reasons.  This property is visible only if **Contribute GI** is enabled in the GameObject’s [Static Editor Flags](StaticObjects.html), your project uses the Built-in Render Pipeline, and Enlighten [Realtime Global Illumination](class-LightingSettings.html#RealtimeLighting) is enabled in your scene. |
| **Mesh **LOD**The *Level Of Detail* (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](LevelOfDetail.html) See in [Glossary](Glossary.html#LOD) for **Global Illumination**A group of techniques that model both direct and indirect lighting to provide realistic lighting results. See in [Glossary](Glossary.html#globalillumination)** | The Mesh LOD index to use for global illumination and when baking lights. A less detailed model lowers global illumination quality, but decreases the bake memory usage and increases the bake performance. This setting is only visible if Mesh LODs have been generated for the mesh and the renderer contributes to global illumination. |

## Probes

The **Probes** section contains properties relating to [Light Probe](LightProbes.html) and [Reflection Probes](class-ReflectionProbe.html)A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](class-ReflectionProbe.html)  
See in [Glossary](Glossary.html#ReflectionProbe).

| **Property** | **Description** |
| --- | --- |
| **Light Probes** | Set how this Renderer receives light from the [Light Probes](LightProbes.html) system.  This property corresponds to the [Renderer.lightProbeUsage](../ScriptReference/Renderer-lightProbeUsage.html) API.  The options are:  * **Off**: The Renderer doesn’t use any interpolated Light Probes. * **Blend Probes**: The Renderer uses one interpolated Light Probe. This is the default value. * **Use Proxy Volume**: The Renderer uses a 3D grid of interpolated Light Probes. * **Custom Provided**: The Renderer extracts Light Probe shader uniform values from the [MaterialPropertyBlock](../ScriptReference/MaterialPropertyBlock.html). |
| **Proxy Volume Override** | Set a reference to another GameObject that has a Light Probe Proxy Volume component.  This property is only visible when **Light Probes** is set to **Use Proxy Volume**. |
| **Reflection Probes** | Set how the Renderer receives reflections from the [Reflection Probe](class-ReflectionProbe.html) system. This property is available only if you use the Built-In Render Pipeline.  This property corresponds to the [Renderer.probeAnchor](../ScriptReference/Renderer-probeAnchor.html) API.  The options are:  * **Off**: Disables Reflection Probes. Unity uses a skybox for reflection. * **Blend Probes**: Enables Reflection Probes. Blending occurs only between Reflection Probes. This is useful in indoor environments where the character may transition between areas with different lighting settings. * **Blend Probes and Skybox**: Enables Reflection Probes. Blending occurs between Reflection Probes, or between Reflection Probes and the default reflection. This is useful for outdoor environments. * **Simple**: Enables Reflection Probes, but no blending occurs between Reflection Probes when there are two overlapping volumes. |
| **Anchor Override** | Set the Transform that Unity uses to determine the interpolation position when using the [Light Probe](LightProbes.html) or [Reflection Probe](class-ReflectionProbe.html) systems. By default, this is the centre of the bounding box of the Renderer’s geometry.  This property corresponds to the [Renderer.probeAnchor](../ScriptReference/Renderer-probeAnchor.html) API. |

## Ray Tracing

The Ray Tracing section contains properties that relate to ray tracing effects.

This section only appears if your graphics card supports ray tracing and you [upgrade your project to use DirectX 12 in the Player settings window](GraphicsAPIs.html).

These properties have no effect unless you configure your project in one of the following ways:

* You use the High Definition **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
  See in [Glossary](Glossary.html#renderpipeline) (HDRP) and [enable ray tracing](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@14.0/manual/Ray-Tracing-Getting-Started.html).
* You write your own C# script to implement ray tracing effects with [RayTracingShader](../ScriptReference/Rendering.RayTracingShader.html) and [RayTracingAccelerationStructure](../ScriptReference/Rendering.RayTracingAccelerationStructure.html).

| **Property** | **Description** |
| --- | --- |
| **Ray Tracing Mode** | Specify if and how often Unity updates this Renderer during ray tracing. More frequent updates increase rendering time. The options are:  * **Off**: Unity excludes this Renderer from ray tracing calculations. This option causes the Renderer to not appear in ray-traced reflections, for example. * **Static**: Unity doesn’t update the [ray tracing acceleration structure](../ScriptReference/Rendering.RayTracingAccelerationStructure.html) if the GameObject’s **Transform** or mesh geometry changes. This means ray tracing effects don’t change at runtime. * **Dynamic Transform**: Unity updates the ray tracing acceleration structure if the GameObject’s **Transform** changes, but not if the mesh geometry changes. This is the default value for a Mesh Renderer. If your project uses HDRP, this setting is the same as **Dynamic Geometry** because HDRP rebuilds the acceleration structure every frame. * **Dynamic Geometry**: Unity updates the ray tracing acceleration structure every frame with the GameObject’s **Transform** and mesh geometry. This is the default value for a Skinned Mesh Renderer. |
| **Procedural Geometry** | Causes Unity to render this Renderer procedurally with an intersection **shader**A program that runs on the GPU. [More info](Shaders.html) See in [Glossary](Glossary.html#shader) rather than with the mesh in the **Mesh Filter** component. |
| **Acceleration Structure Build Flags** | Specifies whether this Renderer overrides the default build flags you specify when you create a [ray tracing acceleration structure](../ScriptReference/Rendering.RayTracingAccelerationStructure.html). |

### Mesh LOD

Settings for configuring the [Mesh LOD](lod/mesh-lod-introduction.html) behavior.

| **Property** | **Description** |
| --- | --- |
| **LOD Override** | Disables automatic LOD selection and sets the LOD index to the value in the **Override Level** property. |
| **Override Level** | Sets the LOD index to the value in this property when **LOD Override** is enabled. |
| **LOD Selection Bias** | Sets the value that Unity adds to the calculated LOD index. Increasing this value results in Unity selecting less detailed LODs, reducing the value - in more detailed LODs. Both the calculated index and the **LOD Selection Bias** value can be a decimal. Unity floors the sum of the values to calculate the LOD index. For example: if Unity calculated an index value of 4.3, and the bias value is 0.9, the resulting LOD index is 5. |

## Additional Settings

The **Additional Settings** section contains additional properties.

| **Property** | **Description** |
| --- | --- |
| **Skinned Motion Vectors** | Enable this option to double-buffer the Mesh **skinning**The process of binding bone joints to the vertices of a character’s mesh or ‘skin’. Performed with an external tool, such as Blender or Autodesk Maya. [More info](UsingHumanoidChars.html) See in [Glossary](Glossary.html#Skinning) data, so Unity can interpolate the skinned motion and place it into the motion vector Texture. This uses more GPU memory, but leads to more correct motion vectors. |
| **Dynamic Occlusion** | When **Dynamic Occlusion** is enabled, Unity’s [occlusion culling](OcclusionCulling.html)A process that disables rendering GameObjects that are hidden (occluded) from the view of the camera. [More info](OcclusionCulling.html) See in [Glossary](Glossary.html#occlusionculling) system culls this Renderer when it is blocked from a Camera’s view by a Static Occluder. Otherwise, the system does not cull this Renderer when it is blocked from a Camera’s view by a Static Occluder.  Dynamic Occlusion is enabled by default. Disable it for effects such as drawing the outline of a character behind a wall. |

SkinnedMeshRenderer

Mesh Renderer component reference

Mesh Filter component reference

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
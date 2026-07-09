* [Optimization](analysis.html)
* [Graphics performance and profiling](graphics-performance-profiling.html)
* [Optimize mesh rendering using level of detail (LOD)](lod-landing.html)
* Introduction to level of detail

Optimize mesh rendering using level of detail (LOD)

Mesh LOD

# Introduction to level of detail

Level of detail (LOD) is a technique that improves performance by reducing the rendering workload.

Without a **LOD**The *Level Of Detail* (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](LevelOfDetail.html)  
See in [Glossary](Glossary.html#LOD) solution, Unity renders an object with the same complexity no matter the size of the object on the screen. For example, in one frame, a 3D model of a building might occupy the whole game view. Then a player moves away from the building and it might be only a few **pixels**The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) high on the screen, but Unity has to render the same **mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh).

With a LOD solution, as a **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) becomes smaller on the screen, Unity can reduce the rendering workload using one or a combination of the following approaches:

* Reduce the number of polygons to render.
* Reduce the complexity or the number of materials to render.
* Reduce the number of ****Mesh Renderer**A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](class-MeshRenderer.html)  
  See in [Glossary](Glossary.html#MeshRenderer)** components.

Unity refers to objects representing levels of detail using indices, where a LOD with index 0 (LOD0) represents the most detailed LOD, and LODs with higher indices have progressively lower amounts of detail (LOD1, LOD2, and so on).

![Left: at LOD0, meshes have a large number of small triangles. Right: at LOD1, the meshes have far fewer triangles, which are much larger in size.](../uploads/Main/lod/lod-introduction-general.jpg)


Left: at LOD0, meshes have a large number of small triangles. Right: at LOD1, the meshes have far fewer triangles, which are much larger in size.

## LOD features in Unity

Unity implements two different LOD features:

* [Mesh LOD](lod/mesh-lod-introduction.html)
* [LOD Group](lod/lod-group-landing.html)A component to manage level of detail (LOD) for GameObjects. [More info](class-LODGroup.html)  
  See in [Glossary](Glossary.html#LODGroup)

Each feature has its advantages and uses a different format for LOD objects. The following table provides a comparison of key characteristics of the features.

| **Mesh LOD** | **LOD Group** |
| --- | --- |
| The feature focuses on reducing the number of polygons to draw with minimum memory footprint and computational overhead. Does not optimize materials or number of draw calls. | A flexible solution with a larger memory footprint and computational overhead. When authoring LOD objects, you have the following optimization options for each LOD:  * Create a less detailed mesh. * Reduce the number of materials or submeshes, which reduces the number of draw calls. * Optimize settings on materials. * Optimize **Mesh Renderer** settings. |
| Provides the option to create LODs automatically on model import. | Requires manual authoring of each LOD mesh in an external tool. |
| Unity stores each LOD in the index buffer of the original mesh. | Each LOD is one or a set of Mesh Renderer components. Users can access and configure each LOD using the Editor interface. |
| Provides a smaller memory footprint compared with LOD Group. Has a smaller rendering workload overhead compared to LOD Group because Mesh LOD does not use any extra GameObjects, components, or meshes. | Has a larger memory footprint and computational overhead compared with Mesh LOD. |
| Provides parameters that control LOD transitions implicitly. | Lets users explicitly specify object size on screen at which a LOD transition occurs per LOD index. |

## LOD transitions

By default, Unity displays one LOD at a time. When Unity transitions from one LOD to another, the transition is noticeable and abrupt.

To make LOD transitions smooth, enable LOD cross-fading. Unity renders both the current and the next LOD, and blends them together.

![A sphere (LOD 1) blends smoothly into a cube (LOD 2) as the camera zooms out.](../uploads/Main/lod/lod-crossfade.gif)


A sphere (LOD 1) blends smoothly into a cube (LOD 2) as the camera zooms out.

For more information, refer to:

* [Make LOD transitions smooth in Mesh LOD](lod/lod-transitions-mesh-lod.html)
* [Make LOD transitions smooth in LOD Group](lod/lod-transitions-lod-group.html)

**Additional resources**

* [LOD directive in ShaderLab reference](SL-ShaderLOD.html)
* [Introduction to Mesh LOD](lod/mesh-lod-introduction.html)
* [LOD Group](lod/lod-group-landing.html)

Optimize mesh rendering using level of detail (LOD)

Mesh LOD

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
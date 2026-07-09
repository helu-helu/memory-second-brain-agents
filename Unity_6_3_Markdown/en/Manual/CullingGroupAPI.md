* [Cameras](Cameras.html)
* [Excluding hidden objects with occlusion culling](OcclusionCulling-landing.html)
* [Configure culling with the CullingGroup API](CullingGroupAPI-landing.html)
* Introduction to the CullingGroup API

Configure culling with the CullingGroup API

Create a Culling Group

# Introduction to the CullingGroup API

CullingGroup offers a way to integrate your own systems into Unity’s culling and **LOD**The *Level Of Detail* (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](LevelOfDetail.html)  
See in [Glossary](Glossary.html#LOD) pipeline. This can be used for many purposes; for example:

* Simulating a crowd of people, while only having full **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
  See in [Glossary](Glossary.html#GameObject) for the characters that are actually visible right now
* Building a GPU **particle**A small, simple image or mesh that is emitted by a particle system. A particle system can display and move particles in great numbers to represent a fluid or amorphous entity. The effect of all the particles together creates the impression of the complete entity, such as smoke. [More info](class-ParticleSystem.html)  
  See in [Glossary](Glossary.html#particle) system driven by Graphics.DrawProcedural, but skipping rendering **particle systems**A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](class-ParticleSystem.html)  
  See in [Glossary](Glossary.html#particlesystem) that are behind a wall
* Tracking which spawn points are hidden from the **camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
  See in [Glossary](Glossary.html#Camera) in order to spawn enemies without the player seeing them ‘pop’ into view
* Switching characters from full-quality animation and AI calculations when close, to lower-quality cheaper behaviour at a distance
* Having 10,000 marker points in your **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
  See in [Glossary](Glossary.html#Scene) and efficiently finding out when the player gets within 1m of any of them

The API works by having you provide an array of bounding spheres. The visibility of these spheres relative to a particular camera is then calculated, along with a ‘distance band’ value that can be treated like a LOD level number.

## CullingGroup API Best Practices

When considering how you might apply CullingGroup to your project, consider the following aspects of the CullingGroup design.

### Using visibility

All the volumes for which CullingGroup computes visibility are defined by bounding spheres - in practice, a position (the center of the sphere) and a radius value. No other bounding shapes are supported, for performance reasons. In practice this means you will be defining a sphere that fully encloses the object you are interested in culling. If a tighter fit is needed, consider using multiple spheres to cover different parts of the object, and making decisions based on the visibility state of all of the spheres.

In order to evaluate visibility, the CullingGroup needs to know which camera visibility should be computed from. Currently a single CullingGroup only supports a single camera. If you need to evaluate visibility to multiple cameras, you should use one CullingGroup per camera and combine the results.

The CullingGroup will calculate visibility based on frustum culling and static **occlusion culling**A process that disables rendering GameObjects that are hidden (occluded) from the view of the camera. [More info](OcclusionCulling.html)  
See in [Glossary](Glossary.html#occlusionculling) only. It will not take dynamic objects into account as potential occluders.

### Using distance

The CullingGroup is capable of calculating the distance between some reference point (for example, the position of the camera or player) and the closest point on each sphere. This distance value is not provided to you directly, but is instead quantized using a set of threshold values that you provide, in order to calculate a discrete ‘distance band’ integer result. The intention is that you interpret these distance bands as ‘close range’, ‘medium range’, ‘far range’, and so on.

The CullingGroup will provide callbacks when an object moves from being in one band to being in another, giving you the opportunity to do things like change the behaviour of that object to something less CPU-intensive.

Any spheres that are beyond the last distance band will be considered to be invisible, allowing you to easily construct a culling implementation that completely deactivates objects that are very far away. If you do not want this behaviour, simply set your final threshold value to be at an infinite distance away.

Only a single reference point is supported per CullingGroup.

### Performance and design

The CullingGroup API does not give you the ability to make changes to your scene and then immediately request the new visibility state of a bounding sphere. For performance reasons, the CullingGroup only calculates new visibility information during execution of culling for the camera as a whole; it’s at this point that the information is available to you, either via a callback, or via the CullingGroup query API. In practice, this means you should approach CullingGroup in an asynchronous manner.

The bounding spheres array you provide to the CullingGroup is referenced by the CullingGroup, rather than copied. This means you should keep a reference to the array that you pass to SetBoundingSpheres, and that you can modify the contents of this array without needing to call SetBoundingSpheres again. If you need multiple CullingGroups that calculate visibility and distances for the same set of spheres - for example, for multiple cameras - then it’s efficient to have all the CullingGroups share the same bounding sphere array instance.

Configure culling with the CullingGroup API

Create a Culling Group

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
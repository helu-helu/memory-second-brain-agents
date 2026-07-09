* [Cameras](Cameras.html)
* [The camera view](CameraView.html)
* Calculate the size of the frustum at a distance

Make the camera perspective oblique

Rays from the camera

# Calculate the size of the frustum at a distance

A cross-section of the view frustum at a certain distance from the **camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) defines a rectangle in world space that frames the visible area. It is sometimes useful to calculate the size of this rectangle at a given distance, or find the distance where the rectangle is a given size. For example, if a moving camera needs to keep an object (such as the player) completely in shot at all times then it must not get so close that part of that object is cut off.

The height of the frustum at a given distance (both in world units) can be obtained with the following formula:

```
var frustumHeight = 2.0f * distance * Mathf.Tan(camera.fieldOfView * 0.5f * Mathf.Deg2Rad);
```

…and the process can be reversed to calculate the distance required to give a specified frustum height:

```
var distance = frustumHeight * 0.5f / Mathf.Tan(camera.fieldOfView * 0.5f * Mathf.Deg2Rad);
```

It is also possible to calculate the FOV angle when the height and distance are known:

```
var cameraFieldOfView = 2.0f * Mathf.Atan(frustumHeight * 0.5f / distance) * Mathf.Rad2Deg;
```

Each of these calculations involves the height of the frustum but this can be obtained from the width (and vice versa) very easily:

```
var frustumWidth = frustumHeight * camera.aspect;
var frustumHeight = frustumWidth / camera.aspect;
```

Make the camera perspective oblique

Rays from the camera

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
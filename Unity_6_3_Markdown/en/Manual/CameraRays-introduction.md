* [Cameras](Cameras.html)
* [The camera view](CameraView.html)
* [Rays from the camera](CameraRays.html)
* Introduction to raycasting

Rays from the camera

Cast a ray from a camera

# Introduction to raycasting

In the section [Understanding the View Frustum](UnderstandingFrustum.html), it was explained that any point in the **camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera)’s view corresponds to a line in world space. It is sometimes useful to have a mathematical representation of that line and Unity can provide this in the form of a [Ray](../ScriptReference/Ray.html) object. The Ray always corresponds to a point in the view, so the Camera class provides the [ScreenPointToRay](../ScriptReference/Camera.ScreenPointToRay.html) and [ViewportPointToRay](../ScriptReference/Camera.ViewportPointToRay.html) functions. The difference between the two is that ScreenPointToRay expects the point to be provided as a **pixel**The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) coordinate, while ViewportPointToRay takes normalized coordinates in the range 0..1 (where 0 represents the bottom or left and 1 represents the top or right of the view). Each of these functions returns a Ray which consists of a point of origin and a vector which shows the direction of the line from that origin. The Ray originates from the near **clipping plane**A plane that limits how far or close a camera can see from its current position. A camera’s viewable range is between the far and near clipping planes. See far clipping plane and near clipping plane. [More info](class-Camera.html)  
See in [Glossary](Glossary.html#clippingplane) rather than the Camera’s transform.position point.

Rays from the camera

Cast a ray from a camera

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
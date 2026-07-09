* [Cameras](Cameras.html)
* Control a camera in first person

Introduction to cameras

The camera view

# Control a camera in first person

Navigate through the **Scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) view while you look through a camera. In first-person, work through the lens of a camera to better frame your shots.

You can use the [Cameras overlay](cameras-overlay.html) to select and take first-person control of a **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) that has a Camera or [Cinemachine camera](https://docs.unity3d.com/Packages/com.unity.cinemachine@latest/) component attached to it.

While you control a camera, you can use Editor tools as you do when you use the Scene Camera. For example, select a GameObject and press the F key to frame the camera on a specific GameObject. You can also adjust the position, orientation, and scale of a GameObject while you look through a camera to change the composition of your shot.

You can adjust the overscan of cameras you directly control with the Cameras overlay. Use overscan to intentionally see more or less of the Scene in the camera’s view than what the final output of the camera produces.

The Cameras overlay supports Timeline and Animation camera path authoring and Animated cameras. Control a camera in first person to animate cameras and generate **keyframes**A frame that marks the start or end point of a transition in an animation. Frames in between the keyframes are called inbetweens.  
See in [Glossary](Glossary.html#keyframe) for their GameObjects.

To control a camera in the first-person view:

1. Press **`** to open the [Overlays menu](overlays.html).
2. In the Overlays menu, enable the Cameras overlay.
3. In the Cameras overlay dropdown list, select a camera you want to control in first person.
4. Select **Control selected camera in first person**.
5. To adjust overscan size and opacity, select **Configure overscan settings** and do the following:
   * To select a size for the view guide, enter a value for **Overscan** or use the scroll wheel on your mouse. 1 is the default value. Enter a value greater than 1 to see more than the camera frustum. Enter a value below 1 to zoom in and see less than the camera frustum.
   * To adjust how opaque the view guide is, enter a value for **Overscan Opacity**.
6. Use the [Scene view navigation controls](SceneViewNavigation.html#tools) to move the camera through the scene.
7. To exit the camera view, in the Cameras overlay, select **Return to Scene Camera**.

## Additional resources

* [Overlays](overlays.html)
* [Cameras overlay](cameras-overlay.html)
* [Cameras](CamerasOverview.html)A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
  See in [Glossary](Glossary.html#Camera)
* [Cinemachine](https://docs.unity3d.com/Packages/com.unity.cinemachine@latest/)
* [Timeline](https://docs.unity3d.com/Packages/com.unity.timeline@latest/)

Introduction to cameras

The camera view

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
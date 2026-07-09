* [Cameras](Cameras.html)
* [Cameras in the Built-In Render Pipeline](cameras-birp.html)
* Camera Inspector window reference for the Built-In Render Pipeline

Set the camera background with Clear Flags in the Built-In Render Pipeline

Troubleshooting cameras

# Camera Inspector window reference for the Built-In Render Pipeline

[Switch to Scripting](../ScriptReference/Camera.html "Go to Camera page in the Scripting Reference")

Explore the properties in the **Camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) component window to customize cameras.

| ***Property:*** | ***Function:*** |
| --- | --- |
| **Clear Flags** | Determines which parts of the screen will be cleared. This is handy when using multiple Cameras to draw different game elements. |
| **Background** | The color applied to the remaining screen after all elements in view have been drawn and there is no **skybox**A special type of Material used to represent skies. Usually six-sided. [More info](sky-landing.html) See in [Glossary](Glossary.html#Skybox). |
| **Culling Mask**Allows you to include or omit objects to be rendered by a Camera, by Layer. See in [Glossary](Glossary.html#CullingMask) | Includes or omits layers of objects to be rendered by the Camera. Assigns layers to your objects in the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html) See in [Glossary](Glossary.html#Inspector). |
| **Projection** | Toggles the camera’s capability to simulate perspective. |
| *Perspective* | Camera will render objects with perspective intact. |
| *Orthographic* | Camera will render objects uniformly, with no sense of perspective. **NOTE:** Deferred rendering is not supported in Orthographic mode. **Forward rendering**A rendering path that renders each object in one or more passes, depending on lights that affect the object. Lights themselves are also treated differently by Forward Rendering, depending on their settings and intensity. [More info](RenderTech-ForwardRendering.html) See in [Glossary](Glossary.html#ForwardRendering) is always used. |
| **Size** (when Orthographic is selected) | The **viewport**The user’s visible area of an app on their screen. See in [Glossary](Glossary.html#viewport) size of the Camera when set to Orthographic. |
| **FOV Axis** (when Perspective is selected) | Field of view axis. |
| *Horizontal* | The Camera uses a horizontal field of view axis. |
| *Vertical* | The Camera uses a vertical field of view axis. |
| **Field of view** (when Perspective is selected) | The Camera’s view angle, measured in degrees along the axis specified in the **FOV Axis** drop-down. |
| **Physical Camera** | Tick this box to enable the [Physical Camera](PhysicalCameras.html) properties for this camera.    When the Physical Camera properties are enabled, Unity calculates the **Field of View** using the properties that simulate real-world camera attributes: **Focal Length**, **Sensor Size**, and **Lens Shift**.   Physical Camera properties are not visible in the Inspector until you tick this box. |
| *Focal Length* | Set the distance, in millimeters, between the camera sensor and the camera lens.  Lower values result in a wider **Field of View**, and vice versa.   When you change this value, Unity automatically updates the **Field of View** property accordingly. |
| *Sensor Type* | Specify the real-world camera format you want the camera to simulate. Choose the desired format from the list.   When you choose a camera format, Unity sets the the **Sensor Size > X** and **Y** properties to the correct values automatically.   If you change the **Sensor Size** values manually, Unity automatically sets this property to **Custom**. |
| *Sensor Size* | Set the size, in millimeters, of the camera sensor.   Unity sets the **X** and **Y** values automatically when you choose the **Sensor Type**. You can enter custom values if needed. |
| *X* | The width of the sensor. |
| *Y* | The height of the sensor. |
| *Lens Shift* | Shift the lens horizontally or vertically from center. Values are multiples of the sensor size; for example, a shift of 0.5 along the X axis offsets the sensor by half its horizontal size.   You can use lens shifts to correct distortion that occurs when the camera is at an angle to the subject (for example, converging parallel lines).   Shift the lens along either axis to make the camera frustum [oblique](ObliqueFrustum.html). |
| *X* | The horizontal sensor offset. |
| *Y* | The vertical sensor offset. |
| *Gate Fit* | Options for changing the size of the **resolution gate** (size/aspect ratio of the game view) relative to the **film gate** (size/aspect ratio of the Physical Camera sensor).   For further information about resolution gate and film gate, see documentation on [Physical Cameras](PhysicalCameras.html). |
| *Vertical* | Fits the resolution gate to the height of the film gate.   If the sensor aspect ratio is larger than the game view aspect ratio, Unity crops the rendered image at the sides.   If the sensor aspect ratio is smaller than the game view aspect ratio, Unity overscans the rendered image at the sides.   When you choose this setting, changing the sensor width (**Sensor Size > X property**) has no effect on the rendered image. |
| *Horizontal* | Fits the resolution gate to the width of the film gate.   If the sensor aspect ratio is larger than the game view aspect ratio, Unity overscans the rendered image on the top and bottom.   If the sensor aspect ratio is smaller than the game view aspect ratio, Unity crops the rendered image on the top and bottom.   When you choose this setting, changing the sensor height (**Sensor Size > Y** property) has no effect on the rendered image. |
| *Fill* | Fits the resolution gate to either the width or height of the film gate, whichever is smaller. This crops the rendered image. |
| *Overscan* | Fits the resolution gate to either the width or height of the film gate, whichever is larger. This overscans the rendered image. |
| *None* | Ignores the resolution gate and uses the film gate only. This stretches the rendered image to fit the game view **aspect ratio**The relationship of an image’s proportional dimensions, such as its width and height. See in [Glossary](Glossary.html#aspectratio). |
| **Clipping Planes** | Distances from the camera to start and stop rendering. |
| *Near* | The closest point relative to the camera that drawing will occur. |
| *Far* | The furthest point relative to the camera that drawing will occur. |
| **Viewport Rect** | Four values that indicate where on the screen this camera view will be drawn. Measured in Viewport Coordinates (values 0–1). |
| *X* | The beginning horizontal position that the camera view will be drawn. |
| *Y* | The beginning vertical position that the camera view will be drawn. |
| *W* (Width) | Width of the camera output on the screen. |
| *H* (Height) | Height of the camera output on the screen. |
| **Depth** | The camera’s position in the draw order. Cameras with a larger value will be drawn on top of cameras with a smaller value. |
| **Rendering Path**The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](RenderingPaths.html) See in [Glossary](Glossary.html#renderingpath) | Options for defining what rendering methods will be used by the camera. |
| *Use Player Settings* | This camera will use whichever Rendering Path is set in the **Player Settings**Settings that let you set various player-specific options for the final game built by Unity. [More info](class-PlayerSettings.html) See in [Glossary](Glossary.html#PlayerSettings). |
| *Vertex Lit* | All objects rendered by this camera will be rendered as Vertex-Lit objects. |
| *Forward* | All objects will be rendered with one pass per material. |
| **Target Texture** | Reference to a [Render Texture](class-RenderTexture.html)A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](class-RenderTexture.html) See in [Glossary](Glossary.html#RenderTexture) that will contain the output of the Camera view. Setting this reference will disable this Camera’s capability to render to the screen. |
| **Occlusion Culling**A process that disables rendering GameObjects that are hidden (occluded) from the view of the camera. [More info](OcclusionCulling.html) See in [Glossary](Glossary.html#occlusionculling) | Enables Occlusion Culling for this camera. Occlusion Culling means that objects that are hidden behind other objects are not rendered, for example if they are behind walls. See [Occlusion Culling](OcclusionCulling.html) for details. |
| **Allow HDR** | Enables High Dynamic Range rendering for this camera. See [High Dynamic Range Rendering](hdr-landing.html) for details. |
| **Allow MSAA** | Enables multi sample **antialiasing**A technique for decreasing artifacts, like jagged lines (jaggies), in images to make them appear smoother. See in [Glossary](Glossary.html#antialiasing) for this camera. |
| **Allow Dynamic Resolution** | Enables Dynamic Resolution rendering for this camera. See [Dynamic Resolution](DynamicResolution-landing.html)A Camera setting that allows you to dynamically scale individual render targets to reduce workload on the GPU. [More info](DynamicResolution-landing.html) See in [Glossary](Glossary.html#dynamicresolution) for details. |
| **Target Display** | Defines which external device to render to. Between 1 and 8. |

Set the camera background with Clear Flags in the Built-In Render Pipeline

Troubleshooting cameras

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
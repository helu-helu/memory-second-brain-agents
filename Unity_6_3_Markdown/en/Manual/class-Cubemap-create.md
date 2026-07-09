* [Materials and shaders](materials-and-shaders.html)
* [Custom textures](Textures-landing.html)
* [Cubemaps](class-Cubemap-landing.html)
* Create a cubemap

Introduction to cubemaps

Create a cubemap array

# Create a cubemap

## Creating Cubemaps from Textures

The fastest way to create **cubemaps**A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](class-Cubemap-landing.html)  
See in [Glossary](Glossary.html#Cubemap) is to import them from specially laid out [Textures](class-TextureImporter.html)An image used when rendering a GameObject, Sprite, or UI element. Textures are often applied to the surface of a mesh to give it visual detail. [More info](class-TextureImporter.html)  
See in [Glossary](Glossary.html#texture).
Select the Texture in the **Project window**A window that shows the contents of your `Assets` folder (Project tab) [More info](ProjectView.html)  
See in [Glossary](Glossary.html#Projectwindow), to see the Import Settings in the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window. In the Import Settings, set the **Texture Type** to **Default**, **Normal Map**A type of Bump Map texture that allows you to add surface detail such as bumps, grooves, and scratches to a model which catch the light as if they are represented by real geometry.  
See in [Glossary](Glossary.html#normalmap) or **Single Channel**, and the **Texture Shape** to **Cube**. Unity then automatically sets the Texture up as a Cubemap.

Several commonly-used cubemap layouts are supported (and in most cases, Unity detects them automatically).

Vertical and horizontal cross layouts, as well as column and row of cubemap faces are supported:

![A vertical cross layout where four faces form a column, a horizontal cross layout where four faces form a row, a column layout, and a row layout.](../uploads/Textures/CubeLayout6Faces1.png)


A vertical cross layout where four faces form a column, a horizontal cross layout where four faces form a row, a column layout, and a row layout.

Another common layout is `LatLong` (Latitude-Longitude, sometimes called cylindrical). Panorama images are
often in this layout:

![A latitude-longitude layout. Four faces form a row, and the two remaining faces stretch along the top and bottom of the texture.](../uploads/Textures/CubeLayoutLatLong.png)


A latitude-longitude layout. Four faces form a row, and the two remaining faces stretch along the top and bottom of the texture.

`SphereMap` (spherical environment map) images can also be found:

![A spherical environment map. The texture is circular, with one face in the centre and four faces surrounding it in a ring. The sixth face is the outer shell of the texture.](../uploads/Textures/CubeLayoutSphereMap.png)


A spherical environment map. The texture is circular, with one face in the centre and four faces surrounding it in a ring. The sixth face is the outer shell of the texture.

By default Unity looks at the **aspect ratio**The relationship of an image’s proportional dimensions, such as its width and height.  
See in [Glossary](Glossary.html#aspectratio) of the imported texture to determine the most appopriate layout from
the above. When imported, a cubemap is produced which can be used for skyboxes and reflections:

Selecting `Glossy Reflection` option is useful for cubemap textures that will be used by
[Reflection Probes](class-ReflectionProbe.html)A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](class-ReflectionProbe.html)  
See in [Glossary](Glossary.html#ReflectionProbe). It processes cubemap mipmap levels in a special way
(specular convolution) that can be used to simulate reflections from surfaces of different smoothness:

![A cubemap used in a Reflection Probe to create reflections on surfaces of varying smoothnesses.](../uploads/Textures/CubeOptionGlossyReflections.png)


A cubemap used in a Reflection Probe to create reflections on surfaces of varying smoothnesses.

## Other Techniques

Another useful technique is to generate the cubemap from the contents of a Unity **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) using a script.
The [Camera.RenderToCubemap](../ScriptReference/Camera.RenderToCubemap.html) function can record the six face
images from any desired position in the scene; the code example on the function’s script reference page
adds a menu command to make this task easy.

## Legacy Cubemap Assets

Unity also supports creating cubemaps out of six separate [textures](class-TextureImporter.html).
Select **Assets** > **Create** > **Rendering** > **Legacy Cubemap** from the menu,
and drag six textures into empty slots in the inspector.

| ***Property:*** | ***Function:*** |
| --- | --- |
| **Right..Back Slots** | Textures for the corresponding cubemap face. |
| **Face Size** | Width and Height of each Cubemap face in **pixels**The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html) See in [Glossary](Glossary.html#pixel). The textures will be scaled automatically to fit this size. |
| **Mipmap** | Should mipmaps be created? |
| **Linear** | Should the cubemap use linear color? |
| **Readable** | Should the cubemap allow **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html) See in [Glossary](Glossary.html#Scripts) to access the pixel data? |
| **Filter Mode** | The filtering mode to use for the cubemap. For more details, refer to [Filter Mode](../ScriptReference/FilterMode.html) |
| **Aniso Level**The anisotropic filtering (AF) level of a texture. Allows you to increase texture quality when viewing a texture at a steep angle. Good for floor and ground textures. [More info](class-TextureImporter.html) See in [Glossary](Glossary.html#AnisoLevel) | The anisotropic filtering level to use for the cubemap. For more details, refer to [Aniso Level](../ScriptReference/Texture-anisoLevel.html) |

Note that it is preferred to create cubemaps using the Cubemap texture import type (see above) - this
way cubemap texture data can be compressed; edge fixups and glossy reflection convolution be performed;
and **HDR**high dynamic range  
See in [Glossary](Glossary.html#HDR) cubemaps are supported.

Introduction to cubemaps

Create a cubemap array

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
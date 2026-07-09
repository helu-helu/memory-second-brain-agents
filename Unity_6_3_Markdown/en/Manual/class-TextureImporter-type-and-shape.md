* [Materials and shaders](materials-and-shaders.html)
* [Custom textures](Textures-landing.html)
* [Textures reference](textures-reference.html)
* [Texture Import Settings window reference](class-TextureImporter.html)
* Texture type and shape settings reference

Texture Import Settings window reference

Platform-specific texture overrides panel reference

# Texture type and shape settings reference

![The Texture Import Settings window with all the settings up to the Advanced section highlighted.](../uploads/Main/texture-import-settings-top.png)


The Texture Import Settings window with all the settings up to the **Advanced** section highlighted.

**Note:** Some of the less commonly used properties are hidden by default. Expand the [Advanced](#advanced) section in the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window to view these properties.

## Texture Type

Use the **Texture Type** property to select the type of Texture you want to create from the source image file. The other properties in the Texture Import settings window change depending on the value you set.

| **Property** | **Function** |
| --- | --- |
| **Default** | This is the most common setting used for all Textures. It provides access to most of the properties for Texture importing. For more information, see the [Default](texture-type-default.html) Texture type. |
| **Normal map**A type of Bump Map texture that allows you to add surface detail such as bumps, grooves, and scratches to a model which catch the light as if they are represented by real geometry. See in [Glossary](Glossary.html#normalmap) | The **Normal map** texture type formats the texture asset so it’s suitable for real-time normal mapping. For more information, see the [Normal map](texture-type-normal-map.html) texture type documentation.   For more information on normal mapping in general, see [Importing Textures](texture-type-normal-map.html). |
| **Editor GUI and Legacy GUI** | The **Editor GUI and Legacy GUI** texture type formats the texture asset so it’s suitable for HUD and GUI controls. For more information, see the [Editor GUI and Legacy GUI](texture-type-editor-gui-and-legacy-gui.html) texture type documentation. |
| **Sprite (2D and UI)** | The **Sprite (2D and UI)** texture type formats the texture asset so it’s suitable to use in 2D applications as a [Sprite](sprite/sprite-landing.html)A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](sprite/sprite-landing.html) See in [Glossary](Glossary.html#Sprite). For more information, see the [Sprite (2D and UI)](texture-type-sprite.html) texture type documentation. |
| **Cursor** | The **Cursor** texture type formats the texture asset so it’s suitable to use as a custom mouse cursor. For more information, see the [Cursor](texture-type-cursor.html) texture type documentation. |
| **Cookie** | The **Cookie** texture type formats the texture asset so it’s suitable to use as a [light cookie](Cookies.html) in the Built-in **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html) See in [Glossary](Glossary.html#renderpipeline). For more information, see the [Cookie](texture-type-cookie.html) texture type documentation. |
| **Lightmap**A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](Lightmapping.html) See in [Glossary](Glossary.html#Lightmap) | The **Lightmap** texture type formats the texture asset so it’s suitable to use as a [Lightmap](class-LightmapParameters.html). This option enables encoding into a specific format (RGBM or dLDR depending on the platform) and a **post-processing**A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](PostProcessingOverview.html) post processing, postprocessing, postprocess See in [Glossary](Glossary.html#post-processing) step on texture data (a push-pull dilation pass). For more information, see the [Lightmap](texture-type-lightmap.html) texture type documentation. |
| **Directional Lightmap** | The **Directional Lightmap** texture type formats the texture asset so it’s suitable to use as a directional [Lightmap](class-LightmapParameters.html). For more information, see the [Directional Lightmap](texture-type-directional-lightmap.html) texture type documentation. |
| **Shadowmask** | The **Shadowmask** texture type formats the texture asset so it’s suitable to use as a [shadowmask](lighting-mode.html#shadowmask)A shadowmask texture uses the same UV layout and resolution as its corresponding lightmap texture. [More info](lighting-mode.html#shadowmask) See in [Glossary](Glossary.html#Shadowmask). For more information, see the [Shadowmask](texture-type-shadowmask.html) texture type documentation. |
| **Single Channel** | The **Single Channel** texture type formats the texture asset so it only has one channel. For information on the properties available only for the this type, see the [Single Channel](texture-type-singlechannel.html) texture type documentation. |

## Texture Shape

Use the **Texture Shape** property to select and define the shape and structure of the Texture. There are four shape types:

* **2D** is the most common setting for all Textures; it defines the image file as a 2D Texture. These are used to map Textures to 3D Meshes and GUI elements, among other Project elements.
* **Cube** defines the Texture as a [cubemap](class-Cubemap-landing.html)A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](class-Cubemap-landing.html)  
  See in [Glossary](Glossary.html#Cubemap). You could use this for Skyboxes or **Reflection Probes**A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](class-ReflectionProbe.html)  
  See in [Glossary](Glossary.html#ReflectionProbe), for example. This type is only available with the [Default](texture-type-default.html), [Normal Map](texture-type-normal-map.html), and [Single Channel](texture-type-singlechannel.html) Texture types.
* **2D Array** defines the Texture as a [2D array texture](class-Texture2DArray.html). This is commonly used as an optimization for some rendering techniques, where many textures of the same size & format are used.
* **3D** defines the Texture as a [3D texture](class-Texture3D.html). 3D textures are used by some rendering techniques to represent volumetric data.

### 2D Array and 3D columns and rows

When you set the **Texture Shape** property to **2D Array** or **3D**, Unity displays the **Columns** and **Rows** properties. Use these to tell Unity how to divide the flipbook texture into cells.

| **Property:** | **Function:** |
| --- | --- |
| **Columns** | The number of columns that the source flipbook texture is divided into. |
| **Rows** | The number of rows that the source flipbook texture is divided into. |

## Other settings

Depending on which **Texture Type** you select, different properties can appear in the Texture Import Settings window. Some of these properties are specific to the Texture Type itself, such as **Sprite Mode** available with the [Sprite (2D and UI)](texture-type-sprite.html) type.

Use Advanced settings to make finer adjustments to the way Unity handles the Texture. The order and availability of these settings can vary depending on the **Texture Type** you choose.

For information on the properties for each texture type, refer to the documentation for that texture type:

* [Default](texture-type-default.html)
* [Normal map](texture-type-normal-map.html)
* [Editor GUI and Legacy GUI](texture-type-editor-gui-and-legacy-gui.html)
* [Sprite (2D and UI)](texture-type-sprite.html)
* [Cursor](texture-type-cursor.html)
* [Cookie](texture-type-cookie.html)
* [Lightmap](texture-type-lightmap.html)
* [Directional Lightmap](texture-type-directional-lightmap.html)
* [Shadowmask](texture-type-shadowmask.html)
* [Single Channel](texture-type-singlechannel.html)

## Additional resources

* [Platform-specific texture overrides panel reference](class-TextureImporter-type-specific.html)

Texture Import Settings window reference

Platform-specific texture overrides panel reference

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
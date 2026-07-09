* [Lighting](LightingOverview.html)
* [Lighting in the Built-In Render Pipeline](lighting-birp.html)
* Create cookies in the Built-In Render Pipeline

Emit light from a GameObject in the Built-In Render Pipeline

Customize how shaders contribute lightmap data in the Built-In Render Pipeline

# Create cookies in the Built-In Render Pipeline

The most convenient way to create a [cookie](Cookies.html) for use with the Built-in **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#renderpipeline) is to create a grayscale texture, import that texture to Unity, and then let Unity convert the texture’s brightness to alpha.

Note that in the Built-in Render Pipeline, cookies only use data from the alpha channel. This means that you can define a shape for a cookie, but not a color.

![A simple grayscale cookie for a window light](../uploads/Main/Cookie.png)


A simple grayscale cookie for a window light


![The same cookie simulating light from a window](../uploads/Main/CookieExample.png)


The same cookie simulating light from a window

To do this:

1. Create a grayscale texture in the image editor of your choice. If you are creating a cookie to use with a Point Light, lay your texture out as a **cubemap**A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](class-Cubemap-landing.html)  
   See in [Glossary](Glossary.html#Cubemap). If you are creating a cookie to use with a Spot Light or Directional Light, lay your texture out as a regular 2D texture.
2. Place the texture in your Project’s Asset folder to import the texture into Unity.
3. In your Project view, select the Texture Asset that represents the texture. Unity displays the [Texture import settings](class-TextureImporter.html) in the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
   See in [Glossary](Glossary.html#Inspector).
4. In the Inspector, set the following values:
   * Set **Texture Type** to **Cookie**
   * Set **Light Type** to match the Type of the Light that you are creating the cookie for
   * Set **Alpha Source** to **From Gray Scale**
5. At the bottom of the Inspector, click **Apply**. Unity applies the updated import settings to the Texture Asset.

Note that the **pixels**The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) of a cookie does not need to be completely transparent or opaque, but can also incorporate any values in between. You can use in-between values to simulate dust or dirt in the path of the light, or to simulate caustic effects such as those produced by the ridges in a car’s headlight.

For more information on configuring the import settings for cookies in the Built-in Render Pipeline, see [Texture Type: Cookie](texture-type-cookie.html).

## Limitations

In the Built-In Render Pipeline, [VertexLit](Built-inShaderGuide.html) **shaders**A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#shader) can’t display Cookies or Shadows.

Shadows are disabled for directional lights with cookies when **forward rendering**A rendering path that renders each object in one or more passes, depending on lights that affect the object. Lights themselves are also treated differently by Forward Rendering, depending on their settings and intensity. [More info](RenderTech-ForwardRendering.html)  
See in [Glossary](Glossary.html#ForwardRendering) is used. It’s possible to write custom shaders to enable shadows in this case; see documentation on [writing surface shaders](SL-SurfaceShaders.html) for further details.

## Additional resources

* [Cookies](Cookies.html)

Emit light from a GameObject in the Built-In Render Pipeline

Customize how shaders contribute lightmap data in the Built-In Render Pipeline

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
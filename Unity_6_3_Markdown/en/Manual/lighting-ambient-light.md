* [Lighting](LightingOverview.html)
* [Light sources](lighting-light-sources.html)
* Add ambient light from the environment

Customize the Light Explorer

Cookies

# Add ambient light from the environment

Ambient light, also known as diffuse environmental light, is light that is present all around the **Scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) and doesn’t come from any specific source object. It can be an important contributor to the overall look and brightness of a scene.

Ambient light can be useful in a number of cases, depending upon your chosen art style. An example would be bright, cartoon-style rendering where dark shadows may be undesirable or where lighting is perhaps hand-painted into textures. **Ambient light**Light that doesn’t come from any specific direction, and contributes equal light in all directions to the Scene. [More info](lighting-window.html)  
See in [Glossary](Glossary.html#ambientlight) can also be useful if you need to increase the overall brightness of a scene without adjusting individual lights.

## Add ambient light

After you [create a skybox material](skyboxes-using.html), Unity can use it to generate ambient lighting in your Scene. To make Unity do this:

1. Open the Lighting window (menu: **Window** > **Rendering** > **Lighting**).
2. Select the **Environment** tab.
3. Assign your chosen **skybox**A special type of Material used to represent skies. Usually six-sided. [More info](sky-landing.html)  
   See in [Glossary](Glossary.html#Skybox) to the **Skybox Material** property.
4. Click the **Source** drop-down and, from the list, click **Skybox**.

## Additional resources

* [Skyboxes](sky-landing.html)
* [Visual environment in the High Definition Render Pipeline (HDRP)](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/Override-Visual-Environment.html)
* [Changing lighting at runtime](urp/probe-volumes-change-lighting-at-runtime.html)
* [Add ambient occlusion](LightingBakedAmbientOcclusion.html)
* [Screen space ambient occlusion in URP](urp/post-processing-ssao-landing.html)

Customize the Light Explorer

Cookies

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
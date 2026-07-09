* [Lighting](LightingOverview.html)
* [Lighting reference](lighting-reference.html)
* Lighting Settings Asset Inspector window reference

Lighting window reference

Lightmap Parameters Asset Inspector window reference

# Lighting Settings Asset Inspector window reference

[Switch to Scripting](../ScriptReference/LightingSettings.html "Go to LightingSettings page in the Scripting Reference")

When you view the Lighting Settings Asset in the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) or the Lighting window, the properties that you can view or edit are divided into the following sections:

* [Realtime Lighting](#RealtimeLighting)
* [Mixed Lighting](#MixedLighting)

For information about **Lightmapping Settings** section of the Lighting Settings Asset, refer to [Lightmapping settings in the Lighting Settings Asset reference](Lightmaps-reference.html).

## Realtime Lighting

This section contains [settings](https://docs.unity3d.com/Manual/lighting-window.html) related to the [Enlighten Realtime Global Illumination system](realtime-gi-using-enlighten.html).

| **Property** | **Description** |
| --- | --- |
| **Realtime **Global Illumination**A group of techniques that model both direct and indirect lighting to provide realistic lighting results. See in [Glossary](Glossary.html#globalillumination)** | Enable this property to use the **Enlighten**A lighting system by Geomerics used in Unity for Enlighten Realtime Global Illumination. [More info](https://www.siliconstudio.co.jp/en/products-service/enlighten/) See in [Glossary](Glossary.html#Enlighten) Realtime Global Illumination system in **Scenes**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html) See in [Glossary](Glossary.html#Scene) that use this Lighting Settings Asset. |
| **Realtime Environment Lighting** | Enable this property to use the Enlighten Realtime Global Illumination system to calculate and update ambient light in real-time.   This property is only available when both Enlighten **Realtime Global Illumination** and **Baked Global Illumination** are enabled in the Scene. |
| **Indirect Resolution** | Specifies the number of texels per unit to use for realtime lightmaps. Increasing this value improves lightmap quality, but also increases render time.  This property is only available if you enable **Realtime Global Illumination**. |

## Mixed Lighting

This section contains settings that affect the behavior of [Baked Lights](LightModes-introduction.html#baked)Light components whose Mode property is set to Baked. Unity pre-calculates the illumination from Baked Lights before runtime, and does not include them in any runtime lighting calculations. [More info](LightModes-introduction.html#baked)  
See in [Glossary](Glossary.html#bakedlights) and [Mixed Lights](LightModes-introduction.html#mixed)Light components whose Mode property is set to Mixed. Some calculations for Mixed Lights are performed in advance, and some calculations for Mixed Lights are performed at runtime. The behavior of all Mixed Lights in a Scene is determined by the Scene’s Lighting Mode. [More info](LightModes-landing.html)  
See in [Glossary](Glossary.html#MixedLights) in Scenes that use this Lighting Settings Asset.

| **Property** | **Description** |
| --- | --- |
| **Baked Global Illumination** | When this setting is enabled, Unity enables the Baked Global Illumination system for the Scenes that use this Lighting Settings Asset. When this setting is disabled, Unity disables the Baked Global Illumination system for the Scenes that use this Lighting Settings Asset.  When the Baked Global Illumination system is enabled, Unity uses Baked lights in the Scene for lightmapping only, and Mixed lights behave according to the **Lighting Mode** setting. When the Baked Global Illumination system is disabled, Unity forces all Baked and Mixed lights in the Scene to act as though they were Realtime Lights. |
| **Lighting Mode** | Specifies which [Lighting Mode](lighting-mode.html) Unity uses for all Mixed Lights in the Scenes that use this Lighting Settings Asset. |

### Lighting Mode dropdown

| **Value** | **Description** |
| --- | --- |
| **Baked Indirect** | Use [Baked Indirect Lighting Mode](lighting-mode.html#baked-indirect) for all Mixed Lights in the Scenes that use this Lighting Settings Asset.  In Baked Indirect Lighting Mode, Mixed Lights provide real-time direct lighting and Unity bakes indirect light into lightmaps and Light Probes. Real-time shadow maps provide shadows. |
| **Shadowmask** | Use [Shadowmask Lighting Mode](lighting-mode.html#shadowmask) for all Mixed Lights in the Scenes that use this Lighting Settings Asset.  In Shadowmask Lighting Mode Mixed Lights provide real-time direct lighting while indirect light is baked into lightmaps and probes. This mode combines real-time and baked shadows. |
| **Subtractive** | Use [Subtractive Lighting Mode](lighting-mode.html#subtractive) for all Mixed Lights in the Scenes that use this Lighting Settings Asset.  In Subtractive Lighting Mode Mixed Lights provide baked direct and indirect lighting for static objects. Dynamic objects receive real-time direct lighting and cast shadows using the Directional Light. |

## Additional resources

* [Create lighting presets with a Lightmap Parameters Asset](configure-with-lightmap-parameters-asset.html)
* [Configure lightmapping with a Lighting Settings Asset](global-illumination-configure.html)
* [Lightmapping settings in the Lighting Settings Asset reference](Lightmaps-reference.html)

LightingSettings

Lighting window reference

Lightmap Parameters Asset Inspector window reference

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
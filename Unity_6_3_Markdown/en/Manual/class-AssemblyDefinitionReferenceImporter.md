* [Programming in Unity](scripting.html)
* [Compilation and code reload](compilation-and-code-reload.html)
* [Script compilation](script-compilation.html)
* [Organizing scripts into assemblies](assembly-definition-files.html)
* Assembly Definition Reference Inspector window reference

Assembly Definition Inspector window reference

Assembly Definition file format reference

# Assembly Definition Reference Inspector window reference

An Assembly Definition Reference is an asset that defines a reference to an Assembly Definition. Create an Assembly Definition Reference asset in a folder to include the **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) in that folder in the referenced Assembly Definition (rather than creating a new assembly). Scripts in child folders are also included, unless they have their own Assembly Definition or Assembly Definition Reference asset.

![An Assembly Definition Reference asset in the Inspector.](../uploads/Main/asmdef-17.png)


An Assembly Definition Reference asset in the Inspector.

| **Property** | **Description** |
| --- | --- |
| **Use GUID** | This setting controls how Unity serializes the reference to the Assembly Definition Reference asset. When you enable this property, Unity saves the reference as the asset’s GUID, instead of the Assembly Definition name. It’s good practice to use the GUID instead of the name, because it means you can make changes to the name of an Assembly Definition asset without having to update other Assembly Definitions and References that reference it. |
| **Assembly Definition** | The referenced Assembly Definition asset. |

## Additional resources

[Create an Assembly Definition Reference asset](assembly-definitions-creating.html#create-asmref)

Assembly Definition Inspector window reference

Assembly Definition file format reference

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
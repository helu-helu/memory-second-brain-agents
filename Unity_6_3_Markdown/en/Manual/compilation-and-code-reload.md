* [Programming in Unity](scripting.html)
* Compilation and code reload

Using randomness

Script compilation

# Compilation and code reload

Compilation transforms the code you write into code that runs in a given context on a given platform. As you work in the Unity Editor, there are several scenarios where Unity may recompile and reload your code. Depending on your settings and the location of your code, opening the Editor for the first time, modifying your code, reimporting a script asset, and entering Play mode can all trigger code reload.

Reloading code is an important way to preserve or reset data between context switches and to ensure relevant changes take effect, but it can negatively impact your development iteration times. It’s important to understand when, why, and how Unity compiles and reloads **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) and other assets and how you can configure this behavior. It’s also important to understand how Unity prioritizes executing different parts of your compiled code to ensure things happen in the order you intend them to.

| **Topic** | **Description** |
| --- | --- |
| [Script compilation](script-compilation.html) | How and in what order Unity compiles your scripts and how you can organize your scripts into assemblies. |
| [Code and scene reload on entering Play mode](code-reloading-editor.html) | Understand what Unity reloads by default on entering Play mode and how you can configure this behavior for faster development iteration times. |
| [Script serialization](script-serialization.html) | Details of how Unity transforms your scripted data structures and object states into a serialized format for storage or reconstruction later on, and how this affects your application performance. |
| [Integrating third-party code libraries (plug-ins)](./plug-ins.html) | Add third-party code libraries to your Unity project. |

## Additional resources

* [C# Compiler](./csharp-compiler.html)

Using randomness

Script compilation

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
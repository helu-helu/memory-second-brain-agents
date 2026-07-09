* [Programming in Unity](scripting.html)
* [Object-oriented development](object-oriented-development.html)
* Fundamental Unity types

Object-oriented development

Object

# Fundamental Unity types

Unity has some fundamental built-in classes that are particularly important for scripting. These are classes which your own custom types can inherit from to integrate with Editor and Engine functionality. It’s helpful to understand these types, their behavior, and why you should inherit from or use them.

For a complete reference of all the built-in classes and every member available, refer to the [Script Reference](../ScriptReference/index.html).

| **Topic** | **Description** |
| --- | --- |
| **[Object](class-Object.html)The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html) See in [Glossary](Glossary.html#object)** | `UnityEngine.Object` is the base class for all objects the Editor can reference from fields in the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html) See in [Glossary](Glossary.html#Inspector) window. |
| **[MonoBehaviour](class-MonoBehaviour.html)** | Inherit from `MonoBehaviour` to make your script a component and control the behaviour of GameObjects and make them responsive to events. |
| **[ScriptableObject](class-ScriptableObject.html)** | Inherit from `ScriptableObject` to store data that’s independent of GameObjects. |
| **[Unity attributes](unity-attributes.html)** | Use Unity-specific C# attributes to define special behavior for your code. |

## Additional resources

* [Unity Scripting reference](../ScriptReference/index.html)

Object-oriented development

Object

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
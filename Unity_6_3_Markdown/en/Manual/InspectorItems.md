* [Unity Editor interface](unity-editor.html)
* [Unity Editor windows and views reference](editor-windows-views-reference.html)
* [Inspector window reference](UsingTheInspector.html)
* Inspect items

Manage the Inspector window

Focus an Inspector window

# Inspect items

What you can view and edit in an **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window depends on the type of item you’re inspecting. This section describes what an Inspector window displays for different types of items you can select.

| Item type | Description |
| --- | --- |
| **Single GameObject** | The GameObject’s components and materials. For more information, refer to [Manage components and their values](InspectorManageComponents.html). |
| **Multiple GameObjects** | The components that the selected GameObjects have in common, and a message if:  - Any components are hidden because one or more GameObjects don’t have those components.  - Any components don’t support editing across multiple GameObjects.  - If a component’s values are the same across all selected GamedObjects, the Inspector shows the value. If the values are different across two or more selected GameObjects, the Inspector displays a dash (**-**). To apply a property value from one selected GameObject to all selected GameObjects, right-click the property name and select **Set to Value of `[Name of GameObject]`** from the context menu. |
| **Single prefab** | Same as other GameObjects, but with additional actions. When you edit a prefab instance, the Inspector window displays options for working with the prefab asset and [applying overrides](PrefabInstanceOverrides.html). The Inspector window displays the names of properties you override in bold. |
| **Multiple prefabs** | You can inspect multiple prefab instances in the same way as multiple GameObjects, but the Inspector hides the **Select**, **Revert**, and **Apply** buttons. For more information, refer to [Prefab instance Inspector reference](prefab-instance-inspector-reference.html). |
| **Single assets** | The asset’s import settings and runtime properties. Each type of asset has its own settings, for example the [Model Import Settings](class-FBXImporter.html), [Audio Clip Import Settings](class-AudioClip.html), and the [Texture Import Settings](class-TextureImporter.html). |
| **Multiple assets** | The properties that the selected assets have in common. If a property’s values are the same across all selected assets, the Inspector shows the value. If the values are different across two or more selected assets, the Inspector displays a dash (**-**). Properties you can’t edit for all assets at once are grayed out. |
| **Script** | The Inspector displays the script’s public variables, and private fields with the [SerializeField](../ScriptReference/SerializeField.html) attribute. Use these to set parameters and default values without modifying the script’s code. To hide these variables, use [HideInInspector](../ScriptReference/HideInInspector.html). |

**Tip:** You can use the **Inspector** window to locate an item in the **Hierarchy** window. From the Inspector window’s **More Items** (**⋮**) menu, select **Ping**.

## Additional resources

* [Inspecting scripts](inspecting-scripts.html)
* [GameObjects](working-with-gameobjects.html)The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
  See in [Glossary](Glossary.html#GameObject)
* [Components](unity-components.html)A functional part of a GameObject. A GameObject can contain any number of components. Unity has many built-in components, and you can create your own by writing scripts that inherit from MonoBehaviour. [More info](UsingComponents.html)  
  See in [Glossary](Glossary.html#component)
* [Prefabs](Prefabs.html)An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](Prefabs.html)  
  See in [Glossary](Glossary.html#prefab)
* [The Hierarchy window](Hierarchy.html)

Manage the Inspector window

Focus an Inspector window

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
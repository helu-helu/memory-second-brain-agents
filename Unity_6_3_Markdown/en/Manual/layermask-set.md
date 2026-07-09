* [GameObjects](working-with-gameobjects.html)
* [Assign GameObjects to layers](Layers.html)
* [Layers and layerMasks](layers-and-layermasks.html)
* Set a layerMask

Introduction to layerMasks

Add a layer to a layerMask

# Set a layerMask

This page explains how to set up a layerMask correctly so you can use it in API calls that use a serialized layerMask property.

## Use a serialized layerMask property

The simplest way to set a layermask in the Unity Editor is to create a property that uses Unity’s [LayerMask](../ScriptReference/LayerMask.html) class. If the property is `public` or uses the [SerializeField](../ScriptReference/SerializeField.html) attribute, Unity provides an interface in the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) that you can use to select which layers the layermask represents.

```
using UnityEngine;

public class LayerMaskExample : MonoBehaviour
{
    [SerializeField] private LayerMask layermask;
}
```

## Convert from a layer

If you want to convert a layer to a layermask in a script at runtime, use the [binary left-shift operator](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators/bitwise-and-shift-operators#left-shift-operator-) to left-shift `1` by the layer. The result is a layermask that represents the single layer.

```
using UnityEngine;

public class LayerExample : MonoBehaviour
{
    [SerializeField] private int layer = 10;
    private int layerAsLayerMask;

    private void Start()
    {
        layerAsLayerMask = (1 << layer);
    }
}
```

## Additional resources

* [Add a layer to a layermask](layermask-add.html)
* [Remove a layer from a layermask](layermask-remove.html)

Introduction to layerMasks

Add a layer to a layerMask

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
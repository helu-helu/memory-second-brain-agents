* [GameObjects](working-with-gameobjects.html)
* [Assign GameObjects to layers](Layers.html)
* [Layers and layerMasks](layers-and-layermasks.html)
* Add a layer to a layerMask

Set a layerMask

Remove a layer from a layerMask

# Add a layer to a layerMask

To add a layer to a layermask, use the [logical OR operator](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators/bitwise-and-shift-operators#logical-or-operator-) on the original layermask and the layer to add.

```
originalLayerMask |= (1 << layerToAdd);
```

## Additional resources

* [Set a layermask](layermask-set.html)
* [Remove a layer from a layermask](layermask-remove.html)

Set a layerMask

Remove a layer from a layerMask

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
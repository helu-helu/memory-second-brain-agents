* [GameObjects](working-with-gameobjects.html)
* [Assign GameObjects to layers](Layers.html)
* [Layers and layerMasks](layers-and-layermasks.html)
* Introduction to layerMasks

Layers and layerMasks

Set a layerMask

# Introduction to layerMasks

Every **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) exists on a single layer, but Unity APIs that let you set which layers the API affect don’t directly use layers. Instead, they use layerMasks.

A [layer](../ScriptReference/GameObject-layer.html)Layers in Unity can be used to selectively opt groups of GameObjects in or out of certain processes or calculations. This includes camera rendering, lighting, physics collisions, or custom calculations in your own code. [More info](Layers.html)  
See in [Glossary](Glossary.html#layer) is a standard integer, but a layerMask is an integer formatted as a bitmask where every `1` represents a layer to include and every `0` represents a layer to exclude. This means that you can pass a layer to an API that expects a layerMasks and the script will still compile because layers and layerMasks use the same underlying type. However, the API call won’t produce the behavior you expect.

For example, if you want to perform a [RayCast](../ScriptReference/Physics.Raycast.html) against GameObjects on layer 9, if you pass `9` into the Physics.Raycast call as the layerMask, Unity actually performs the ray cast against GameObjects on layers `3` and `0`. This is because the binary representation of 9 is `00001001` and if you interpret this as a mask, the `1`s are in the place of layers `3` and `0`.

Layers and layerMasks

Set a layerMask

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
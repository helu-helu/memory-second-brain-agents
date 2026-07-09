* [Animation](AnimationSection.html)
* [Mecanim Animation system](animation-mecanim.html)
* [Animation clips](animation-clips-landing.html)
* [Animation window](AnimationEditorGuide.html)
* Key manipulation in Dopesheet mode

Rotation in animations

Key manipulation in Curves mode

# Key manipulation in Dopesheet mode

Use Box Selection to select multiple keys while viewing the Animation window in Dopesheet mode. Use Box Selection to select and manipulate many keys at once.

Perform the following actions to select multiple keys:
* Hold Shift and click to add individual keys to your selection.
* Drag a rectangle with the mouse to select a group of keys.
* Hold Shift and drag a rectangle to add/remove keys to/from the Box Selection.

![Drag a rectangle to select multiple keys in Dopesheet mode](../uploads/Main/animeditor-DopeSheetDragSelectKeys.png)


Drag a rectangle to select multiple keys in **Dopesheet** mode

As you add keys to the selection, Box Selection handles appear on either side of the selected keys. If you add keys or remove keys, the Box Selection handles automatically adjust their position and size to surround the selected keys.

![Box Selection handles display to the left and right of the selected keys](../uploads/Main/animeditor-DopeSheetSelectedKeys.png)


Box Selection handles display to the left and right of the selected keys

Use the Box Selection handles to move, scale, and ripple edit the selected keys (consult **Ripple edit**, below).

## Move selected keys

Click and drag anywhere within the Box Selection to move the selected keys. You do not need to click directly on a key; you can click any empty space between the Box Selection handles.

As you drag the selection of keys, the time of the first and last key displays to help you position the Box Selection. If you drag the selection of keys to the left, keys that are in negative time (to the left of 0) are deleted when you release the mouse button.

![Drag a selection of keys. The start and end times of the Box Selection display under the timeline bar.](../uploads/Main/animeditor-DopeSheetDraggingKeys.png)


Drag a selection of keys. The start and end times of the Box Selection display under the timeline bar.

## Scale selected keys

When you have multiple keys selected, you can **Scale** the selected keys. For example, you can increase the distance between the selected keys which slows down the animation. You can also decrease the distance between the selected keys which speeds up the animation. To scale the selected keys, click a Box Selection handle to the left or right of the selected keys, and drag horizontally.

As you scale the selected keys, the time of the first and last key displays to help you scale your animation. While scaling, some keys might end up on the same frame as each other. If this happens, the extra keys that occupy the same frame are discarded when you release the mouse button. In this case, the last key is kept.

![Scale a selection of keys. The start and end times of the Box Selection display under the timeline bar.](../uploads/Main/animeditor-DopeSheetScalingKeys.png)


Scale a selection of keys. The start and end times of the Box Selection display under the timeline bar.

## Ripple edit

A ripple edit is a method of either moving or scaling the keys in a Box Selection. A ripple edit also affects the unselected keys for the same properties as the selected keys. How the unselected keys are affected depends on whether the ripple edit is a ripple move or a ripple scale:

* To perform a ripple move, press and hold the **2** key, then drag inside the Box Selection. This moves the Box Selection and pushes unselected keys either left or right depending on the direction you drag. Ripple move preserves the distance between unselected keys.
* To perform a ripple scale, press and hold the **2** key, then drag one of the Box Selection handles. This scales the distance between the selected keys based on the direction in which you drag. This also pushes unselected keys either left or right while preserving the distance between the unselected keys and the Box Selection.

Rotation in animations

Key manipulation in Curves mode

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
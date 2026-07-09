* [Optimization](analysis.html)
* [Graphics performance and profiling](graphics-performance-profiling.html)
* [Collect rendering performance data](profile-rendering.html)
* [Frame Debugger](FrameDebugger-landing.html)
* Check or find a rendering event

Debug a frame

Attach the Frame Debugger to a built project

# Check or find a rendering event

The Event Hierarchy panel in the [Frame Debugger window](frame-debugger-window.html) displays the sequence of rendering events that constitute the frame. The panel organizes the events into a hierarchy so you can see where each event originates from.

![The Event Hierarchy for the URP template scene.](../uploads/Main/frame-debugger-event-hierarchy.png)


The Event Hierarchy for the URP template scene.

To view information about an event, select the event in the Event Hierarchy. When you select an event:

* The Frame Debugger displays information about the event in the [event information](frame-debugger-window-event-information.html) panel.
* Unity processes events up to and including the selected event and displays the result in the Game view.
* If there is a single **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
  See in [Glossary](Glossary.html#GameObject) associated with the event, you can double click or CTRL + click the event to highlight the GameObject in the [Hierarchy](Hierarchy.html). If the event represents a batch that contains multiple GameObjects, Unity doesn’t highlight the GameObjects.

For more information, see [Frame Debugger](FrameDebugger.html).

## Hierarchy search bar

The search bar at the top of the Event Hierarchy can filter events by name. Use it to quickly find specific events by name.

Debug a frame

Attach the Frame Debugger to a built project

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
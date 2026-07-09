* [Programming in Unity](scripting.html)
* [Compilation and code reload](compilation-and-code-reload.html)
* [Code and scene reload on entering Play mode](code-reloading-editor.html)
* Configuring how Unity enters Play mode

Code and scene reload on entering Play mode

Enter Play mode with domain reload disabled

# Configuring how Unity enters Play mode

The ability to test your application by switching from Edit mode to Play mode is one of Unity’s core features. You can use Play mode to run your project directly inside the Editor, through the **Play** button in the [Toolbar](Toolbar.html)A row of buttons and basic controls at the top of the Unity Editor that allows you to interact with the Editor in various ways (e.g. scaling, translation). [More info](Toolbar.html)  
See in [Glossary](Glossary.html#toolbar).

Play mode is intended to provide a realistic preview of how your application is likely to behave for users. By default Unity performs two significant actions on entering Play mode to ensure your project starts and runs as it would in a build:

* It reloads the scripting domain to reset the application state. For more information on the implications of disabling domain reload and how to compensate for it in your code, refer to [Enter Play mode with domain reload disabled](domain-reloading.html).
* It reloads the **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
  See in [Glossary](Glossary.html#Scene). For more information on the implications of disabling scene reload and how to compensate for it in your code, refer to [Enter Play mode with scene reload disabled](scene-reloading.html).

These two actions take time to perform, and the amount of time increases as your **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) and scenes become more complex. When you frequently make and preview changes, the cumulative time spent waiting to enter Play mode can significantly slow down your development process.

To prioritize faster development iteration times over accuracy of the Play mode simulation, Unity offers the ability to disable domain reload and scene reload on entering Play mode.

The following diagram provides a high-level overview of the effects of disabling domain reload and scene reload:

![The effects of disabling domain reload and scene reload settings](../uploads/Main/EnterPlayModeDiagram.svg)


The effects of disabling domain reload and scene reload settings

For more detailed information on the effects of disabling domain and scene reload, refer to [Details of disabling domain and scene reload](configurable-enter-play-mode-details.html).

## Configure Play mode settings

You can configure what processes start when you enter Play mode in **Enter Play Mode Settings** in the [Editor](class-EditorManager.html) section of the [Project Settings](comp-ManagerGroup.html)A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](comp-ManagerGroup.html)  
See in [Glossary](Glossary.html#ProjectSettings) window. To disable domain reload and/or scene reload on enter Play mode:

1. Open the [Project Settings window](comp-ManagerGroup.html) (**Edit** > **Project Settings**).
2. Click on the [Editor](class-EditorManager.html) tab.
3. In the **Enter Play Mode Settings** section, in the **When entering Play Mode** dropdown menu, do one of the following:
   * To disable domain reloading but enable scene reloading, select **Reload Scene only**.
   * To disable scene reloading but enable domain reloading, select **Reload Domain only**.
   * To disable both domain reloading and scene reloading, select **Do not reload Domain or Scene**.

## Additional resources

* [Project Settings window](comp-ManagerGroup.html)
* [Editor Project Settings](class-EditorManager.html)
* [Toolbar](Toolbar.html)
* [Enter Play mode with domain reload disabled](domain-reloading.html)
* [Enter Play mode with scene reload disabled](scene-reloading.html)

Code and scene reload on entering Play mode

Enter Play mode with domain reload disabled

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
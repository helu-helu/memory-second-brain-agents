* [Unity Editor interface](unity-editor.html)
* [Unity Editor settings reference](editor-settings-reference.html)
* [Project Settings reference](comp-ManagerGroup.html)
* Script Execution Order reference

Quality settings tab reference

Services

# Script Execution Order reference

Use the **Script Execution Order** settings to specify the relative execution order of different MonoBehaviour [script components](CreatingComponents.html) in your project. The execution order between different **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) in the project is different from and doesn’t change the [order of execution for event functions](execution-order.html) within each individual script. Unity always calls [`Awake`](../ScriptReference/MonoBehaviour.Awake.html) before the first [`Update`](../ScriptReference/MonoBehaviour.Update.html) for each script, but you can configure script execution order to ensure that `Awake` for one script is always called before `Awake` for another. For example, if you have two scripts, `EngineBehaviour` and `SteeringBehaviour`, you can set the script execution order so that `EngineBehaviour` always updates before `SteeringBehaviour`.

## Configuring execution order

To configure script execution order, go to: **Edit** > **Project Settings**, and then select the **Script Execution Order** category.

![The Script Execution Order section of the Project Settings window displays a list of script classes and their currently configured execution order values.](../uploads/Main/ScriptExecSet.png)


The Script Execution Order section of the Project Settings window displays a list of script classes and their currently configured execution order values.

* Use the plus (+) button to add scripts to the list. Use the minus (-) button on a list item to remove it from the list.
* To specify the execution order, drag items in the list into the desired position or edit the integer values of a script in the list.

The integer values assigned to each script don’t represent any quantity but define each script’s execution order relative to the others. Unity executes scripts in order from lowest first to highest last, for example: –200, –100, –50, 50, 100, 200. The Editor stores these values in the script [metadata files](AssetMetadata.html). You can leave gaps between the values to help avoid unnecessary file changes when you add or move other scripts in the list.

Unity executes any scripts not in the list during the **Default Time** slot, which occurs after any scripts with negative values and before any scripts with positive values.

**Note**: You can specify the script execution order from code rather than configuring it in the Editor by applying the `[DefaultExecutionOrder]` attribute to your MonoBehaviour-derived classes. For more information, refer to the [`[DefaultExecutionOrder]`](../ScriptReference/DefaultExecutionOrder.html) API reference.

For more information on how Unity executes scripts and interprets the configured order, refer to [Script execution order](script-execution-order.html).

## Additional resources

* [Managing update and execution order](managing-update-order.html)
* [`[DefaultExecutionOrder]` API reference](../ScriptReference/DefaultExecutionOrder.html)

Quality settings tab reference

Services

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
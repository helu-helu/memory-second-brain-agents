* [Programming in Unity](scripting.html)
* [Object-oriented development](object-oriented-development.html)
* [Split tasks across frames with coroutines](coroutines-section.html)
* Yield instruction reference

Analyzing coroutines

Interacting with web servers

# Yield instruction reference

Coroutines suspend their execution at a `yield return` statement. A `yield return null` suspends execution of the coroutine until the next frame. But the `yield return` can also return an instruction for the Unity Editor or runtime to, for example, wait for a specified amount of time or until a condition is met before resuming execution of the coroutine.

## Runtime yield instructions

Unity has a set of custom yield instructions derived from [`UnityEngine.YieldInstruction`](../ScriptReference/YieldInstruction.html) that you can use to resume after a specified time, when a specified conditions is met, or at specific points in the Player loop.

| Instruction | Description |
| --- | --- |
| [`AsyncOperation`](../ScriptReference/AsyncOperation.html) | Suspends a coroutine and resumes when an asynchronous operation completes, such as loading a **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html) See in [Glossary](Glossary.html#Scene) or asset. |
| [`WaitForEndOfFrame`](../ScriptReference/WaitForEndOfFrame.html) | Suspends a coroutine and resumes at the end of the frame, after all rendering and GUI events.    **Note**: `WaitForEndOfFrame` never runs in Edit mode when the Editor is in batch mode, even if scripts are marked with `[ExecuteInEditMode]` or `[ExecuteAlways]`. |
| [`WaitForFixedUpdate`](../ScriptReference/WaitForFixedUpdate.html) | Suspends a coroutine and resumes at the end of the next physics update, after all physics calculations. |
| [`WaitForSeconds`](../ScriptReference/WaitForSeconds.html) | Suspends a coroutine and resumes after a specified number of seconds, taking the time scale into account. |
| [`WaitForSecondsRealtime`](../ScriptReference/WaitForSecondsRealtime.html) | Suspends a coroutine and resumes after a specified number of seconds, ignoring the time scale. |
| [`WaitUntil`](../ScriptReference/WaitUntil.html) | Suspends a coroutine and resumes when a supplied delegate evaluates to `true`. |
| [`WaitWhile`](../ScriptReference/WaitWhile.html) | Suspends a coroutine and resumes when a supplied delegate evaluates to `false`. |

For more information and example usage of these yield instructions, refer to their API reference pages.

For a visual representation of where different coroutines resume in the Player loop, refer to the diagram in [Event function execution order](execution-order.html).

## UnityTest yield instructions

Unity Test Framework tests marked with the `[UnityTest]` attribute run as coroutines. The Test Framework package adds support for additional yield instructions to control the Unity Editor from tests and provides the possibility to define custom yield instructions.

| Instruction | Description |
| --- | --- |
| [`EnterPlayMode`](https://docs.unity3d.com/Packages/com.unity.test-framework@latest/index.html?subfolder=/api/UnityEngine.TestTools.EnterPlayMode.html) | Creates a yield instruction for the Unity Editor to enter Play mode. |
| [`ExitPlayMode`](https://docs.unity3d.com/Packages/com.unity.test-framework@latest/index.html?subfolder=/api/UnityEngine.TestTools.ExitPlayMode.html) | Creates a yield instruction for the Unity Editor to exit Play mode. |
| [`RecompileScripts`](https://docs.unity3d.com/Packages/com.unity.test-framework@latest/index.html?subfolder=/api/UnityEngine.TestTools.RecompileScripts.html) | Triggers a recompilation of **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html) See in [Glossary](Glossary.html#Scripts) in the Unity Editor. |
| [`WaitForDomainReload`](https://docs.unity3d.com/Packages/com.unity.test-framework@latest/index.html?subfolder=/api/UnityEngine.TestTools.WaitForDomainReload.html) | Delays the execution of scripts until after an incoming domain reload. |

For more information on the yield instructions provided by Unity Test Framework, refer to [Yield instructions for the Editor](test-framework/reference-custom-yield-instructions.html).

## Editor yield instructions

The Editor coroutines package adds support for coroutines that run in the Unity Editor’s Edit mode. The package includes additional yield instructions for Edit mode coroutines.

| Instruction | Description |
| --- | --- |
| [`EditorWaitForSeconds`](https://docs.unity3d.com/Packages/com.unity.editorcoroutines@latest/index.html?subfolder=/api/Unity.EditorCoroutines.Editor.EditorWaitForSeconds.html) | Resumes an EditorCoroutine after a specified number of seconds, taking the time scale into account. |

For more information, refer to [Editor coroutines](https://docs.unity3d.com/Packages/com.unity.editorcoroutines@latest).

## Batch mode support

All runtime coroutine yield instructions run as normal when you run a standalone [Player in batch mode](PlayerCommandLineArguments.html).

If you run the [Editor in batch mode](EditorCommandLineArguments.html#batchmode) and your project has scripts marked with [`[ExecuteInEditMode]`](../ScriptReference/ExecuteInEditMode.html) or [`[ExecuteAlways]`](../ScriptReference/ExecuteAlways.html) so that they also run in Edit mode, all runtime coroutines in those scripts run in Edit mode except for `WaitForEndOfFrame`. This is because not all Unity subsystems update as regularly in Edit mode as they do at runtime. For more information, refer to the [`[ExecuteAlways]`](../ScriptReference/ExecuteAlways.html) API reference.

## Additional resources

* [Command-line arguments](CommandLineArguments.html)
* [`[ExecuteAlways]`](../ScriptReference/ExecuteAlways.html) API reference

Analyzing coroutines

Interacting with web servers

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
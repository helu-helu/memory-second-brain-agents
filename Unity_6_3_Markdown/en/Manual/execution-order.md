* [Programming in Unity](scripting.html)
* [Object-oriented development](object-oriented-development.html)
* [Managing update and execution order](managing-update-order.html)
* Event function execution order

Event functions

Customizing the Player loop

# Event function execution order

The following diagram provides a high-level overview of the execution sequence for event functions that run during the lifecycle of a MonoBehaviour script component. For readability, the scope of the chart is limited to key parts of the script lifecycle, with some extra internal subsystem updates provided for context. The full Player loop is a longer and more complex sequence of updates for specific systems and subsystems, which run one after the other in a defined default order. To retrieve the full Player loop and all of its systems, you can use the [PlayerLoop API](../ScriptReference/LowLevel.PlayerLoop.html). You can also use this API to [customize the Player loop](player-loop-customizing.html) sequence by removing systems, adding your own, and changing the update order.

For more information on each individual callback’s meaning and limitations, refer to the **Messages** section of the [MonoBehaviour](../ScriptReference/MonoBehaviour.html) API reference.

![Order of execution for event functions during the lifecycle of a MonoBehaviour script.](../uploads/Main/monobehaviour_flowchart.svg)


Order of execution for event functions during the lifecycle of a MonoBehaviour script.

## Before scene load and unload

Not shown in the previous diagram are the [`SceneManager.sceneLoaded`](../ScriptReference/SceneManagement.SceneManager-sceneLoaded.html) and [`SceneManager.sceneUnloaded`](../ScriptReference/SceneManagement.SceneManager-sceneUnloaded.html) events which allow you to receive callbacks when a **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) has loaded and unloaded respectively. Unity raises the `sceneLoaded` event after `OnEnable` but before `Start` for all objects in the scene. For details and example usage, refer to the relevant API reference pages.

For a diagram that includes scene load as part of the execution flow, refer to [Details of disabling Domain and Scene reload](configurable-enter-play-mode-details.html)

## Run code on Editor launch

Sometimes it can be useful to make parts of your code run immediately on launch of the Unity Editor or runtime, without any additional user action and without the code needing to be part of a MonoBehaviour script. You can run code on Editor launch without requiring any user action by applying the [`[InitializeOnLoad]`](../ScriptReference/InitializeOnLoadAttribute.html) attribute to a class that has a [static constructor](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/static-constructors). Alternatively, you can apply the [`[InitializeOnLoadMethod]`](../ScriptReference/InitializeOnLoadMethodAttribute.html) attribute to individual methods. For more information and usage examples, refer to the API references for these attributes.

## Run code on runtime intialization

You can run code on initialization of the runtime application by applying the [`[RuntimeInitializeOnLoadMethodAttribute]`](../ScriptReference/RuntimeInitializeOnLoadMethodAttribute.html) to methods. You can also specify a [`RunTimeInitializeLoadType`](../ScriptReference/RuntimeInitializeLoadType.html) attribute parameter to control where in the Player loop the attributed code executes. For more information on the execution order of methods marked with this attribute, refer to the API reference for [`RuntimeInitializeOnLoadMethodAttribute`](../ScriptReference/RuntimeInitializeOnLoadMethodAttribute.html).

## Internal animation update

The following diagram shows the order of execution for the regular Animation update loop, and expands the nodes labelled **Internal animation update** in the previous diagram:

![Order of execution for the regular Animation update loop.](../uploads/Main/animation-update-sequence.svg)


Order of execution for the regular Animation update loop.

The following Animation loop callbacks shown in the diagram are called on **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) that derive from [MonoBehaviour](../ScriptReference/MonoBehaviour.html):

* [`MonoBehaviour.OnAnimatorMove`](../ScriptReference/MonoBehaviour.OnAnimatorMove.html)
* [`MonoBehaviour.OnAnimatorIK`](../ScriptReference/MonoBehaviour.OnAnimatorIK.html)

Additional animation-related event functions are called on scripts that derive from [`StateMachineBehaviour`](../ScriptReference/StateMachineBehaviour.html):

* [`StateMachineBehaviour.OnStateMachineEnter`](../ScriptReference/StateMachineBehaviour.OnStateMachineEnter.html)
* [`StateMachineBehaviour.OnStateMachineExit`](../ScriptReference/StateMachineBehaviour.OnStateMachineExit.html)
* [`StateMachineBehaviour.OnStateEnter`](../ScriptReference/StateMachineBehaviour.OnStateEnter.html)
* [`StateMachineBehaviour.OnStateUpdate`](../ScriptReference/StateMachineBehaviour.OnStateUpdate.html)
* [`StateMachineBehaviour.OnStateExit`](../ScriptReference/StateMachineBehaviour.OnStateExit.html)
* [`StateMachineBehaviour.OnStateMove`](../ScriptReference/StateMachineBehaviour.OnStateMove.html)
* [`StateMachineBehaviour.OnStateIK`](../ScriptReference/StateMachineBehaviour.OnStateIK.html)

Other animation functions shown in the diagram are internal to the animation system and are provided for context. These functions have associated Profiler markers so you can use the [Profiler](Profiler.html)A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) to see when in the frame Unity calls them. Knowing when Unity calls these functions can help you understand exactly when the event functions you do call are executed. For a full execution order of animation functions and profiler markers, refer to [Profiler markers](profiler-markers.html#animation)Placed in code to describe a CPU or GPU event that is then displayed in the Unity Profiler window. Added to Unity code by default, or you can use [ProfilerMarker API](https://docs.unity3d.com/Packages/com.unity.profiling.core@latest/index.html?subfolder=/manual/profilermarker-guide.html) to add your own custom markers. [More info](profiler-markers.html)  
See in [Glossary](Glossary.html#profilermarker).

## Rendering

This execution order applies for the [Built-in Render Pipeline](built-in-render-pipeline.html) only. For details of execution order in **render pipelines**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#renderpipeline) based on the [Scriptable Render Pipeline](scriptable-render-pipeline-introduction.html), refer to the relevant sections of the documentation for the [Universal Render Pipeline](urp/customize/custom-pass-injection-points.html) or the [High Definition Render Pipeline](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/rendering-execution-order.html). If you want to do work immediately prior to rendering, refer to [Application.onBeforeRender](../ScriptReference/Application-onBeforeRender.html).

* [`OnPreCull`](../ScriptReference/MonoBehaviour.OnPreCull.html): Called before the **camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
  See in [Glossary](Glossary.html#Camera) culls the scene. Culling determines which objects are visible to the camera. `OnPreCull` is called just before culling takes place.
* [`OnBecameVisible`](../ScriptReference/MonoBehaviour.OnBecameVisible.html)/[`OnBecameInvisible`](../ScriptReference/MonoBehaviour.OnBecameInvisible.html): Called when an object becomes visible/invisible to any camera. `OnBecameInvisible` is not shown in the flow chart above since an object may become invisible at any time.
* [`OnWillRenderObject`](../ScriptReference/MonoBehaviour.OnWillRenderObject.html): Called **once** for each camera if the object is visible.
* [`OnPreRender`](../ScriptReference/MonoBehaviour.OnPreRender.html): Called before the camera starts rendering the scene.
* [`OnRenderObject`](../ScriptReference/MonoBehaviour.OnRenderObject.html): Called after all regular scene rendering is done. You can use [GL](../ScriptReference/GL.html) class or [Graphics.DrawMeshNow](../ScriptReference/Graphics.DrawMeshNow.html) to draw custom geometry at this point.
* [`OnPostRender`](../ScriptReference/MonoBehaviour.OnPostRender.html): Called after a camera finishes rendering the scene.
* [`OnRenderImage`](../ScriptReference/MonoBehaviour.OnRenderImage.html): Called after scene rendering is complete to allow **post-processing**A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](PostProcessingOverview.html) post processing, postprocessing, postprocess  
  See in [Glossary](Glossary.html#post-processing) of the image, see [Post-processing Effects](PostProcessingOverview.html).
* [`OnGUI`](../ScriptReference/MonoBehaviour.OnGUI.html): Called multiple times per frame in response to GUI events. The Layout and Repaint events are processed first, followed by a Layout and keyboard/mouse event for each input event.
* [`OnDrawGizmos`](../ScriptReference/MonoBehaviour.OnDrawGizmos.html) Used for drawing **Gizmos**A graphic overlay associated with a GameObject in a Scene, and displayed in the Scene View. Built-in scene tools such as the move tool are Gizmos, and you can create custom Gizmos using textures or scripting. Some Gizmos are only drawn when the GameObject is selected, while other Gizmos are drawn by the Editor regardless of which GameObjects are selected. [More info](GizmosMenu.html#GizmosIcons)  
  See in [Glossary](Glossary.html#Gizmo) in the **scene view**An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](UsingTheSceneView.html)  
  See in [Glossary](Glossary.html#SceneView) for visualisation purposes.

**Note**: [OnPreCull](../ScriptReference/Camera.OnPreCull.html), [OnPreRender](../ScriptReference/Camera.OnPreRender.html), [OnPostRender](../ScriptReference/Camera.OnPostRender.html), and [OnRenderImage](../ScriptReference/Camera.OnRenderImage.html) are built-in Unity event functions that are called on MonoBehaviour scripts but **only if those scripts are attached to the same object as an enabled Camera component**. If you want to receive the equivalent callbacks for `OnPreCull`, `OnPreRender`, and `OnPostRender` on a MonoBehaviour attached to a **different** object, you must use the equivalent delegates (note the lowercase `on` in the names) [Camera.onPreCull](../ScriptReference/Camera-onPreCull.html), [Camera.onPreRender](../ScriptReference/Camera-onPreRender.html), and [Camera.onPostRender](../ScriptReference/Camera-onPostRender.html) as shown in the code examples in the relevant pages of the scripting reference.

## Resumption of coroutines and asynchronous tasks

Suspended coroutines can resume at different points in the execution sequence depending on the yield instruction used. For example, coroutines that use [`WaitForEndOfFrame`](../ScriptReference/WaitForEndOfFrame.html) resume at the end of the frame, while those that use [`WaitForFixedUpdate`](../ScriptReference/WaitForFixedUpdate.html) resume at the end of the fixed update step. For more information, refer to [Coroutines](coroutines.html).

Regular .NET Tasks and asynchronous methods resume in the `Update` phase. Similarly to coroutines, Unity’s custom [`Awaitable`](../ScriptReference/Awaitable.html) class can resume at different points depending on the method you use when awaiting. For more information, refer to [Asynchronous programming with the Awaitable class](async-await-support.html).

**Note**: The exact order of execution between resuming coroutines and asynchronous tasks is not guaranteed. Awaitables are grouped together and executed in the order they were awaited.

## Combining MonoBehaviours with Entities

When using the [Entity Component System](https://docs.unity3d.com/Packages/com.unity.entities@latest/index.html) (ECS), Unity merges ECS system group updates into the Player update loop.

You can use the Entities Systems window to view the update order of ECS system groups relative to the full Player loop. For more information, refer to [Update order of systems](https://docs.unity3d.com/Packages/com.unity.entities@1.4/manual/systems-update-order.html#update-order-of-systems) in the Entities package documentation.

## Limitations

In general, you can’t rely on the order in which the same event function is invoked for different **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject), except when the order is explicitly documented or settable.

You can’t specify the order in which an event function is called for different instances of the same MonoBehaviour script. For example, the `Update` function of one MonoBehaviour might be called before or after the `Update` function for the same MonoBehaviour on another GameObject, including its own parent or child GameObjects.

To configure the execution order between different MonoBehaviour scripts, refer to [Script execution order](script-execution-order.html).

## Additional resources

* [Event functions](event-functions.html)
* [MonoBehaviour](class-MonoBehaviour.html)
* [PlayerLoop API reference](../ScriptReference/LowLevel.PlayerLoop.html)
* [Script execution order](script-execution-order.html)

Event functions

Customizing the Player loop

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
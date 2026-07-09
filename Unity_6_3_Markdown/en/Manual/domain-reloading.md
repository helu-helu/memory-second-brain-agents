* [Programming in Unity](scripting.html)
* [Compilation and code reload](compilation-and-code-reload.html)
* [Code and scene reload on entering Play mode](code-reloading-editor.html)
* Enter Play mode with domain reload disabled

Configuring how Unity enters Play mode

Enter Play mode with scene reload disabled

# Enter Play mode with domain reload disabled

The scripting domain, also known as the [application domain](https://learn.microsoft.com/en-us/dotnet/framework/app-domains/application-domains), or simply domain, is a core feature of Unity’s managed scripting environment. The domain is an isolated section of memory dedicated to a particular application, which contains the compiled types required by the application, grouped into logical units called [assemblies](assembly-definition-files.html). It also contains the data that represents the current application state, such as the values of variables and object references in the various sections of [managed memory](performance-managed-memory.html).

By default Unity reloads the domain on entering Play mode to reset the application state. Resetting state before entering Play mode is often desirable so your application starts up as it would at the beginning of a new build. For example, static counters that were incremented in a previous Play mode session should begin from zero again in the next one. However, domain reload is also a time-consuming operation that negatively impacts iteration times when you frequently switch between Edit and Play mode. For faster iteration times, you can [disable domain reload](configurable-enter-play-mode.html#configure-play-mode) on entering Play mode but you must then manually [reset state in your code](#reset-state).

**Note**: Unity also performs domain reload as part of an asset database refresh when it detects changes to **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts). This still happens even when domain reload on entering Play mode is disabled. For more information on when and how asset database refreshes happen, refer to [Refreshing the Asset Database](AssetDatabaseRefreshing.html).

## Effects of disabling domain reload when entering Play mode

When you disable domain reload:

* Non-serialized fields keep the values assigned to them during Play mode on returning to Edit mode. This applies for fields of all script types, including MonoBehaviours (including those on prefab assets), ScriptableObjects, and your own custom C# types. For detailed information on what is and isn’t serialized in different contexts, refer to [Serialization rules](script-serialization-rules.html).
* Static variables keep their values between Play mode sessions.
* Static events keep their registered subscribers between Play mode sessions.
* There are no additional `OnDisable` or `OnEnable` calls for scripts marked with the [`[ExecuteInEditMode]`](../ScriptReference/ExecuteInEditMode.html) or [`[ExecuteAlways]`](../ScriptReference/ExecuteAlways.html).

To compensate for this persistence of data between Play mode sessions and enter Play mode with a fresh application state, you must [reset state in your code](#reset-state).

For more information on the effects of disabling domain and **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) reload, refer to [Details of disabling domain and scene reload](configurable-enter-play-mode-details.html).

## Resetting state from code

When domain reloading is disabled, the values of [static fields](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/static-classes-and-static-class-members#static-members) and the handlers assigned to static events persist between Play mode runs. The following code example has a static counter that increments on a press of any keyboard key. The code also registers a method to handle the static event [`EditorApplication.playModeStateChanged`](../ScriptReference/EditorApplication-playModeStateChanged.html).

With domain reload enabled, Unity reinitializes this code on entering Play mode, erasing the state from the previous Play mode run, including the counter value and the registration of the event handler. With domain reload disabled, the counter value and the event handler registration are both preserved from the previous run. On the next run of Play mode, the counter begins with the value it had at the end of the previous run and the event handler method is called multiple times on one occurrence of the event, generating multiple “Exiting Play mode!” messages in the console.

```
// Copy-paste this code into a MonoBehaviour script attached to a GameObject in your project.
// Run it with domain reload enabled and then with domain reload disabled and note the different behavior.

using UnityEngine;
#if UNITY_EDITOR
using UnityEditor;
#endif

public class StateResetExample : MonoBehaviour
{
    // With domain reload disabled this counter won't reset to zero on exiting Play mode
    static int counter = 0;

    void Start()
    {
    // Register handler
#if UNITY_EDITOR
        EditorApplication.playModeStateChanged += OnExitPlayMode;
#endif    
    }

    void Update()
    {
        if (Input.anyKeyDown)
        {
            counter++;
            Debug.Log("Counter: " + counter);
        }
    }
#if UNITY_EDITOR
    private static void OnExitPlayMode(PlayModeStateChange state)
    {
        if(state == PlayModeStateChange.ExitingPlayMode)
        {
            // With domain reload disabled this message prints multiple times after the first Play mode run
            Debug.Log("Exiting Play mode!");
        }
    }
#endif
}
```

You can fix the problem behavior with code that explicitly resets the counter and unregisters the event handler between Play mode runs. You can either do this on entering Play mode or on exiting Play mode.

### Resetting state on exiting Play mode

It’s often most efficient to reset state on exiting Play mode rather than on entering. You can use the [`EditorApplication.playModeStateChanged`](../ScriptReference/EditorApplication-playModeStateChanged.html) event and its [`ExitingPlayMode`](../ScriptReference/PlayModeStateChange.ExitingPlayMode.html) enum value to catch the Play mode exit event and reset state at that point. In the following example the event handler for Play mode exit is used to unregister itself, but you can also use this method to unregister any other static event handlers at this point:

```
using UnityEngine;
#if UNITY_EDITOR
using UnityEditor;
#endif

public class StateResetOnExit : MonoBehaviour
{
    static int counter = 0;

    void Start()
    {
#if UNITY_EDITOR
        EditorApplication.playModeStateChanged += OnExitPlayMode;
#endif        
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.anyKeyDown)
        {
            counter++;
            Debug.Log("Counter: " + counter);
        }
    }

#if UNITY_EDITOR
    private static void OnExitPlayMode(PlayModeStateChange state)
    {
        if(state == PlayModeStateChange.ExitingPlayMode)
        {
            Debug.Log("Exiting Play mode!");
            Debug.Log("Unregistering handler.");
            // Unregister the handler so it doesn't affect the next Play mode run
            EditorApplication.playModeStateChanged -= OnExitPlayMode;
            Debug.Log("Resetting counter.");
            // Reset the counter so it starts from 0 on the next Play mode run
            counter = 0;
        }
    }
#endif
}
```

[`EditorApplication.playModeStateChanged`](../ScriptReference/EditorApplication-playModeStateChanged.html) is in the `UnityEditor` namespace so it only works in Play mode within the Unity Editor and not in a standalone Player build.

If your code executes in Edit mode in addition to Play mode, you can’t rely on resetting state on exiting Play mode. Your code might modify a static variable while in Edit mode, so you must reset the variable [on entering Play mode](#reset-on-enter) instead.

**Note**: For scripts that execute in Edit mode, disabling domain reload skips [`MonoBehaviour.OnDisable`](../ScriptReference/MonoBehaviour.OnDisable.html) and disabling scene reload skips [`MonoBehaviour.OnDestroy`](../ScriptReference/MonoBehaviour.OnDestroy.html), which makes these methods inappropriate for resetting state in such scripts. For more information, refer to [Details of disabling domain and scene reload](configurable-enter-play-mode-details.html).

### Resetting state on entering Play mode

You can also reset state on entering Play mode. This can be a useful alternative if you encounter any platform-specific problems with capturing the exiting Play mode event, or if you have code that also executes in Edit mode. For the purposes of illustration, the following example demonstrates both resetting static variables and unregistering static event handlers on entering Play mode. Best practice is to always unregister static event handlers [on exiting Play mode](#reset-on-exit). Waiting until the next Play mode session can cause object reference issues that lead to unregistering the wrong handler.

Unity has custom initialization attributes in both the `UnityEngine` and `UnityEditor` namespaces, which you can use to perform initialization work, including manual state reset. Which attributes you should use depends on whether your code runs in Edit mode or Play mode. To reset state on entering Play mode for your Player (runtime) scripts, you can use the [`[RuntimeInitializeOnLoadMethod]`](../ScriptReference/RuntimeInitializeOnLoadMethodAttribute.html) attribute with the [`RuntimeInitializeLoadType.SubsystemRegistration`](../ScriptReference/RuntimeInitializeLoadType.SubsystemRegistration.html) parameter:

```
using UnityEngine;
#if UNITY_EDITOR
using UnityEditor;
#endif

public class StateResetOnEnter : MonoBehaviour
{
    static int counter = 0;

    [RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.SubsystemRegistration)]
    static void Init()
    {
        Debug.Log("Unregistering handler.");
        // Unregister the handler so it doesn't affect the next Play mode run
        EditorApplication.playModeStateChanged -= OnExitPlayMode;
        Debug.Log("Resetting counter.");
        // Reset the counter so it starts from 0 on the next Play mode run
        counter = 0;  
    }

    void Start()
    {
#if UNITY_EDITOR
        EditorApplication.playModeStateChanged += OnExitPlayMode;
#endif
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.anyKeyDown)
        {
            counter++;
            Debug.Log("Counter: " + counter);
        }
    }
#if UNITY_EDITOR
    private static void OnExitPlayMode(PlayModeStateChange state)
    {
        if(state == PlayModeStateChange.ExitingPlayMode)
        {
            Debug.Log("Exiting Play mode!");
        }
    }
#endif
}
```

[`[RuntimeInitializeOnLoadMethod]`](../ScriptReference/RuntimeInitializeOnLoadMethodAttribute.html) is in the `UnityEngine` namespace so it’s only available in Play mode. For Editor-only scripts such as custom Editor windows or **Inspectors**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) that use statics, you can do one of the following:

* Use [`[InitializeOnLoadAttribute]`](../ScriptReference/InitializeOnLoadAttribute.html) to register a handler for [`EditorApplication.playModeStateChanged`](../ScriptReference/EditorApplication-playModeStateChanged.html) and then perform state cleanup on either entering or exiting Play mode. Refer to the [`EditorApplication.playModeStateChanged`](../ScriptReference/EditorApplication-playModeStateChanged.html) API reference for an example.
* Use the [`[InitializeOnEnterPlayMode]`](../ScriptReference/InitializeOnEnterPlayModeAttribute.html) attribute to perform cleanup specifically on entering Play mode.

**Note**: While the previous code examples use MonoBehaviour classes, you can also use these initialization attributes on scripts of any kind, including those that inherit from ScriptableObject or your own custom C# types.

## Additional resources

* [Project Settings window](comp-ManagerGroup.html)
* [Editor Project Settings](class-EditorManager.html)
* [Toolbar](Toolbar.html)A row of buttons and basic controls at the top of the Unity Editor that allows you to interact with the Editor in various ways (e.g. scaling, translation). [More info](Toolbar.html)  
  See in [Glossary](Glossary.html#toolbar)
* [Scene Reloading](scene-reloading.html)
* [Configurable Enter Play Mode](configurable-enter-play-mode.html)

Configuring how Unity enters Play mode

Enter Play mode with scene reload disabled

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
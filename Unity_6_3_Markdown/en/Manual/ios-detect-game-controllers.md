* [Platform development](PlatformSpecific.html)
* [iOS](iphone.html)
* [Developing for iOS](ios-developing.html)
* [Input for iOS devices](ios-input.html)
* [Game Controller support](ios-game-controller-support.html)
* Detect Game Controllers

Game Controller support

Handle Game Controller input

# Detect Game Controllers

Unity includes the **Game Controller**A device to control objects and characters in a game.  
See in [Glossary](Glossary.html#gamecontroller) framework in the project only if a script in the project references [`Input.GetJoystickNames`](../ScriptReference/Input.GetJoystickNames.html). If it’s available, Unity iOS Runtime loads the framework dynamically.

To get the list of all available controllers, call [`Input.GetJoystickNames`](../ScriptReference/Input.GetJoystickNames.html). You can re-check this list at any time to detect if controllers have been attached or detached.

You can call this API to detect the type of controller that’s attached. Names follow the pattern: `[$profile_type,$connection_type] joystick $number by $model`. `$profile_type` can be either **basic** or **extended**, and `$connection_type` is either **wired** or **wireless**. When Unity detects at least one controller, you can either disable on-screen touch controls or amend them to supplement controller input.

## Example: Detect attached Game Controllers

The following code sample checks whether any controllers are connected to the device.

```
using System.Collections;
using UnityEngine;

public class GameControllers : MonoBehaviour
{
    private bool connected = false;

    IEnumerator CheckForControllers() {
        while (true) {
            var controllers = Input.GetJoystickNames();

            if (!connected && controllers.Length > 0) {
                connected = true;
                Debug.Log("Connected");
            
            } else if (connected && controllers.Length == 0) {         
                connected = false;
                Debug.Log("Disconnected");
            }

            yield return new WaitForSeconds(1f);
        }
    }

    void Awake() {
        StartCoroutine(CheckForControllers());
    }
}
```

## Additional resources:

* [Input class](../ScriptReference/Input.html)

Game Controller support

Handle Game Controller input

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
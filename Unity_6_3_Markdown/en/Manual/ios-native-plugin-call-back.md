* [Platform development](PlatformSpecific.html)
* [iOS](iphone.html)
* [Developing for iOS](ios-developing.html)
* [Native plug-ins for iOS](PluginsForIOS.html)
* [Use your native plug-in for iOS](ios-native-plugin-use.html)
* Callback from native code

Call native plug-ins for iOS

Automated plug-in integration

# Callback from native code

Unity iOS supports limited native-to-managed callback functionality using one of the following methods:

* [`UnitySendMessage`](#unitySendMessage)
* [Delegates](#delegates)

## Use UnitySendMessage

`UnitySendMessage` looks like this:

`UnitySendMessage("GameObjectName1", "MethodName1", "Message to send");`

There are three parameters:

* The name of the target GameObject
* The script method to call on that object
* The message string to pass to the called method

`UnitySendMessage` has the following limitations:

1. From native code, you can only call script methods that correspond to the following signature: `void MethodName(string message);`.
2. Calls to `UnitySendMessage` are asynchronous and have a delay of one frame.
3. If two or more **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
   See in [Glossary](Glossary.html#GameObject) have the same name, this can cause conflicts when you use `UnitySendMessage`.

## Use delegates

When you use delegates, the method on the C# side must be static and marked with the `MonoPInvokeCallback` attribute.

To use delegates:

1. Pass the method as a delegate to the extern method.
2. Implement the extern method in native code as a function that accepts a pointer to functions with the corresponding signature.

The function pointer in the native code then points back to the static method in C#.

The C# code for this method looks like this:

```
delegate void MyFuncType();

[AOT.MonoPInvokeCallback(typeof(MyFuncType))]

static void MyFunction() { }

[DllImport ("__Internal")] 

static extern void RegisterCallback(MyFuncType func);
```

The C code that accepts the callback then looks like this:

```
typedef void (*MyFuncType)();

void RegisterCallback(MyFuncType func) {}
```

**Note:** Ensure string values returned from a native method are UTF–8 encoded and allocated on the heap.

## Additional resources

* [Automated plug-in integration for iOS](ios-native-plugin-automated-integration.html)

Call native plug-ins for iOS

Automated plug-in integration

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
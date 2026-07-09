* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Developing for Android](android-developing.html)
* [Create and use plug-ins in Android](PluginsForAndroid.html)
* [Calling Java and Kotlin plug-in code from C# scripts](android-plugins-java-code-from-c-sharp.html)
* Best practices for calling Java/Kotlin code

Supported data types for Java/Kotlin and C# code

Integrating Unity into Android applications

# Best practices for calling Java/Kotlin code

Learn about the best practices for calling Java and Kotlin **plug-in**A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#plug-in) code from C# **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) to improve performance of your application.

## Minimize JNI calls

Using the Java Native Interface (JNI), through either the high-level or low-level C# API is resource intensive and can be slow. To improve performance, and also code clarity, it’s best practice to keep the number of JNI calls low.

To avoid unnecessary JNI calls, the high-level C# API caches the [ID](../ScriptReference/AndroidJNI.GetMethodID.html) of each Java method that you call. This means that subsequent calls to the same method aren’t as resource intensive as the first call. The calls don’t need to be during the same frame or even from the same `AndroidJavaObject`/`AndroidJavaClass` instance. If you use the low-level API and want this performance benefit, you must manually cache method ID. Otherwise, it’s best practice to use the high-level API.

**Note**: Unity maintains the cache until the application [closes](https://support.google.com/android/answer/9079646?hl=en-GB). This includes while the application is in the background.

## Manage garbage collection

It’s best practice to wrap any instance of `AndroidJavaObject` or `AndroidJavaClass` with a `using` statement to ensure Unity destroys them as soon as possible. If you don’t use `using`, Unity’s [garbage collector](performance-garbage-collector.html) will still release all created instances, but you lose control over when this happens.

The following code example demonstrates how to use `using` statements to access the system language in an optimal way:

```
using UnityEngine;

public class LocaleExample : MonoBehaviour
{
    void Start()
    {
        using (AndroidJavaClass cls = new AndroidJavaClass("java.util.Locale"))
        using (AndroidJavaObject locale = cls.CallStatic<AndroidJavaObject>("getDefault"))
        {
            if (locale != null)
            {
                Debug.Log("current lang = " + locale.Call<string>("getDisplayLanguage"));
            }
        }
    }
}
```

## Additional resources

* [Code examples: Call Java/Kotlin code from C# scripts](android-high-level-api-code-examples.html)
* [Supported data types for Java/Kotlin and C# code](android-datatypes-java-kotlin-csharp.html)
* [Example: Create and use Kotlin source plug-in](AndroidJavaSourcePlugins.html#CreateUseKotlinSourcePlugin)

Supported data types for Java/Kotlin and C# code

Integrating Unity into Android applications

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
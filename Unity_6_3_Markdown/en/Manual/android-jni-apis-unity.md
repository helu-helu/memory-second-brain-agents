* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Developing for Android](android-developing.html)
* [Create and use plug-ins in Android](PluginsForAndroid.html)
* [Calling Java and Kotlin plug-in code from C# scripts](android-plugins-java-code-from-c-sharp.html)
* Java Native Interface APIs in Unity

Calling Java and Kotlin plug-in code from C# scripts

Code examples: Call Java/Kotlin code from C# scripts

# Java Native Interface APIs in Unity

Unity provides low-level and high-level [Java Native Interface](https://developer.android.com/training/articles/perf-jni) (JNI) APIs that allow you to interact with Java code from C# **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts).

## Low-level API

The low-level [AndroidJNI](../ScriptReference/AndroidJNI.html) class wraps JNI calls and provides static methods that directly map to JNI methods. The [AndroidJNIHelper](../ScriptReference/AndroidJNIHelper.html) API provides helper functionality that’s primarily used by the high-level API, but they can be useful in certain situations.

## High-level API

The high-level [AndroidJavaObject](../ScriptReference/AndroidJavaObject.html), [AndroidJavaClass](../ScriptReference/AndroidJavaClass.html), and [AndroidJavaProxy](../ScriptReference/AndroidJavaProxy.html) classes automate a lot of tasks required for JNI calls. They also use caching to make calls to Java faster. The combination of `AndroidJavaObject` and `AndroidJavaClass` is built on top of `AndroidJNI` and `AndroidJNIHelper`, but they also contain additional functionality such as static methods that you can use to access static members of Java classes.

Additionally, Unity provides the [AndroidApplication](../ScriptReference/Android.AndroidApplication.html) class to simplify access to instances of `currentActivity`, `currentContext`, and `currentConfiguration` for your application. This class also allows you to delegate code execution on the UI or main thread based on your application’s requirement.

Instances of `AndroidJavaObject` and `AndroidJavaClass` have a one-to-one mapping to an instance of [java.lang.Object](https://docs.oracle.com/javase/7/docs/api/java/lang/Object.html) and [java.lang.Class](https://docs.oracle.com/javase/7/docs/api/java/lang/Class.html) respectively. They provide three types of interactions with Java/Kotlin code:

* [Call](../ScriptReference/AndroidJavaObject.Call.html) a method.
* [Get](../ScriptReference/AndroidJavaObject.Get.html) the value of a field.
* [Set](../ScriptReference/AndroidJavaObject.Set.html) the value of a field.

Each interaction also has a static version:

* [CallStatic](../ScriptReference/AndroidJavaObject.CallStatic.html) to call a static method.
* [GetStatic](../ScriptReference/AndroidJavaObject.GetStatic.html) to get the value of a static field.
* [SetStatic](../ScriptReference/AndroidJavaObject.SetStatic.html) to set the value of a static field.

When you get the value of a field or call a method that returns a value, you use [generics](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/types/generics) to specify the return type. When you set the value of a field, you also use generics to specify the type of the field that you’re setting. For methods that don’t return a value, there’s a regular, non-generic version of [Call](../ScriptReference/AndroidJavaObject.Call.html).

**Important**: You must access any [non-primitive type](http://developer.android.com/reference/java/lang/Class.html) as an `AndroidJavaObject`. The only exception is a string which you access directly, even though they don’t represent a primitive type in Java.

## Additional resources

* [Code examples: Call Java/Kotlin code from C# scripts](android-high-level-api-code-examples.html)
* [Best practices for calling Java/Kotlin code](android-call-java-kotlin-code-best-practices.html)

Calling Java and Kotlin plug-in code from C# scripts

Code examples: Call Java/Kotlin code from C# scripts

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
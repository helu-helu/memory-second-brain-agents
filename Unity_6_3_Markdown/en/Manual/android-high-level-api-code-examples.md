* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Developing for Android](android-developing.html)
* [Create and use plug-ins in Android](PluginsForAndroid.html)
* [Calling Java and Kotlin plug-in code from C# scripts](android-plugins-java-code-from-c-sharp.html)
* Code examples: Call Java/Kotlin code from C# scripts

Java Native Interface APIs in Unity

Supported data types for Java/Kotlin and C# code

# Code examples: Call Java/Kotlin code from C# scripts

Unity provides high-level APIs such as `AndroidJavaObject`, `AndroidJavaClass`, `AndroidJavaProxy`, and `AndroidApplication` that allow you to interact with Java/Kotlin code from C# **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts).

The following code examples demonstrate how to use these APIs.

## Example 1: Get the hash code for a Java string

The following code example creates an instance of [java.lang.String](http://developer.android.com/reference/java/lang/String.html) initialized with a [string](http://developer.android.com/reference/java/lang/String.html#String(java.lang.StringBuilder)), and retrieves the [hash value](http://developer.android.com/reference/java/lang/String.html#hashCode()) for that string.

```
using UnityEngine;
public class JavaExamples
{
    public static int GetJavaStringHashCode(string text)
    {
        using (AndroidJavaObject jo = new AndroidJavaObject("java.lang.String", text))
        {
            int hash = jo.Call<int>("hashCode");
            return hash;
        }
    }
}
```

This example:

1. Creates an `AndroidJavaObject` that represents a [java.lang.String](http://developer.android.com/reference/java/lang/String.html).
2. The `AndroidJavaObject` constructor takes at least one parameter, which is the name of the class to construct an instance of. Any parameters after the class name are for the constructor call on the object, in this case the `text` parameter from `GetJavaStringHashCode`.
3. Calls [hashCode()](https://developer.android.com/reference/java/lang/String.html#hashCode()) to get the hash code of the string. This call uses the `int` generic type parameter for `Call` because `hashCode()` returns the hash code as an integer.

**Note**: You can’t use dotted notation to instantiate a nested Java class. You must use the `$` separator to instantiate inner classes. For example, Use `android.view.ViewGroup$LayoutParams` or `android/view/ViewGroup$LayoutParams`, where the `LayoutParams` class is nested in the `ViewGroup` class.

## Example 2: Retrieve the application’s cache directory

The following code example retrieves the cache directory for the current application in C# using the `AndroidApplication` class.

```
using UnityEngine;
using UnityEngine.Android;

public class JavaExamples
{
    public static string GetApplicationCacheDirectory()
    {
        using var javaFile = AndroidApplication.currentActivity.Call<AndroidJavaObject>("getCacheDir");
        var cacheDirectory = javaFile.Call<string>("getCanonicalPath");
        return cacheDirectory;
    }
}
```

This example:

1. Uses `AndroidApplication.currentActivity` to access the current Android activity, without explicitly creating `AndroidJavaClass` or `AndroidJavaObject` instances.
2. Calls [getCacheDir()](http://developer.android.com/reference/android/content/Context.html#getCacheDir()) on the Activity object, which returns a [File](https://developer.android.com/reference/java/io/File.html) object that represents the cache directory.
3. Calls [getCanonicalPath()](http://developer.android.com/reference/java/io/File.html#getCanonicalPath()) on the File object can to get the cache directory as a string.

**Note**: This example is for reference purposes. Instead, to access the application’s cache and file directory use the [Application.temporaryCachePath](../ScriptReference/Application-temporaryCachePath.html) and [Application.persistentDataPath](../ScriptReference/Application-persistentDataPath.html) APIs.

## Example 3: Pass data from Java to Unity

The following code example shows how to pass data from Java to Unity using `UnitySendMessage`.

```
using UnityEngine;
using UnityEngine.Android;

public class JavaExamples : MonoBehaviour
{
    private void Start()
    {
        AndroidJNIHelper.debug = true;
        AndroidApplication.unityPlayer.CallStatic("UnitySendMessage", "My GameObject", "JavaMessage", "NewMessage");
    }

    private void JavaMessage(string message)
    {
        Debug.Log("message from java: " + message);
    }
}
```

This example:

1. Uses `AndroidApplication.unityPlayer` to access the Java instance used by an activity without explicitly creating an `AndroidJavaClass` instance.
2. Calls the static`UnitySendMessage` method that’s a member of `com.unity3d.player.UnityPlayer`.

Although you call `UnitySendMessage` from within Unity, it uses Java to relay the message, which then calls back to the native/Unity code to deliver it to the **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) named `My GameObject` which has an attached script that contains a method called `JavaMessage`.

## Additional resources

* [Supported data types for Java/Kotlin and C# code](android-datatypes-java-kotlin-csharp.html)
* [Best practices for calling Java/Kotlin code](android-call-java-kotlin-code-best-practices.html)
* [Example: Create and use Kotlin source plug-in](AndroidJavaSourcePlugins.html#CreateUseKotlinSourcePlugin)

Java Native Interface APIs in Unity

Supported data types for Java/Kotlin and C# code

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
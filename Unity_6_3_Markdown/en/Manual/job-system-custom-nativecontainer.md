* [Programming in Unity](scripting.html)
* [Code optimization](scripting-optimization.html)
* [Write multithreaded code with the job system](job-system.html)
* [Thread safe types](job-system-thread-safe-types.html)
* Implement a custom native container

Introduction to NativeContainer

Copying NativeContainer structures

# Implement a custom native container

To implement a custom native container, you must annotate your type with the the [`NativeContainer`](../ScriptReference/Unity.Collections.LowLevel.Unsafe.NativeContainerAttribute.html) attribute. You should also understand how native containers are integrated with [the safety system](job-system-native-container.html#safety-system).

There are two major elements to implement:

* **Usage tracking:** Allows Unity to keep track of scheduled jobs that use a `NativeContainer` instance, so that it can detect and prevent potential conflicts, such as two jobs writing to the same native container at the same time.
* **Leak tracking:** Detects when a `NativeContainer` isn’t disposed of properly. In this situation, a memory leak happens, where the memory allocated to the `NativeContainer` becomes unavailable for the entire remaining lifetime of the program.

## Implement usage tracking

To access usage tracking in your code, use the [`AtomicSafetyHandle`](../ScriptReference/Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.html) class. `AtomicSafetyHandle` holds a reference to the central information that the safety system stores for a given native container, and is the main way that the methods of a `NativeContainer` interact with the safety system. Because of this, every `NativeContainer` instance must contain an `AtomicSafetyHandle` field named `m_Safety`.

Each `AtomicSafetyHandle` stores a set of flags that indicate what types of operation can be performed on the native container in the current context. When a job contains a `NativeContainer` instance, the job system automatically configures the flags in the `AtomicSafetyHandle` to reflect the way that the native container can be used in that job.

When a job tries to read from a `NativeContainer` instance, the job system calls the `CheckReadAndThrow` method before reading, to confirm that the job has read access to the native container. Similarly, when a job tries to write to a native container, the job system calls `CheckWriteAndThrow` before writing, to check that the job has write access to the native container. Two jobs that have been assigned the same `NativeContainer` instance have separate `AtomicSafetyHandle` objects for that native container, so although they both reference the same set of central information, they can each hold separate flags that indicate what read and write access each job has to the native container.

## Implement leak tracking

Unity’s native code primarily implements leak tracking. It uses the [`UnsafeUtility.MallocTracked`](../ScriptReference/Unity.Collections.LowLevel.Unsafe.UnsafeUtility.MallocTracked.html) method to allocate the memory needed to store `NativeContainer` data, and then uses [`UnsafeUtility.FreeTracked`](../ScriptReference/Unity.Collections.LowLevel.Unsafe.UnsafeUtility.FreeTracked.html) to dispose of it.

In earlier versions of Unity the [`DisposeSentinel`](../ScriptReference/Unity.Collections.LowLevel.Unsafe.DisposeSentinel.html) class provides leak tracking. Unity reports a memory leak when the [garbage collector](performance-garbage-collector.html) collects the `DisposeSentinel` object. To create a `DisposeSentinel`, use the `Create` method, which also initializes the `AtomicSafetyHandle` at the same time. When you use this method, you don’t need to initialize the `AtomicSafetyHandle`. When the `NativeContainer` is disposed of, the `Dispose` method disposes of both the `DisposeSentinel` and the `AtomicSafetyHandle` in a single call.

To identify where the leaked `NativeContainer` was created, you can capture the stack trace of where the memory was originally allocated. To do this, use the [`NativeLeakDetection.Mode`](../ScriptReference/Unity.Collections.NativeLeakDetection.Mode.html) property. You can also access this property in the Editor. To do this, go to **Preferences** > **Jobs** > **Leak Detection Level** and choose the leak detection level you need.

## Nested native containers

The safety system doesn’t support nested native containers in jobs, because the job system can’t correctly configure the `AtomicSafetyHandle` for each individual `NativeContainer` inside the larger `NativeContainer` instance.

To prevent scheduling jobs that use nested native containers, use `SetNestedContainer`, which flags a `NativeContainer` as nested when they contain other `NativeContainer` instances.

## Safety IDs and error messages

The safety system provides error messages that indicate when your code doesn’t adhere to safety constraints. To help make the error messages clearer, you can register a `NativeContainer` object’s name with the safety system.

To register a name, use [`NewStaticSafetyId`](../ScriptReference/Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.NewStaticSafetyId.html), which returns a safety ID that you can pass to [`SetStaticSafetyId`](../ScriptReference/Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.SetStaticSafetyIdl.html). Once you create a safety ID, you can reuse it for all instances of the `NativeContainer`, so a common pattern is to store it in a static member of the container class.

You can also override the error messages for specific safety constraint violations with [`SetCustomErrorMessage`](../ScriptReference/Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.SetCustomErrorMessage.html).

## Additional resources

* [Copying NativeContainer structures](job-system-copy-nativecontainer.html)
* [Custom NativeContainer example](job-system-custom-nativecontainer-example.html)

Introduction to NativeContainer

Copying NativeContainer structures

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
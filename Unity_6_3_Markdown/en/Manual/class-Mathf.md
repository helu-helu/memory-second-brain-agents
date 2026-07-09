* [Programming in Unity](scripting.html)
* [Object-oriented development](object-oriented-development.html)
* [Programming with mathematics](programming-math.html)
* Using common math functions

Moving objects with vectors

Using randomness

# Using common math functions

[Switch to Scripting](../ScriptReference/Mathf.html "Go to Mathf page in the Scripting Reference")

Unity’s Mathf class provides a collection of common math functions, including trigonometric, logarithmic, and other functions commonly required in games and app development.

This page provides an overview of the Mathf class and its common uses when scripting with it. For an exhaustive reference of every member of the Mathf class, see the [Mathf script reference](../ScriptReference/Mathf.html).

## Trigonometric

All Unity’s trigonometry functions work in **radians**.

* [`Sin`](../ScriptReference/Mathf.Sin.html)
* [`Cos`](../ScriptReference/Mathf.Cos.html)
* [`Tan`](../ScriptReference/Mathf.Tan.html)
* [`Asin`](../ScriptReference/Mathf.Asin.html)
* [`Acos`](../ScriptReference/Mathf.Acos.html)
* [`Atan`](../ScriptReference/Mathf.Atan.html)
* [`Atan2`](../ScriptReference/Mathf.Atan2.html)

[`PI`](../ScriptReference/Mathf.PI.html) is available as a constant, and you can multiply by the static values [`Rad2Deg`](../ScriptReference/Mathf.Rad2Deg.html) or [`Deg2Rad`](../ScriptReference/Mathf.Deg2Rad.html) to convert between radians and degrees.

## Powers and Square Roots

Unity provides the common power and square root functions you would expect:
- [`Pow`](../ScriptReference/Mathf.Pow.html)
- [`Sqrt`](../ScriptReference/Mathf.Sqrt.html)
- [`Exp`](../ScriptReference/Mathf.Exp.html)

As well as some useful power-of-two related functions. These are useful when working with common binary data sizes, which are often constrained or optimized to power-of-two values (such as texture dimensions):

* [`ClosestPowerOfTwo`](../ScriptReference/Mathf.ClosestPowerOfTwo.html)
* [`NextPowerOfTwo`](../ScriptReference/Mathf.NextPowerOfTwo.html)
* [`IsPowerOfTwo`](../ScriptReference/Mathf.IsPowerOfTwo.html)

## Interpolation

Unity’s interpolation functions allows you to calculate a value that is some way between two given points. Each of these functions behaves in a different way, suitable for different situations. See the examples in each for more information:

* [`Lerp`](../ScriptReference/Mathf.Lerp.html)
* [`LerpAngle`](../ScriptReference/Mathf.LerpAngle.html)
* [`LerpUnclamped`](../ScriptReference/Mathf.LerpUnclamped.html)
* [`InverseLerp`](../ScriptReference/Mathf.InverseLerp.html)
* [`MoveTowards`](../ScriptReference/Mathf.MoveTowards.html)
* [`MoveTowardsAngle`](../ScriptReference/Mathf.MoveTowardsAngle.html)
* [`SmoothDamp`](../ScriptReference/Mathf.SmoothDamp.html)
* [`SmoothDampAngle`](../ScriptReference/Mathf.SmoothDampAngle.html)
* [`SmoothStep`](../ScriptReference/Mathf.SmoothStep.html)

Note that the [Vector classes](scripting-vectors.html) and the [`Quaternion`](class-Quaternion.html) class all have their own interpolation functions (such as Quaternion.Lerp) which allow you to interpolate positions, directions and rotations in multiple dimensions.

## Limiting and repeating values

These simple helper functions are often useful in games or apps and can save you time when you need to limit values to a certain range or repeat them within a certain range.

* [`Max`](../ScriptReference/Mathf.Max.html) and [`Min`](../ScriptReference/Mathf.Min.html)
* [`Repeat`](../ScriptReference/Mathf.Repeat.html) and [`PingPong`](../ScriptReference/Mathf.PingPong.html)
* [`Clamp`](../ScriptReference/Mathf.Clamp.html) and [`Clamp01`](../ScriptReference/Mathf.Clamp01.html)
* [`Ceil`](../ScriptReference/Mathf.Ceil.html) and [`Floor`](../ScriptReference/Mathf.Floor.html)

## Logarithmic

The [`Log`](../ScriptReference/Mathf.Log.html) function allows you to calculate the logarithm of a specified number, either the natural logarithm or in a specified base. Additionally the [`Log10`](../ScriptReference/Mathf.Log10.html) function returns the base–10 logarithm of the specified number.

## Other functions

For the full list of functions in the Mathf class, see the [Mathf script reference](../ScriptReference/Mathf.html).

Mathf

Moving objects with vectors

Using randomness

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
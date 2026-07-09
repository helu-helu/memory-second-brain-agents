* [Platform development](PlatformSpecific.html)
* [iOS](iphone.html)
* [Introducing iOS](ios-introducing.html)
* iOS requirements and compatibility

Introducing iOS

How Unity builds iOS applications

# iOS requirements and compatibility

Learn about the system requirements and compatibility information for iOS to make sure you’re aware of any limitations for developing a Unity application for this platform.

## iOS version support

Unity supports iOS 15 and above. For more information, refer to [`PlayerSettings.iOS-targetOSVersionString`](../ScriptReference/PlayerSettings.iOS-targetOSVersionString.html).

## Xcode version support

When developing for iOS, it’s recommended to use Xcode version 16 or later. For more information, refer to [Xcode](https://developer.apple.com/support/xcode/).

## Graphics API support

iOS devices support [Metal](https://developer.apple.com/documentation/metal). For more information, refer to [Metal Graphics API](Metal.html).

## Audio compression

Unity supports importing a variety of source format sound files. However, when importing these files (with the exception of tracker files), they are always re-encoded to the build target format. By default, this format is Vorbis, though this can be overridden per platform to other formats (ADPCM, MP3, etc.) if required. Vorbis playback provides better **compression**A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](texture-choose-format-by-platform.html), [Animation Compression](class-AnimationClip.html#AssetProperties), [Audio Compression](class-AudioClip.html), [Build Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) and quality for iOS compared with MP3 playback.

## ASTC instead of DXT texture compression

Unity iOS does not support DXT textures. Instead, ASTC, ETC2, and ETC **texture compression**3D Graphics hardware requires Textures to be compressed in specialized formats which are optimized for fast Texture sampling. [More info](texture-choose-format-by-platform.html)  
See in [Glossary](Glossary.html#texturecompression) are natively supported by iPhone/iPad devices. For more information about iOS **texture formats**A file format for handling textures during real-time rendering by 3D graphics hardware, such as a graphics card or mobile device. [More info](texture-choose-format-by-platform.html)  
See in [Glossary](Glossary.html#textureformat), refer to [texture import settings](class-TextureImporter.html) and [texture compression format](texture-choose-format-by-platform.html#ios-and-tvos).

## iPadOS multitasking

iPadOS supports multitasking modes that allow users to run applications in split-screen or windowed layouts. The available modes vary by iPadOS version: Split View and Slide Over (iPadOS 9 to iPadOS 18), Stage Manager (iPadOS 16 and later), and Windowed Apps (iPadOS 26 and later). Unity applications support all multitasking modes and respond correctly when the available space changes. For more information, refer to [iPad multitasking modes](iphone-API.html#ipad-multitasking-modes).

Introducing iOS

How Unity builds iOS applications

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
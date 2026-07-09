* [Assets and media](assets-and-media.html)
* [Types of assets](AssetTypes.html)
* [Models](models.html)
* [Creating models outside of Unity](CreatingDCCAssets.html)
* Model file formats reference

Creating models outside of Unity

Support for proprietary model file formats

# Model file formats reference

Unity uses the `.fbx` file format as its internal importing chain. It’s best practice to use the `.fbx` file format whenever possible, and not use proprietary **model file** formats in production.

## Supported model file formats

Unity supports the following standard and proprietary model file formats.

### Standard file formats

Unity can read the following standard 3D file formats:

* [.fbx](https://www.autodesk.com/products/fbx/overview)
* [.dae (Collada)](https://www.khronos.org/collada/)
* .dxf
* .obj.

These file formats are widely supported. They’re also often smaller than the proprietary equivalent, which makes your project size smaller, and faster to iterate over.

You can also re-import exported .fbx or .obj files into your 3D modeling software of choice to check that all the information has been exported correctly.

### Proprietary file formats

Don’t use proprietary file formats in production and export to the `.fbx`format wherever possible. If you need to include these files as part of your project, then Unity can import proprietary files from the following 3D modeling software, and then convert them into `.fbx` files:

* [Autodesk Maya](https://www.autodesk.com/products/maya/overview)
* [Blender](https://www.blender.org/)
* [Modo](https://www.foundry.com/products/modo)
* [Cheetah3D](https://www.cheetah3d.com/)

For more information, refer to [Importing proprietary model files into Unity](HOWTO-ImportObjectsFrom3DApps.html).

The following applications don’t use `.fbx` as an intermediary. Unity converts them into `.fbx` files before importing them into the Unity Editor:

* [SketchUp](https://www.sketchup.com/)
* [SpeedTree](https://unity.com/products/speedtree)
* [Autodesk® 3ds Max®](https://www.autodesk.com/products/3ds-max/overview)

For more information, see the documentation on [SketchUp Import Settings](class-SketchUpImporter.html) and [SpeedTree Import Settings](class-SpeedTreeImporter.html).

## Unsupported model file formats

Unity doesn’t provide built-in support for Cinema4D files. To use Cinema4D files in Unity, export them from the proprietary software as `.fbx` files.

Assets saved as `.ma`, `.mb`, `.max`, `.c4d`, or `.blend` files fail to import unless you have the corresponding 3D modeling software installed on your computer. This means that everybody working on your Unity project must have the correct software installed.

## Additional resources

* [Model Import Settings window](class-FBXImporter.html)
* [Importing objects from 3D applications](HOWTO-ImportObjectsFrom3DApps.html)
* [Creating and using Materials](Materials.html)
* [Working with textures](Textures.html)
* [Asset workflow](AssetWorkflow.html)

Creating models outside of Unity

Support for proprietary model file formats

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
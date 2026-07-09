* [Platform development](PlatformSpecific.html)
* [Cross-platform features and considerations](cross-platform-features.html)
* [Device Simulator](device-simulator.html)
* Adding a device

Simulated classes

Extending the device simulator

# Adding a device

To add a new device to the Device Simulator, you create a device definition and a device overlay.

A device definition is a text file with the `.device` extension in your Unity project. It contains JSON that describes the properties of a device.

A device overlay is an image that contains the border of the device screen, together with notches, punchouts, and any other additions to the screen rectangle. You can optionally use it with a device definition to visualize how hardware elements obstruct the device screen, and to determine when touch inputs fail as a result.

**Note**: Unity includes built-in device definitions that represent common screen characteristics (such as notch styles, punch hole positions, and screen sizes). These are intended for testing layout and interaction patterns. For production testing, we recommend to always validate your application on actual target devices.

## Creating a device definition

A device definition is a JSON file that represents the device. It has both required properties and some optional properties. If a device definition file contains any errors, the errors appear in the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) when you select the file.

### Schema

| **Property** | **Required** | **Description** |
| --- | --- | --- |
| **friendlyName** | Yes | The name to display in the UI for this device. |
| **version** | Yes | Indicates the version of the device definition file. Currently, the version is `1`. |
| **screens** | Yes | A list of objects that each describe a screen to simulate the device for. This must contain at least one screen. For information about the schema of each screen object, see [screen](#screen). |
| **systemInfo** | Yes | An object that describes the capabilities of the device. The values in this object map to [SystemInfo](../ScriptReference/SystemInfo.html). For information about the schema of the systemInfo object, see [systemInfo](#systeminfo). |

#### screen

| **Property** | **Required** | **Description** |
| --- | --- | --- |
| **width** | Yes | The width, in **pixels**The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html) See in [Glossary](Glossary.html#pixel), of the screen. |
| **height** | Yes | The height, in pixels, of the screen. |
| **navigationBarHeight** | No | The height, in pixels, of the on-screen Android navigation bar that appears on some devices when not in fullscreen. |
| **dpi** | Yes | The dpi of the screen. |
| **orientations** | No | A list of objects that each describe an orientation the screen can simulate. If you don’t set a value for this property, the screen supports all orientations. For information about the schema of each orientation object, see [orientation](#orientation). |
| **presentation** | No | An object that describes the device overlay. For information about the schema of this object, see [presentation](#presentation). |

#### orientation

| **Properties** | **Required** | **Description** |
| --- | --- | --- |
| **orientation** | Yes | The screen orientation. The value of this property is a number that maps to the [ScreenOrientation](../ScriptReference/ScreenOrientation.html) enum. |
| **safeArea** | No | A [Rect](../ScriptReference/Rect.html) that determines the safe area of the screen. If you don’t set a value for this property, the simulator assumes the entire screen is safe. |
| **cutouts** | No | A list of [Rect](../ScriptReference/Rect.html)s that specify areas of the screen that aren’t functional for displaying content. |

#### presentation

| **Property** | **Required** | **Description** |
| --- | --- | --- |
| **overlayPath** | No | A relative path from the device definition file to an image to use as the device overlay. |
| **borderSize** | No | The distance, in pixels, from the overlay to where the screen begins. |

#### systeminfo

The properties in this object describe the capabilities and system information of the device. Since they describe the system information, many of them map to properties in [SystemInfo](../ScriptReference/Device.SystemInfo.html).

| **Property** | **Required** | **Description** |
| --- | --- | --- |
| **deviceModel** | No | See [Device.SystemInfo.deviceModel](../ScriptReference/Device.SystemInfo-deviceModel.html). |
| **deviceType** | No | See [Device.SystemInfo.deviceType](../ScriptReference/Device.SystemInfo-deviceType.html). |
| **operatingSystem** | Yes | See [Device.SystemInfo.operatingSystem](../ScriptReference/Device.SystemInfo-operatingSystem.html). |
| **operatingSystemFamily** | No | See [Device.SystemInfo.operatingSystemFamily](../ScriptReference/Device.SystemInfo-operatingSystemFamily.html). |
| **processorCount** | No | See [Device.SystemInfo.processorCount](../ScriptReference/Device.SystemInfo-processorCount.html). |
| **processorFrequency** | No | See [Device.SystemInfo.processorFrequency](../ScriptReference/Device.SystemInfo-processorFrequency.html). |
| **processorType** | No | See [Device.SystemInfo.processorType](../ScriptReference/Device.SystemInfo-processorType.html). |
| **supportsAccelerometer** | No | See [Device.SystemInfo.supportsAccelerometer](../ScriptReference/Device.SystemInfo-supportsAccelerometer.html). |
| **supportsAudio** | No | See [Device.SystemInfo.supportsAudio](../ScriptReference/Device.SystemInfo-supportsAudio.html). |
| **supportsGyroscope** | No | See [Device.SystemInfo.supportsGyroscope](../ScriptReference/Device.SystemInfo-supportsGyroscope.html). |
| **supportsLocationService** | No | See [Device.SystemInfo.supportsLocationService](../ScriptReference/Device.SystemInfo-supportsLocationService.html). |
| **supportsVibration** | No | See [Device.SystemInfo.supportsVibration](../ScriptReference/Device.SystemInfo-supportsVibration.html). |
| **systemMemorySize** | No | See [Device.SystemInfo.systemMemorySize](../ScriptReference/Device.SystemInfo-systemMemorySize.html). |
| **unsupportedIdentifier** | No | See [Device.SystemInfo.unsupportedIdentifier](../ScriptReference/Device.SystemInfo-unsupportedIdentifier.html). |
| **graphicsDependentData** | No | A list of objects that each describe graphics APIs that the device supports. For information about the schema of each object, see [graphicsDependentData](#graphicsdependentdata). |

#### graphicsDependentData

The properties in the object describe a graphics API that the device supports.

| **Property** | **Required** | **Description** |
| --- | --- | --- |
| **graphicsDeviceType** | Yes | See [Device.SystemInfo.graphicsDeviceType](../ScriptReference/Device.SystemInfo-graphicsDeviceType.html). |
| **graphicsMemorySize** | No | See [Device.SystemInfo.graphicsMemorySize](../ScriptReference/Device.SystemInfo-graphicsMemorySize.html). |
| **graphicsDeviceName** | No | See [Device.SystemInfo.graphicsDeviceName](../ScriptReference/Device.SystemInfo-graphicsDeviceName.html). |
| **graphicsDeviceVendor** | No | See [Device.SystemInfo.graphicsDeviceVendor](../ScriptReference/Device.SystemInfo-graphicsDeviceVendor.html). |
| **graphicsDeviceID** | No | See [Device.SystemInfo.graphicsDeviceID](../ScriptReference/Device.SystemInfo-graphicsDeviceID.html). |
| **graphicsDeviceVendorID** | No | See [Device.SystemInfo.graphicsDeviceVendorID](../ScriptReference/Device.SystemInfo-graphicsDeviceVendorID.html). |
| **graphicsUVStartsAtTop** | No | See [Device.SystemInfo.graphicsUVStartsAtTop](../ScriptReference/Device.SystemInfo-graphicsUVStartsAtTop.html). |
| **graphicsDeviceVersion** | No | See [Device.SystemInfo.graphicsDeviceVersion](../ScriptReference/Device.SystemInfo-graphicsDeviceVersion.html). |
| **graphicsShaderLevel** | No | See [Device.SystemInfo.graphicsShaderLevel](../ScriptReference/Device.SystemInfo-graphicsShaderLevel.html). |
| **graphicsMultiThreaded** | No | See [Device.SystemInfo.graphicsMultiThreaded](../ScriptReference/Device.SystemInfo-graphicsMultiThreaded.html). |
| **renderingThreadingMode** | No | See [Device.SystemInfo.renderingThreadingMode](../ScriptReference/Device.SystemInfo-renderingThreadingMode.html). |
| **hasHiddenSurfaceRemovalOnGPU** | No | See [Device.SystemInfo.hasHiddenSurfaceRemovalOnGPU](../ScriptReference/Device.SystemInfo-hasHiddenSurfaceRemovalOnGPU.html). |
| **hasDynamicUniformArrayIndexingInFragmentShaders** | No | See [Device.SystemInfo.hasDynamicUniformArrayIndexingInFragmentShaders](../ScriptReference/Device.SystemInfo-hasDynamicUniformArrayIndexingInFragmentShaders.html). |
| **supportsShadows** | No | See [Device.SystemInfo.supportsShadows](../ScriptReference/Device.SystemInfo-supportsShadows.html). |
| **supportsRawShadowDepthSampling** | No | See [Device.SystemInfo.supportsRawShadowDepthSampling](../ScriptReference/Device.SystemInfo-supportsRawShadowDepthSampling.html). |
| **supportsMotionVectors** | No | See [Device.SystemInfo.supportsMotionVectors](../ScriptReference/Device.SystemInfo-supportsMotionVectors.html). |
| **supports3DTextures** | No | See [Device.SystemInfo.supports3DTextures](../ScriptReference/Device.SystemInfo-supports3DTextures.html). |
| **supports2DArrayTextures** | No | See [Device.SystemInfo.supports2DArrayTextures](../ScriptReference/Device.SystemInfo-supports2DArrayTextures.html). |
| **supports3DRenderTextures** | No | See [Device.SystemInfo.supports3DRenderTextures](../ScriptReference/Device.SystemInfo-supports3DRenderTextures.html). |
| **supportsCubemapArrayTextures** | No | See [Device.SystemInfo.supportsCubemapArrayTextures](../ScriptReference/Device.SystemInfo-supportsCubemapArrayTextures.html). |
| **copyTextureSupport** | No | See [Device.SystemInfo.copyTextureSupport](../ScriptReference/Device.SystemInfo-copyTextureSupport.html). |
| **supportsComputeShaders** | No | See [Device.SystemInfo.supportsComputeShaders](../ScriptReference/Device.SystemInfo-supportsComputeShaders.html). |
| **supportsGeometryShaders** | No | See [Device.SystemInfo.supportsGeometryShaders](../ScriptReference/Device.SystemInfo-supportsGeometryShaders.html). |
| **supportsTessellationShaders** | No | See [Device.SystemInfo.supportsTessellationShaders](../ScriptReference/Device.SystemInfo-supportsTessellationShaders.html). |
| **supportsInstancing** | No | See [Device.SystemInfo.supportsInstancing](../ScriptReference/Device.SystemInfo-supportsInstancing.html). |
| **supportsHardwareQuadTopology** | No | See [Device.SystemInfo.supportsHardwareQuadTopology](../ScriptReference/Device.SystemInfo-supportsHardwareQuadTopology.html). |
| **supports32bitsIndexBuffer** | No | See [Device.SystemInfo.supports32bitsIndexBuffer](../ScriptReference/Device.SystemInfo-supports32bitsIndexBuffer.html). |
| **supportsSparseTextures** | No | See [Device.SystemInfo.supportsSparseTextures](../ScriptReference/Device.SystemInfo-supportsSparseTextures.html). |
| **supportedRenderTargetCount** | No | See [Device.SystemInfo.supportedRenderTargetCount](../ScriptReference/Device.SystemInfo-supportedRenderTargetCount.html). |
| **supportsSeparatedRenderTargetsBlend** | No | See [Device.SystemInfo.supportsSeparatedRenderTargetsBlend](../ScriptReference/Device.SystemInfo-supportsSeparatedRenderTargetsBlend.html). |
| **supportedRandomWriteTargetCount** | No | See [Device.SystemInfo.supportedRandomWriteTargetCount](../ScriptReference/Device.SystemInfo-supportedRandomWriteTargetCount.html). |
| **supportsMultisampledTextures** | No | See [Device.SystemInfo.supportsMultisampledTextures](../ScriptReference/Device.SystemInfo-supportsMultisampledTextures.html). |
| **supportsMultisampleAutoResolve** | No | See [Device.SystemInfo.supportsMultisampleAutoResolve](../ScriptReference/Device.SystemInfo-supportsMultisampleAutoResolve.html). |
| **supportsTextureWrapMirrorOnce** | No | See [Device.SystemInfo.supportsTextureWrapMirrorOnce](../ScriptReference/Device.SystemInfo-supportsTextureWrapMirrorOnce.html). |
| **usesReversedZBuffer** | No | See [Device.SystemInfo.usesReversedZBuffer](../ScriptReference/Device.SystemInfo-usesReversedZBuffer.html). |
| **npotSupport** | No | See [Device.SystemInfo.npotSupport](../ScriptReference/Device.SystemInfo-npotSupport.html). |
| **maxTextureSize** | No | See [Device.SystemInfo.maxTextureSize](../ScriptReference/Device.SystemInfo-maxTextureSize.html). |
| **maxCubemapSize** | No | See [Device.SystemInfo.maxCubemapSize](../ScriptReference/Device.SystemInfo-maxCubemapSize.html). |
| **maxComputeBufferInputsVertex** | No | See [Device.SystemInfo.maxComputeBufferInputsVertex](../ScriptReference/Device.SystemInfo-maxComputeBufferInputsVertex.html). |
| **maxComputeBufferInputsFragment** | No | See [Device.SystemInfo.maxComputeBufferInputsFragment](../ScriptReference/Device.SystemInfo-maxComputeBufferInputsFragment.html). |
| **maxComputeBufferInputsGeometry** | No | See [Device.SystemInfo.maxComputeBufferInputsGeometry](../ScriptReference/Device.SystemInfo-maxComputeBufferInputsGeometry.html). |
| **maxComputeBufferInputsDomain** | No | See [Device.SystemInfo.maxComputeBufferInputsDomain](../ScriptReference/Device.SystemInfo-maxComputeBufferInputsDomain.html). |
| **maxComputeBufferInputsHull** | No | See [Device.SystemInfo.maxComputeBufferInputsHull](../ScriptReference/Device.SystemInfo-maxComputeBufferInputsHull.html). |
| **maxComputeBufferInputsCompute** | No | See [Device.SystemInfo.maxComputeBufferInputsCompute](../ScriptReference/Device.SystemInfo-maxComputeBufferInputsCompute.html). |
| **maxComputeWorkGroupSize** | No | See [Device.SystemInfo.maxComputeWorkGroupSize](../ScriptReference/Device.SystemInfo-maxComputeWorkGroupSize.html). |
| **maxComputeWorkGroupSizeX** | No | See [Device.SystemInfo.maxComputeWorkGroupSizeX](../ScriptReference/Device.SystemInfo-maxComputeWorkGroupSizeX.html). |
| **maxComputeWorkGroupSizeY** | No | See [Device.SystemInfo.maxComputeWorkGroupSizeY](../ScriptReference/Device.SystemInfo-maxComputeWorkGroupSizeY.html). |
| **maxComputeWorkGroupSizeZ** | No | See [Device.SystemInfo.maxComputeWorkGroupSizeZ](../ScriptReference/Device.SystemInfo-maxComputeWorkGroupSizeZ.html). |
| **supportsAsyncCompute** | No | See [Device.SystemInfo.supportsAsyncCompute](../ScriptReference/Device.SystemInfo-supportsAsyncCompute.html). |
| **supportsGraphicsFence** | No | See [Device.SystemInfo.supportsGraphicsFence](../ScriptReference/Device.SystemInfo-supportsGraphicsFence.html). |
| **supportsAsyncGPUReadback** | No | See [Device.SystemInfo.supportsAsyncGPUReadback](../ScriptReference/Device.SystemInfo-supportsAsyncGPUReadback.html). |
| **supportsParallelPSOCreation** | No | See [Device.SystemInfo.supportsParallelPSOCreation](../ScriptReference/Device.SystemInfo-supportsParallelPSOCreation.html). |
| **supportsRayTracing** | No | See [Device.SystemInfo.supportsRayTracing](../ScriptReference/Device.SystemInfo-supportsRayTracing.html). |
| **supportsRayTracingShaders** | No | See [Device.SystemInfo.supportsRayTracingShaders](../ScriptReference/Device.SystemInfo-supportsRayTracingShaders.html). |
| **supportsInlineRayTracing** | No | See [Device.SystemInfo.supportsInlineRayTracing](../ScriptReference/Device.SystemInfo-supportsInlineRayTracing.html). |
| **supportsSetConstantBuffer** | No | See [Device.SystemInfo.supportsSetConstantBuffer](../ScriptReference/Device.SystemInfo-supportsSetConstantBuffer.html). |
| **hasMipMaxLevel** | No | See [Device.SystemInfo.hasMipMaxLevel](../ScriptReference/Device.SystemInfo-hasMipMaxLevel.html). |
| **supportsMipStreaming** | No | See [Device.SystemInfo.supportsMipStreaming](../ScriptReference/Device.SystemInfo-supportsMipStreaming.html). |
| **usesLoadStoreActions** | No | See [Device.SystemInfo.usesLoadStoreActions](../ScriptReference/Device.SystemInfo-usesLoadStoreActions.html). |

#### Minimal device definition

The following device definition contains every required property and no optional properties. This is the minimum device definition you can have.

**Note**: This device definition doesn’t provide orientation data, so the simulator assumes the device supports all orientations and that the safe area covers the entire screen.

```
{
    "friendlyName": "Minimal Device",
    "version": 1,
    "screens": [
        {
            "width": 1080,
            "height": 1920,
            "dpi": 450.0
        }
    ],
    "systemInfo": {
        "operatingSystem": "Android"
    }
}
```

#### Complete device definition

The following device definition contains every required and optional property.

```
{
    "friendlyName": "Apple iPhone XR",
    "version": 1,
    "screens": [
        {
            "width": 828,
            "height": 1792,
            "navigationBarHeight": 0,
            "dpi": 326.0,
            "orientations": [
                {
                    "orientation": 1,
                    "safeArea": {
                        "serializedVersion": "2",
                        "x": 0.0,
                        "y": 68.0,
                        "width": 828.0,
                        "height": 1636.0
                    },
                    "cutouts": [
                        {
                            "serializedVersion": "2",
                            "x": 184.0,
                            "y": 1726.0,
                            "width": 460.0,
                            "height": 66.0
                        }
                    ]
                },
                {
                    "orientation": 3,
                    "safeArea": {
                        "serializedVersion": "2",
                        "x": 88.0,
                        "y": 42.0,
                        "width": 1616.0,
                        "height": 786.0
                    },
                    "cutouts": [
                        {
                            "serializedVersion": "2",
                            "x": 0.0,
                            "y": 184.0,
                            "width": 66.0,
                            "height": 460.0
                        }
                    ]
                },
                {
                    "orientation": 4,
                    "safeArea": {
                        "serializedVersion": "2",
                        "x": 88.0,
                        "y": 42.0,
                        "width": 1616.0,
                        "height": 786.0
                    },
                    "cutouts": [
                        {
                            "serializedVersion": "2",
                            "x": 1726.0,
                            "y": 184.0,
                            "width": 66.0,
                            "height": 460.0
                        }
                    ]
                }
            ],
            "presentation": {
                "overlayPath": "Apple iPhone 11_Overlay.png",
                "borderSize": {
                    "x": 51.0,
                    "y": 51.0,
                    "z": 51.0,
                    "w": 51.0
                }
            }
        }
    ],
    "systemInfo": {
        "deviceModel": "iPhone11,8",
        "deviceType": 1,
        "operatingSystem": "iOS 12.0",
        "operatingSystemFamily": 0,
        "processorCount": 6,
        "processorFrequency": 0,
        "processorType": "arm64e",
        "supportsAccelerometer": true,
        "supportsAudio": true,
        "supportsGyroscope": true,
        "supportsLocationService": true,
        "supportsVibration": true,
        "systemMemorySize": 2813,
        "unsupportedIdentifier": "n/a",
        "graphicsDependentData": [
            {
                "graphicsDeviceType": 16,
                "graphicsMemorySize": 1024,
                "graphicsDeviceName": "Apple A12 GPU",
                "graphicsDeviceVendor": "Apple",
                "graphicsDeviceID": 0,
                "graphicsDeviceVendorID": 0,
                "graphicsUVStartsAtTop": true,
                "graphicsDeviceVersion": "Metal",
                "graphicsShaderLevel": 50,
                "graphicsMultiThreaded": true,
                "renderingThreadingMode": 0,
                "hasHiddenSurfaceRemovalOnGPU": true,
                "hasDynamicUniformArrayIndexingInFragmentShaders": true,
                "supportsShadows": true,
                "supportsRawShadowDepthSampling": true,
                "supportsMotionVectors": true,
                "supports3DTextures": true,
                "supports2DArrayTextures": true,
                "supports3DRenderTextures": true,
                "supportsCubemapArrayTextures": true,
                "copyTextureSupport": 31,
                "supportsComputeShaders": true,
                "supportsGeometryShaders": false,
                "supportsTessellationShaders": true,
                "supportsInstancing": true,
                "supportsHardwareQuadTopology": false,
                "supports32bitsIndexBuffer": true,
                "supportsSparseTextures": false,
                "supportedRenderTargetCount": 8,
                "supportsSeparatedRenderTargetsBlend": true,
                "supportedRandomWriteTargetCount": 8,
                "supportsMultisampledTextures": 1,
                "supportsMultisampleAutoResolve": false,
                "supportsTextureWrapMirrorOnce": 0,
                "usesReversedZBuffer": true,
                "npotSupport": 2,
                "maxTextureSize": 16384,
                "maxCubemapSize": 16384,
                "maxComputeBufferInputsVertex": 8,
                "maxComputeBufferInputsFragment": 8,
                "maxComputeBufferInputsGeometry": 0,
                "maxComputeBufferInputsDomain": 8,
                "maxComputeBufferInputsHull": 8,
                "maxComputeBufferInputsCompute": 8,
                "maxComputeWorkGroupSize": 1024,
                "maxComputeWorkGroupSizeX": 1024,
                "maxComputeWorkGroupSizeY": 1024,
                "maxComputeWorkGroupSizeZ": 1024,
                "supportsAsyncCompute": false,
                "supportsGraphicsFence": true,
                "supportsAsyncGPUReadback": true,
                "supportsParallelPSOCreation": true,
                "supportsRayTracing": false,
                "supportsRayTracingShaders": false,
                "supportsInlineRayTracing": false,
                "supportsSetConstantBuffer": true,
                "hasMipMaxLevel": true,
                "supportsMipStreaming": true,
                "usesLoadStoreActions": true,
                "supportedTextureFormats": [1, 2, 3, 4, 5],
                "supportedRenderTextureFormats": [1, 2, 3, 4, 5],
                "ldrGraphicsFormat": 59,
                "hdrGraphicsFormat": 74
            }
        ]
    }
}
```

## Creating a device overlay

A device overlay is an image that contains the border of the device screen and other features such as notches, punchouts, and any other additions to the screen rectangle. You can optionally use it with a device definition to visualize how hardware elements obstruct the device screen, and to determine when touch inputs fail as a result.

The Device Simulator interprets transparent pixels as areas of the screen you can tap, and opaque pixels of any other color as areas that the hardware obstructs. The texture itself can be any shape.

The following examples show device overlays for two iPhone models.

![iPhone 8 overlay, displaying Unity’s default skybox filling the area of the iPhone 8 screen where you can tap](../uploads/Main/device-simulator-overlay-iphone8.png)


iPhone 8 overlay, displaying Unity’s default skybox filling the area of the iPhone 8 screen where you can tap


![iPhone XS overlay, displaying Unity’s default skybox filling the area of the iPhone XS screen where you can tap](../uploads/Main/device-simulator-overlay-iphonexs.png)


iPhone XS overlay, displaying Unity’s default skybox filling the area of the iPhone XS screen where you can tap

**Note**: To mimic what you see when you use a device overlay, these examples display Unity’s default **skybox**A special type of Material used to represent skies. Usually six-sided. [More info](sky-landing.html)  
See in [Glossary](Glossary.html#Skybox) in the area of the screen where you can tap. In a real device overlay, these pixels should be transparent.

### Using a device overlay

After you create a device overlay texture, to use it with a device definition you must first import the device overlay texture file into your project.

**Note**: When the Device Simulator loads a device overlay texture, it attempts to enable **Read/Write** for it. If this isn’t possible, the Device Simulator displays the texture but can’t use the texture to mask input. This means that if you click on notches and other areas of the screen that the device overlay should mask, the Device Simulator detects input. To ensure this doesn’t happen, when you import the device overlay texture, enable **Read/Write** in the Texture Import Settings window.

When the device overlay texture is in your project, open the device definition file and, in the object that defines a screen the device supports, add the [presentation](#presentation) property. Here, set the path to the image file (`overlayPath`) and the size of the borders (`borderSize`). For an example of how to do this, see the following device definition file:

```
{
    "friendlyName": "Minimal Device with Overlay",
    "version": 1,
    "screens": [
        {
            "width": 1080,
            "height": 1920,
            "dpi": 450.0,
            "presentation": {
                "overlayPath": "Overlays/MinimalDeviceOverlay.png",
                "borderSize": {
                    "x": 51.0,
                    "y": 51.0,
                    "z": 51.0,
                    "w": 130.0
                }
            }
        }
    ],
    "systemInfo": {
        "operatingSystem": "Android"
    }
}
```

**Note**: The path to the device overlay texture file can be relative to the device definition file, or relative to the directory that contains the **Assets** or **Packages** directory in your Unity project. For example, if the device definition file is in the **Assets/Devices** directory and the device overlay file is in the **Assets/Devices/Overlays** directory, the following file paths are both valid:

* Relative to the device definition file: **Overlays/MinimalDeviceOverlay.png**
* Relative to the directory that contains the **Assets** directory: **Assets/Devices/Overlays/MinimalDeviceOverlay.png**

Simulated classes

Extending the device simulator

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
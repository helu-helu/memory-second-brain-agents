* [Video and cutscenes](Video.html)
* [Video sources](video-sources.html)
* Video Clip Importer reference

Set up transparent videos in Unity

Video Player

# Video Clip Importer reference

Configure the settings of the Video Clip Importer to transcode video files into different formats, ensuring compatibility with your target platforms. For more information on transcoding video files, refer to [Transcoding video files](video-transcoding.html).

**Note:** The transcoding process can result in longer build times and lower video quality.

## Video Clip Importer settings

The following settings are available in the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window when you select a video file in your project.

| **Property** | **Description** |
| --- | --- |
| **sRGB (Color Texture)** | Choose whether the VideoPlayer converts sRGB to Linear color space when it loads the video data into textures. Unity enables this setting by default because most video clips store color data in sRGB color space. For non-color video clips, disable this setting to avoid unnecessary conversions. |
| **Transcode** | Transcode the source content into a format that’s compatible with the target platform.   **Note:** Verify that the source format is compatible with each target platform. For more information, refer to [Video file compatibility](VideoSources-FileCompatibility.html). |

The following settings are available after you enable the **Transcode** property.

| **Property** | **Description** |
| --- | --- |
| **Dimensions** | Control how Unity resizes the source content in **pixels**The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html) See in [Glossary](Glossary.html#pixel). **Aspect ratio**The relationship of an image’s proportional dimensions, such as its width and height. See in [Glossary](Glossary.html#aspectratio) is controllable for all options. For information about the different resize options, refer to [Dimensions options](#dimension-options). |
| **Codec** | Choose the codec to encode the video track. For option details, refer to [Codec options](#codec-options). For information about codec support, refer to [Video file compatibility](VideoSources-FileCompatibility.html). |
| **Bitrate Mode** | How much data a video uses per second. Choose a bitrate relative to the chosen codec’s baseline profile. For more information about the bitrate types, refer to [Bitrate Mode options](#bitrate-mode-options).   **Note:** Higher bitrates provide a higher quality video, but impose a higher load on network connections or storage. |
| **Spatial Quality** | How sharp and detailed the image looks within each video frame. Choose whether to reduce the spatial quality of video images during transcoding. For information about the different options, refer to [Spatial Quality options](#spatial-quality-options).   **Note:** Resizing images uses less storage but also results in blurriness during playback. |
| **Keep Alpha** | Preserve the [alpha channel](VideoTransparency.html) and encode it during transcoding so you can use the video even if the target platform doesn’t natively support videos with transparency.   **Note:** This property is only visible for sources that have an alpha channel. |
| **Deinterlace** | Interlaced videos have two time samples in each frame: one in odd-numbered lines, and one in even-numbered lines. Deinterlacing converts interlaced video into progressive frames for smoother display.    Control how much Unity deinterlaces interlaced sources during transcoding. For details about the options, refer to [Deinterlace options](#deinterlace-options). |
| **Flip Horizontally** | Flip the source content along a horizontal axis when transcoding. |
| **Flip Vertically** | Flip the source content along a vertical axis when transcoding. |
| **Import Audio** | Import the audio tracks when transcoding.   **Note:** This property is available only for sources that have audio tracks. |

### Dimensions options

Set **Dimensions** to one of the following options:

| **Property** | **Description** |
| --- | --- |
| **Original Size** | Keep the original size of the source. |
| **Three Quarter Res** | Resize the source to three quarters of its original width and height. |
| **Half Res** | Resize the source to half of its original width and height. |
| **Quarter Res** | Resize the source to a quarter of its original width and height. |
| **Square 1024** | Resize the source to a 1024 x 1024 square image. |
| **Square 512** | Resize the source to a 512 x 512 square image. |
| **Square 256** | Resize the source to a 256 x 256 square image. |
| **Custom Size** | Resize the source to a custom width and height. |

### Codec options

Set **Codec** to one of the following options:

| **Property** | **Description** |
| --- | --- |
| **Auto** | Choose the best video codec for the target platform automatically. |
| **H264** | Choose the MPEG–4 Advanced Video Coding (AVC) video codec, supported by hardware on most platforms. |
| **H265** | Choose the MPEG-H Part 2, or High Efficiency Video Coding (HEVC), video codec, supported by hardware on some platforms. |
| **VP8** | Choose the VP8 video codec, supported by software on most platforms, and by hardware on Android and Web. |

### Bitrate Mode options

Set **Bitrate Mode** to one of the following options:

| **Property** | **Description** |
| --- | --- |
| **Low** | Choose a low bitrate. |
| **Medium** | Choose a medium bitrate. |
| **High** | Choose a high bitrate. |

### Spatial Quality options

Set **Spatial Quality** to one of the following options:

| **Property** | **Description** |
| --- | --- |
| **Low Spatial Quality** | The image is significantly reduced in size during transcoding (typically to a quarter of its original dimensions), and then expanded back to its original size upon playback. This is the highest amount of resizing, meaning it saves the most storage space but results in the largest amount of blurriness upon playback. |
| **Medium Spatial Quality** | The image is moderately reduced in size during transcoding (typically to half of its original dimensions), and then expanded back to its original size upon playback. Although there’s some resizing, images are less blurry than those that use the **Low Spatial Quality** option, and there’s some reduction in required storage space. |
| **High Spatial Quality** | Keep the image’s original size. The image isn’t reduced in size during transcoding, and therefore maintains the video’s original level of visual clarity. |

### Deinterlace options

Set **Deinterlace** to one of the following:

| **Property** | **Description** |
| --- | --- |
| **Off** | The source isn’t interlaced and there’s no processing to perform. This is the default setting. |
| **Even** | Take the even lines of each frame and interpolate them to create missing content. Drops the odd lines. |
| **Odd** | Take the odd lines of each frame and interpolate them to create missing content. Drops the even lines. |

---

## Additional resources

* [Video file compatibility with the Unity Editor](VideoSources-FileCompatibility.html)
* [Video file compatibility with target platforms](video-sources-compatibility-target-platforms.html)
* [Video encoding compatibility](video-encoding-compatibility.html)
* [Understand video files](VideoSources-VideoFiles.html)

Set up transparent videos in Unity

Video Player

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
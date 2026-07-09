* [Materials and shaders](materials-and-shaders.html)
* [Custom textures](Textures-landing.html)
* [2D texture arrays](class-Texture2DArray.html)
* Create a 2D texture array in a script

Create a 2D texture array

Render to a 2D texture array

# Create a 2D texture array in a script

To create a 2D texture array in a script, use the [`Texture2DArray`](../ScriptReference/Texture2DArray.html) API.

For example:

```
// Set the 2D texture array parameters
int width = 32;
int height = 32;
int slices = 8;
TextureFormat format = TextureFormat.RGBA32;
bool mipChain = false;

// Create a 2D texture array with a width and height of 32 pixels, and 8 slices
Texture2DArray textureArray = new Texture2DArray(width, height, slices, format, mipChain);
```

## Example

The following example creates an instance of the 2D texture array class, sets each slice to a different color, then saves the 2D texture array to your project as a serialized asset file.

```
using UnityEditor;
using UnityEngine;

public class ExampleEditorScript : MonoBehaviour
{
    [MenuItem("Examples/Create2DTextureArray")]
    static void Create2DTextureArray()
    {
        // Set the texture parameters
        int width = 32;
        int height = 32;
        int slices = 3;
        TextureFormat format = TextureFormat.RGBA32;
        bool mipChain = false;

        // Create the texture array and apply the parameters
        Texture2DArray textureArray = new Texture2DArray(width, height, slices, format, mipChain);

        // Create a 2D array of colors, to store color data for each pixel in a slice
        Color[] colors = new Color[width * height];

        // Loop through each slice
        for (int slice = 0; slice < slices; slice++)
        {
            // Generate a random color
            Color randomColor = new Color(Random.value, Random.value, Random.value, 1f);

            // Set all the pixels in the color array to the random color
            for (int color = 0; color < colors.Length; color++)
            {
                colors[color] = randomColor;
            }

            // Set the pixels of the slice to the color array
            textureArray.SetPixels(colors, slice);
        }

        // Apply the changes to the texture array by uploading the updated pixels to the GPU
        textureArray.Apply();

        // Save the texture array to your Unity project
        AssetDatabase.CreateAsset(textureArray, "Assets/Example2DTextureArray.asset");
    }
}
```

Create a 2D texture array

Render to a 2D texture array

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
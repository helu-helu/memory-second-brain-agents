* [Cameras](Cameras.html)
* [Excluding hidden objects with occlusion culling](OcclusionCulling-landing.html)
* [Configure culling with the CullingGroup API](CullingGroupAPI-landing.html)
* Get culling results

Create a Culling Group

Troubleshooting occlusion culling

# Get culling results

### Receiving results via the onStateChanged callback

The most efficient way to respond to spheres changing their visibility or distance state is to use the onStateChanged callback field. Set this to a function which takes a CullingGroupEvent structure as an argument; it will then be called after culling is complete, for each sphere that has changed state. The members of the CullingGroupEvent structure tell you about the previous and new states of the sphere.

```
group.onStateChanged = StateChangedMethod;

private void StateChangedMethod(CullingGroupEvent evt)
{
    if(evt.hasBecomeVisible)
        Debug.LogFormat("Sphere {0} has become visible!", evt.index);
    if(evt.hasBecomeInvisible)
        Debug.LogFormat("Sphere {0} has become invisible!", evt.index);
}
```

### Receiving results via the CullingGroup Query API

In addition to the onStateChanged delegate, the CullingGroup provides an API for retrieving the latest visibility and distance results of any sphere in the bounding spheres array. To check the states of a single sphere, use the IsVisible and GetDistance methods:

```
bool sphereIsVisible = group.IsVisible(0);
int sphereDistanceBand = group.GetDistance(0);
```

To check the states of multiple spheres, you can use the QueryIndices method. This method scans a continuous range of spheres to find ones that match a given visibility or distance state.

```
// Allocate an array to hold the resulting sphere indices - the size of the array determines the maximum spheres checked per call
int[] resultIndices = new int[1000];
// Also set up an int for storing the actual number of results that have been placed into the array
int numResults = 0;

// Find all spheres that are visible
numResults = group.QueryIndices(true, resultIndices, 0);
// Find all spheres that are in distance band 1
numResults = group.QueryIndices(1, resultIndices, 0);
// Find all spheres that are hidden in distance band 2, skipping the first 100
numResults = group.QueryIndices(false, 2, resultIndices, 100);
```

Remember that the information retrieved by the query API is only updated when the **camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) used by the CullingGroup actually performs its culling.

Create a Culling Group

Troubleshooting occlusion culling

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)
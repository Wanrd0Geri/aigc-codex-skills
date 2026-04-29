# 八维诊断标准 / 8-Dimension Diagnostic Criteria

This file is the diagnostic rubric. Walk through every dimension in order. For each, decide ✅ Working / ⚠️ Weak / ❌ Broken, and note specifically what's happening.

These dimensions are not arbitrary — they are the choices a cinematographer (DP) actively controls on every frame. AI-generated images tend to fail because the model averages across many sources and ends up making *no choice* — which reads as flat or incoherent.

---

## 1. Light direction & hardness / 光线方向与硬度

**What to look for:**
- Where is the dominant light coming from? (top / side / back / front / multiple)
- How hard is it? (sharp shadow edges = hard light; soft falloff = soft light)
- Does the direction match the implied environment? (forest at dawn ≠ harsh top-down sun)
- Is there one clear key, or does the image have 3-4 competing key lights with no hierarchy?

**❌ Broken signs:** Multiple equally-strong light sources fighting each other; god rays so intense they look like a special effect rather than ambient light; lighting direction contradicts the scene logic (e.g., night forest with full noon sun).

**⚠️ Weak signs:** Direction is correct but hardness is wrong (e.g., should be soft moonlight but rendered as hard spotlight); light is unmotivated (no visible source justifies it).

**✅ Working signs:** One clear key with a defined direction; fill light is subordinate; hardness matches the source's physical nature (sun = hard, overcast = soft, moon = soft, candle = soft & warm).

**The fix language:** "single soft key from [direction] at [angle], with subtle ambient fill at [ratio]"

---

## 2. Lighting ratio & black point / 光比与黑位

**What to look for:**
- What's the ratio between the brightest and darkest parts of the subject's face?
- Are the shadows actually black, or are they grey? (lifted blacks = TV news look, true blacks = film look)
- Does the highlight roll off smoothly, or does it clip into pure white?

**❌ Broken signs:** Image is entirely mid-tones, no real black anywhere; everything sits in 30-70% gray; "everything visible" lighting (like a video game tutorial level).

**⚠️ Weak signs:** Black point exists but is timid; some clipped highlights but no rich shadow detail; ratio is too even (1:2 ratio reads as flat — cinema usually wants 1:4 to 1:16 for drama).

**✅ Working signs:** Clear separation between lit and shadowed sides of the face; black point sits at IRE 0-15; highlights have texture, not blown out; ratio supports the mood (high contrast for drama, low contrast for melancholy).

**The fix language:** "high-contrast lighting ratio 1:8, with deep crushed blacks and protected highlight detail"

---

## 3. Color temperature unity / 色温统一度

**What to look for:**
- How many color temperatures are competing in the image?
- Do shadows and highlights agree on a temperature, or do shadows trend one way and highlights another deliberately (split-toning) vs. accidentally (color pollution)?
- Is there a "muddy" hue that doesn't belong? (most common: yellow-green pollution in night scenes, magenta pollution in skin tones)

**❌ Broken signs:** Three or more unrelated color casts in different parts of the frame; green-tinted fog in a scene that should be cold blue; skin pulling magenta in a scene graded teal.

**⚠️ Weak signs:** One stray color cast that wasn't intended; subject is correctly colored but environment leaks an off-hue.

**✅ Working signs:** Either monochromatic (all one temperature family) or deliberately split-toned (e.g., cool shadows + warm highlights, or teal-and-orange) with clean separation.

**The fix language:** "unified cool blue-cyan color palette across all elements, removing any green/yellow tint from atmosphere and shadows"

---

## 4. Overall exposure & midtone control / 整体明度与曝光

**What to look for:**
- Where does the average luminance sit? (low-key = dark scene; high-key = bright scene; mid = neutral)
- Does the exposure choice match the emotional intent?
- Are midtones controlled, or has the image been pushed bright across the board to "make sure you can see it"?

**❌ Broken signs:** Night scenes that look like dusk because the model brightened them to be "readable"; overall exposure 1-2 stops too hot, washing out atmosphere.

**⚠️ Weak signs:** Exposure is in the right direction but a half-stop off; midtones are bright but darks aren't anchoring properly.

**✅ Working signs:** A night scene reads as night; a noon scene reads as noon; the eye is led by exposure, not just by composition.

**The fix language:** "low-key exposure, overall image pushed 1.5 stops darker, with controlled midtones at IRE 25-40"

---

## 5. Atmospheric perspective / 大气透视

**What to look for:**
- Is there fog/haze/mist? Where does it sit in depth?
- Does it create a depth gradient (background more obscured than foreground), or is it uniform across the frame (which flattens depth)?
- Is the haze too bright? (over-bright haze becomes a wall, not air)

**❌ Broken signs:** Uniform fog covering the whole frame at the same density; fog brighter than the subjects, making it a glowing curtain; fog with the wrong color (warm fog in a cold scene).

**⚠️ Weak signs:** Fog density is right but it lacks gradient; midground and background are equally hazed.

**✅ Working signs:** Foreground is clear, midground softly veiled, background dissolved — creating three distinct depth planes; haze color matches the scene's color temperature; haze is darker than the brightest light source.

**The fix language:** "atmospheric haze with depth gradient — clear foreground, 30% haze midground, 70% haze background — haze color tuned to match scene temperature"

---

## 6. Subject-environment light integration / 主体与环境的光线融合

**What to look for:**
- Do the subjects look lit by the *same* light as the environment, or do they look pasted on?
- Is there rim light / edge light on the subjects that ties them to the background brightness?
- Do the shadows under the subjects belong to the same light source as the environment shadows?

**This is the #1 tell of "AI image" — subjects rendered by the model with their own internal lighting that disagrees with the background.**

**❌ Broken signs:** Subjects are uniformly lit while environment has dramatic light/shadow; subjects have no rim light despite a strong backlight in the scene; subject's shadow direction disagrees with environmental shadow direction.

**⚠️ Weak signs:** Subjects are roughly integrated but lack edge definition; the rim light is the wrong color for the source.

**✅ Working signs:** Subjects have clear rim/edge light from the same direction as the environmental key; subject shadows fall on the environment correctly; subject's color temperature shifts to match the local lighting (e.g., blue moonlight should turn skin slightly cool).

**The fix language:** "integrate subjects into the scene lighting — add cool blue rim light from upper-left matching the moonlight source, allow ambient bounce to subtly cool the subjects' shadows"

---

## 7. Compositional depth & layer rhythm / 构图与景深节奏

**What to look for:**
- Are there clear foreground / midground / background layers?
- Is the eye led somewhere by composition, or does it bounce around?
- Is the subject given enough negative space, or is the frame cluttered?

**❌ Broken signs:** Everything sits at the same depth; subject is centered with no compositional hierarchy; background elements compete with the subject for attention.

**⚠️ Weak signs:** Layers exist but the rhythm is even (foreground, midground, background equally weighted); no clear focal point.

**✅ Working signs:** A clear foreground anchor, a midground containing the subject, a background that recedes; eye flows along a deliberate path.

**The fix language:** "preserve compositional layers — subjects in midground, soft background recession, optional foreground silhouette element for depth"

---

## 8. Color emotion consistency / 色彩情绪一致性

**What to look for:**
- Does the color palette emotionally match what the scene is trying to say?
- Are the colors making a coherent statement, or are they just whatever the model defaulted to?

**❌ Broken signs:** Tense scene rendered in cheerful warm colors; melancholy scene rendered with high saturation; horror scene rendered with cozy palette.

**⚠️ Weak signs:** Right direction but undercommitted (e.g., wants to be cold and threatening but only gets to "neutral cool").

**✅ Working signs:** Palette commits to one emotional register; saturation, temperature, and contrast all reinforce the same feeling.

**The fix language:** "commit to a [adjective] color emotion — [specific palette description supporting that emotion]"

---

## How to use this rubric

Don't just check boxes — **rank the findings by impact**. A single ❌ on dimension 6 (subject integration) usually hurts an image more than three ⚠️s on dimensions 7-8. The transformation prompt should target the top 3-5 issues, not all 8.

If two dimensions are giving conflicting fix directions (e.g., dimension 4 says "push darker" but dimension 6 says "add rim light to subjects"), there is no conflict — these stack: push the overall scene darker AND add a localized rim light. The model handles this fine if the prompt is clearly structured.

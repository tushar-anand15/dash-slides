# dash-slides

Make truly interactive slides in Python with Dash.

---

This is a Dash app with built in slide navigation, logo, web title, etc. Just run `python index.py` in a terminal to see it work!

## To use:

1. Give `dash-slides` a star on GitHub. This step is very important.
1. Download, clone, or fork `dash-slides/`.
1. Delete the example slides and add your own slides (individual Dash apps) in `slides/` as files with content and associated callbacks, with a filename like `<slide_name>.py`.
   - Slide names must be valid Python variable names e.g. `example.py` or `_intro5.py` but not `my great slide.py` or `5 people.py`.
   - Each slide's content is named `content = html.Div...` (similar to multipage Dash app where each page has a `layout = html.Div...`
   - Do not remove `from app import app` from any slide.
3. In `presentation.py`:
   - List your slides' names in order (without the `.py`) in `slide_order`
   - e.g. `['intro','template','last_slide','end']`
2. Store custom functions, utilities, objects, etc. in `custom_utilities/` or however else you'd like.
4. `pip install dash dash-bootstrap-components`
   - the navigation depends on it

Then run it like a normal Dash app with `python index.py` or using Gunicorn or whatever else you'd normally use with Dash or Flask.

How this would look:
```
# files structure
/dash-slides
   /assets
   /slides
      intro.py
      body1.py
      body2.py
      conclusion.py
   index.py
   app.py
   presentation.py

# in /slides/presentation.py
slide_order = [
    'intro',
    'body1',
    'body2',
    'conclusion'
]
...
```

![example pic](https://raw.githubusercontent.com/russellromney/dash-slides/master/example/assets/example_pic.png)

---

## More custom stuff

**Logo:** Replace `assets/logo.png` with your own file named `logo.png` for your logo to appear on all slides.

**Favicon:** Like a normal Dash app, replace `assets/favicon.ico` with your own favicon for an even more custom experience.

**Title:** Give your presentation a title by changing `presentation_title`.

**Custom navigation text:** Replace `prev_text` and `next_text` values with new words to have any navigation text you want.


---

Made with :heart: by Russell Romney in Madison, WI.

> Shoutout to dash_bootstrap_components, which is used to make navigation pretty

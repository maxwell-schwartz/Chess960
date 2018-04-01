# Chess960 Generator

Generates one of the 960 possible starting positions for chess960 (aka Fischer Random Chess) https://en.wikipedia.org/wiki/Chess960.

### Contents

- `src/chess960.py` generates all 960 legal starting positions and writes these to a file to be used in the frontend.
- `Images/` contains all the images used to render the board and pieces.
- `style.css` formats the images and keeps everything in place.
- `index.html` contains a `vue.js` script that uses the file created in step 1 to determine the placement of the pieces.
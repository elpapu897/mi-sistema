# Redesign 'Tu Jugador' Screen

The current 'Tu Jugador' screen appears stacked and basic (as seen in the first image), especially on wider screens or depending on the CSS breakpoints. The goal is to completely redesign this screen to look like a premium, state-of-the-art console football game (as seen in the second image).

## Proposed Changes

I will modify the HTML and CSS inside `ladiez.html`.

### 1. CSS Structure Updates
*   **`.pjWrap` Background**: Update the dark blue gradient and lighting effects to perfectly match the deep stadium aesthetic shown in the target image.
*   **Layout Adjustments (`.pjTop`)**: Ensure a strict grid/flexbox layout that places the 3D player on the left and the information card on the right, overriding mobile-first stacking where appropriate or adapting it smoothly.
*   **Top Navigation**: Add a new CSS class for the top header and tabs (`INFORMACIÓN`, `APARIENCIA`, etc.) to match the top-left section of the target image.
*   **Info Card (`.pjFicha`)**: Restyle the player info card on the right. Give it a clean dark background, a precise layout for the Name, Nickname, Position, Club, and Overall Rating (`10 GLB`). Make the table rows (`Posición`, `Pie hábil`, etc.) match the clean, minimalistic style.
*   **Tabs & Options (`.pjTabs` and `.pjOpts`)**: Style the bottom customization tabs (`CARA`, `PELO`, `DETALLES`, etc.) to be clean blocks with a bright neon-green active state.

### 2. HTML Structure Updates (in `R.personalizar`)
*   Replace the generic `<h2>Tu jugador</h2>` with the bold, uppercase `TU JUGADOR` title and the new top tab menu (`INFORMACIÓN`, `APARIENCIA`, `EQUIPACIÓN`, `ANIMACIONES`).
*   Reorganize the `pjFicha` HTML to place the overall rating prominently in the top right, match the new typography, and restyle the `SORPRENDEME` button with the exact visual treatment (dice icon, gradient border).
*   Clean up the "girá con el dedo" overlay text to be less intrusive or hidden if not needed on desktop.

## User Review Required

> [!IMPORTANT]
> The target image uses a landscape (wide) aspect ratio layout. I will optimize this design so it looks exactly like the image on wider screens (tablets/desktops/landscape phones). On vertical phone screens, I will maintain the premium aesthetic but stack the character and the card vertically to fit the screen.

## Verification Plan

I will test the game locally by running `ladiez.html` in a browser and ensuring the `Tu Jugador` screen perfectly mimics the layout, typography, neon-green accents, and premium feel of the second reference image.

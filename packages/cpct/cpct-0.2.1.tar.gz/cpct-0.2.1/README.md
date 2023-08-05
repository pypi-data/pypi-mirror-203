# cpct (Chipy's PathOfExile Chaos Tool)

[![PyPI - Version](https://img.shields.io/pypi/v/cpct.svg)](https://pypi.org/project/cpct)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cpct.svg)](https://pypi.org/project/cpct)

-----

**Table of Contents**

- [Installation](#installation)
- [Why Chaos Recipe](#Why_Chaos_Recipe)
- [Features](#Features)
- [Features Requests](#FeaturesRequests)
- [License](#license)
- [chipy.dev](https://chipy.dev)

## Installation

*PIP install method*
```console
pip install cpct --upgrade -t c:/chipy-scripts/
run C:/chipy-scripts/cpct/cpct.py OR C:/chipy-scripts/cpct/_START_HERE.cmd
```
*GitHub download*
```console
Download from [GitHub](https://github.com/iamchipy/chipys-pathofexile-chaos-tool) 
Unzip to a desired location
run _install_requirements.py (to install needed packages to global env)
run cpct.py OR _START_HERE.cmd
```

**You will need to request a Client Secrect from me (PLEASE keep this private, if client secrects get shared it'll invalidate the whole app on GGG's side)**

- Go to Settings > Request client secrect > Enter your DiscordName#1234 (this is how I'll reach you)
- Enter the client secrect and then attempt to log-in (top left) 
- One logged in select your Chaos Recipe tab from the dropdown menus (only supports a single tab right now)
- Then select how many recipe sets you are aiming for before turning them in (I recommend 4-8 but NO less than 2)

# Why Chaos Recipe
As many wealthy players have already said; the chaos recipe is a trap. They suggest that it's simply not time efficient. If you spend 30 minutes just farming unidentified items to complete 2x chaos recipes then thats roughly 8chaos/hour. The argument is that in an hour of running T1 rolled maps you should easily make more than that. *WHICH IS TRUE* 

However, there are some cases where I'd venture to ammend that sentiment. There are definitely times when chaos recipe is still helpful. For these edge cases there are things you should and shouldn't do to make it worth your time:

**You should NOT . . .**

- **Do NOT** have chaos recipe as your only/primary objective as you play *(As a rule of thumb)* 
- **Do NOT** waste your time selling identified sets ( 1c instead of 2c is almost NEVER worth it in trade leagues )
- **Do NOT** waste your time selling recipe in single sets

**You SHOULD . . .**

- **Do** passively collect choas recipe items and just toss them in a dump tab
- **Do** keep your jewlery unidentified in trade leagues ( Statistically 2c is almost ALWAYS able to buy you a better ring/amulet than what you will ID )
- **Do** collect a minimum of 2x complete recipe sets before selling them as you can fit 2x complete sets in your inventory

**Edge cases . . .**

- You may need to continue chaos recipe if you play SSF (Solo Self Found) and you need chaos for crafting or map device
- Early in every league the trade value of chaos is still relatively strong (good value for invested time) so for the first week it's still worth your time if you do it efficiently and passively
- If you are a new player and you aren't fast or efficient and some basic currency to improve your gear would help you progress (remeber to aim to outgrow chaos recipe as your income source)


## Features
[![GUI](https://chipy.dev/res/ctcp_gui.png)](#)

**OAuth2 permissions** 

- The is the appropriate way to get correct permissions and access
- No need to dig out and reuse your webbrowser's sessionID token (which is against ToC)
- Can be easily revoked from your [PoE Profile](https://www.pathofexile.com/my-account/applications) at any time

**Automated itemfilter updating** 

- Works with existing items filters to modify/overlay recipe highlights
- Only affects item backgrouns so your existing border and text colors will be unaffected
- It can also update those when you enter a new zone to high items types that you have enough of

**Itemfilter color selection** 

- In app filter customization now allows you to select any color you like for each slot
- *PLANNED* Filters boarders/text/size will be customizable too

**Itemfilter mode selection** 

- Default will add it's recipe items colors to existing filter
- Disabled will no affect your filter at all
- *PLANNED* FilterBlade will edit the chaos recipe section of a filterblade filter


## Feature Requests

[ ] Integration with FilterBlade filters (rather than just added it's own)
[ ] Integration with Online filters (if possible)
[ ] Additional filter color/font/size customization options
[ ] Add alpha slider to picker
[ ] Rebuild item reading system into ENUM to easy class changes
[ ] Add 2-H weapon options to filter
[ ] Add league and tab memory
[ ] Add never hide rings/ammy options
[ ] Add sets ready counters (with ilvl checking)
[ ] Add feature to indicate next items
[ ] Fix auto refresh not renewing the list in the GUI display
[ ] Add auto check limiter to read and log last checked zone entry
[ ] Fix GUI and regal filter to be i75 (not 70)
[ ] Write for Steam Version and path options!

 

## License
`cpct` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

## DISCLAIMER:
This product isn't affiliated with or endorsed by Grinding Gear Games in any way.

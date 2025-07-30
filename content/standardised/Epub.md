---
aliases: 
category: LANG
date modified: 27-07-2025
tags:
  - system
---
An **EPUB** (short for *electronic publication*) file is a widely used **open eBook format** that is designed for **reflowable content**, meaning it can adapt its layout to fit various screen sizes-unlike PDFs, which preserve a fixed layout.

### Key Features of EPUB
- **Reflowable Text:** The content adjusts to screen size, font preferences, and orientation. This is ideal for smartphones, tablets, and e-readers like Kobo or Apple Books.
- **HTML + CSS Based:** Internally, an EPUB file is a compressed archive (`.zip`) that contains HTML files, images, stylesheets, metadata, and a manifest.
- **Navigation:** It supports **table of contents**, **internal links**, and **chapters** for easy navigation.
- **Supports Rich Media:** EPUB 3 can include audio, video, interactive elements, and MathML.

### How EPUB Shows “Pages”

EPUB doesn't have fixed "pages" like PDF. Instead:

- The **reading software** (like Apple Books, Calibre, or Kobo) dynamically **splits content into pages** based on screen size, font size, and user settings.
- Pages can vary in number depending on:
  - Device screen resolution
  - Font size or style
  - Margin settings

Because of this, you can't refer to a fixed page number universally across devices.
### EPUB vs PDF

| Feature                | EPUB                                 | PDF                                |
|------------------------|--------------------------------------|------------------------------------|
| Layout                 | Reflowable                           | Fixed                              |
| Usability on small screens | Excellent                         | Poor                               |
| Internal format        | HTML + CSS + XML                     | PostScript-based (binary)          |
| Navigation             | Flexible (TOC, links, metadata)      | Static (can have TOC, but fixed)   |

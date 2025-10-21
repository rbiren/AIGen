# AIGen Frontend UI Preview

## Visual Design

### Color Scheme
- **Background**: Beautiful purple gradient (`linear-gradient(135deg, #667eea 0%, #764ba2 100%)`)
- **Primary Accent**: Gold/Yellow (#ffd700) for the logo icon
- **Cards**: White with transparency effects and shadows
- **Text**: High contrast white on gradient, dark on white cards

---

## Component Layout

### 1. HEADER (Top of Page)
```
┌─────────────────────────────────────────────────────────┐
│  ⚡ AIGen                                               │
│  AI-Powered Photo Processing                            │
└─────────────────────────────────────────────────────────┘
```
- Glassmorphism effect (blur + transparency)
- Lightning bolt icon in gold with glow effect
- Large "AIGen" branding text
- Subtitle below

### 2. UPLOAD SECTION
```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│                      ☁️                                  │
│                                                         │
│               Upload Your Images                        │
│                                                         │
│     Drag and drop your images here, or click to browse  │
│     Supports: JPG, PNG, GIF, WebP                       │
│                                                         │
│                 [ Choose Files ]                        │
│                                                         │
└─────────────────────────────────────────────────────────┘
```
- Large white card with dashed purple border
- Cloud upload icon at top
- Hover effects: lifts up, border brightens
- Drag-over state: purple tint, border highlights
- Button with purple gradient background

**When Processing:**
```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│                      ⟳                                  │
│                (spinning)                               │
│                                                         │
│               Processing images...                      │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### 3. GALLERY SECTION (When images uploaded)
```
Gallery Header:
┌─────────────────────────────────────────────────────────┐
│  Your Images (3)                        [ Clear All ]   │
└─────────────────────────────────────────────────────────┘

Image Grid (Responsive):
┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐
│          │  │          │  │          │  │          │
│  Image   │  │  Image   │  │  Image   │  │  Image   │
│   [🗑]    │  │   [🗑]    │  │   [🗑]    │  │   [🗑]    │
│          │  │          │  │          │  │          │
│photo1.jpg│  │photo2.png│  │photo3.jpg│  │photo4.gif│
│ 2.3 MB   │  │ 1.8 MB   │  │ 3.1 MB   │  │ 892 KB   │
└──────────┘  └──────────┘  └──────────┘  └──────────┘
```
- Grid layout (4 columns on desktop, 2 on mobile)
- White cards with shadows
- Square image previews
- Trash icon appears on hover (red circular button)
- Smooth hover animations (lift + scale image)
- Filename and file size below each image

### 4. EMPTY STATE (No images)
```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│                      🖼️                                  │
│                                                         │
│        No images yet. Upload some to get started!       │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### 5. FOOTER
```
┌─────────────────────────────────────────────────────────┐
│           Powered by AI | Built with React              │
└─────────────────────────────────────────────────────────┘
```
- Semi-transparent dark background
- Centered text

---

## Interactions & Animations

### Upload Area
- **Hover**: Slight lift (translateY -2px), enhanced shadow
- **Drag Over**: Scale 1.02, purple background tint, bright border
- **Click**: Opens file picker

### Image Cards
- **Hover on Card**: Lift up 5px, enhanced shadow
- **Hover on Image**: Slight zoom (scale 1.05)
- **Hover on Overlay**: Red delete button fades in
- **Click Delete**: Confirmation, then smooth removal

### Buttons
- **Upload Button**: Purple gradient, shadow, lifts on hover
- **Clear All**: Transparent with white border, fills on hover
- **Delete Button**: Red circular, scales up on hover

---

## Responsive Design

### Desktop (>768px)
- Gallery: 4 columns (250px each)
- Upload area: 60px padding
- Large icons and text

### Mobile (≤768px)
- Gallery: 2 columns (150px each)
- Upload area: 40px padding
- Smaller icons and text
- Stacked header elements

---

## Technical Features

✅ Drag and drop file upload
✅ Multi-file selection
✅ File type validation (images only)
✅ Real-time preview
✅ File size display
✅ Loading states
✅ Empty states
✅ Error handling
✅ Smooth animations
✅ Responsive layout
✅ Accessibility features


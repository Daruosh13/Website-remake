with open('C:/Users/M. Gustave/piksort/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Insertion point: right after the Material Tracking item closes,
# before the w-dyn-items closing div
# Pattern: last </div></div> of material-tracking item, then </div></div></nav>
INSERT_AFTER = 'material-tracking" class="image-full"></a></div></div>'
INSERT_BEFORE = '</div></div></nav></div><div data-hover="true"'

# Verify both anchors exist
if INSERT_AFTER not in content:
    print("ERROR: INSERT_AFTER not found"); exit(1)
if INSERT_BEFORE not in content:
    print("ERROR: INSERT_BEFORE not found"); exit(1)

# Quality/checklist icon as SVG data URI (clipboard with checkmark)
ICON_URI = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='currentColor'%3E%3Cpath d='M9 11l3 3L22 4M21 12v7a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2h11'/%3E%3C/svg%3E"

# Professional laptop+dashboard image (Unsplash — office analytics shot)
IMG_SRC = "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=602&h=400&q=85"
IMG_SRC_500 = "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=500&h=333&q=85"

ARROW_URL = "https://cdn.prod.website-files.com/691a64dbefbb704b5550e811/693698544a457dff127fb7f3_Arrow%20Right%20No%20Line.svg"

new_item = (
'<div role="listitem" class="nav_dropdown-item w-dyn-item">'
  '<div class="nav_dropdown-item-head">'
    '<div class="nav_dropdown-head-icon">'
      '<div class="w-embed">'
        f'<div class="icon-mask icon-1x1-32" style="mask-image: url(\'{ICON_URI}\');"></div>'
      '</div>'
    '</div>'
    '<div class="nav_dropdown-head-text">'
      '<p class="heading-style-h6">Quality Completion</p>'
      '<div class="text-color-gray-700">'
        '<p class="text-size-small">Real-time % completion dashboards that give every stakeholder a clear view of project progress.</p>'
      '</div>'
    '</div>'
    '<div class="nav_dropdown-item-img-outer">'
      '<div class="nav_dropdown-item-img">'
        '<div class="nav_dropdown-item-img-inner">'
          f'<img src="{IMG_SRC}" loading="lazy" alt="Quality Completion dashboard on laptop in office"'
          f' sizes="100vw" srcset="{IMG_SRC_500} 500w, {IMG_SRC} 602w"'
          ' class="image-full is-cover"/>'
        '</div>'
      '</div>'
    '</div>'
  '</div>'
  '<div class="nav_dropdown-item-icon">'
    f'<div STYLE="mask-image: url({ARROW_URL});" class="icon-mask icon-1x1-20"></div>'
  '</div>'
  '<div class="nav-dropdown_link-block w-embed">'
    '<a href="/products/quality-completion" class="image-full"></a>'
  '</div>'
'</div>'
)

# Replace: insert new item just before the closing tags of the products list
old = INSERT_AFTER + INSERT_BEFORE
new = INSERT_AFTER + new_item + INSERT_BEFORE

if old not in content:
    print("ERROR: combined anchor not found in content"); exit(1)

new_content = content.replace(old, new, 1)

with open('C:/Users/M. Gustave/piksort/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Quality Completion product added to nav dropdown")

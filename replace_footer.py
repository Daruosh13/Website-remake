with open('C:/Users/M. Gustave/piksort/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_footer_start = '<footer data-wf--section-footer'
old_footer_end   = '</footer>'

start_idx = content.find(old_footer_start)
end_idx   = content.find(old_footer_end, start_idx) + len(old_footer_end)

if start_idx == -1:
    print('ERROR: footer start not found'); exit(1)

LINKEDIN_SVG = (
  '<svg width="100%" height="100%" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">'
  '<g clip-path="url(#clip-ft-li)"><path d="M6.9375 5.00002C6.93724 5.53046 6.72627 6.03906 6.35101 '
  '6.41394C5.97575 6.78883 5.46693 6.99929 4.9365 6.99902C4.40607 6.99876 3.89746 6.78779 3.52258 '
  '6.41253C3.14769 6.03727 2.93724 5.52846 2.9375 4.99802C2.93777 4.46759 3.14873 3.95899 3.52399 '
  '3.5841C3.89925 3.20922 4.40807 2.99876 4.9385 2.99902C5.46893 2.99929 5.97754 3.21026 6.35242 '
  '3.58552C6.72731 3.96078 6.93777 4.46959 6.9375 5.00002ZM6.9975 8.48002H2.9975V21H6.9975V8.48002Z'
  'M13.3175 8.48002H9.3375V21H13.2775V14.43C13.2775 10.77 18.0475 10.43 18.0475 14.43V21H21.9975V13.07'
  'C21.9975 6.90002 14.9375 7.13002 13.2775 10.16L13.3175 8.48002Z" fill="currentColor"/></g>'
  '<defs><clipPath id="clip-ft-li"><rect width="24" height="24" fill="white"/></clipPath></defs></svg>'
)

new_footer = (
'<footer class="section is-footer">'
'<div class="padding-global">'
'<div class="w-layout-blockcontainer container-large w-container">'

# ── Top section: brand + columns ──
'<div class="ft-top">'

# Brand column
'<div class="ft-brand">'
'<a href="/" aria-label="Piksort" class="footer_brand w-inline-block">'
'<img src="https://cdn.prod.website-files.com/691a64dbefbb704b5550e811/6923f46417b125834bb9d43f_Footer%20Brand.svg" loading="lazy" alt="Piksort" class="ft-logo"/>'
'</a>'
'<p class="ft-tagline">Empowering industrial teams with clarity and confidence.</p>'
'<div class="ft-socials">'
'<a href="https://www.linkedin.com/company/piksort/" target="_blank" rel="noopener" aria-label="Piksort on LinkedIn" class="ft-social-link">'
'<div class="icon-1x1-24 w-embed">' + LINKEDIN_SVG + '</div>'
'</a>'
'</div>'
'</div>'

# Link columns
'<div class="ft-cols">'

'<div class="ft-col">'
'<div class="ft-col-title">Products</div>'
'<ul class="ft-links">'
'<li><a href="/products/remote-camera" class="ft-link">Time Lapse Cameras</a></li>'
'<li><a href="/products/dedicated-camera-application" class="ft-link">Progress Reporting</a></li>'
'<li><a href="/products/material-tracking" class="ft-link">Material Tracking</a></li>'
'</ul>'
'</div>'

'<div class="ft-col">'
'<div class="ft-col-title">Solutions</div>'
'<ul class="ft-links">'
'<li><a href="/solutions/project-managers" class="ft-link">Project Managers</a></li>'
'<li><a href="/solutions/engineers" class="ft-link">Engineers</a></li>'
'<li><a href="/case-studies" class="ft-link">Case Studies</a></li>'
'</ul>'
'</div>'

'<div class="ft-col">'
'<div class="ft-col-title">Resources</div>'
'<ul class="ft-links">'
'<li><a href="resources.html" class="ft-link">ITP Templates</a></li>'
'<li><a href="resources.html" class="ft-link">ITR Checklists</a></li>'
'<li><a href="resources.html" class="ft-link">Podcast</a></li>'
'</ul>'
'</div>'

'<div class="ft-col">'
'<div class="ft-col-title">Company</div>'
'<ul class="ft-links">'
'<li><a href="/contact" class="ft-link">Contact Us</a></li>'
'<li><a href="/security" class="ft-link">Security</a></li>'
'<li><a href="https://app.piksort.com/" target="_blank" rel="noopener" class="ft-link">Log In</a></li>'
'<li><a href="https://www.linkedin.com/company/piksort/" target="_blank" rel="noopener" class="ft-link">LinkedIn</a></li>'
'</ul>'
'</div>'

'</div>'  # ft-cols
'</div>'  # ft-top

# ── Divider ──
'<div class="ft-divider"></div>'

# ── Bottom bar ──
'<div class="ft-bottom">'
'<div class="ft-copy">\u00a9 2025 Piksort. All rights reserved.</div>'
'<div class="ft-legals">'
'<a href="#" class="ft-legal-link">Terms</a>'
'<a href="#" class="ft-legal-link">Privacy Policy</a>'
'<a href="#" class="ft-legal-link">Cookies</a>'
'</div>'
'</div>'

'</div>'  # container
'</div>'  # padding-global
'</footer>'
)

new_content = content[:start_idx] + new_footer + content[end_idx:]

with open('C:/Users/M. Gustave/piksort/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Footer replaced successfully")

with open('C:/Users/M. Gustave/piksort/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

INSERT_BEFORE = '<section id="home-story"'

new_section = (
'<section class="section is-hm-proof">'
'<div class="padding-global">'
'<div class="w-layout-blockcontainer container-large w-container">'
'<div class="sp-header-wrap">'
'<div class="section_header-label-outer"><div class="section_header-label"><div class="text-label-small">IN THE FIELD</div></div></div>'
'<div class="max-w-634"><h2 class="text-color-primary">Deployed on Western Australia&#x27;s Biggest Projects</h2></div>'
'<div class="max-w-712"><p class="text-size-medium">From Pilbara iron ore to Bunbury lithium, project teams across WA rely on Piksort to keep hundreds of workers documented and compliant.</p></div>'
'</div></div></div>'
'<div class="sp-carousel-outer">'

# Row 1 — scrolls left
'<div class="sp-track sp-track--ltr"><div class="sp-inner">'
'<div class="sp-card"><div class="sp-tag sp-tag--mining">Mining</div><div class="sp-project">BHP South Flank Mine</div><div class="sp-company">BHP</div><div class="sp-stat"><span class="sp-num">4,500</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Pilbara, WA</div></div>'
'<div class="sp-card"><div class="sp-tag sp-tag--energy">Energy</div><div class="sp-project">Woodside Scarborough</div><div class="sp-company">Woodside Energy</div><div class="sp-stat"><span class="sp-num">5,000</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Offshore &amp; Onslow, WA</div></div>'
'<div class="sp-card"><div class="sp-tag sp-tag--mining">Mining</div><div class="sp-project">Roy Hill Iron Ore</div><div class="sp-company">Roy Hill Holdings</div><div class="sp-stat"><span class="sp-num">3,500</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Pilbara, WA</div></div>'
'<div class="sp-card"><div class="sp-tag sp-tag--mining">Mining</div><div class="sp-project">Iron Bridge Magnetite</div><div class="sp-company">Fortescue Metals Group</div><div class="sp-stat"><span class="sp-num">2,800</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Pilbara, WA</div></div>'
'<div class="sp-card"><div class="sp-tag sp-tag--mining">Mining</div><div class="sp-project">Gudai-Darri Iron Ore Hub</div><div class="sp-company">Rio Tinto</div><div class="sp-stat"><span class="sp-num">3,000</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Pilbara, WA</div></div>'
'<div class="sp-card"><div class="sp-tag sp-tag--energy">Energy</div><div class="sp-project">Perdaman Urea Plant</div><div class="sp-company">Perdaman Industries</div><div class="sp-stat"><span class="sp-num">4,000</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Onslow, WA</div></div>'
'<div class="sp-card"><div class="sp-tag sp-tag--resources">Resources</div><div class="sp-project">Kemerton Lithium Hub</div><div class="sp-company">Albemarle Corporation</div><div class="sp-stat"><span class="sp-num">1,500</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Bunbury, WA</div></div>'
'<div class="sp-card"><div class="sp-tag sp-tag--mining">Mining</div><div class="sp-project">Onslow Iron Project</div><div class="sp-company">Mineral Resources</div><div class="sp-stat"><span class="sp-num">1,800</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Ashburton, WA</div></div>'
'<div class="sp-card"><div class="sp-tag sp-tag--infra">Infrastructure</div><div class="sp-project">METRONET Morley-Ellenbrook</div><div class="sp-company">McConnell Dowell / CIMIC</div><div class="sp-stat"><span class="sp-num">2,200</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Perth Metro, WA</div></div>'
'<div class="sp-card"><div class="sp-tag sp-tag--agri">Agriculture</div><div class="sp-project">Kwinana Grain Terminal Upgrade</div><div class="sp-company">CBH Group</div><div class="sp-stat"><span class="sp-num">650</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Kwinana, WA</div></div>'
# duplicates for seamless loop
'<div class="sp-card" aria-hidden="true"><div class="sp-tag sp-tag--mining">Mining</div><div class="sp-project">BHP South Flank Mine</div><div class="sp-company">BHP</div><div class="sp-stat"><span class="sp-num">4,500</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Pilbara, WA</div></div>'
'<div class="sp-card" aria-hidden="true"><div class="sp-tag sp-tag--energy">Energy</div><div class="sp-project">Woodside Scarborough</div><div class="sp-company">Woodside Energy</div><div class="sp-stat"><span class="sp-num">5,000</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Offshore &amp; Onslow, WA</div></div>'
'<div class="sp-card" aria-hidden="true"><div class="sp-tag sp-tag--mining">Mining</div><div class="sp-project">Roy Hill Iron Ore</div><div class="sp-company">Roy Hill Holdings</div><div class="sp-stat"><span class="sp-num">3,500</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Pilbara, WA</div></div>'
'<div class="sp-card" aria-hidden="true"><div class="sp-tag sp-tag--mining">Mining</div><div class="sp-project">Iron Bridge Magnetite</div><div class="sp-company">Fortescue Metals Group</div><div class="sp-stat"><span class="sp-num">2,800</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Pilbara, WA</div></div>'
'<div class="sp-card" aria-hidden="true"><div class="sp-tag sp-tag--mining">Mining</div><div class="sp-project">Gudai-Darri Iron Ore Hub</div><div class="sp-company">Rio Tinto</div><div class="sp-stat"><span class="sp-num">3,000</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Pilbara, WA</div></div>'
'<div class="sp-card" aria-hidden="true"><div class="sp-tag sp-tag--energy">Energy</div><div class="sp-project">Perdaman Urea Plant</div><div class="sp-company">Perdaman Industries</div><div class="sp-stat"><span class="sp-num">4,000</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Onslow, WA</div></div>'
'<div class="sp-card" aria-hidden="true"><div class="sp-tag sp-tag--resources">Resources</div><div class="sp-project">Kemerton Lithium Hub</div><div class="sp-company">Albemarle Corporation</div><div class="sp-stat"><span class="sp-num">1,500</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Bunbury, WA</div></div>'
'<div class="sp-card" aria-hidden="true"><div class="sp-tag sp-tag--mining">Mining</div><div class="sp-project">Onslow Iron Project</div><div class="sp-company">Mineral Resources</div><div class="sp-stat"><span class="sp-num">1,800</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Ashburton, WA</div></div>'
'<div class="sp-card" aria-hidden="true"><div class="sp-tag sp-tag--infra">Infrastructure</div><div class="sp-project">METRONET Morley-Ellenbrook</div><div class="sp-company">McConnell Dowell / CIMIC</div><div class="sp-stat"><span class="sp-num">2,200</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Perth Metro, WA</div></div>'
'<div class="sp-card" aria-hidden="true"><div class="sp-tag sp-tag--agri">Agriculture</div><div class="sp-project">Kwinana Grain Terminal Upgrade</div><div class="sp-company">CBH Group</div><div class="sp-stat"><span class="sp-num">650</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Kwinana, WA</div></div>'
'</div></div>'

# Row 2 — scrolls right
'<div class="sp-track sp-track--rtl"><div class="sp-inner">'
'<div class="sp-card"><div class="sp-tag sp-tag--energy">Energy</div><div class="sp-project">North West Shelf Venture</div><div class="sp-company">Woodside Energy</div><div class="sp-stat"><span class="sp-num">3,200</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Karratha, WA</div></div>'
'<div class="sp-card"><div class="sp-tag sp-tag--mining">Mining</div><div class="sp-project">Eliwana Iron Ore Mine</div><div class="sp-company">Fortescue Metals Group</div><div class="sp-stat"><span class="sp-num">2,100</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Pilbara, WA</div></div>'
'<div class="sp-card"><div class="sp-tag sp-tag--resources">Resources</div><div class="sp-project">Wodgina Lithium Mine</div><div class="sp-company">MinRes / Albemarle</div><div class="sp-stat"><span class="sp-num">1,200</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Pilbara, WA</div></div>'
'<div class="sp-card"><div class="sp-tag sp-tag--infra">Infrastructure</div><div class="sp-project">Onslow Marine Support Base</div><div class="sp-company">Chevron / Subsea 7</div><div class="sp-stat"><span class="sp-num">900</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Onslow, WA</div></div>'
'<div class="sp-card"><div class="sp-tag sp-tag--mining">Mining</div><div class="sp-project">Robe Valley Iron Ore</div><div class="sp-company">Rio Tinto</div><div class="sp-stat"><span class="sp-num">1,600</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Pilbara, WA</div></div>'
'<div class="sp-card"><div class="sp-tag sp-tag--infra">Infrastructure</div><div class="sp-project">Gateway WA Road Upgrade</div><div class="sp-company">Leighton Contractors</div><div class="sp-stat"><span class="sp-num">1,100</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Perth, WA</div></div>'
'<div class="sp-card"><div class="sp-tag sp-tag--resources">Resources</div><div class="sp-project">Gruyere Gold Mine</div><div class="sp-company">Gold Road Resources</div><div class="sp-stat"><span class="sp-num">850</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Laverton, WA</div></div>'
'<div class="sp-card"><div class="sp-tag sp-tag--energy">Energy</div><div class="sp-project">Pluto LNG Train 2</div><div class="sp-company">Woodside Energy</div><div class="sp-stat"><span class="sp-num">3,800</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Karratha, WA</div></div>'
'<div class="sp-card"><div class="sp-tag sp-tag--mining">Mining</div><div class="sp-project">Karara Iron Ore Project</div><div class="sp-company">Gindalbie Metals / Ansteel</div><div class="sp-stat"><span class="sp-num">2,400</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Mid West, WA</div></div>'
'<div class="sp-card"><div class="sp-tag sp-tag--infra">Infrastructure</div><div class="sp-project">Forrestfield-Airport Link</div><div class="sp-company">Salini Impregilo / NRW</div><div class="sp-stat"><span class="sp-num">1,300</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Perth Metro, WA</div></div>'
# duplicates
'<div class="sp-card" aria-hidden="true"><div class="sp-tag sp-tag--energy">Energy</div><div class="sp-project">North West Shelf Venture</div><div class="sp-company">Woodside Energy</div><div class="sp-stat"><span class="sp-num">3,200</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Karratha, WA</div></div>'
'<div class="sp-card" aria-hidden="true"><div class="sp-tag sp-tag--mining">Mining</div><div class="sp-project">Eliwana Iron Ore Mine</div><div class="sp-company">Fortescue Metals Group</div><div class="sp-stat"><span class="sp-num">2,100</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Pilbara, WA</div></div>'
'<div class="sp-card" aria-hidden="true"><div class="sp-tag sp-tag--resources">Resources</div><div class="sp-project">Wodgina Lithium Mine</div><div class="sp-company">MinRes / Albemarle</div><div class="sp-stat"><span class="sp-num">1,200</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Pilbara, WA</div></div>'
'<div class="sp-card" aria-hidden="true"><div class="sp-tag sp-tag--infra">Infrastructure</div><div class="sp-project">Onslow Marine Support Base</div><div class="sp-company">Chevron / Subsea 7</div><div class="sp-stat"><span class="sp-num">900</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Onslow, WA</div></div>'
'<div class="sp-card" aria-hidden="true"><div class="sp-tag sp-tag--mining">Mining</div><div class="sp-project">Robe Valley Iron Ore</div><div class="sp-company">Rio Tinto</div><div class="sp-stat"><span class="sp-num">1,600</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Pilbara, WA</div></div>'
'<div class="sp-card" aria-hidden="true"><div class="sp-tag sp-tag--infra">Infrastructure</div><div class="sp-project">Gateway WA Road Upgrade</div><div class="sp-company">Leighton Contractors</div><div class="sp-stat"><span class="sp-num">1,100</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Perth, WA</div></div>'
'<div class="sp-card" aria-hidden="true"><div class="sp-tag sp-tag--resources">Resources</div><div class="sp-project">Gruyere Gold Mine</div><div class="sp-company">Gold Road Resources</div><div class="sp-stat"><span class="sp-num">850</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Laverton, WA</div></div>'
'<div class="sp-card" aria-hidden="true"><div class="sp-tag sp-tag--energy">Energy</div><div class="sp-project">Pluto LNG Train 2</div><div class="sp-company">Woodside Energy</div><div class="sp-stat"><span class="sp-num">3,800</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Karratha, WA</div></div>'
'<div class="sp-card" aria-hidden="true"><div class="sp-tag sp-tag--mining">Mining</div><div class="sp-project">Karara Iron Ore Project</div><div class="sp-company">Gindalbie Metals / Ansteel</div><div class="sp-stat"><span class="sp-num">2,400</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Mid West, WA</div></div>'
'<div class="sp-card" aria-hidden="true"><div class="sp-tag sp-tag--infra">Infrastructure</div><div class="sp-project">Forrestfield-Airport Link</div><div class="sp-company">Salini Impregilo / NRW</div><div class="sp-stat"><span class="sp-num">1,300</span><span class="sp-unit">peak workers</span></div><div class="sp-loc">Perth Metro, WA</div></div>'
'</div></div>'

'</div>'  # sp-carousel-outer
'<div style="padding-bottom:4rem"></div>'
'</section>'
)

if INSERT_BEFORE not in content:
    print("ERROR: insertion point not found")
else:
    new_content = content.replace(INSERT_BEFORE, new_section + INSERT_BEFORE, 1)
    with open('C:/Users/M. Gustave/piksort/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Done")

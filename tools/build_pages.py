"""Generate the service pages + services hub for expressapplianceonline.com.

Run from the repo root:  python tools/build_pages.py
Rewrites: services.html, <slug>.html for every entry in SERVICES, blog.html,
<slug>.html for every post in tools/blog_posts.py, and sitemap.xml.
Does NOT touch index.html (nav links there are edited once by hand).

The site is a flat GitHub Pages repo with no build step, so every page is a
self-contained single file. This script is the one place the shared header,
footer, and schema live, so re-running it keeps every page consistent.
"""
import io, os, re, html, datetime, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from blog_posts import POSTS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
SITE = "https://expressapplianceonline.com"
GA_MEASUREMENT_ID = "G-ZWZY46H1VZ"  # GA4 property "Express Appliance Care & HVAC", stream 15722460860
PHONE = "773-255-1773"
PHONE_TEL = "7732551773"
EMAIL = "Prorod360@gmail.com"
TODAY = datetime.date.today().isoformat()

# ---------------------------------------------------------------- services
# slug, nav label, page h1, short blurb, hero image, common problems, body paragraphs, related blog titles
SERVICES = [
    dict(
        slug="refrigerator-repair", label="Refrigerator Repair", h1="Refrigerator Repair in Chicago",
        title="Refrigerator Repair Chicago | Express Appliance Care",
        desc="Same-day refrigerator repair in Chicago. Not cooling, leaking, noisy, or ice buildup. 30 years experience, up to one year warranty. Call 773-255-1773.",
        image="refrigerator18.jpeg", alt="Technician repairing a refrigerator",
        blurb="Not cooling, leaking, or making noise? We fix all major refrigerator brands, usually the same day.",
        problems=["Not cooling or cooling unevenly", "Freezer works but fridge section is warm", "Water pooling inside or under the unit",
                  "Ice maker not making ice, or making too much", "Compressor running constantly or cycling on and off",
                  "Grinding, buzzing, or rattling noises", "Door seals cracked or not closing tight", "Control board or thermostat faults"],
        body=["A refrigerator that stops cooling can cost you a full week of groceries in a single afternoon. We diagnose the real cause first, whether that is a failed evaporator fan, a clogged condenser coil, a bad start relay, or a sealed-system leak, and give you a straight answer on whether a repair makes sense before any work starts.",
              "We service standard top-freezer and side-by-side units as well as French-door, counter-depth, and built-in models. High-end refrigerators are worth fixing properly: condenser replacement, sealed-system work, and control board repair can add years to an expensive unit."],
        related=["Signs Your Refrigerator Needs Repair", "Refrigerator Running Too Loud", "Expensive Refrigerator Repairs Worth Fixing"],
    ),
    dict(
        slug="water-heater-repair", label="Hot Water Tank Installation & Repair", h1="Hot Water Tank Installation and Repair in Chicago",
        title="Water Heater Repair Chicago | Express Appliance Care",
        desc="Hot water tank repair and installation in Chicago. No hot water, leaks, pilot light problems, new tank installs. Same-day service. Call 773-255-1773.",
        image="water-heater-rheem-proterra.jpg", alt="Rheem ProTerra heat pump water heater installed in a Chicago home",
        blurb="No hot water, a leaking tank, or a pilot that will not stay lit. We repair and replace gas and electric water heaters.",
        problems=["No hot water or water not hot enough", "Pilot light goes out or will not light", "Tank leaking or water around the base",
                  "Rumbling or popping sounds from sediment buildup", "Rusty or discolored hot water", "Pressure relief valve dripping",
                  "Thermostat or heating element failure on electric units", "Old tank due for replacement"],
        body=["We repair gas and electric hot water tanks and install new ones when a repair no longer makes sense. A tank that is more than 10 to 12 years old, leaking from the shell, or heavily corroded is usually a replacement, and we will tell you that up front rather than sell you a repair that will not last.",
              "New installations include removing and hauling away the old unit, connecting water and gas or electric supply, checking venting, and testing the unit before we leave."],
        related=["HVAC Winter Prep"],
    ),
    dict(
        slug="washer-dryer-repair", label="Washer & Dryer Repair", h1="Washer and Dryer Repair in Chicago",
        title="Washer & Dryer Repair Chicago | Express Appliance Care",
        desc="Washer and dryer repair in Chicago. Leaks, no spin, not draining, dryer not heating, loud noises. Same-day service, up to one year warranty. 773-255-1773.",
        image="washeranddryer.png", alt="Washer and dryer set",
        blurb="Leaking washer, dryer that will not heat, or a load that never finishes. We fix top-load, front-load, and stacked units.",
        problems=["Washer leaking water onto the floor", "Washer not draining or not spinning", "Drum not turning or loud banging during spin",
                  "Washer stuck on a cycle or not starting", "Dryer runs but does not heat", "Dryer takes two or three cycles to dry clothes",
                  "Burning smell from the dryer", "Dryer drum squealing or thumping"],
        body=["A leaking washer is not just a puddle. Water under a machine leads to subfloor damage and mold, so we find the actual source, whether it is a hose, pump, tub seal, or door boot, and fix it properly.",
              "For dryers, the most common call we get is a unit that runs but will not dry. That is often a heating element, thermal fuse, or a lint-clogged vent duct. Restricted vents are also a fire hazard, so we check the venting on every dryer visit."],
        related=["Washer Leaking Water", "Dryer Maintenance Tips"],
    ),
    dict(
        slug="stove-oven-repair", label="Stove & Oven Repair", h1="Stove and Oven Repair in Chicago",
        title="Stove & Oven Repair Chicago | Express Appliance Care",
        desc="Gas and electric stove and oven repair in Chicago. Burners not lighting, oven not heating, bad igniters, broken thermostats. Same-day service. 773-255-1773.",
        image="stove19.jpeg", alt="Kitchen stove and oven",
        blurb="Burners that will not light, an oven that will not hold temperature, or a smell that is not right. Gas and electric.",
        problems=["Gas burner clicks but will not light", "Oven not heating or heating unevenly", "Oven temperature off from the dial setting",
                  "Igniter glowing but no flame", "Electric burner or bake element not working", "Oven door not sealing or not closing",
                  "Control panel or display dead", "Gas smell around the stove"],
        body=["We repair gas and electric ranges, wall ovens, and cooktops. Weak igniters, failed bake elements, bad thermostats, and door seal problems are all routine fixes.",
              "If you smell gas, do not use the stove. Open windows, leave the area, and call your gas utility first. Once it is safe we can find and repair the fault."],
        related=["Oven Safety Tips", "Strange Smells From Your Oven"],
    ),
    dict(
        slug="freezer-repair", label="Freezer Repair", h1="Freezer Repair in Chicago",
        title="Freezer Repair Chicago | Express Appliance Care",
        desc="Freezer repair in Chicago for chest, upright, and built-in freezers. Not freezing, frost buildup, compressor problems. Same-day service. Call 773-255-1773.",
        image="freezercoils.png", alt="Freezer coils being serviced",
        blurb="Frost building up, food thawing, or a compressor that will not stop running. Chest, upright, and built-in freezers.",
        problems=["Freezer not cold enough or food thawing", "Heavy frost or ice buildup inside", "Compressor runs constantly",
                  "Freezer too cold and over-freezing", "Loud humming, buzzing, or clicking", "Door gasket torn or not sealing",
                  "Defrost system failure", "Freezer not turning on at all"],
        body=["Frost building up on the walls or coils usually means a defrost timer, heater, or thermostat has failed. Left alone it blocks airflow and the freezer stops holding temperature.",
              "We service chest freezers, upright freezers, and the freezer section of combination refrigerators, and we will tell you honestly if an older unit is worth the repair."],
        related=["Signs Your Refrigerator Needs Repair"],
    ),
    dict(
        slug="microwave-repair", label="Microwave Repair", h1="Microwave Repair in Chicago",
        title="Microwave Repair Chicago | Express Appliance Care",
        desc="Built-in and over-the-range microwave repair in Chicago. Not heating, sparking, turntable or door problems. Same-day service. Call 773-255-1773.",
        image="microwave-repair.jpg", alt="Technician servicing an over-the-range microwave",
        blurb="Runs but does not heat, sparks inside, or the door will not latch. We repair built-in and over-the-range microwaves.",
        problems=["Runs but does not heat food", "Sparking or arcing inside", "Turntable not spinning", "Door will not latch or unit will not start",
                  "Buttons or display not responding", "Loud buzzing or humming", "Exhaust fan or light not working on over-the-range units"],
        body=["Built-in and over-the-range microwaves are worth repairing because replacing them means cabinetry and installation work, not just a new box. A microwave that runs but does not heat is usually a magnetron, diode, or capacitor, all of which we can replace.",
              "Microwaves store a dangerous electrical charge even when unplugged. Please leave the cover on and let a technician handle the inside."],
        related=[],
    ),
    dict(
        slug="garbage-disposal-repair", label="Garbage Disposal", h1="Garbage Disposal Repair and Installation in Chicago",
        title="Garbage Disposal Repair Chicago | Express Appliance Care",
        desc="Garbage disposal repair and installation in Chicago. Jammed, humming, leaking, or dead disposals fixed or replaced. Same-day service. Call 773-255-1773.",
        image="garbage-disposal-repair.jpg", alt="Garbage disposal mounted under a double kitchen sink with the drain trap and supply lines",
        credit='Photo: <a href="https://commons.wikimedia.org/wiki/File:Under_Sink_Garbage_Disposal_and_White_Pipes_(53370206837).jpg" rel="noopener" target="_blank">Tony Webster</a>, <a href="https://creativecommons.org/licenses/by/2.0/" rel="noopener" target="_blank">CC BY 2.0</a>',
        blurb="Humming but not grinding, leaking under the sink, or completely dead. We repair or replace garbage disposals.",
        problems=["Disposal hums but does not grind", "Jammed and will not turn", "Leaking from the bottom or the sink flange",
                  "Trips the reset button repeatedly", "Drains slowly or backs up into the sink", "Unit is dead with no sound at all",
                  "Bad odor that will not clear"],
        body=["A disposal that hums but does not spin is usually jammed and can often be freed. One that leaks from the bottom housing has a failed seal and is normally replaced, since the repair costs about as much as a new unit.",
              "We install new disposals, including upgrading to a quieter or higher-horsepower model, and make sure the drain and dishwasher connections are tight before we leave."],
        related=[],
    ),
    dict(
        slug="ac-repair-installation", label="AC Repair & Installation", h1="AC Repair and Installation in Chicago",
        title="AC Repair & Installation Chicago | Express Appliance Care",
        desc="Central air and mini split AC repair and installation in Chicago. Not cooling, frozen coils, refrigerant leaks, new system installs. Call 773-255-1773.",
        image="minisplit.png", alt="Mini split air conditioning unit",
        blurb="Central air and ductless mini splits. Repairs, tune-ups, and new installations before the Chicago summer hits.",
        problems=["AC running but not cooling", "Evaporator coil frozen over", "Refrigerant leak or low charge", "Outdoor condenser fan not spinning",
                  "Unit short-cycling on and off", "Water leaking from the indoor unit", "Thermostat not communicating with the system",
                  "Mini split zone not cooling or showing an error code"],
        body=["We repair and install central air conditioning and ductless mini split systems. Mini splits are a strong option for Chicago two-flats, additions, and rooms the existing ductwork never reached, and we size and install them properly so each zone cools the way it should.",
              "A spring tune-up, cleaning the coils, checking refrigerant, and changing filters, is the cheapest AC service you will ever buy. It prevents the July emergency call when every company is booked out.",
              "Outdoor condensers are a theft target on the South Side. Ask us about anti-theft cages that protect the unit while keeping airflow and service access clear."],
        related=["AC Maintenance Saves Money", "Mini Split AC Units for Comfort", "Protect Your AC Unit from Theft"],
    ),
    dict(
        slug="furnace-repair-service", label="Furnace Repair & Service", h1="Furnace Repair and Service in Chicago",
        title="Furnace Repair & Service Chicago | Express Appliance Care",
        desc="Furnace repair, tune-ups, and heating service in Chicago. No heat, short-cycling, blower or igniter problems, annual inspections. Call 773-255-1773.",
        image="furnace-goodman.jpg", alt="Goodman high-efficiency gas furnace installed in a Chicago home",
        blurb="No heat in January is an emergency. We repair gas furnaces and boilers and offer fall tune-ups so it never gets that far.",
        problems=["Furnace not turning on or no heat", "Blows cold air", "Short-cycling on and off", "Pilot or igniter not lighting",
                  "Blower motor noisy or not running", "Furnace runs constantly", "Thermostat not calling for heat",
                  "Boiler pressure or radiator heating problems"],
        body=["Chicago winters do not forgive a weak furnace. We repair gas furnaces and boilers, replace igniters, flame sensors, blower motors, and control boards, and clean burners so the system lights reliably every time.",
              "An annual fall inspection catches cracked heat exchangers, dirty flame sensors, and worn belts before the first deep freeze. It is also when we test for carbon monoxide leaks, which you cannot smell."],
        related=["Furnace Systems Keep You Warm", "HVAC Winter Prep"],
    ),
    dict(
        slug="duct-cleaning-repair", label="Duct Cleaning & Repair", h1="Duct Cleaning and Repair in Chicago",
        title="Duct Cleaning & Repair Chicago | Express Appliance Care",
        desc="Air duct cleaning, sealing, and repair in Chicago. Dust, uneven airflow, disconnected or leaking ducts, dryer vent cleaning. Call 773-255-1773.",
        image="hvac18.jpeg", alt="HVAC ductwork and equipment",
        blurb="Dusty air, rooms that never get warm or cool, or ducts that have come apart in the basement. Cleaning, sealing, and repair.",
        problems=["Excess dust or musty smell when the system runs", "One room much hotter or colder than the rest", "Weak airflow from vents",
                  "Ducts disconnected or crushed in the basement or attic", "Leaking joints wasting heated or cooled air", "Rodent or pest activity in ducts",
                  "Dryer vent duct clogged with lint"],
        body=["Leaky or dirty ductwork makes a good furnace or AC work harder for less comfort. We clean supply and return ducts, seal leaking joints, and repair or replace damaged runs so the air actually reaches the rooms it is meant to.",
              "Dryer vent cleaning is part of this service. A lint-packed dryer vent is one of the most common causes of house fires, and it is a quick job to clear."],
        related=["Dryer Maintenance Tips", "HVAC Winter Prep"],
    ),
]

# ---------------------------------------------------------------- pull shared facts from index.html
INDEX = io.open("index.html", encoding="utf-8", newline="").read()
m = re.search(r'<section class="brands" id="brands">(.*?)</section>', INDEX, re.S)
BRANDS = re.findall(r'<div class="brand-item">\s*([^<]+?)\s*</div>', m.group(1)) if m else []
if not BRANDS:
    BRANDS = re.findall(r'>\s*([A-Z][A-Za-z&\- ]{1,30})\s*</(?:div|span|li)>', m.group(1)) if m else []
BRANDS = [b.strip() for b in BRANDS if b.strip() and b.strip().lower() not in ("brands we service", "brands")]

def esc(s):
    return html.escape(s, quote=True)

# ---------------------------------------------------------------- shared chrome
STYLE = """
    <style>
        :root { --primary-blue:#0052CC; --accent-red:#FF4444; --light-gray:#f8f9fa; --dark-gray:#333; --text-gray:#666; --border-color:#e0e0e0; }
        * { margin:0; padding:0; box-sizing:border-box; }
        html { scroll-behavior:smooth; }
        body { font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height:1.7; color:var(--text-gray); background:#fff; }
        a { color:var(--primary-blue); }
        .info-bar { background:#fff; border-bottom:1px solid var(--border-color); font-size:13px; }
        .info-bar-content { max-width:1200px; margin:0 auto; padding:8px 20px; display:flex; flex-wrap:wrap; gap:8px 24px; justify-content:center; color:var(--dark-gray); }
        .info-bar a { text-decoration:none; font-weight:700; }
        nav { background:#fff; box-shadow:0 2px 8px rgba(0,0,0,.08); position:sticky; top:0; z-index:10; }
        .nav-content { max-width:1200px; margin:0 auto; padding:8px 20px; display:flex; align-items:center; flex-wrap:wrap; gap:4px 18px; }
        .nav-content .logo { margin-right:auto; display:flex; align-items:center; }
        .nav-content .logo img { height:64px; object-fit:contain; }
        .nav-content a { color:var(--dark-gray); text-decoration:none; font-weight:600; padding:6px 0; }
        .nav-content a:hover, .nav-content a.active { color:var(--primary-blue); }
        .dropdown { position:relative; display:inline-block; }
        .dropdown-content { display:none; position:absolute; left:50%; transform:translateX(-50%); top:100%; background:var(--primary-blue); min-width:300px; box-shadow:0 8px 16px rgba(0,0,0,.2); padding:8px 0; z-index:20; border-radius:0 0 8px 8px; }
        @media (max-width:820px) { .dropdown { position:static; } .dropdown-content { position:absolute; left:0; right:0; transform:none; min-width:0; border-radius:0; } nav { position:relative; } }
        .dropdown-content a { display:block; color:#fff; padding:10px 20px; font-weight:500; }
        .dropdown-content a:hover { background:rgba(255,255,255,.15); color:#fff; }
        @media (hover:hover) { .dropdown:hover .dropdown-content { display:block; } }
        .dropdown.open .dropdown-content { display:block; }
        .hero { background:linear-gradient(135deg, var(--primary-blue), #003d99); color:#fff; padding:56px 20px; }
        .hero-inner { max-width:1100px; margin:0 auto; display:grid; grid-template-columns:1.2fr 1fr; gap:36px; align-items:center; }
        .hero h1 { font-size:36px; line-height:1.2; font-weight:700; }
        .hero p { margin-top:14px; font-size:18px; opacity:.95; }
        .hero img { width:100%; max-height:320px; object-fit:cover; border-radius:10px; box-shadow:0 8px 24px rgba(0,0,0,.25); }
        .credit { font-size:11px; opacity:.75; margin-top:6px; text-align:right; }
        .credit a { color:#fff; }
        .cta-row { margin-top:22px; display:flex; flex-wrap:wrap; gap:12px; }
        .btn { display:inline-block; padding:13px 24px; border-radius:6px; font-weight:700; text-decoration:none; }
        .btn-red { background:var(--accent-red); color:#fff; }
        .btn-white { background:#fff; color:var(--primary-blue); }
        .btn:hover { opacity:.92; }
        main { max-width:1100px; margin:0 auto; padding:48px 20px; }
        .two-col { display:grid; grid-template-columns:1.4fr 1fr; gap:40px; }
        h2 { color:var(--dark-gray); font-size:26px; margin:0 0 14px; }
        h3 { color:var(--dark-gray); font-size:19px; margin:0 0 10px; }
        main p { margin-bottom:14px; }
        .problems { background:var(--light-gray); border-left:4px solid var(--primary-blue); border-radius:6px; padding:22px 24px; }
        .problems ul { list-style:none; }
        .problems li { padding:6px 0 6px 26px; position:relative; }
        .problems li::before { content:"\\2713"; color:var(--primary-blue); font-weight:700; position:absolute; left:0; }
        .promise { display:grid; grid-template-columns:repeat(auto-fit, minmax(210px, 1fr)); gap:18px; margin:40px 0; }
        .promise div { border:1px solid var(--border-color); border-radius:8px; padding:20px; }
        .promise strong { display:block; color:var(--primary-blue); font-size:17px; margin-bottom:6px; }
        .brands { margin:36px 0; }
        .brands span { display:inline-block; background:var(--light-gray); border-radius:20px; padding:6px 14px; margin:4px 6px 4px 0; font-size:14px; color:var(--dark-gray); }
        .cards { display:grid; grid-template-columns:repeat(auto-fit, minmax(240px, 1fr)); gap:20px; }
        .card { border:1px solid var(--border-color); border-radius:8px; overflow:hidden; background:#fff; text-decoration:none; color:inherit; display:block; transition:transform .15s, box-shadow .15s; }
        .card:hover { transform:translateY(-3px); box-shadow:0 8px 20px rgba(0,0,0,.1); }
        .card img { width:100%; height:160px; object-fit:cover; display:block; }
        .card .card-body { padding:16px; }
        .card h3 { font-size:17px; }
        .card p { font-size:14px; margin:0; }
        .cta-band { background:linear-gradient(135deg, var(--primary-blue), var(--accent-red)); color:#fff; text-align:center; padding:44px 20px; }
        .cta-band h2 { color:#fff; }
        .cta-band p { margin:8px 0 18px; opacity:.95; }
        footer { background:#0a0a0a; color:rgba(255,255,255,0.7); padding:30px 20px; text-align:center; font-size:13px; }
        footer a { color:var(--primary-blue); text-decoration:none; }
        .floating-call { position:fixed; right:18px; bottom:18px; background:var(--accent-red); color:#fff; width:56px; height:56px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:24px; text-decoration:none; box-shadow:0 6px 16px rgba(0,0,0,.3); }
        @media (max-width:820px) { .hero-inner, .two-col { grid-template-columns:1fr; } .hero h1 { font-size:28px; } .nav-content .logo img { height:52px; } }
    </style>
"""

def info_bar():
    return f"""    <div class="info-bar">
        <div class="info-bar-content">
            <span>&#128205; 83rd St &amp; Stony Island, Chicago, IL 60619 | 30 mile radius</span>
            <span>&#128336; Mon-Fri: 8:00am-3:00pm | Sat: 7:00am-12:00pm | Sun: 9:00am-12:00pm</span>
            <span>&#128222; <a href="tel:{PHONE_TEL}">{PHONE}</a> | <span style="color:var(--accent-red);font-weight:700;">Text for faster service</span></span>
            <span>&#128176; Ask about senior pricing</span>
        </div>
    </div>
"""

def nav(active=""):
    return f"""    <nav>
        <div class="nav-content">
            <a href="/" class="logo"><img src="logo.jpeg" alt="Express Appliance Care &amp; HVAC"></a>
            <a href="/">Home</a>
            <a href="/#about">About us</a>
            <div class="dropdown">
                <a href="services.html"{' class="active"' if active == 'services' else ''} aria-haspopup="true" aria-expanded="false">Services &#9662;</a>
                <div class="dropdown-content">
                    <a href="services.html"><strong>All services</strong></a>
{"".join(f'                    <a href="{x["slug"]}.html">{esc(x["label"])}</a>' + chr(10) for x in SERVICES)}                </div>
            </div>
            <a href="/#brands">Brands</a>
            <a href="/#testimonials">Reviews</a>
            <a href="blog.html"{' class="active"' if active == 'blog' else ''}>Blog</a>
            <a href="/#contact">Contact</a>
        </div>
    </nav>
"""

def footer():
    return f"""    <footer>
        <p>&copy; 2026 Express Appliance Care &amp; HVAC. All Rights Reserved. | <a href="terms.html">Terms of Use</a> and <a href="privacy.html">Privacy Policy</a></p>
    </footer>
    <a href="tel:{PHONE_TEL}" class="floating-call" title="Call us">&#128222;</a>
    <script>
    (function () {{
        var dd = document.querySelector('.dropdown');
        if (!dd) return;
        var trigger = dd.querySelector(':scope > a');
        trigger.addEventListener('click', function (e) {{
            // First tap opens the list; a second tap on "Services" follows the link.
            if (!dd.classList.contains('open')) {{
                e.preventDefault();
                dd.classList.add('open');
                trigger.setAttribute('aria-expanded', 'true');
            }}
        }});
        document.addEventListener('click', function (e) {{
            if (!dd.contains(e.target)) {{ dd.classList.remove('open'); trigger.setAttribute('aria-expanded', 'false'); }}
        }});
    }})();
    </script>
"""

def cta_band(service_label):
    return f"""    <section class="cta-band">
        <h2>Need {esc(service_label)} today?</h2>
        <p>Same-day service across Chicago and a 30-mile radius. Free estimates. Ask about senior pricing.</p>
        <div class="cta-row" style="justify-content:center;">
            <a class="btn btn-white" href="tel:{PHONE_TEL}">Call {PHONE}</a>
            <a class="btn btn-white" href="sms:{PHONE_TEL}">Text us</a>
            <a class="btn btn-white" href="/#contact">Request a free estimate</a>
        </div>
    </section>
"""

def head(title, desc, path, image, jsonld):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-ZWZY46H1VZ"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', 'G-ZWZY46H1VZ');
    </script>
    <meta name="description" content="{esc(desc)}">
    <title>{esc(title)}</title>
    <link rel="canonical" href="{SITE}/{path}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="{SITE}/{path}">
    <meta property="og:site_name" content="Express Appliance Care &amp; HVAC">
    <meta property="og:title" content="{esc(title)}">
    <meta property="og:description" content="{esc(desc)}">
    <meta property="og:image" content="{SITE}/{image}">
    <meta property="og:locale" content="en_US">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{esc(title)}">
    <meta name="twitter:description" content="{esc(desc)}">
    <meta name="twitter:image" content="{SITE}/{image}">
    <link rel="icon" type="image/svg+xml" href="favicon.svg">
    <script type="application/ld+json">
{jsonld}
    </script>
{STYLE}</head>
"""

PROVIDER = f"""{{
            "@type": "LocalBusiness",
            "name": "Express Appliance Care & HVAC",
            "telephone": "{PHONE}",
            "url": "{SITE}",
            "address": {{"@type": "PostalAddress", "streetAddress": "1435 East 83rd Street", "addressLocality": "Chicago", "addressRegion": "IL", "postalCode": "60619", "addressCountry": "US"}}
        }}"""

def service_jsonld(s):
    name = s["label"].replace("&", "and")
    return f"""    {{
        "@context": "https://schema.org",
        "@type": "Service",
        "name": "{name}",
        "serviceType": "{name}",
        "description": "{s['desc'].replace('"', "'")}",
        "url": "{SITE}/{s['slug']}.html",
        "image": "{SITE}/{s['image']}",
        "areaServed": {{"@type": "City", "name": "Chicago", "containedInPlace": {{"@type": "State", "name": "Illinois"}}}},
        "provider": {PROVIDER}
    }}"""

def hub_jsonld():
    items = ",\n".join(f'            {{"@type": "ListItem", "position": {i+1}, "name": "{s["label"].replace("&", "and")}", "url": "{SITE}/{s["slug"]}.html"}}' for i, s in enumerate(SERVICES))
    return f"""    {{
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "Appliance and HVAC Services in Chicago",
        "itemListElement": [
{items}
        ]
    }}"""

def promise_block():
    return """        <section class="promise">
            <div><strong>Same-day service</strong>We arrive on time and get your appliance working today whenever parts allow.</div>
            <div><strong>Up to one year warranty</strong>Parts and labor on work performed. If it's not right, we make it right.</div>
            <div><strong>Fair, upfront pricing</strong>No surprise charges. A clear estimate before the work starts.</div>
            <div><strong>30 years in Chicago</strong>Serving the South Side and a 30-mile radius around 83rd and Stony Island.</div>
        </section>
"""

def brands_block():
    if not BRANDS:
        return ""
    return "        <section class=\"brands\">\n            <h2>Brands we service</h2>\n            " + "".join(f"<span>{esc(b)}</span>" for b in BRANDS) + "\n        </section>\n"

def service_cards(exclude_slug=None, heading="Other services"):
    cards = "".join(f"""                <a class="card" href="{s['slug']}.html">
                    <img src="{s['image']}" alt="{esc(s['alt'])}" loading="lazy">
                    <div class="card-body"><h3>{esc(s['label'])}</h3><p>{esc(s['blurb'])}</p></div>
                </a>
""" for s in SERVICES if s["slug"] != exclude_slug)
    return f"""        <section>
            <h2>{heading}</h2>
            <div class="cards">
{cards}            </div>
        </section>
"""

def related_block(s):
    by_title = {q["title"]: q for q in POSTS}
    posts = [by_title[t] for t in s["related"] if t in by_title]
    if not posts:
        return ""
    return f"""        <section style="margin:44px 0;">
            <h2>From our blog</h2>
            <div class="cards">
{"".join(post_card(q) for q in posts)}            </div>
        </section>
"""

def service_page(s):
    problems = "".join(f"                    <li>{esc(p)}</li>\n" for p in s["problems"])
    body = "".join(f"            <p>{esc(p)}</p>\n" for p in s["body"])
    return head(s["title"], s["desc"], s["slug"] + ".html", s["image"], service_jsonld(s)) + f"""<body>
{info_bar()}{nav('services')}    <section class="hero">
        <div class="hero-inner">
            <div>
                <h1>{esc(s['h1'])}</h1>
                <p>{esc(s['blurb'])}</p>
                <div class="cta-row">
                    <a class="btn btn-red" href="tel:{PHONE_TEL}">Call {PHONE}</a>
                    <a class="btn btn-white" href="/#contact">Free estimate</a>
                </div>
            </div>
            <div>
                <img src="{s['image']}" alt="{esc(s['alt'])}">
                {('<p class="credit">' + s['credit'] + '</p>') if s.get('credit') else ''}
            </div>
        </div>
    </section>
    <main>
        <div class="two-col">
            <div>
                <h2>{esc(s['label'])} you can count on</h2>
{body}            </div>
            <aside class="problems">
                <h3>Common problems we fix</h3>
                <ul>
{problems}                </ul>
            </aside>
        </div>
{promise_block()}{brands_block()}{related_block(s)}{service_cards(exclude_slug=s['slug'])}    </main>
{cta_band(s['label'])}{footer()}</body>
</html>
"""

def hub_page():
    title = "Appliance & HVAC Services Chicago | Express Appliance Care"
    desc = "All appliance and HVAC services from Express Appliance Care in Chicago: refrigerator, washer, dryer, stove, water heater, AC, furnace, ducts. 773-255-1773."
    return head(title, desc, "services.html", "HVAC25.jpeg", hub_jsonld()) + f"""<body>
{info_bar()}{nav('services')}    <section class="hero">
        <div class="hero-inner" style="grid-template-columns:1fr;text-align:center;">
            <div>
                <h1>Appliance and HVAC Services in Chicago</h1>
                <p>Thirty years of repair and installation work across the South Side and a 30-mile radius. Pick a service to see what we fix and what to expect.</p>
                <div class="cta-row" style="justify-content:center;">
                    <a class="btn btn-red" href="tel:{PHONE_TEL}">Call {PHONE}</a>
                    <a class="btn btn-white" href="/#contact">Free estimate</a>
                </div>
            </div>
        </div>
    </section>
    <main>
{service_cards(heading="Our services")}{promise_block()}{brands_block()}    </main>
{cta_band("appliance or HVAC service")}{footer()}</body>
</html>
"""

def post_jsonld(p):
    return f"""    {{
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": "{p['title']}",
        "description": "{p['desc'].replace('"', "'")}",
        "image": "{SITE}/{p['image']}",
        "datePublished": "{p['date']}",
        "dateModified": "{p['date']}",
        "mainEntityOfPage": "{SITE}/{p['slug']}.html",
        "author": {{"@type": "Organization", "name": "Express Appliance Care & HVAC"}},
        "publisher": {{"@type": "Organization", "name": "Express Appliance Care & HVAC", "logo": {{"@type": "ImageObject", "url": "{SITE}/logo.jpeg"}}}}
    }}"""

def blog_index_jsonld():
    items = ",\n".join(f'            {{"@type": "ListItem", "position": {i+1}, "name": "{p["title"]}", "url": "{SITE}/{p["slug"]}.html"}}' for i, p in enumerate(POSTS))
    return f"""    {{
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "Appliance and HVAC Repair Tips and Articles",
        "itemListElement": [
{items}
        ]
    }}"""

def nice_date(iso):
    d = datetime.date.fromisoformat(iso)
    return f"{d.strftime('%B')} {d.day}, {d.year}"

def post_card(q):
    return f"""                <a class="card" href="{q['slug']}.html">
                    <img src="{q['image']}" alt="{esc(q['alt'])}" loading="lazy">
                    <div class="card-body"><h3>{esc(q['title'])}</h3><p>{esc(q['desc'])}</p></div>
                </a>
"""

def blog_post(p):
    svc = next((x for x in SERVICES if x["slug"] == p["service"]), None)
    sections = ""
    for h, paras in p["sections"]:
        sections += f"            <h2>{esc(h)}</h2>\n" + "".join(f"            <p>{esc(x)}</p>\n" for x in paras)
    related = [q for q in POSTS if q["service"] == p["service"] and q["slug"] != p["slug"]][:3]
    related_html = ""
    if related:
        related_html = ('        <section style="margin:44px 0;">\n            <h2>Related articles</h2>\n            <div class="cards">\n'
                        + "".join(post_card(q) for q in related) + "            </div>\n        </section>\n")
    svc_html = ""
    if svc:
        svc_html = f"""            <div class="problems" style="margin:36px 0;">
                <h3>Need a hand with this?</h3>
                <p style="margin:0 0 12px;">{esc(svc['blurb'])}</p>
                <a class="btn btn-red" href="{svc['slug']}.html">{esc(svc['label'])} in Chicago</a>
            </div>
"""
    return head(p.get("seo_title") or (p["title"] + " | Express Appliance Care"), p["desc"], p["slug"] + ".html", p["image"], post_jsonld(p)) + f"""<body>
{info_bar()}{nav('blog')}    <section class="hero">
        <div class="hero-inner">
            <div>
                <p style="margin:0 0 10px;font-size:14px;opacity:.85;"><a href="blog.html" style="color:#fff;">Tips &amp; Articles</a> &middot; {nice_date(p['date'])}</p>
                <h1>{esc(p['title'])}</h1>
                <p>{esc(p['desc'])}</p>
                <div class="cta-row">
                    <a class="btn btn-red" href="tel:{PHONE_TEL}">Call {PHONE}</a>
                    <a class="btn btn-white" href="/#contact">Free estimate</a>
                </div>
            </div>
            <img src="{p['image']}" alt="{esc(p['alt'])}">
        </div>
    </section>
    <main>
        <article style="max-width:820px;">
            <p style="font-size:18px;color:var(--dark-gray);">{esc(p['intro'])}</p>
{sections}{svc_html}        </article>
{related_html}{service_cards(heading="Our services")}    </main>
{cta_band(svc['label'] if svc else "appliance or HVAC service")}{footer()}</body>
</html>
"""

def blog_index():
    title = "Appliance & HVAC Repair Tips | Express Appliance Care"
    desc = "Practical appliance and HVAC advice from Express Appliance Care in Chicago: refrigerators, washers, dryers, ovens, furnaces, AC, and seasonal maintenance."
    return head(title, desc, "blog.html", "HVAC25.jpeg", blog_index_jsonld()) + f"""<body>
{info_bar()}{nav('blog')}    <section class="hero">
        <div class="hero-inner" style="grid-template-columns:1fr;text-align:center;">
            <div>
                <h1>Appliance and HVAC Repair Tips</h1>
                <p>Straight answers about the problems we see every week in Chicago homes, and what you can do before you call.</p>
            </div>
        </div>
    </section>
    <main>
        <section>
            <div class="cards">
{"".join(post_card(q) for q in POSTS)}            </div>
        </section>
{promise_block()}    </main>
{cta_band("appliance or HVAC service")}{footer()}</body>
</html>
"""

def sitemap():
    def url(loc, lastmod, freq, pri):
        return f"    <url>\n        <loc>{loc}</loc>\n        <lastmod>{lastmod}</lastmod>\n        <changefreq>{freq}</changefreq>\n        <priority>{pri}</priority>\n    </url>\n"
    out = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    out += url(SITE + "/", TODAY, "weekly", "1.0")
    out += url(SITE + "/services.html", TODAY, "monthly", "0.9")
    for s in SERVICES:
        out += url(f"{SITE}/{s['slug']}.html", TODAY, "monthly", "0.8")
    out += url(SITE + "/blog.html", TODAY, "weekly", "0.8")
    for p in POSTS:
        out += url(f"{SITE}/{p['slug']}.html", p["date"], "monthly", "0.6")
    # terms.html / privacy.html are noindex,follow - deliberately NOT listed in the sitemap.
    return out + "</urlset>\n"

if __name__ == "__main__":
    for s in SERVICES:
        io.open(s["slug"] + ".html", "w", encoding="utf-8", newline="\n").write(service_page(s))
    io.open("services.html", "w", encoding="utf-8", newline="\n").write(hub_page())
    for p in POSTS:
        io.open(p["slug"] + ".html", "w", encoding="utf-8", newline="\n").write(blog_post(p))
    io.open("blog.html", "w", encoding="utf-8", newline="\n").write(blog_index())
    io.open("sitemap.xml", "w", encoding="utf-8", newline="\n").write(sitemap())
    print(f"wrote {len(SERVICES)} service pages + services.html + {len(POSTS)} posts + blog.html + sitemap.xml; brands={len(BRANDS)}")

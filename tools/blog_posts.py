"""Blog post content for expressapplianceonline.com. Imported by build_pages.py.

Each post: slug, title (must match the homepage teaser <h3> exactly so the
homepage card can be linked), meta description, image (existing repo file),
date, the service slug it relates to, and sections as (heading, [paragraphs]).
Plain, honest advice only. No invented business facts.
"""

POSTS = [
    dict(
        slug="signs-your-refrigerator-needs-repair",
        title="Signs Your Refrigerator Needs Repair",
        desc="Food spoiling early, ice buildup, constant running, water pooling, or new noises. What each refrigerator warning sign means and when to call for repair.",
        seo_title="Signs Your Refrigerator Needs Repair | Express Appliance",
        image="refrigerator18.jpeg", alt="Technician repairing a refrigerator",
        date="2026-09-03", service="refrigerator-repair",
        intro="A refrigerator rarely fails all at once. It usually gives you a few weeks of warning first. Catching these signs early is the difference between a small part replacement and a lost fridge full of groceries.",
        sections=[
            ("Food is spoiling faster than it should", [
                "Milk turning early, produce wilting in a couple of days, or meat that smells off before its date means the box is not holding a safe temperature. Put a thermometer on the middle shelf. The fridge should sit between 35 and 38 degrees, the freezer at 0. If it is warmer than that and the setting is correct, something inside is failing."]),
            ("Ice or frost building up", [
                "A layer of frost on the back wall of the freezer, or ice forming around the vents, usually points to a failed defrost heater, defrost timer, or thermostat. Left alone, the ice blocks airflow to the fresh-food section and the fridge slowly warms up even though the freezer feels fine."]),
            ("The compressor never stops running", [
                "Refrigerators are supposed to cycle. If you hear it running constantly, it is working harder than it should. Common causes are dirty condenser coils, a worn door gasket letting warm air in, a failing fan, or low refrigerant from a sealed-system leak. Constant running also shows up on your electric bill."]),
            ("Water pooling inside or on the floor", [
                "Water under the crisper drawers usually means a clogged defrost drain. Water on the kitchen floor can be the drain pan, a cracked water line to the ice maker, or a leaking inlet valve. Either way, it will not fix itself, and water under a fridge damages flooring quickly."]),
            ("New sounds", [
                "A soft hum is normal. Grinding, loud buzzing, rattling, or clicking every few minutes is not. Clicking often means the start relay is failing and the compressor cannot start. A grinding fan can seize and take the cooling with it."]),
            ("What to do", [
                "Clean the condenser coils if you can reach them, check that the door seals close tight, and make sure nothing is blocking the vents inside. If the problem is still there after that, call for a diagnosis. We service all major brands across Chicago and can usually tell you on the first visit whether a repair makes sense for the age of the unit."]),
        ],
    ),
    dict(
        slug="dryer-maintenance-tips",
        title="Dryer Maintenance Tips",
        desc="Lint buildup wastes energy, ruins clothes, and causes house fires. Simple dryer maintenance steps for Chicago homes and when to call for vent cleaning.",
        image="dryer.png", alt="Clothes dryer",
        date="2026-09-03", service="washer-dryer-repair",
        intro="Dryers are simple machines, and most of what goes wrong with them comes down to one thing: lint. A few minutes of maintenance keeps a dryer running efficiently and, more importantly, safely.",
        sections=[
            ("Clean the lint screen every load", [
                "This is the one everyone knows and many people still skip. A clogged screen forces the dryer to run longer and hotter. Once a month, wash the screen with warm soapy water too. Dryer sheet residue builds up an invisible film that blocks airflow even when the screen looks clean."]),
            ("Check the vent duct twice a year", [
                "The duct running from the back of the dryer to the outside collects lint the screen misses. Pull the dryer out, disconnect the duct, and clear it. If your duct is the flexible foil or plastic kind, replace it with rigid or semi-rigid metal. Foil ducts sag, trap lint, and are a real fire risk."]),
            ("Look at the outside vent", [
                "Go outside and find where the dryer vents. The flap should open freely when the dryer runs and close when it stops. If the flap is stuck, packed with lint, or a bird has nested in it, air cannot leave and the dryer cannot dry."]),
            ("Do not overload it", [
                "A stuffed drum keeps clothes from tumbling, so they take two cycles to dry and the heating element runs far longer than it was designed to. Two medium loads beat one huge one."]),
            ("Warning signs that need a technician", [
                "Clothes still damp after a full cycle, the top of the dryer hot to the touch, a burning smell, or a drum that squeals or thumps all point to a problem past basic maintenance. A dryer that runs but does not heat is usually a heating element or thermal fuse, and a blown thermal fuse is often caused by a blocked vent."]),
            ("Professional vent cleaning", [
                "Long duct runs, ducts that go through walls or up to a roof, and stacked units in condos are hard to clean by hand. We clean the full run and check the connections while we are there. It is a quick job and one of the cheapest forms of fire prevention in the house."]),
        ],
    ),
    dict(
        slug="mini-split-ac-units-for-comfort",
        title="Mini Split AC Units for Comfort",
        desc="How ductless mini split systems work, where they make sense in Chicago homes, and what to expect from installation and service.",
        image="HVAC26.jpeg", alt="Mini split air conditioning unit",
        date="2026-09-03", service="ac-repair-installation",
        intro="A ductless mini split is an air conditioner, and often a heat pump, that cools one zone at a time without any ductwork. For a lot of Chicago homes it is the most practical way to add real air conditioning.",
        sections=[
            ("How it works", [
                "An outdoor compressor unit connects to one or more indoor wall units through a small refrigerant line that only needs a three-inch hole in the wall. Each indoor unit has its own remote and thermostat, so a bedroom can sit at 68 while the living room is at 74."]),
            ("Where mini splits shine", [
                "Older Chicago houses and two-flats with radiator or boiler heat and no ducts. Attic conversions and additions the original system never reached. Garages, sunrooms, and home offices. Anywhere a window unit is loud, ugly, or a security worry."]),
            ("Efficiency and noise", [
                "Because there are no ducts, there is no duct loss, which is where a lot of a central system's cooling goes. Inverter compressors ramp up and down instead of switching on and off, which is easier on the equipment and the electric bill. Indoor units are quieter than a window unit, and the compressor sits outside."]),
            ("Installation", [
                "A single-zone install is usually a one-day job: mount the indoor unit, set the outdoor unit on a pad or wall bracket, run the line set, pull a vacuum on the lines, and charge the system. Multi-zone systems take longer. Proper sizing matters. An oversized unit short-cycles and never removes humidity; an undersized one runs all day."]),
            ("Keeping it running", [
                "Rinse the indoor filters monthly during the season. Keep the outdoor unit clear of leaves and snow. Have the coils cleaned and the refrigerant charge checked once a year. If a zone stops cooling or shows an error code on the display, call before the next heat wave, not during it."]),
        ],
    ),
    dict(
        slug="hvac-winter-prep",
        title="HVAC Winter Prep",
        desc="A fall checklist for Chicago homes: outdoor condensers and mini splits, refrigerant lines, furnace filters, and a tune-up before the first freeze.",
        image="house-hvac-units.jpeg", alt="Outdoor mini split and AC condenser units at a Chicago home",
        date="2026-09-03", service="furnace-repair-service",
        intro="Chicago winters are hard on heating and cooling equipment, and the outdoor units take the worst of it. An hour of prep in October prevents most of the emergency calls we get in January.",
        sections=[
            ("Outdoor condensers and mini splits", [
                "Clear leaves, grass clippings, and debris from around the unit and from the fins. Trim back anything growing within two feet. If the unit will sit idle all winter, a breathable cover over the top keeps ice and debris out, but never wrap it in plastic, which traps moisture and rusts the coil. Mini splits that also heat should stay uncovered and clear of snow on all sides."]),
            ("Refrigerant lines and insulation", [
                "Look at the insulated line running from the outdoor unit into the house. If the foam is cracked, chewed, or missing, replace it. Bare lines lose efficiency and can sweat and freeze. Seal the wall penetration where the lines enter the house so cold air and pests stay out."]),
            ("Test heat before you need it", [
                "Switch the thermostat to heat on a cool day in October and let it run for a while. Listen for the burners lighting, feel for warm air at the vents, and note any burning-dust smell that does not clear in a few minutes. Finding a problem now means a normal service call, not a no-heat emergency on a holiday weekend."]),
            ("Furnace basics", [
                "Change the filter and keep spares. Make sure supply and return vents are open and not blocked by furniture. Clear the area around the furnace, especially anything flammable. Check that the exhaust and intake pipes outside the house are clear."]),
            ("Schedule the tune-up", [
                "A fall tune-up cleans the burners and flame sensor, checks the heat exchanger for cracks, tests the igniter and safety controls, and checks for carbon monoxide leaks. It is the single most effective thing you can do to avoid a mid-winter breakdown."]),
        ],
    ),
    dict(
        slug="oven-safety-tips",
        title="Oven Safety Tips",
        desc="Cracked door seals, weak igniters, and failed thermostats are safety problems. What to check on a gas or electric oven and when to stop using it.",
        image="stove19.jpeg", alt="Kitchen stove and oven",
        date="2026-09-03", service="stove-oven-repair",
        intro="An oven that is not working right is more than an inconvenience. Gas leaks, overheating, and electrical faults are real hazards in a kitchen. Here is what to watch for and what to do about it.",
        sections=[
            ("Door seals", [
                "Run your hand around the closed oven door while it is warm. If you feel heat escaping, the gasket is cracked, flattened, or has come loose. A bad seal makes the oven work harder, cooks unevenly, and puts hot air right where people stand. It is an inexpensive part to replace."]),
            ("Igniters on gas ovens", [
                "A gas oven igniter glows to light the burner. When it weakens, it glows but does not get hot enough to open the gas valve fully, so the oven takes a long time to light or lights with a whump. An igniter that clicks or glows for more than a minute without a flame should be replaced before it fails completely."]),
            ("Thermostats and temperature", [
                "Put an oven thermometer inside and set the dial to 350. If the reading is off by more than 25 degrees either way, the thermostat or temperature sensor is failing. An oven that overshoots badly can scorch food and stress the wiring and the door glass."]),
            ("Electric elements", [
                "A bake or broil element that has a bright spot, a bubble, or a visible break should be turned off and replaced. Elements can arc when they fail, and a shorted element can trip breakers or damage the control board."]),
            ("When to stop using the oven", [
                "If you smell gas, do not light anything and do not use the oven. Open windows, leave the room, and call your gas company. If you see sparks, smell burning plastic, or the control panel is dead or flashing error codes, switch the breaker off and call for service. We repair gas and electric ranges and wall ovens across Chicago."]),
        ],
    ),
    dict(
        slug="protect-your-ac-unit-from-theft",
        title="Protect Your AC Unit from Theft",
        desc="AC condenser theft is common in Chicago. How anti-theft cages work, what else deters thieves, and why a stolen unit is worse than the price of the copper.",
        image="ac-anti-theft-cage.jpg", alt="Outdoor AC condenser secured inside a steel anti-theft cage",
        date="2026-09-03", service="ac-repair-installation",
        intro="Outdoor air conditioning units get stolen for the copper inside them. Thieves may get a few dollars of scrap; the homeowner is left with a cut refrigerant line, a damaged system, and a replacement bill in the thousands. A steel cage is the most reliable way to stop it.",
        sections=[
            ("Why condensers are targeted", [
                "The condenser sits outside, often on the side of the house or in a gangway where nobody is watching. It has copper coils and copper line sets, and it can be disconnected and carried off in minutes. Vacant properties and units near an alley are hit most often."]),
            ("How an anti-theft cage works", [
                "A cage is a welded steel enclosure bolted into the concrete pad or the ground around the unit and locked shut. It is built with open sides so airflow is not restricted and the unit does not lose efficiency. A technician can still open it for service. A thief with hand tools cannot get through it quickly, which is the whole point."]),
            ("Other things that help", [
                "Motion lights and a camera pointed at the unit. Locking the disconnect box so the power cannot be pulled quietly. Keeping the unit visible from the street rather than hidden behind a fence. Marking the unit with your address. None of these replaces a cage, but together they make your house the harder target."]),
            ("If your unit is stolen", [
                "Turn off the breaker to the air handler or furnace so the indoor equipment does not try to run without the outdoor unit. Do not let the open refrigerant lines sit exposed any longer than necessary, since moisture in the lines contaminates the whole system. Call your insurance company and call us. We replace stolen condensers and can install the cage at the same time."]),
        ],
    ),
    dict(
        slug="expensive-refrigerator-repairs-worth-fixing",
        title="Expensive Refrigerator Repairs Worth Fixing",
        seo_title="Refrigerator Repairs Worth Fixing | Express Appliance Care",
        desc="Condenser, sealed-system, and control board repairs on high-end refrigerators. When a big repair still beats replacing the unit, and when it does not.",
        image="refrigerator15.jpeg", alt="Technician servicing a high-end refrigerator",
        date="2026-09-03", service="refrigerator-repair",
        intro="On a cheap top-freezer fridge, a big repair usually is not worth it. On a built-in, counter-depth, or French-door unit that cost several thousand dollars, the math changes. Some of the repairs that sound scary are exactly the ones worth doing.",
        sections=[
            ("Condenser fan and condenser coil replacement", [
                "The condenser dumps heat out of the refrigerator. When the fan seizes or the coil is damaged, the unit runs hot and constantly, and the compressor eventually pays for it. Replacing these parts is a moderate job that restores the whole system, and it is far cheaper than a new built-in."]),
            ("Sealed-system work", [
                "A refrigerant leak, a failed compressor, or a clogged filter-drier is sealed-system work. It requires recovering the refrigerant, replacing the part, pulling a vacuum, and recharging. Not every repair shop does it. On a high-end unit that is otherwise in good shape, it can add many years of service."]),
            ("Control boards", [
                "Modern refrigerators run on one or more circuit boards. When one fails, the symptoms are strange: lights that flicker, a compressor that will not start, a display full of error codes. Boards are not cheap, but they are a straight swap and the fridge comes back like new."]),
            ("When replacement wins", [
                "A unit more than 12 to 15 years old with a sealed-system failure. Rust-through on the cabinet or liner. Multiple failures at once. A budget unit where the repair is more than half of a replacement. We will tell you honestly which side of the line your refrigerator is on."]),
            ("Do not trust amateurs with it", [
                "Sealed-system work done wrong can destroy a compressor. Boards installed without diagnosing what killed the original fail again. An expensive refrigerator deserves a technician who works on that brand regularly and stands behind the repair."]),
        ],
    ),
    dict(
        slug="washer-leaking-water",
        title="Washer Leaking Water",
        desc="Where washing machine leaks come from, how to narrow down the source, and why a small leak becomes a floor and mold problem fast.",
        image="washingmachine.png", alt="Washing machine",
        date="2026-09-03", service="washer-dryer-repair",
        intro="A puddle by the washer is easy to mop up and ignore. It is also how subfloors rot and mold gets started behind the machine. Finding where the water is actually coming from is the first step, and it is not always obvious.",
        sections=[
            ("Leaks that show up during fill", [
                "If water appears while the machine is filling, look at the hoses first. Rubber supply hoses crack and bulge with age. Check both ends, the fittings at the wall and at the back of the washer. The inlet valve inside the machine can also crack and drip from the moment the water turns on."]),
            ("Leaks during the wash or spin", [
                "Water that appears during agitation or spin usually comes from inside the machine: a worn tub seal, a cracked outer tub, a loose or split hose between the tub and pump, or a failed drain pump. On front-loaders, a torn door boot is the most common cause and shows up as water at the front of the machine."]),
            ("Leaks during drain", [
                "If the puddle appears when the machine empties, check the drain hose and the standpipe it drains into. A hose that has slipped out, a kinked hose, or a standpipe that is clogged and backing up all put water on the floor."]),
            ("Overuse of detergent", [
                "Too much detergent in a high-efficiency washer makes suds that push out past the seals. If the puddle is soapy and the machine seems otherwise fine, cut the detergent in half and see if it stops."]),
            ("Why it matters", [
                "Water under a washer sits. It soaks the subfloor, feeds mold, and on an upper floor it finds its way into the ceiling below. A leak that costs a little to fix today can cost thousands in repairs later. We find the actual source and fix it properly on top-load, front-load, and stacked units."]),
        ],
    ),
    dict(
        slug="refrigerator-running-too-loud",
        title="Refrigerator Running Too Loud",
        desc="Grinding, buzzing, clicking, and rattling from a refrigerator each point to a different failing part. What each noise means and which ones need repair soon.",
        image="hvac17.jpeg", alt="Express Appliance HVAC technician at work",
        date="2026-09-03", service="refrigerator-repair",
        intro="Every refrigerator makes some noise. A gentle hum, an occasional click, the sound of ice dropping into the bin. When the noise changes, gets louder, or turns into something you notice from the next room, it is telling you which part is on its way out.",
        sections=[
            ("Grinding or scraping", [
                "Almost always a fan. The evaporator fan in the freezer or the condenser fan near the compressor has a worn bearing or is hitting ice or debris. A fan that grinds will eventually seize, and when it does the fridge stops cooling."]),
            ("Loud buzzing", [
                "A steady loud buzz from the back is usually the compressor working too hard, often because the condenser coils are packed with dust. A buzz from inside the freezer can be the ice maker trying to fill with the water line shut off. A buzz that comes and goes with a click is the start relay struggling."]),
            ("Clicking every few minutes", [
                "The compressor is trying to start and failing. A worn start relay or overload protector clicks on, the compressor cannot start, it clicks off, and the cycle repeats. Caught early this is a small part. Ignored, the compressor itself can fail."]),
            ("Rattling or vibrating", [
                "Sometimes it is just the fridge not sitting level, or something on top of it vibrating. If leveling does not fix it, a loose fan blade, a cracked fan mount, or a compressor mount that has worn out is the usual cause."]),
            ("Gurgling and hissing", [
                "Refrigerant moving through the lines gurgles and hisses, and that is normal, especially right after the compressor shuts off. A new, constant hiss with poor cooling could be a refrigerant leak and needs a technician."]),
            ("Noise only gets worse", [
                "Refrigerator noises do not fix themselves. Fans seize, relays burn out, and compressors fail. If the sound is new and the fridge is worth keeping, have it diagnosed before a cheap repair turns into an expensive one."]),
        ],
    ),
    dict(
        slug="furnace-systems-keep-you-warm",
        title="Furnace Systems Keep You Warm",
        desc="How a gas furnace works, why annual maintenance matters in Chicago, and the warning signs that mean a furnace is about to fail.",
        image="HVAC28.jpeg", alt="Furnace and HVAC equipment",
        date="2026-09-03", service="furnace-repair-service",
        intro="A furnace runs for months at a stretch in a Chicago winter. Most of the failures we see in January were visible in October to anyone who looked. Here is what the system does, what wears out, and how to keep it working.",
        sections=[
            ("What happens when the thermostat calls for heat", [
                "The control board runs the inducer fan to clear the exhaust, the igniter glows or a pilot lights, the gas valve opens, the burners light, and the flame sensor confirms it. Once the heat exchanger is warm, the blower pushes air across it and through the ducts. Any link in that chain can fail, and each one has its own symptoms."]),
            ("Filters", [
                "The cheapest part of the system and the one that causes the most trouble. A dirty filter restricts airflow, overheats the heat exchanger, and trips the high-limit switch, which is why a furnace with a clogged filter runs a few minutes, shuts off, and starts again. Change it every one to three months in heating season."]),
            ("Flame sensors and igniters", [
                "A flame sensor coated with residue cannot see the flame, so the board shuts the gas off a few seconds after the burners light. The furnace lights, dies, lights, dies. Cleaning the sensor is part of every tune-up. Igniters wear out with age and crack; a furnace that clicks or hums but never lights often needs one."]),
            ("Heat exchangers and carbon monoxide", [
                "The heat exchanger keeps combustion gases separate from the air you breathe. When it cracks, carbon monoxide can enter the house. You cannot smell it. Every home with gas heat needs working carbon monoxide detectors, and every furnace more than a few years old should have the exchanger inspected annually."]),
            ("Warning signs", [
                "Short-cycling, cold air from the vents, a yellow or flickering flame instead of a steady blue one, a burning smell that does not clear, a rise in the gas bill, or a furnace that is simply louder than it used to be. Any of these is a reason to call before the cold snap, not during it."]),
        ],
    ),
    dict(
        slug="strange-smells-from-your-oven",
        title="Strange Smells From Your Oven",
        desc="Rotten egg, burning plastic, and electrical smells from an oven each mean something different. Which ones are emergencies and what to do right now.",
        image="stove19.jpeg", alt="Kitchen stove and oven",
        date="2026-09-03", service="stove-oven-repair",
        intro="Some oven smells are harmless. Some mean you should turn the breaker off and step outside. Knowing the difference is worth two minutes of reading.",
        sections=[
            ("Rotten eggs: stop and leave", [
                "Natural gas has no smell of its own; the utility adds a rotten-egg odor so leaks are noticed. If you smell it near the oven or stove, do not use the appliance, do not flip switches, and do not light anything. Open windows, get everyone out, and call your gas company from outside. Once they clear the house, we can find and repair the leak, which is often a fitting, a valve, or a failed igniter letting gas flow without lighting."]),
            ("Burning plastic or electrical smell", [
                "A sharp chemical or burning-plastic smell from an electric oven or from the control panel usually means wiring insulation or a component is overheating. Turn the oven off at the breaker and call for service. Do not keep using an oven that smells like burning wire; the next stage is a small fire behind the panel."]),
            ("Burning food or grease", [
                "Spilled sugar, grease on the bottom, or a forgotten piece of foil on the element will smoke and smell. This is a cleaning job, not a repair. Let the oven cool fully, clean the interior, and run it empty for a few minutes."]),
            ("New-oven smell", [
                "A new oven or a new heating element gives off a chemical smell the first few times it heats as protective coatings burn off. Run it empty at a high temperature with the windows open for an hour and it should clear."]),
            ("Gas smell only when the oven is lighting", [
                "A brief whiff of gas as the oven lights can be normal on older models, but a strong smell every time, or an oven that takes a long time to light, means the igniter is weak and gas is flowing before it lights. That is a repair, and one worth doing soon."]),
        ],
    ),
    dict(
        slug="ac-maintenance-saves-money",
        title="AC Maintenance Saves Money",
        desc="What a spring AC tune-up actually includes, why coil cleaning and refrigerant checks matter, and how maintenance avoids the peak-summer emergency call.",
        image="hvac15.jpeg", alt="HVAC technician performing air conditioner maintenance",
        date="2026-09-03", service="ac-repair-installation",
        intro="Air conditioners fail on the hottest day of the year because that is the day they work hardest. Most of those failures start as a dirty coil or a slightly low charge that a spring tune-up would have caught for a fraction of the emergency cost.",
        sections=[
            ("Coil cleaning", [
                "The outdoor condenser coil collects cottonwood, dust, and grass clippings all summer. The indoor evaporator coil collects dust that gets past the filter. Dirty coils cannot move heat, so the system runs longer for less cooling and the compressor works under strain. Cleaning both is the core of a tune-up."]),
            ("Refrigerant check", [
                "A system low on refrigerant cools poorly, freezes the evaporator coil, and can burn out the compressor. Refrigerant does not get used up, so a low charge means a leak. Catching it early means a small repair and a top-off instead of a compressor replacement."]),
            ("Filters and airflow", [
                "A clogged filter starves the system of airflow, freezes the coil, and lets dust through to the evaporator. Change filters monthly in heavy use. During the tune-up we also check the blower, the ductwork connections, and the condensate drain, which clogs with algae and overflows into the furnace or the ceiling below."]),
            ("Electrical and safety", [
                "Capacitors weaken with age and heat, and a weak capacitor is the most common reason an AC hums but will not start. Contactors pit and stick. We test both, tighten connections, and check the disconnect so a small part does not take the whole system down in July."]),
            ("The math", [
                "A tune-up costs about the same every year. An emergency call in a heat wave costs more, comes with a wait, and often involves a part that failed because of a problem maintenance would have caught. A clean, properly charged system also uses less electricity every hour it runs."]),
        ],
    ),
]

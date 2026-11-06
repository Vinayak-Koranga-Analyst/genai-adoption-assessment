"""Write data/synthetic_repair_emails.csv.

All emails are SYNTHETIC: written for this practice case study. They contain no
real tenant data. Each has a trade and a priority, as an adviser would assign.

Usage:
    python data/make_synthetic_emails.py
"""

import csv
from pathlib import Path

# (email text, trade, priority)
EMAILS = [
    # --- Plumbing ---
    ("Kitchen tap has been dripping for a week, it's getting worse and won't turn off fully.", "plumbing", "routine"),
    ("The toilet keeps running after flushing, can someone look at the cistern?", "plumbing", "routine"),
    ("Water is pouring through the kitchen ceiling from the flat above and it's near the lights.", "plumbing", "emergency"),
    ("Bath plug hole is draining really slowly, think it's blocked.", "plumbing", "routine"),
    ("Our only toilet is blocked and won't flush at all. There are four of us in the house.", "plumbing", "urgent"),
    ("There's a leak under the bathroom sink, I've put a bowl under it for now.", "plumbing", "urgent"),
    ("Burst pipe in the airing cupboard, water everywhere and I can't find the stopcock.", "plumbing", "emergency"),
    ("Shower head is loose and the hose is split.", "plumbing", "routine"),
    ("The outside drain is overflowing and smells awful.", "plumbing", "urgent"),
    ("Washing machine pipe connection is leaking onto the floor every time it runs.", "plumbing", "urgent"),
    ("Cold tap in the bathroom is very stiff and hard to turn.", "plumbing", "routine"),
    ("Sink in the kitchen is completely blocked, water just sits there.", "plumbing", "urgent"),
    ("Water coming through the light fitting in the hallway, it's dripping onto the floor.", "plumbing", "emergency"),
    ("Toilet seat is broken and the hinge has snapped.", "plumbing", "routine"),
    ("Small drip from the pipe behind the toilet, not urgent but would like it checked.", "plumbing", "routine"),
    ("No water coming out of any taps since this morning.", "plumbing", "emergency"),
    ("The bath sealant has gone mouldy and is coming away from the wall.", "plumbing", "routine"),
    ("Sewage is coming back up through the shower drain.", "plumbing", "emergency"),
    ("Low water pressure in the shower for the last few weeks.", "plumbing", "routine"),
    ("Overflow pipe outside is constantly dripping onto the path.", "plumbing", "routine"),
    # --- Electrical ---
    ("Socket in the bedroom is sparking when I plug anything in.", "electrical", "emergency"),
    ("The light in the hallway doesn't work even with a new bulb.", "electrical", "routine"),
    ("We have no electricity in the whole flat, neighbours have power.", "electrical", "emergency"),
    ("Extractor fan in the bathroom has stopped working.", "electrical", "routine"),
    ("There's a burning smell coming from the fuse box.", "electrical", "emergency"),
    ("The trip switch keeps going off when we use the kettle.", "electrical", "urgent"),
    ("Kitchen light flickers on and off all evening.", "electrical", "routine"),
    ("Smoke alarm keeps beeping even after I changed the battery.", "electrical", "urgent"),
    ("Exposed wires hanging out of the wall where the light switch used to be.", "electrical", "emergency"),
    ("Outside security light is not coming on at night.", "electrical", "routine"),
    ("Cooker switch is cracked and gets hot.", "electrical", "urgent"),
    ("Doorbell has stopped working.", "electrical", "routine"),
    ("Half the sockets downstairs have no power.", "electrical", "urgent"),
    ("The pull cord in the bathroom snapped and the light stays on.", "electrical", "routine"),
    ("Heard a bang and now the plug socket is black and melted.", "electrical", "emergency"),
    ("Carbon monoxide alarm is going off in the kitchen.", "electrical", "emergency"),
    ("Light fitting in the living room is hanging loose from the ceiling.", "electrical", "urgent"),
    ("TV aerial socket is loose in the wall.", "electrical", "routine"),
    ("Emergency lighting in the communal stairwell is not working.", "electrical", "urgent"),
    ("Storage heater switch is broken.", "electrical", "routine"),
    # --- Heating ---
    ("We have no heating or hot water and my mum is 84 and on oxygen.", "heating", "emergency"),
    ("Boiler is showing an error code and won't fire up.", "heating", "urgent"),
    ("I can smell gas near the boiler in the kitchen.", "heating", "emergency"),
    ("One radiator upstairs is cold at the top, think it needs bleeding.", "heating", "routine"),
    ("No hot water but the heating is working fine.", "heating", "urgent"),
    ("Boiler is making a loud banging noise when the heating comes on.", "heating", "urgent"),
    ("Thermostat isn't responding, heating stays on all the time.", "heating", "routine"),
    ("There's a funny smell near the boiler and I feel dizzy.", "heating", "emergency"),
    ("Radiator valve in the bedroom is leaking slightly.", "heating", "routine"),
    ("No heating at all, it's freezing and I have a newborn baby.", "heating", "emergency"),
    ("Boiler pressure keeps dropping and I have to top it up every day.", "heating", "urgent"),
    ("Heating timer is broken so the heating comes on at the wrong times.", "heating", "routine"),
    ("The pilot light on the gas fire keeps going out.", "heating", "urgent"),
    ("Radiator in the living room is not getting warm at all.", "heating", "routine"),
    ("No heating or hot water since last night, it's cold but we're managing.", "heating", "urgent"),
    ("Hot water is only lukewarm.", "heating", "routine"),
    ("Boiler is leaking water onto the floor.", "heating", "urgent"),
    ("Black marks around the gas fire and the room feels stuffy.", "heating", "emergency"),
    ("Can someone service the boiler, it's been over a year.", "heating", "routine"),
    ("Radiator came away from the wall and is hanging off the bracket.", "heating", "urgent"),
    # --- Damp and mould ---
    ("Black mould is spreading across the bedroom ceiling and my son has asthma.", "damp_mould", "urgent"),
    ("There's condensation on all the windows every morning.", "damp_mould", "routine"),
    ("Damp patch on the living room wall is getting bigger.", "damp_mould", "routine"),
    ("Mould behind the wardrobe has ruined our clothes.", "damp_mould", "urgent"),
    ("The bathroom ceiling is covered in black spots of mould.", "damp_mould", "routine"),
    ("Wallpaper is peeling off because the wall is wet.", "damp_mould", "routine"),
    ("Mould in the baby's room, she keeps coughing at night.", "damp_mould", "urgent"),
    ("Musty smell in the hallway and the skirting boards feel damp.", "damp_mould", "routine"),
    ("Plaster on the ceiling is bulging and wet and looks like it could come down.", "damp_mould", "emergency"),
    ("Damp coming up the walls downstairs, about a metre high.", "damp_mould", "routine"),
    ("Green mould growing on the window frames in every room.", "damp_mould", "routine"),
    ("My daughter is disabled and the damp in her room is making her chest worse.", "damp_mould", "urgent"),
    ("Mould is back again two months after it was treated.", "damp_mould", "urgent"),
    ("The kitchen wall is wet to touch after it rains.", "damp_mould", "routine"),
    ("White fluffy mould on the carpet in the corner of the bedroom.", "damp_mould", "routine"),
    ("Severe damp and mould throughout the flat, we are all getting ill.", "damp_mould", "urgent"),
    ("Damp smell in the cupboard under the stairs.", "damp_mould", "routine"),
    ("Mould around the shower tray and on the grout.", "damp_mould", "routine"),
    ("Water stains on the bedroom ceiling and the paint is bubbling.", "damp_mould", "routine"),
    ("Mould in every room and I'm pregnant, I'm really worried.", "damp_mould", "urgent"),
    # --- Carpentry / doors / windows ---
    ("Front door won't lock properly, the key just spins.", "carpentry", "urgent"),
    ("Kitchen cupboard door has come off its hinges.", "carpentry", "routine"),
    ("Back door was kicked in during a break-in last night and won't close.", "carpentry", "emergency"),
    ("Bedroom window won't shut, it's stuck open.", "carpentry", "urgent"),
    ("Floorboard in the hallway is loose and creaks.", "carpentry", "routine"),
    ("Stair handrail is wobbly and coming away from the wall.", "carpentry", "urgent"),
    ("Window handle snapped off in the living room.", "carpentry", "routine"),
    ("Can't get out of the flat, the front door lock is jammed shut.", "carpentry", "emergency"),
    ("Kitchen drawer runner is broken.", "carpentry", "routine"),
    ("Glass in the back door is cracked right across.", "carpentry", "urgent"),
    ("Internal door rubs on the carpet and won't close.", "carpentry", "routine"),
    ("Window pane smashed by a football, there's broken glass and a hole.", "carpentry", "emergency"),
    ("Skirting board has come away in the bedroom.", "carpentry", "routine"),
    ("The communal entrance door doesn't shut so anyone can walk in.", "carpentry", "urgent"),
    ("Worktop next to the sink is swollen and lifting.", "carpentry", "routine"),
    ("Letterbox flap has fallen off the front door.", "carpentry", "routine"),
    ("Step on the stairs is split and I nearly fell.", "carpentry", "urgent"),
    ("Shed door has blown off in the wind.", "carpentry", "routine"),
    ("Bathroom door lock is stuck and my child is locked inside.", "carpentry", "emergency"),
    ("Window seal has gone and the glass is misty between the panes.", "carpentry", "routine"),
    # --- Roofing / external ---
    ("Several roof tiles came off in the storm and rain is getting into the loft.", "roofing", "urgent"),
    ("Gutter at the front is hanging down and overflowing.", "roofing", "routine"),
    ("Part of the chimney has collapsed onto the path.", "roofing", "emergency"),
    ("Water dripping into the bedroom from the roof when it rains.", "roofing", "urgent"),
    ("Moss growing all over the roof, is it ok?", "roofing", "routine"),
    ("Downpipe is broken and water is pouring down the wall.", "roofing", "routine"),
    ("A large piece of the roof blew off and there's a hole above the bedroom.", "roofing", "emergency"),
    ("Flat roof on the extension has a puddle that never drains.", "roofing", "routine"),
    ("Fascia board is rotten and coming loose.", "roofing", "routine"),
    ("Ceiling in the top flat is stained after the heavy rain.", "roofing", "routine"),
    ("Loose slates on the roof are rattling in the wind and could fall.", "roofing", "urgent"),
    ("Gutters are full of leaves.", "roofing", "routine"),
    ("Garden wall is leaning badly and children play next to it.", "roofing", "urgent"),
    ("Loft has a leak above the water tank.", "roofing", "urgent"),
    ("Brick has fallen out of the wall above the front door.", "roofing", "urgent"),
    ("Roof is leaking onto the electrics in the loft.", "roofing", "emergency"),
    ("Bird nest blocking the gutter.", "roofing", "routine"),
    ("Pointing on the outside wall is crumbling.", "roofing", "routine"),
    ("Water comes in round the chimney breast in heavy rain.", "roofing", "routine"),
    ("Fence panel blew down in the storm.", "roofing", "routine"),
]


def main() -> None:
    out = Path(__file__).with_name("synthetic_repair_emails.csv")
    with out.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["email_id", "text", "trade", "priority"])
        for i, (text, trade, priority) in enumerate(EMAILS, start=1):
            w.writerow([f"E{i:03d}", text, trade, priority])
    print(f"Wrote {len(EMAILS)} synthetic emails to {out.name}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python
"""Build the verbatim inventory JSON for Round 2 of the site inventory."""

import json, os

FETCHED = "2026-09-01"
AAU_URL = "https://www.peaceyouthct.org/aau"
SPBL_URL = "https://www.peaceyouthct.org/page/show/8134836-peace-boys-basketball-league"
SUMMER_URL = "https://www.peaceyouthct.org/page/show/8561799-2024-summer-league"

inventory = []
c = 0  # counter

# ======================== AAU PAGE ===========================================

# AAU-001: Page title heading
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Information",
    "type": "heading",
    "content": "AAU Information",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": ""
})

# AAU-002: Image - 11th grade varsity champs
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "",
    "type": "image",
    "content": "[no alt text]",
    "verbatim": False,
    "fetched": FETCHED,
    "notes": "Hero photo: 11th grade Varsity CT State Champs; cutline reads 'ZG CT State Varsity Champs 2022 (11th)'"
})

# AAU-003: Cutline
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "",
    "type": "paragraph",
    "content": "ZG CT State Varsity Champs 2022 (11th)",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Photo cutline"
})

# AAU-004: CTA image (2026 Spring AAU)
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "2026 Spring AAU",
    "type": "image",
    "content": "[no alt text]",
    "verbatim": False,
    "fetched": FETCHED,
    "notes": "Call-to-action banner image"
})

# AAU-005: CTA heading overlay text
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "",
    "type": "heading",
    "content": "2026 Spring AAU",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Call-to-action overlay heading"
})

# AAU-006: CTA link
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "",
    "type": "link",
    "content": "2026 Spring AAU -> /26aau",
    "verbatim": False,
    "fetched": FETCHED,
    "notes": "CTA links to 2026 Spring AAU page at /26aau"
})

# AAU-007: Image - in column 2 no cutline
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "",
    "type": "image",
    "content": "[no alt text]",
    "verbatim": False,
    "fetched": FETCHED,
    "notes": "Hero photo in column 2; no alt text or cutline"
})

# AAU-008: Image - 8th grade purple champs
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "",
    "type": "image",
    "content": "[no alt text]",
    "verbatim": False,
    "fetched": FETCHED,
    "notes": "Hero photo: 8th grade Purple CT State Champs; cutline reads 'ZG CT State Champs 2022 (8th)'"
})

# AAU-009: Cutline
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "",
    "type": "paragraph",
    "content": "ZG CT State Champs 2022 (8th)",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Photo cutline"
})

# AAU-010: Heading
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "PEACE AAU Program",
    "type": "heading",
    "content": "PEACE AAU Program",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": ""
})

# AAU-011: Paragraph about PEACE AAU program
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "PEACE AAU Program",
    "type": "paragraph",
    "content": "PEACE offers a first-rate basketball educational experience emphasizing the development of strong fundamentals and high quality competition, as well as establishing a culture of excellence among our players and in our overall approach to the game. PEACE is built on a foundation consisting of teamwork, discipline, leadership, and sportsmanship. Rather than focusing exclusively on wins and losses, the goal of PEACE includes using the game of basketball as a vehicle through which to positively influence young people within Stamford and other lower Fairfield County communities towards academic achievement, community service, and other life skills. As a nationally elite program, PEACE's spring/summer AAU travel schedule includes some of the most competitive age-group tournaments and college showcase events in the United States.",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": ""
})

# AAU-012: Heading
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "heading",
    "content": "AAU Program Handbook/FAQ",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": ""
})

# AAU-013: Link - Academic Policy (anchor link)
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "link",
    "content": "Academic Policy -> #Academic Policy",
    "verbatim": False,
    "fetched": FETCHED,
    "notes": "Table of contents anchor link"
})

# AAU-014: Link - Teams/Age group(s)
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "link",
    "content": "Teams/ Age group(s) -> #Teams/Age Groups",
    "verbatim": False,
    "fetched": FETCHED,
    "notes": "Table of contents anchor link"
})

# AAU-015: Link - Coaching Philosophy
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "link",
    "content": "Coaching Philosophy -> #Coaching Philosophy",
    "verbatim": False,
    "fetched": FETCHED,
    "notes": "Table of contents anchor link"
})

# AAU-016: Link - Tryouts
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "link",
    "content": "Tryouts -> #Try-outs",
    "verbatim": False,
    "fetched": FETCHED,
    "notes": "Table of contents anchor link"
})

# AAU-017: Link - Number of Players
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "link",
    "content": "Number of Players -> #Number of Players",
    "verbatim": False,
    "fetched": FETCHED,
    "notes": "Table of contents anchor link"
})

# AAU-018: Link - Registration Fee
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "link",
    "content": "Registration Fee -> #Registration Fee",
    "verbatim": False,
    "fetched": FETCHED,
    "notes": "Table of contents anchor link"
})

# AAU-019: Link - Uniforms & Equipment
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "link",
    "content": "Uniforms & Equipment -> #Uniforms and Equipment",
    "verbatim": False,
    "fetched": FETCHED,
    "notes": "Table of contents anchor link"
})

# AAU-020: Link - Practice Schedule
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "link",
    "content": "Practice Schedule -> #Practice Schedule",
    "verbatim": False,
    "fetched": FETCHED,
    "notes": "Table of contents anchor link"
})

# AAU-021: Link - Games/Tournament
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "link",
    "content": "Games/Tournament -> #Games/Tournaments",
    "verbatim": False,
    "fetched": FETCHED,
    "notes": "Table of contents anchor link"
})

# AAU-022: Link - Playing Time
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "link",
    "content": "Playing Time -> #Playing Time",
    "verbatim": False,
    "fetched": FETCHED,
    "notes": "Table of contents anchor link"
})

# AAU-023: Link - Season Length
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "link",
    "content": "Season Length -> #Season Length",
    "verbatim": False,
    "fetched": FETCHED,
    "notes": "Table of contents anchor link"
})

# AAU-024: Heading - Academic Policy (sub-heading within handbook)
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "heading",
    "content": "Academic Policy-",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Sub-heading within handbook; note: rendered as bold+underline in HTML"
})

# AAU-025: Paragraph - Academic Policy
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "paragraph",
    "content": "Peace Basketball is deeply concerned with the academic performance and conduct of its players. As a condition to playing with Peace, participants are required to submit a copy of their report card or other academic progress reports, which are then reviewed to identify those in need of individualized academic support.",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": ""
})

# AAU-026: Heading - Teams/ Age Group(s)
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "heading",
    "content": "Teams/ Age Group(s)-",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Sub-heading within handbook"
})

# AAU-027: Paragraph - Teams/Age Groups (first paragraph)
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "paragraph",
    "content": "Eligibility is determined based upon a player's grade in school ( as of August 31st), subject to certain age exceptions, which may allow a player to play at a lower grade level than his or her current grade.",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Note: the source has a period before 'Eligibility' - ' . Eligibility' - preserved"
})

# AAU-028: Paragraph - Teams/Age Groups (second paragraph)
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "paragraph",
    "content": "Depending upon the level of interest we receive from both players and quality coaches in the area, Stamford peace may add more or different teams and age groups as we see fit.",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": ""
})

# AAU-029: Heading - Coaching Philosophy
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "heading",
    "content": "Coaching Philosophy-",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Sub-heading within handbook"
})

# AAU-030: Paragraph - Coaching Philosophy
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "paragraph",
    "content": "Despite different coaching styles among coaches within the program, the general philosophy of Stamford Peace- focusing on high-level competition, training and instruction, with an emphasis on strong fundamentals, defensive intensity and unselfish play- plays a central role throughout the program.",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": ""
})

# AAU-031: Heading - Try-outs
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "heading",
    "content": "Try-outs-",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Sub-heading within handbook; note the hyphenated spelling 'Try-outs'"
})

# AAU-032: Paragraph - Try-outs
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "paragraph",
    "content": "Try-outs are usually held over a 2 day period around the end of January / beginning of February for each Spring season and end of August / beginning of September for Fall season. Tryouts are intended to offer our players a fair process by which coaches can evaluate skills and experience levels, as well as to assess a player's potential fit within the Peace Basketball Program. The degree to which a given player may benefit from the general life skills component of our program may also be considered; however, a player's basketball ability always remains a paramount consideration. Players are not required to attend every tryout, but may be at a disadvantage- all other things being equal- over players who have been in attendance more consistently. Players selected to make a Peace team will be notified promptly following the final tryout date for such team, at which time his or her full registration package (including a registration form, birth certificate, and most recent school report card or other academic progress report) will be due. In the coaches discretion, players may be invited to participate as a member of more than one team.",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": ""
})

# AAU-033: Heading - Number of Players
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "heading",
    "content": "Number of Players-",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Sub-heading within handbook"
})

# AAU-034: Paragraph - Number of Players
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "paragraph",
    "content": "Generally, teams will carry no more than 10-12 players (with potential alternates being named as well), mainly to provide a reasonable cushion against a player(s) not being able to make a given game; as well as to ensure high quality competitive practices.",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": ""
})

# AAU-035: Heading - Registration Info/ Code of Conduct
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "heading",
    "content": "Registration Info/ Code of Conduct-",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Sub-heading within handbook"
})

# AAU-036: Paragraph - Registration Info (first paragraph)
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "paragraph",
    "content": "Registration must be completed to confirm a roster spot. Ideally, program participants will submit their fully completed registration forms prior to each team's initial tryouts. Registration forms generally seek the following information, including: for each player, his or her name, address and telephone number(s); school and academic grade; and uniform size and number preference; as well as parent(s)'/guardian(s)' emergency contact information. Upon being accepted to a team, each player must submit a copy of his or her birth certificate, and most recent school report card or other academic progress report.",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": ""
})

# AAU-037: Paragraph - Code of Conduct
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "paragraph",
    "content": "Most importantly, all players and their parents/guardians must sign a pledge confirming their willingness to adhere to (and support) all rules and responsibilities of the Peace Program, including with respect to their attendance at practices and games, and exemplary conduct at school, at home and in their communities. Players who fail to honor their commitment to the program may face disciplinary action, up to and including the possibility of extra in-practice running, benching, suspension and/or full dismissal.",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": ""
})

# AAU-038: Heading - Registration Fee
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "heading",
    "content": "Registration Fee-",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Sub-heading within handbook"
})

# AAU-039: Paragraph - Registration Fee
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "paragraph",
    "content": "Historically, Coaches K and Latta have underwritten a majority of the costs of the Stamford Peace Program, as well as for each team. While this remains the case today, each players pays a registration fee. Participants in the Peace Program (and their families) are expected to assist with fundraising, merchandise sales, and other solicitations to help even further defray our program costs. Peace hopes to pursue broader sponsorship opportunities from among local businesses and personal contacts within the program. If you have any questions with respect to sponsorship, please do not hesitate to contact us.",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Note: 'each players pays' is how the site writes it"
})

# AAU-040: Heading - Uniforms and Equipment
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "heading",
    "content": "Uniforms and Equipment-",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Sub-heading within handbook"
})

# AAU-041: Paragraph - Uniforms and Equipment
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "paragraph",
    "content": "We hope that wearing PEACE \"purple-and-gold\" becomes a major source of pride for all program participants. With that in mind, we have spared no expense in custom designing and purchasing professional quality home and away game uniforms for all players. A $100 refundable deposit is required for all uniforms. These uniforms remain on loan to all participants; players are responsible for any lost or damaged uniforms, or any uniforms that go un-returned by them at each season's end.",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": ""
})

# AAU-042: Heading - Practice Schedule
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "heading",
    "content": "Practice Schedule-",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Sub-heading within handbook"
})

# AAU-043: Paragraph - Practice Schedule (first)
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "paragraph",
    "content": "Peace teams practice at least two afternoons or evenings per week- at local gyms. In addition, from time to time, individual coaches may schedule other practice(s) as they deep appropriate in preparation for particular games or tournaments.",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Note: 'deep appropriate' is how the source text reads"
})

# AAU-044: Paragraph - Attendance at practices
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "paragraph",
    "content": "Attendance at practices is mandatory. While it is understood that scheduling conflicts or other activities or events may arise from time to time, players are responsible for notifying their coaches as far in advance as possible of any expected (or unexpected) absences.",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": ""
})

# AAU-045: Paragraph - Academic encouragement
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "paragraph",
    "content": "Consistent with Peace's broader educational focus, participants in the Peace program are strongly encouraged to complete any homework assignments and/or other academic work prior to attending their practice on a given day. See Academic Policy Statement.",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": ""
})

# AAU-046: Heading - Games/ Tournaments
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "heading",
    "content": "Games/ Tournaments-",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Sub-heading within handbook"
})

# AAU-047: Paragraph - Games/Tournaments
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "paragraph",
    "content": "Each Peace team expects to participate in somewhere between 5-8 tournaments per season- an average of three every 4-5 weeks. Most tournaments involve 3-5 weekend games; which are played at host sites throughout New England and the New York Metropolitan area. As performance merits, individual teams may enter tournament(s) beyond the Connecticut and New York regions, which could involve more significant travel and overnight stay. For example, teams that achieve success in the Connecticut State Championships, which usually take place at the end of June (beginning of July) at locations usually in the Midwestern or Southern region of the U.S. We will strive to get out to players and parents each team's practice/game/tournament schedule as early in each season as possible. Schedules will also be posted to each team's \"calendar\" on the Peace Website.",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": ""
})

# AAU-048: Heading - Playing Time
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "heading",
    "content": "Playing Time-",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Sub-heading within handbook"
})

# AAU-049: Paragraph - Playing Time
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "paragraph",
    "content": "Allocating playing time on any select team is not easy. As a general proposition, Peace coaches play those players who they believe provide their team the best opportunity for success; and who otherwise reflect the values of the Peace Program in terms of attitude, commitment and talent. Nonetheless, in most games coaches do strive to get all of a team's players at least some playing time.",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": ""
})

# AAU-050: Heading - Season Length
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "heading",
    "content": "Season Length-",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Sub-heading within handbook"
})

# AAU-051: Paragraph - Season Length
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "paragraph",
    "content": "The official AAU season typically runs from mid- March until the first or second week of July for the Spring season and September through November for the Fall season. In past years, Peace teams and players have sometimes participated in summer leagues, or attended summer basketball camps or clinics together. This remains a possibility for the future.",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": ""
})

# AAU-052: Paragraph - Fall programming
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "AAU Program Handbook/FAQ",
    "type": "paragraph",
    "content": "Peace also offers certain fall programming including weekly clinics and competitive \"open gym\" sessions, and participation in select fall tournaments.",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": ""
})

# AAU-053: Heading
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "Alumni",
    "type": "heading",
    "content": "Alumni",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": ""
})

# AAU-054: Paragraph - Former Peace AAU Players heading
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "Alumni",
    "type": "paragraph",
    "content": "Former Peace AAU Players:",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Styled as bold heading text"
})

# Now the 53 alumni entries. I'll list them as a list type since they're a list of names.
alumni_names = [
    "Rassoul Abakar – Gettysburg College",
    "Michael Alphonse – Harcum College Track and Basketball",
    "Jasyn Andrews – Western New England University Football",
    "Kweshon Askew – Long Island University Brooklyn",
    "Luke Brown – Ithaca College",
    "Cory Cannavino – Hampshire College",
    "Sean Cullinance – Grinnell College",
    "Erin Cunningham – Trinity College",
    "Ronan Doherty -- U.S. Merchant Marine Academy",
    "Cantavio Dutreil – Sacred Heart University",
    "Haley English – Skidmore College",
    "Kevin Florio – Stevens Institute of Technology",
    "Anisa Fortt – U of Delaware Track & Field",
    "McKenna Frank -- Wake Forest University",
    "Whitney Fulton – UMass Boston",
    "Petey Galgano – Manhattanville College",
    "Emma Garner – Bryn Mawr",
    "Liz Grosso – Sacred Heart University",
    "Claire Gulbin – Connecticut College",
    "Jonas Harper – Boston University",
    "Mustafa Heron – St. John's University",
    "Christina Holmgren – Swarthmore College",
    "Peace Ilegomah – U of Evansville",
    "Jaylen Jennings – Roger Williams College",
    "Dylan Johnson - Tufts University Football",
    "Akim Joseph – Gettysburg College",
    "Alexa Kellner – University of Massachusetts",
    "Rich Kelly – Quinnipiac University",
    "Maya Klein – Providence College",
    "Asiah Knight – Western Connecticut",
    "Paige Kriftcher – Colgate University",
    "Ryan Kriftcher – Rennsylear Polytechnic Institute",
    "Ami Lakoju – UC Santa Barbara",
    "Sydney Lowrey – Boston College",
    "Jeremiah Livingston - St. Peter's University",
    "Sydney Lowery - Boston College",
    "Michael Manley -- Union College",
    "Luke McGarrity -- Union College",
    "Dimitry Moise -- Utica College",
    "Sean Morris - UNC Lacrosse",
    "Ashley Polera – Muhlenberg College",
    "Will Rayman – Colgate University",
    "Stephanie Roones - Monmouth University Track & Field",
    "Kelsey Santagata – Eastern Connecticut State University",
    "Max Samberg – Cornell University",
    "Jordan Sechan – Bucknell University",
    "Skylar Sinon – Ithaca College",
    "Tyrell St. John – Fitchburg State University",
    "Matt Tepedino -- Johns Hopkins University Football",
    "Edona Thaqi – Fordham University",
    "Jake Thaw -- University of Michigan Footbal",
    "Jordan Tucker – Butler University",
    "Matt Turner – Marist College",
    "Aaron Wheeler – Purdue University",
    "Natalie Wind – Wheaton College"
]

for name in alumni_names:
    c += 1
    inventory.append({
        "id": f"AAU-{c:03d}",
        "source_url": AAU_URL,
        "source_title": "AAU Information",
        "source_section": "Alumni",
        "type": "list",
        "content": name,
        "verbatim": True,
        "fetched": FETCHED,
        "notes": "Alumni list entry"
    })

# Featured alumni: Mustapha Heron (image)
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "Alumni",
    "type": "image",
    "content": "[no alt text]",
    "verbatim": False,
    "fetched": FETCHED,
    "notes": "Featured alumni section - Mustapha Heron placeholder image (St. John's)"
})

# Mustapha Heron heading
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "Alumni",
    "type": "heading",
    "content": "Mustapha Heron",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Featured alumni name"
})

# Cantavio Dutreil image
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "Alumni",
    "type": "image",
    "content": "[no alt text]",
    "verbatim": False,
    "fetched": FETCHED,
    "notes": "Cantavio Dutreil - Sacred Heart University logo image"
})

# Cantavio Dutreil heading
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "Alumni",
    "type": "heading",
    "content": "Cantavio Dutreil",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Featured alumni name"
})

# Edona Thaqi image
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "Alumni",
    "type": "image",
    "content": "[no alt text]",
    "verbatim": False,
    "fetched": FETCHED,
    "notes": "Edona Thaqi - Fordham University logo image"
})

# Edona Thaqi heading
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "Alumni",
    "type": "heading",
    "content": "Edona Thaqi",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Featured alumni name"
})

# Jonas Harper image
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "Alumni",
    "type": "image",
    "content": "[no alt text]",
    "verbatim": False,
    "fetched": FETCHED,
    "notes": "Jonas Harper - Boston University logo image"
})

# Jonas Harper heading
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "Alumni",
    "type": "heading",
    "content": "Jonas Harper",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Featured alumni name"
})

# AAU-NNN: Heading - Fundraising
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "Fundraising",
    "type": "heading",
    "content": "Fundraising",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": ""
})

# AAU-NNN: Paragraph - About fundraising
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "Fundraising",
    "type": "paragraph",
    "content": "Stamford Peace Youth Foundation is a 501 (c) (3) not-for-profit organization reliant on donor contributions to finance the bulk of its activities. Only a very small fraction of its costs are covered via participation fees charged to players. PEACE strives to make activities affordable for all who wish to participate.",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": ""
})

# AAU-NNN: Paragraph - Charitable contributions
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "Fundraising",
    "type": "paragraph",
    "content": "Charitable contributions are always welcome!",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": ""
})

# AAU-NNN: Link - Donate
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "Fundraising",
    "type": "link",
    "content": "Click Here to make a charitable donation -> http://www.peaceyouthct.org/donate",
    "verbatim": False,
    "fetched": FETCHED,
    "notes": ""
})

# AAU-NNN: Paragraph - Foundation description
c += 1
inventory.append({
    "id": f"AAU-{c:03d}",
    "source_url": AAU_URL,
    "source_title": "AAU Information",
    "source_section": "Fundraising",
    "type": "paragraph",
    "content": "Stamford Peace Youth Foundation, Inc., a 501 (c) (3) not-for-profit corporation founded in 2008, is dedicated to the philosophy that \"basketball is a privilege\" - valuing consistent effort and achievement in children's core responsibilities in the classroom, in the community, and at home.",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": ""
})

aau_rows = c

# ======================== SPBL PAGE ==========================================
c = 0

# SPBL-001: Page heading
c += 1
inventory.append({
    "id": f"SPBL-{c:03d}",
    "source_url": SPBL_URL,
    "source_title": "Stamford Peace Basketball League",
    "source_section": "Stamford Peace Basketball League",
    "type": "heading",
    "content": "Stamford Peace Basketball League",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": ""
})

# SPBL-002: Image - SPBL banner
c += 1
inventory.append({
    "id": f"SPBL-{c:03d}",
    "source_url": SPBL_URL,
    "source_title": "Stamford Peace Basketball League",
    "source_section": "",
    "type": "image",
    "content": "[no alt text]",
    "verbatim": False,
    "fetched": FETCHED,
    "notes": "SPBL banner image"
})

# SPBL-003: Image - PEACE JCC logo
c += 1
inventory.append({
    "id": f"SPBL-{c:03d}",
    "source_url": SPBL_URL,
    "source_title": "Stamford Peace Basketball League",
    "source_section": "",
    "type": "image",
    "content": "[no alt text]",
    "verbatim": False,
    "fetched": FETCHED,
    "notes": "PEACE JCC logo"
})

# SPBL-004: Paragraph - League description
c += 1
inventory.append({
    "id": f"SPBL-{c:03d}",
    "source_url": SPBL_URL,
    "source_title": "Stamford Peace Basketball League",
    "source_section": "",
    "type": "paragraph",
    "content": "The Peace Basketball League for 1st thru 8th graders offers high level basketball instruction, well-balanced competition, organized and thoughtful scheduling, energetic and engaged coaches/referees and great fun! Teams will be grade*-based.",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": ""
})

# SPBL-005: Note about grades
c += 1
inventory.append({
    "id": f"SPBL-{c:03d}",
    "source_url": SPBL_URL,
    "source_title": "Stamford Peace Basketball League",
    "source_section": "",
    "type": "paragraph",
    "content": "*Grades may be combined based on numbers.",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Italicized footnote"
})

# SPBL-006: Link - Registration
c += 1
inventory.append({
    "id": f"SPBL-{c:03d}",
    "source_url": SPBL_URL,
    "source_title": "Stamford Peace Basketball League",
    "source_section": "",
    "type": "link",
    "content": "click here for registration -> https://www.stamfordjcc.org/index.php?src=programs&srctype=detail&refno=1087&category=Basketball%20Operations",
    "verbatim": False,
    "fetched": FETCHED,
    "notes": "External link to Stamford JCC registration"
})

# SPBL-007: Heading - SPBL Season
c += 1
inventory.append({
    "id": f"SPBL-{c:03d}",
    "source_url": SPBL_URL,
    "source_title": "Stamford Peace Basketball League",
    "source_section": "2025-2026 SPBL Season",
    "type": "heading",
    "content": "2025-2026 SPBL Season",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": ""
})

# SPBL-008: Season dates
c += 1
inventory.append({
    "id": f"SPBL-{c:03d}",
    "source_url": SPBL_URL,
    "source_title": "Stamford Peace Basketball League",
    "source_section": "2025-2026 SPBL Season",
    "type": "paragraph",
    "content": "November 22 – March 8, including playoffs",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Season date range"
})

# SPBL-009: Practice schedule description
c += 1
inventory.append({
    "id": f"SPBL-{c:03d}",
    "source_url": SPBL_URL,
    "source_title": "Stamford Peace Basketball League",
    "source_section": "2025-2026 SPBL Season",
    "type": "paragraph",
    "content": "One practice one evening a week and one game on the weekend at a local gym.",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": ""
})

# SPBL-010: Sabbath note
c += 1
inventory.append({
    "id": f"SPBL-{c:03d}",
    "source_url": SPBL_URL,
    "source_title": "Stamford Peace Basketball League",
    "source_section": "2025-2026 SPBL Season",
    "type": "paragraph",
    "content": "The Stamford JCC will accommodate Sabbath observers with Sunday only scheduling.",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Italicized"
})

# SPBL-011: Price - Early Bird
c += 1
inventory.append({
    "id": f"SPBL-{c:03d}",
    "source_url": SPBL_URL,
    "source_title": "Stamford Peace Basketball League",
    "source_section": "2025-2026 SPBL Season",
    "type": "stat",
    "content": "$220",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Price: Early Bird, thru Sept. 12"
})

# SPBL-012: Price - Regular
c += 1
inventory.append({
    "id": f"SPBL-{c:03d}",
    "source_url": SPBL_URL,
    "source_title": "Stamford Peace Basketball League",
    "source_section": "2025-2026 SPBL Season",
    "type": "stat",
    "content": "$245",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Price: Sept. 13 - Oct. 31"
})

# SPBL-013: Price - Late
c += 1
inventory.append({
    "id": f"SPBL-{c:03d}",
    "source_url": SPBL_URL,
    "source_title": "Stamford Peace Basketball League",
    "source_section": "2025-2026 SPBL Season",
    "type": "stat",
    "content": "$260",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Price: Starting Nov. 1"
})

# SPBL-014: JCC Member discount
c += 1
inventory.append({
    "id": f"SPBL-{c:03d}",
    "source_url": SPBL_URL,
    "source_title": "Stamford Peace Basketball League",
    "source_section": "2025-2026 SPBL Season",
    "type": "paragraph",
    "content": "JCC Members receive 10% off the registration price.",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Italicized"
})

# SPBL-015: Scholarship info
c += 1
inventory.append({
    "id": f"SPBL-{c:03d}",
    "source_url": SPBL_URL,
    "source_title": "Stamford Peace Basketball League",
    "source_section": "2025-2026 SPBL Season",
    "type": "contact",
    "content": "Scholarships available. Please contact Daniel Ernst at 203.487.0986 or jbasketball@stamfordjcc.org.",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Italicized; note: the mailto href points to alewin@stamfordjcc.org but the display text says jbasketball@stamfordjcc.org"
})

# SPBL-016: Scholarship email link
c += 1
inventory.append({
    "id": f"SPBL-{c:03d}",
    "source_url": SPBL_URL,
    "source_title": "Stamford Peace Basketball League",
    "source_section": "2025-2026 SPBL Season",
    "type": "link",
    "content": "jbasketball@stamfordjcc.org -> mailto:alewin@stamfordjcc.org",
    "verbatim": False,
    "fetched": FETCHED,
    "notes": "The visible email text and the actual href differ (display shows jbasketball, href targets alewin)"
})

# SPBL-017: Heading - Player Evaluations
c += 1
inventory.append({
    "id": f"SPBL-{c:03d}",
    "source_url": SPBL_URL,
    "source_title": "Stamford Peace Basketball League",
    "source_section": "Player Evaluations",
    "type": "heading",
    "content": "Player Evaluations",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": ""
})

# SPBL-018: Paragraph - Evaluations for all
c += 1
inventory.append({
    "id": f"SPBL-{c:03d}",
    "source_url": SPBL_URL,
    "source_title": "Stamford Peace Basketball League",
    "source_section": "Player Evaluations",
    "type": "paragraph",
    "content": "Evaluations will be held for ALL players in 1st through 8th grade.",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": ""
})

# SPBL-019: Paragraph - Draft for 7th/8th
c += 1
inventory.append({
    "id": f"SPBL-{c:03d}",
    "source_url": SPBL_URL,
    "source_title": "Stamford Peace Basketball League",
    "source_section": "Player Evaluations",
    "type": "paragraph",
    "content": "Players in 7th & 8th grade, NBA division, will be drafted by our volunteer coaches.",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": ""
})

# SPBL-020: Paragraph - 7th/8th evaluation date
c += 1
inventory.append({
    "id": f"SPBL-{c:03d}",
    "source_url": SPBL_URL,
    "source_title": "Stamford Peace Basketball League",
    "source_section": "Player Evaluations",
    "type": "paragraph",
    "content": "All players (new and returning) in 7th and 8th grade should attend the Sunday, November 2nd Evaluation.",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": ""
})

# SPBL-021: Note - one evaluation only
c += 1
inventory.append({
    "id": f"SPBL-{c:03d}",
    "source_url": SPBL_URL,
    "source_title": "Stamford Peace Basketball League",
    "source_section": "Player Evaluations",
    "type": "paragraph",
    "content": "*Players only need to attend one evaluation. All players will be placed on teams.",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Italicized"
})

# SPBL-022: Evaluation dates
c += 1
inventory.append({
    "id": f"SPBL-{c:03d}",
    "source_url": SPBL_URL,
    "source_title": "Stamford Peace Basketball League",
    "source_section": "Player Evaluations",
    "type": "paragraph",
    "content": "Saturday, Nov. 1 and Sunday, Nov. 2",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Evaluation date span"
})

# SPBL-023: Location
c += 1
inventory.append({
    "id": f"SPBL-{c:03d}",
    "source_url": SPBL_URL,
    "source_title": "Stamford Peace Basketball League",
    "source_section": "Player Evaluations",
    "type": "paragraph",
    "content": "Yerwood Center • 90 Fairfield Avenue, Stamford",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": ""
})

# SPBL-024: Times heading
c += 1
inventory.append({
    "id": f"SPBL-{c:03d}",
    "source_url": SPBL_URL,
    "source_title": "Stamford Peace Basketball League",
    "source_section": "Player Evaluations",
    "type": "paragraph",
    "content": "Evaluation times are as follows:",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": ""
})

# SPBL-025: 1st & 2nd Grade time
c += 1
inventory.append({
    "id": f"SPBL-{c:03d}",
    "source_url": SPBL_URL,
    "source_title": "Stamford Peace Basketball League",
    "source_section": "Player Evaluations",
    "type": "stat",
    "content": "1st & 2nd Grade • 9 - 9:45 a.m.",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Evaluation time slot"
})

# SPBL-026: 3rd & 4th Grade time
c += 1
inventory.append({
    "id": f"SPBL-{c:03d}",
    "source_url": SPBL_URL,
    "source_title": "Stamford Peace Basketball League",
    "source_section": "Player Evaluations",
    "type": "stat",
    "content": "3rd & 4th Grade • 10 - 10:45 a.m.",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Evaluation time slot"
})

# SPBL-027: 5th & 6th Grade time
c += 1
inventory.append({
    "id": f"SPBL-{c:03d}",
    "source_url": SPBL_URL,
    "source_title": "Stamford Peace Basketball League",
    "source_section": "Player Evaluations",
    "type": "stat",
    "content": "5th & 6th Grade • 11 – 11:45 a.m.",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Evaluation time slot; note en-dash"
})

# SPBL-028: 7th & 8th Grade time
c += 1
inventory.append({
    "id": f"SPBL-{c:03d}",
    "source_url": SPBL_URL,
    "source_title": "Stamford Peace Basketball League",
    "source_section": "Player Evaluations",
    "type": "stat",
    "content": "7th & 8th Grade • 12 – 12:45 p.m.",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Evaluation time slot"
})

# SPBL-029: Subject to change
c += 1
inventory.append({
    "id": f"SPBL-{c:03d}",
    "source_url": SPBL_URL,
    "source_title": "Stamford Peace Basketball League",
    "source_section": "Player Evaluations",
    "type": "paragraph",
    "content": "Date/Times/Location Subject To Change",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": "Italicized"
})

# SPBL-030: Image - game action 1
c += 1
inventory.append({
    "id": f"SPBL-{c:03d}",
    "source_url": SPBL_URL,
    "source_title": "Stamford Peace Basketball League",
    "source_section": "Player Evaluations",
    "type": "image",
    "content": "[no alt text]",
    "verbatim": False,
    "fetched": FETCHED,
    "notes": "Game action photo 1"
})

# SPBL-031: Image - game action 2
c += 1
inventory.append({
    "id": f"SPBL-{c:03d}",
    "source_url": SPBL_URL,
    "source_title": "Stamford Peace Basketball League",
    "source_section": "Player Evaluations",
    "type": "image",
    "content": "[no alt text]",
    "verbatim": False,
    "fetched": FETCHED,
    "notes": "Game action photo 2"
})

# SPBL-032: Contact info heading
c += 1
inventory.append({
    "id": f"SPBL-{c:03d}",
    "source_url": SPBL_URL,
    "source_title": "Stamford Peace Basketball League",
    "source_section": "",
    "type": "heading",
    "content": "For more information contact",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": ""
})

# SPBL-033: Contact - Mo Concepcion
c += 1
inventory.append({
    "id": f"SPBL-{c:03d}",
    "source_url": SPBL_URL,
    "source_title": "Stamford Peace Basketball League",
    "source_section": "",
    "type": "contact",
    "content": "Mo Concepcion at 203-487-0971 or mconcepcion@stamfordjcc.org",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": ""
})

# SPBL-034 through SPBL-041: Tab links (Philosophy, FAQs, etc.)
tab_links = [
    ("Philosophy", "https://www.peaceyouthct.org/layout_container/show_layout_tab?layout_container_id=111076530&page_node_id=8134836&tab_element_id=319820"),
    ("FAQs", "https://www.peaceyouthct.org/layout_container/show_layout_tab?layout_container_id=111076531&page_node_id=8134836&tab_element_id=319820"),
    ("Code of Conduct - Coaches", "https://www.peaceyouthct.org/layout_container/show_layout_tab?layout_container_id=111076532&page_node_id=8134836&tab_element_id=319820"),
    ("Code of Conduct - Players and Spectators", "https://www.peaceyouthct.org/layout_container/show_layout_tab?layout_container_id=111076533&page_node_id=8134836&tab_element_id=319820"),
    ("Disciplinary Actions", "https://www.peaceyouthct.org/layout_container/show_layout_tab?layout_container_id=111076534&page_node_id=8134836&tab_element_id=319820"),
    ("Heads Up Concussion", "https://www.peaceyouthct.org/layout_container/show_layout_tab?layout_container_id=111076535&page_node_id=8134836&tab_element_id=319820"),
    ("Gym Locations", "https://www.peaceyouthct.org/layout_container/show_layout_tab?layout_container_id=111076536&page_node_id=8134836&tab_element_id=319820"),
    ("Coaches Corner", "https://www.peaceyouthct.org/layout_container/show_layout_tab?layout_container_id=111076537&page_node_id=8134836&tab_element_id=319820"),
]
for text, href in tab_links:
    c += 1
    inventory.append({
        "id": f"SPBL-{c:03d}",
        "source_url": SPBL_URL,
        "source_title": "Stamford Peace Basketball League",
        "source_section": "",
        "type": "link",
        "content": f"{text} -> {href}",
        "verbatim": False,
        "fetched": FETCHED,
        "notes": "Bottom tab navigation link"
    })

# SPBL-042: Philosophy paragraph (visible below tabs)
c += 1
inventory.append({
    "id": f"SPBL-{c:03d}",
    "source_url": SPBL_URL,
    "source_title": "Stamford Peace Basketball League",
    "source_section": "",
    "type": "paragraph",
    "content": "The SPBL is designed to provide a positive sports experience. The primary purpose is to offer each participant the opportunity to pursue, through recreational basketball, the physical and emotional benefits of the sport. Our goal is for all players to have the opportunity to gain new skills, make new friends and have fun.",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": ""
})

# SPBL-043: Philosophy paragraph (emphasis)
c += 1
inventory.append({
    "id": f"SPBL-{c:03d}",
    "source_url": SPBL_URL,
    "source_title": "Stamford Peace Basketball League",
    "source_section": "",
    "type": "paragraph",
    "content": "The emphasis is on good sportsmanship, proper conduct, and following the rules and policies of the SPBL. Although competition is a natural part of sports activities, winning is not the primary goal. We want not only our participants, but also our coaches and fans, to play fairly and respect each other. Cheer for one's triumphs and not for their shortcomings. Win with grace and lose with dignity. Encourage others always to do their best and try their hardest.",
    "verbatim": True,
    "fetched": FETCHED,
    "notes": ""
})

spbl_rows = c

# ======================== SUMMER PAGE ========================================
c = 0
c += 1
inventory.append({
    "id": f"SUMMER-{c:03d}",
    "source_url": SUMMER_URL,
    "source_title": "SportsEngine | Sign In Step 1",
    "source_section": "",
    "type": "error",
    "content": "Page redirects to SportsEngine sign-in form rather than displaying page content. Title reads 'SportsEngine | Sign In Step 1'. Visible elements: Sign In heading, email/phone input field, 'CREATE ACCOUNT' link, 'What's SportsEngine?' link, and 'SportsEngine Help Center' link.",
    "verbatim": False,
    "fetched": FETCHED,
    "notes": "Approximately 245 characters of visible text. Page is behind a SportsEngine authentication wall."
})

summer_rows = c

# ======================== WRITE JSON ==========================================
base_dir = "C:/Users/river/OneDrive/Documents/SEO Agency/beyond-limits-site/inventory"
output_path = os.path.join(base_dir, "old-site-inventory-2.json")

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(inventory, f, indent=2, ensure_ascii=False)

# Count rows per page
aau_count = sum(1 for r in inventory if r["id"].startswith("AAU-"))
spbl_count = sum(1 for r in inventory if r["id"].startswith("SPBL-"))
summer_count = sum(1 for r in inventory if r["id"].startswith("SUMMER-"))

print(f"Total rows written: {len(inventory)}")
print(f"  AAU:   {aau_count}")
print(f"  SPBL:  {spbl_count}")
print(f"  SUMMER:{summer_count}")
print(f"\nFile written to: {output_path}")

# Print prices, dates, deadlines
print("\n=== PRICES, DATES, DEADLINES ===")
print("SPBL Season: November 22 – March 8, including playoffs")
print("Prices:")
print("  $220 - Early Bird: thru Sept. 12")
print("  $245 - Sept. 13 - Oct. 31")
print("  $260 - Starting Nov. 1")
print("  JCC Members: 10% off")
print("Evaluations: Saturday, Nov. 1 and Sunday, Nov. 2")
print("  Location: Yerwood Center • 90 Fairfield Avenue, Stamford")
print("  Times: 1st/2nd 9-9:45am, 3rd/4th 10-10:45am, 5th/6th 11-11:45am, 7th/8th 12-12:45pm")
print("Scholarship contact: Daniel Ernst at 203.487.0986 or jbasketball@stamfordjcc.org")
print("Uniform deposit: $100 refundable")

print("\n=== CLASSIFICATION NOTES ===")
print("AAU: Several sub-headings within Handbook/FAQ section are inline bold/underline text, not proper <h> elements. Listed as 'heading' type since they function as headings.")
print("SPBL: Email href (alewin@stamfordjcc.org) differs from displayed text (jbasketball@stamfordjcc.org) - noted in row.")
print("SUMMER: Returns SportsEngine sign-in form. Single error row emitted.")
print("AAU: 'each players pays' and 'deep appropriate' are verbatim from site (potential typos).")
print("AAU: 'Rennsylear Polytechnic Institute' and 'Footbal' are verbatim from alumni list.")

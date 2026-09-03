"""Builds questions_en.json — English translation of the Verité Skin Type
Test question bank, same structure as build_questions.py (20 questions per
axis, 4 answers each, 1-4 points). Family-history questions (mother/father/
grandparents) appear only under PN and WT, matching the Telegram bot."""
import json

# Each tuple: (question, [4 answers])  — answer[0]=1pt ... answer[3]=4pt

OD = [
("How does your skin look about 4-5 hours after cleansing, with no products applied?",
 ["Tight, may start to flake", "Matte, with no discomfort",
  "A slight shine only in the T-zone", "Noticeable shine across the whole face"]),

("What does your skin feel like 2-3 hours after cleansing, if you haven't applied anything?",
 ["Dry and tight", "Comfortable, skin feels neutral",
  "Slightly oily in the center of the face", "Distinctly oily, skin looks shiny"]),

("How do your pores look in daylight?",
 ["Practically invisible", "Visible only up close",
  "Enlarged in the T-zone", "Enlarged across the whole face"]),

("If you press a piece of blotting paper to your face a few hours after cleansing, what shows up on it?",
 ["Nothing, the paper stays clean", "Barely visible traces",
  "Noticeable oily marks in the T-zone", "The paper is saturated with oil across the whole area"]),

("What happens to your foundation over the course of the day?",
 ["It settles into fine lines and emphasizes dry patches", "It stays even for most of the day",
  "It starts to 'move' in the T-zone by evening", "It loses its matte finish within a couple of hours"]),

("How often do you notice flaking or rough patches on your face?",
 ["Regularly, especially in winter", "Very rarely",
  "Almost never", "Never — if anything, my skin runs oily"]),

("How often do you get blackheads or clogged pores?",
 ["Practically never", "Occasionally, in specific spots",
  "Regularly in the T-zone", "Often, across the whole face"]),

("What does your skin feel like right after rinsing with water, before applying anything else?",
 ["Strong tightness, almost uncomfortable", "A light feeling of cleanliness, no tightness",
  "Tightness that fades quickly, skin feels 'revived'", "Barely any tightness at all"]),

("Does your T-zone (forehead, nose, chin) differ from your cheeks in oiliness?",
 ["No, the whole face is equally dry", "The difference is barely noticeable",
  "The T-zone is noticeably oilier than the cheeks", "The whole face is equally oily"]),

("How does your skin respond to weather changes — heat or humidity?",
 ["Barely changes in heat; dryness increases in winter", "Minor changes in either direction",
  "Noticeable shine appears in the heat", "Skin gets oily quickly in any warm weather"]),

("How much does your skin 'ask for' moisturizer?",
 ["Without it, discomfort and tightness build up over the day",
  "Moisturizer feels nice, but skipping it is fine too",
  "A light one works well; anything richer feels like too much",
  "Any moisturizer feels unnecessary and heavy"]),

("How quickly does your hair get oily at the roots after washing it?",
 ["Very slowly — I can go several days without washing", "At a normal pace, about every 2-3 days",
  "Fairly quickly, roots need washing again within a day", "Very quickly, roots look oily within a few hours"]),

("Which textures are usually most comfortable on your skin?",
 ["Rich, thick creams and balms", "Light creams with a balanced texture",
  "Gel-creams that absorb quickly, with no film-like feel", "Light gels or fluids with no oil base"]),

("When did breakouts or noticeably oily skin first show up for you?",
 ["Practically never happened", "Occasionally, as a teenager",
  "As a teenager, and periodically now too", "Very early, and it's continued ever since"]),

("What would happen to your skin if you went a full day without any products at all?",
 ["It would get dry, possibly start flaking", "It would stay comfortable for most of the day",
  "Shine would appear in the T-zone by evening", "Skin would look noticeably oily by midday"]),

("What happens if you skip moisturizer for a day or two?",
 ["Skin reacts right away with dryness and discomfort", "Almost nothing changes",
  "A slight shine appears sooner than usual", "Skin quickly turns oily and 'heavy'"]),

("What does your skin look like right after a workout or heavy sweating?",
 ["Just damp, no real change in oiliness", "Fresh, without much shine",
  "Noticeable shine appears in the T-zone", "The whole face gets shiny and needs blotting"]),

("How often do you need mattifying products (powder, blotting sheets, primer) during the day?",
 ["Never use them", "Rarely, for special occasions",
  "Once or twice a day", "Several times a day, or it starts to shine"]),

("How does your skin feel in a room with air conditioning or heating?",
 ["It quickly starts to feel tight and dry", "Barely reacts",
  "Gets a bit more comfortable, with less shine", "Practically no reaction to dry air"]),

("How would you describe your skin type overall, for as long as you can remember?",
 ["Always dry", "Normal, rarely off-balance",
  "T-zone noticeably oilier than the rest of the face", "Always prone to oiliness"]),
]

SR = [
("What usually happens the first time you try a new product on your face?",
 ["Practically never any reaction", "Occasional slight tingling that fades quickly",
  "Redness or stinging often shows up", "Almost always some irritation, itching, or a rash"]),

("How often does your face flush with no obvious reason (emotions, food, temperature)?",
 ["Almost never", "Occasionally, and briefly",
  "Fairly often, especially in heat or cold", "Very often, and the redness lingers"]),

("How does your skin react to fragranced products (scented creams, lotions)?",
 ["No reaction, I use them without issue", "Occasional mild discomfort",
  "Irritation often shows up", "I avoid them almost entirely because of reactions"]),

("What happens to your skin in a hot or stuffy room?",
 ["Nothing in particular", "Mild redness that fades quickly",
  "Blotches or a rash appear", "Strong redness or a burning feeling"]),

("Have you had past episodes of strong redness, a rash, or flaking with no clear cause?",
 ["Never", "Once or twice in my life",
  "Periodically, a few times a year", "Regularly — it's a familiar part of my experience with my skin"]),

("Has your facial skin ever reacted to a new laundry detergent, fabric, or cosmetic wipes?",
 ["Never", "Very rarely", "Sometimes", "Often — I have to choose hypoallergenic options"]),

("How does your skin react to toners or products containing alcohol?",
 ["Tolerates them well, no discomfort", "Occasional mild tingling",
  "Dryness or irritation often shows up", "Almost always stings or turns red"]),

("What happens when you use acid-based products (AHA/BHA) or scrubs?",
 ["Skin tolerates them well, no reactions", "Occasional mild tingling",
  "Redness often appears afterward", "Almost always strong stinging or irritation"]),

("How does your skin react to cold wind or a sharp change in temperature?",
 ["Barely reacts at all", "Mild redness that fades quickly",
  "Noticeable redness or tightness appears", "Strong stinging, flaking, or a rash"]),

("What happens to your facial skin after a hot shower or steam?",
 ["Nothing in particular", "Mild redness that fades quickly",
  "Noticeable redness that lingers longer", "Strong redness or a burning sensation"]),

("How does your skin react to rubbing briskly with a towel after cleansing?",
 ["No reaction, no redness or discomfort", "Mild, temporary redness that fades quickly",
  "Noticeable redness that lasts a few minutes", "Strong redness or a feeling of irritation"]),

("If you've tried retinol or similar products, how did your skin react at first?",
 ["Never tried it, or no reaction", "Mild flaking that passed quickly",
  "Noticeable redness and irritation early on", "A strong reaction — I had to stop using it"]),

("Do you notice your skin clearly reacting with a rash or redness during stressful periods?",
 ["No, my skin isn't connected to stress", "Occasional mild changes",
  "Breakouts or redness show up fairly often", "There's almost always a noticeable reaction to stress"]),

("How does your skin feel right after a facial treatment (extractions, a peel, massage)?",
 ["No reaction, all fine", "Mild redness that fades within an hour or two",
  "Redness lasts until the end of the day", "A strong reaction, needing a day or two to settle"]),

("Are small blood vessels or visible redness (broken capillaries) noticeable on your face?",
 ["None at all", "Barely visible in a couple of spots",
  "Visible on the cheeks or nose", "A noticeable network of visible vessels in several areas"]),

("How does your skin react to sunscreen?",
 ["Any formula works fine", "Sometimes I have to be picky about the formula",
  "Irritation or breakouts often show up", "Almost all of them cause a reaction — I have to seek out special ones"]),

("Has a new product ever had to be dropped from your routine because of a reaction?",
 ["Never happened", "Once or twice", "A few times", "This happens fairly regularly"]),

("How often do you feel itching on your face for no clear reason?",
 ["Practically never", "Occasionally", "Periodically", "Fairly often"]),

("Does the skin around your lips ever get irritated by toothpaste or oral care products?",
 ["Never", "Very rarely", "Sometimes mild irritation shows up", "Fairly often there's irritation around the lips"]),

("How would you rate your willingness to try new skincare products?",
 ["I try almost anything without worry", "I choose carefully, but it's usually fine",
  "I often worry about a reaction and patch-test first", "Very cautious — my skin reacts to new things often"]),
]

PN = [
("What usually happens to your skin in the sun without protection, over a short period of time?",
 ["Almost always just turns red, barely tans", "Sometimes tans a little, sometimes turns red",
  "Tans fairly easily and evenly", "Tans very quickly and deeply"]),

("Do you have freckles on your face?",
 ["None at all", "A few, barely visible",
  "A noticeable amount, especially in summer", "A lot, across the whole face"]),

("What's left on your skin after a blemish or irritation heals?",
 ["Usually nothing at all", "Sometimes a faint mark that fades quickly",
  "Often a dark mark lasting weeks", "Almost always a noticeable pigmented mark that lingers"]),

("What was your mother's skin like in her youth, in terms of pigmentation?",
 ["No tendency toward spots or uneven tone", "A low tendency — only occasional minor marks",
  "A noticeable tendency toward spots or uneven tone", "Very pronounced pigmentation or spots"]),

("What was your father's skin like in his youth, in terms of pigmentation?",
 ["No tendency toward spots or uneven tone", "A low tendency — only occasional minor marks",
  "A noticeable tendency toward spots or uneven tone", "Very pronounced pigmentation or spots"]),

("If age spots have appeared for you, when did that start — or, going by your family, when did it start for your parents?",
 ["Haven't appeared yet, and it's a late occurrence in my family", "More likely after 40-50",
  "Fairly early, before 40", "Very early — noticeable already in youth"]),

("How even is your skin tone without makeup?",
 ["Very even, no marks", "Generally even, with a few small irregularities",
  "Noticeable unevenness in a few areas", "Pronounced unevenness, with many spots or areas of differing tone"]),

("Do you notice more sun-related marks accumulating on your face over the years?",
 ["No, barely noticeable", "Slightly", "Yes, noticeable with each summer", "Yes, very pronounced"]),

("Roughly how many moles do you have on your face and body?",
 ["Very few", "A moderate amount", "Quite a lot", "A great many, all over the body"]),

("How quickly does a noticeable tan appear in summer?",
 ["Barely appears even over a long time", "After a few weeks of regular sun exposure",
  "Within a few days", "After just one or two sun exposures"]),

("Have you noticed spots or uneven tone intensifying during certain periods (hormonal changes, pregnancy)?",
 ["No, never noticed that", "Very slightly", "Yes, noticeably", "Yes, very pronounced and long-lasting"]),

("If your skin gets injured — a cut, a burn, an insect bite — what's left after it heals?",
 ["The mark disappears without a trace", "Sometimes a faint shadow remains",
  "Often a dark mark lasting months", "Almost always a mark that lingers for a long time"]),

("How long does a tan last after summer ends?",
 ["Fades very quickly", "A few weeks", "A few months", "Lasts almost until the next summer"]),

("Are there areas on your face with a noticeably different tone (around the mouth, under the eyes, on the forehead)?",
 ["No, tone is uniform", "A barely noticeable difference",
  "A noticeable difference in a few areas", "A pronounced difference, easy to spot"]),

("Have you seen — or considered seeing — a dermatologist or aesthetician about pigmented spots?",
 ["Never needed to", "Thought about it, but no clear issue",
  "Yes, there are specific spots that bother me", "Yes, it's an ongoing topic in my skincare visits"]),

("Is the skin around your eyes or lips darker than the rest of your face?",
 ["No difference", "A barely noticeable difference", "Noticeably darker", "Significantly darker, it stands out"]),

("What was your grandparents' skin like overall, in terms of pigmentation?",
 ["No tendency toward spots or uneven tone", "A low tendency — only occasional minor marks",
  "A noticeable tendency toward spots or uneven tone", "Very pronounced pigmentation (age spots, for example)"]),

("How has your skin tone changed over the last 5-10 years?",
 ["Practically unchanged", "A few new spots have appeared",
  "Noticeably more spots have appeared", "Tone has changed significantly, with far more spots"]),

("Is there a difference in how your skin reacted to breakouts as a teenager versus now, in terms of marks left behind?",
 ["Never left marks, even as a teenager", "Rarely before, and rarely now",
  "Noticeable before, and just as noticeable now", "Marks have started lingering more and more visibly with age"]),

("How would you describe your skin's overall tendency toward pigmentation?",
 ["Not prone to spots", "A low tendency, occasional cases",
  "Noticeably prone", "Very prone — it's my main skincare concern"]),
]

WT = [
("What happens to your smile lines (around the eyes) once you stop smiling?",
 ["Disappear immediately, skin is smooth", "Fade within a few seconds",
  "Still slightly visible for a few minutes", "Remain visible even at rest"]),

("Are lines visible on your forehead when your face is fully relaxed?",
 ["No lines at all", "Barely visible, only up close",
  "A few fine lines are noticeable", "Pronounced wrinkles even at rest"]),

("What does the skin under your eyes look like in the morning after sleep?",
 ["Smooth, firm", "Slightly crumpled, but fades quickly",
  "Noticeably thin, with fine creases", "Noticeably slack, with wrinkles under the eyes"]),

("What was your mother's skin like in her youth, in terms of firmness?",
 ["Stayed smooth for a long time, wrinkles appeared very late", "First wrinkles appeared closer to 50",
  "First wrinkles appeared closer to 40", "Wrinkles appeared fairly early, before 40"]),

("What was your father's skin like in his youth, in terms of firmness?",
 ["Stayed smooth for a long time, wrinkles appeared very late", "First wrinkles appeared closer to 50",
  "First wrinkles appeared closer to 40", "Wrinkles appeared fairly early, before 40"]),

("What was your grandparents' skin like overall, in terms of firmness?",
 ["Skin stayed smooth for a long time", "Wrinkles appeared moderately, in line with age",
  "Wrinkles appeared relatively early", "Wrinkles appeared very early, skin 'aged' quickly"]),

("If you gently pinch the skin on your cheek and let go, how quickly does it spring back?",
 ["Instantly, no trace at all", "Very quickly, within a second",
  "Noticeably slower than you'd like", "Slowly — a slight fold remains"]),

("Do you notice changes in your neck skin compared to your face (loss of firmness, lines)?",
 ["No changes at all", "Minor, barely noticeable",
  "Noticeable fine lines or slackness", "Pronounced changes — neck skin clearly looks older than the face"]),

("How pronounced are your nasolabial folds (from the nose to the corners of the mouth)?",
 ["Practically unnoticeable", "A faint shadow when smiling",
  "Noticeable even at rest", "Deep, clearly defined folds"]),

("How often have you used sunscreen over the past 10-15 years?",
 ["Regularly, almost daily", "Mostly in summer or on vacation",
  "On and off, irregularly", "Rarely or almost never"]),

("How would you describe your skin's firmness to the touch — springy, or soft and pliable?",
 ["Very springy, almost like in childhood", "Generally springy",
  "Moderately springy, sometimes feels soft", "Soft and pliable, without much noticeable spring"]),

("Do you notice volume loss in your cheeks compared to how your skin used to look?",
 ["No changes at all", "Very slight changes",
  "Noticeable volume loss", "Pronounced volume loss, the face looks hollow"]),

("What's the texture of the skin around your eyes — smooth, or thin and crinkled like tissue paper?",
 ["Smooth, firm", "Generally smooth",
  "Thin in places, with fine creases", "Noticeably thin and crinkled"]),

("Do you notice a difference between the condition of your hand skin and your face when it comes to signs of aging?",
 ["No difference, everything looks youthful", "A slight difference",
  "Hands look somewhat older than the face", "A noticeable difference — hands clearly give away age"]),

("Does your skin look different after a full night's sleep compared to a poor one — is there a clear difference in how visible your lines are?",
 ["Almost no difference", "A small difference, fresher after sleep",
  "A noticeable difference — poor sleep immediately 'adds' lines", "A very pronounced difference, wrinkles become much more visible"]),

("How does the skin on your décolletage compare to your face?",
 ["Just as smooth and firm", "Minor differences",
  "Noticeably less firm than the face", "Clearly older-looking than the face, with pronounced changes"]),

("What do people usually say when they guess your age?",
 ["Always guess younger than I am", "Generally guess correctly",
  "Sometimes guess older than I am", "Often guess significantly older than I am"]),

("How noticeably has your skin changed over the last 5 years in terms of wrinkles and firmness?",
 ["Practically unchanged", "Minor changes",
  "Noticeable changes, especially around the eyes", "Very noticeable changes across the whole face"]),

("How deep are the lines that appear with expressive movement (laughing, surprise)?",
 ["Very fine, barely noticeable", "Moderately pronounced",
  "Fairly deep", "Very deep and visible from a distance"]),

("How would you rate the overall pace at which your skin is aging compared to peers your age?",
 ["Slower than most", "About the same as most",
  "A bit faster than I'd like", "Noticeably faster — this concerns me the most"]),
]

CATS = {"OD": OD, "SR": SR, "PN": PN, "WT": WT}

for cat, items in CATS.items():
    assert len(items) == 20, f"{cat} has {len(items)} questions"
    for q, a in items:
        assert len(a) == 4, q

data = {cat: [{"q": q, "a": a} for q, a in items] for cat, items in CATS.items()}

with open("questions_en.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Built questions_en.json")
print({k: len(v) for k, v in data.items()})

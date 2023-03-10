"""
Definitions of words.

This is mostly not code, but a data file; it just happens that code is the most
convenient format to maintain the corresponding word definitions.
"""

from .models import PartOfSpeech as POS
from .models import Word

words = [
    Word(
        word="accordion",
        part_of_speech=POS.NOUN,
        definitions=[
            "A small, portable, keyed wind instrument, whose tones are generated by play of the wind upon free metallic reeds.",
        ],
    ),
    Word(
        word="aground",
        part_of_speech=POS.ADVERB,
        definitions=[
            "On the ground; stranded; -- a nautical term applied to a ship when its bottom lodges on the ground.",
        ],
    ),
    Word(
        word="tacit",
        part_of_speech=POS.ADJECTIVE,
        definitions=[
            "Silently indicated or implied; understood from conditions or circumstances; inferred or inferable; expressed otherwise than by speech; indirectly manifested or communicated; wordless.",
            "*logic* Not derived from formal principles of reasoning; based on induction rather than deduction.",
        ],
    ),
    Word(
        word="epee",
        part_of_speech=POS.NOUN,
        definitions=[
            "*fencing* A fencing sword of a certain modern type; frequently opposed to foil and sabre.",
        ],
    ),
    Word(
        word="letup",
        part_of_speech=POS.NOUN,
        definitions=[
            "A reduction in pace, force, or intensity; a slowdown.",
        ],
    ),
    Word(
        word="lollop",
        part_of_speech=POS.VERB,
        definitions=[
            "To walk with a bouncing motion.",
        ],
    ),
    Word(
        word="lope",
        part_of_speech=POS.VERB,
        definitions=[
            "To run or ride with a steady, easy gait.",
        ],
    ),
    Word(
        word="loupe",
        part_of_speech=POS.NOUN,
        definitions=[
            "A magnifying glass, usually mounted in an eyepiece, often used by jewellers and watchmakers.",
        ],
    ),
    Word(
        word="opulent",
        part_of_speech=POS.ADJECTIVE,
        definitions=[
            "Characterized by extravagance or rich abundance; lavish or luxuriant.",
        ],
    ),
    Word(
        word="outpoll",
        part_of_speech=POS.VERB,
        definitions=[
            "To win more votes than.",
        ],
    ),
    Word(
        word="peloton",
        part_of_speech=POS.NOUN,
        definitions=[
            "*cycling* The main group of riders formed during a cycling road race.",
        ],
    ),
    Word(
        word="penult",
        part_of_speech=POS.NOUN,
        definitions=[
            "The next-to-last syllable of a word.",
            "The next to the last in a series.",
        ],
    ),
    Word(
        word="pone",
        part_of_speech=POS.NOUN,
        definitions=[
            "*southern* US A baked or fried cornbread (bread made of cornmeal), often made without milk or eggs.",
        ],
    ),
    Word(
        word="poppet",
        part_of_speech=POS.NOUN,
        definitions=[
            "*informal* An endearingly sweet or beautiful child.",
            "*informal* A young woman or girl.",
            "A figurine or image of idolatry.",
            "A doll made in witchcraft to represent a person, used in casting spells on that person.",
        ],
    ),
    Word(
        word="poult",
        part_of_speech=POS.NOUN,
        definitions=[
            "A young table-bird: turkey, partridge, grouse etc.",
        ],
    ),
    Word(
        word="pule",
        part_of_speech=POS.VERB,
        definitions=[
            "To whine; whimper.",
        ],
    ),
    Word(
        word="pullet",
        part_of_speech=POS.NOUN,
        definitions=[
            "A young hen, especially one less than a year old.",
            "*slang* A spineless person; a coward.",
        ],
    ),
    Word(
        word="pullout",
        part_of_speech=POS.NOUN,
        definitions=[
            "A withdrawal, especially of armed forces",
            "An object, such as a newspaper supplement that can be pulled out from something else",
        ],
    ),
    Word(
        word="putout",
        part_of_speech=POS.NOUN,
        definitions=[
            "A play made by one or more fielders that causes a batter or a base runner to be ruled out.",
        ],
    ),
    Word(
        word="tope",
        part_of_speech=POS.NOUN,
        definitions=[
            "*noun* A small shark (Galeorhinus galeus) that has a long pointed snout and is commercially harvested for food and oil.",
            "*verb* *archaic* To drink excessively; to get drunk.",
        ],
    ),
    Word(
        word="tuneup",
        part_of_speech=POS.NOUN,
        definitions=[
            "An adjustment made to an engine in order to improve its performance",
        ],
    ),
    Word(
        word="tupelo",
        part_of_speech=POS.NOUN,
        definitions=[
            "Any of several trees of the genus Nyssa of Asia and the eastern United States, having simple alternate leaves and small flowers.",
        ],
    ),
    Word(
        word="allowance",
        part_of_speech=POS.NOUN,
        definitions=[
            "Something, such as money, given at regular intervals or for a specific purpose.",
        ],
    ),
    Word(
        word="arachnid",
        part_of_speech=POS.NOUN,
        definitions=[
            "Any of the eight-legged creatures, including spiders and scorpions, of the class Arachnida",
        ],
    ),
    Word(
        word="availability",
        part_of_speech=POS.NOUN,
        definitions=[
            "The quality of being available (present and ready for use; at hand; accessible).",
        ],
    ),
    Word(
        word="axiomatic",
        part_of_speech=POS.ADJECTIVE,
        definitions=[
            "Of, relating to, or resembling an axiom; self-evident.",
        ],
    ),
    Word(
        word="biplane",
        part_of_speech=POS.NOUN,
        definitions=[
            "*aviation* An airplane that has two pairs of wings, one above the other",
        ],
    ),
    Word(
        word="brought",
        part_of_speech=POS.VERB,
        definitions=[
            "Simple past tense and past participle of bring.",
        ],
    ),
    Word(
        word="cardigan",
        part_of_speech=POS.NOUN,
        definitions=[
            "A knitted garment, such as a sweater or jacket, that opens down the full length of the front.",
        ],
    ),
    Word(
        word="carding",
        part_of_speech=POS.NOUN,
        definitions=[
            "The process of combing wool, flax, or cotton.",
        ],
    ),
    Word(
        word="competence",
        part_of_speech=POS.NOUN,
        definitions=[
            "The ability to do something well or efficiently.",
        ],
    ),
    Word(
        word="competent",
        part_of_speech=POS.ADJECTIVE,
        definitions=[
            "Properly or sufficiently qualified; capable.",
        ],
    ),
    Word(
        word="component",
        part_of_speech=POS.NOUN,
        definitions=[
            "A constituent element, as of a system. synonym: element.",
        ],
    ),
    Word(
        word="contempt",
        part_of_speech=POS.NOUN,
        definitions=[
            "The feeling or attitude of regarding someone or something as inferior, base, or worthless; scorn.",
        ],
    ),
    Word(
        word="curtain",
        part_of_speech=POS.NOUN,
        definitions=[
            "A piece of fabric or other material that hangs in a window or open space as a decoration, shade, screen, or divider.",
        ],
    ),
    Word(
        word="dormitory",
        part_of_speech=POS.NOUN,
        definitions=[
            "A building for housing a number of persons, as at a school or resort.",
        ],
    ),
    Word(
        word="draconian",
        part_of_speech=POS.ADJECTIVE,
        definitions=[
            "A code of laws made by Draco. Their measures were so severe that they were said to be written in letters of blood; hence, any laws of excessive rigor.",
        ],
    ),
    Word(
        word="draconic",
        part_of_speech=POS.ADJECTIVE,
        definitions=[
            "Of or suggestive of a dragon.",
            "Draconian.",
        ],
    ),
    Word(
        word="engulfing",
        part_of_speech=POS.VERB,
        definitions=[
            "Present participle of engulf (to swallow up or overwhelm by or as if by overflowing and enclosing).",
        ],
    ),
    Word(
        word="enveloped",
        part_of_speech=POS.ADJECTIVE,
        definitions=[
            "Enclosed or surrounded completely.",
        ],
    ),
    Word(
        word="exultant",
        part_of_speech=POS.ADJECTIVE,
        definitions=[
            "Marked by great joy or jubilation; triumphant.",
        ],
    ),
    Word(
        word="fanciful",
        part_of_speech=POS.ADJECTIVE,
        definitions=[
            "Tending to indulge in fancy.",
        ],
    ),
    Word(
        word="fixable",
        part_of_speech=POS.ADJECTIVE,
        definitions=[
            "Capable of being fixed.",
        ],
    ),
    Word(
        word="flagpole",
        part_of_speech=POS.NOUN,
        definitions=[
            "A pole used to display a flag.",
        ],
    ),
    Word(
        word="fueling",
        part_of_speech=POS.VERB,
        definitions=[
            "Present participle of fuel (something consumed to produce energy, especially).",
        ],
    ),
    Word(
        word="funneling",
        part_of_speech=POS.VERB,
        definitions=[
            "*UK* Alternative spelling of funnelling.",
        ],
    ),
    Word(
        word="habitual",
        part_of_speech=POS.ADJECTIVE,
        definitions=[
            "Formed or acquired by habit or use.",
        ],
    ),
    Word(
        word="halibut",
        part_of_speech=POS.NOUN,
        definitions=[
            "Any of several large edible flatfishes of the genus Hippoglossus and related genera, of northern Atlantic or Pacific waters.",
        ],
    ),
    Word(
        word="hematic",
        part_of_speech=POS.ADJECTIVE,
        definitions=[
            "Of, relating to, resembling, containing, or acting on blood.",
        ],
    ),
    Word(
        word="hiccuped",
        part_of_speech=POS.VERB,
        definitions=[
            "Simple past tense and past participle of hiccup (a spasm of the diaphragm, or the resulting sound).",
        ],
    ),
    Word(
        word="hiccupped",
        part_of_speech=POS.VERB,
        definitions=[
            "Simple past tense and past participle of hiccup (a spasm of the diaphragm, or the resulting sound).",
        ],
    ),
    Word(
        word="hyacinth",
        part_of_speech=POS.NOUN,
        definitions=[
            "A bulbous plant of the genus Hyacinthus, bearing beautiful spikes of fragrant flowers. Hyacinthus orientalis is a common variety.",
        ],
    ),
    Word(
        word="hyphenate",
        part_of_speech=POS.VERB,
        definitions=[
            "To divide or connect (syllables, word elements, or names) with a hyphen.",
        ],
    ),
    Word(
        word="illegality",
        part_of_speech=POS.NOUN,
        definitions=[
            "The quality or state of being illegal.",
        ],
    ),
    Word(
        word="implement",
        part_of_speech=POS.VERB,
        definitions=[
            "To put into practical effect; carry out.",
        ],
    ),
    Word(
        word="individual",
        part_of_speech=POS.NOUN,
        definitions=[
            "A human regarded as a distinctive or unique personality.",
        ],
    ),
    Word(
        word="ineffective",
        part_of_speech=POS.ADJECTIVE,
        definitions=[
            "Not producing an intended effect.",
        ],
    ),
    Word(
        word="infective",
        part_of_speech=POS.ADJECTIVE,
        definitions=[
            "Capable of producing infection; infectious.",
        ],
    ),
    Word(
        word="itemizing",
        part_of_speech=POS.VERB,
        definitions=[
            "Present participle of itemize (to list the items of).",
        ],
    ),
    Word(
        word="janitor",
        part_of_speech=POS.NOUN,
        definitions=[
            "One who attends to the maintenance or cleaning of a building.",
        ],
    ),
    Word(
        word="judicial",
        part_of_speech=POS.ADJECTIVE,
        definitions=[
            "Of, relating to, or proper to courts of law or to the administration of justice.",
        ],
    ),
    Word(
        word="legality",
        part_of_speech=POS.NOUN,
        definitions=[
            "The state or quality of being legal; lawfulness.",
        ],
    ),
    Word(
        word="livability",
        part_of_speech=POS.NOUN,
        definitions=[
            "The property of being livable (suitable to live in, habitable; possible to bear, endurable).",
        ],
    ),
    Word(
        word="mathematic",
        part_of_speech=POS.NOUN,
        definitions=[
            "Same as mathematics (the study of the measurement, properties, and relationships of quantities and sets, using numbers and symbols).",
        ],
    ),
    Word(
        word="modular",
        part_of_speech=POS.ADJECTIVE,
        definitions=[
            "Consisting of separate modules; especially where each module performs or fulfills some specified function and could be replaced by a similar module for the same function, independently of the other modules.",
        ],
    ),
    Word(
        word="mothball",
        part_of_speech=POS.NOUN,
        definitions=[
            "A marble-sized ball, originally of camphor but now of naphthalene, stored with clothes to repel moths.",
        ],
    ),
    Word(
        word="nicknaming",
        part_of_speech=POS.VERB,
        definitions=[
            "Present participle of nickname (a descriptive name added to or replacing the actual name of a person, place, or thing).",
        ],
    ),
    Word(
        word="noncompete",
        part_of_speech=POS.ADJECTIVE,
        definitions=[
            "*law* Of or pertaining to a commitment not to engage in competition with another party.",
        ],
    ),
    Word(
        word="nonviolent",
        part_of_speech=POS.ADJECTIVE,
        definitions=[
            "Peacefully resistant in response to injustice; not using violence; -- used of protests and demonstrations.",
        ],
    ),
    Word(
        word="notably",
        part_of_speech=POS.ADVERB,
        definitions=[
            "Especially; in particular.",
        ],
    ),
    Word(
        word="obliged",
        part_of_speech=POS.ADJECTIVE,
        definitions=[
            "Under an obligation to do something for someone.",
        ],
    ),
    Word(
        word="outback",
        part_of_speech=POS.NOUN,
        definitions=[
            "The remote rural part of a country, especially of Australia or New Zealand.",
        ],
    ),
    Word(
        word="paintball",
        part_of_speech=POS.NOUN,
        definitions=[
            "A game in which players on one team seek to eliminate those on an opposing team by marking them with a water-soluble dye shot in capsules from air guns.",
        ],
    ),
    Word(
        word="pedagogy",
        part_of_speech=POS.NOUN,
        definitions=[
            "The art or profession of teaching.",
        ],
    ),
    Word(
        word="photograph",
        part_of_speech=POS.NOUN,
        definitions=[
            "An image, especially a positive print, recorded by exposing a photosensitive surface to light, especially in a camera.",
        ],
    ),
    Word(
        word="pinewood",
        part_of_speech=POS.NOUN,
        definitions=[
            "The wood of the pine tree.",
        ],
    ),
    Word(
        word="plebeian",
        part_of_speech=POS.ADJECTIVE,
        definitions=[
            "Of, belonging to, or characteristic of commoners.",
        ],
    ),
    Word(
        word="prickly",
        part_of_speech=POS.ADJECTIVE,
        definitions=[
            "Having prickles.",
            "Causing trouble or vexation; thorny.",
        ],
    ),
    Word(
        word="taciturn",
        part_of_speech=POS.ADJECTIVE,
        definitions=[
            "Silent or reserved in speech; saying little; not inclined to speak or converse.",
        ],
    ),
    Word(
        word="talkative",
        part_of_speech=POS.ADJECTIVE,
        definitions=[
            "Marked by or having a disposition to talk.",
        ],
    ),
    Word(
        word="tenacity",
        part_of_speech=POS.NOUN,
        definitions=[
            "The quality or state of being tenacious; as, tenacity, or retentiveness, of memory; tenacity, or persistency, of purpose.",
        ],
    ),
    Word(
        word="thematic",
        part_of_speech=POS.ADJECTIVE,
        definitions=[
            "Relating to, or having a theme or a topic.",
        ],
    ),
    Word(
        word="tributary",
        part_of_speech=POS.NOUN,
        definitions=[
            "A stream that flows into a larger stream or other body of water.",
        ],
    ),
    Word(
        word="uncloak",
        part_of_speech=POS.VERB,
        definitions=[
            "To expose; reveal.",
        ],
    ),
    Word(
        word="unfeeling",
        part_of_speech=POS.ADJECTIVE,
        definitions=[
            "Having no physical feeling or sensation; insentient.",
        ],
    ),
    Word(
        word="upheaval",
        part_of_speech=POS.NOUN,
        definitions=[
            "A sudden, violent disruption or upset.",
        ],
    ),
    Word(
        word="viability",
        part_of_speech=POS.NOUN,
        definitions=[
            "The property of being viable; the ability to live or to succeed.",
        ],
    ),
    Word(
        word="violent",
        part_of_speech=POS.ADJECTIVE,
        definitions=[
            "Moving or acting with physical strength; urged or impelled with force; excited by strong feeling or passion; forcible; vehement; impetuous; fierce; furious; severe.",
        ],
    ),
    Word(
        word="weaving",
        part_of_speech=POS.NOUN,
        definitions=[
            "The act of one who or that which weaves; specifically, the act or art of producing cloth or other textile fabrics by means of a loom from the combination of threads or filaments.",
        ],
    ),
    Word(
        word="windmilled",
        part_of_speech=POS.VERB,
        definitions=[
            "Simple past tense and past participle of windmill.",
        ],
    ),
]

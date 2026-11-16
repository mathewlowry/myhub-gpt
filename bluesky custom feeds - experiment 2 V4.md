---
type: concept
visibility: private
updated: 2026-11-11
sources: 13
project_tags: [atprotocol, client/espon, content-strategy]
hub_tags: [bluesky custom feeds, free our feeds, algorithm, community]
reviewed: false
reviewed-sections: [synthesis]
---

# bluesky custom feeds — experiment 2, V4

*(copied from my personal LLMwiki to illustrate the content strategy I ask my personal agent to follow, as explained in [[Building a Karpathy LLMwiki inside my content pipeline]]. This level 2 file is the result of the application of a Claude skill, integrating ASD-STE100 and the "nibble-bite-meal" structure, being applied to [[bluesky custom feeds]]. As it is from my personal wiki no other links work.)*

---

*Experiment 2, V4: Mathew's restructure of [[bluesky custom feeds - experiment 2 V3]]. V3's Nibble and Bite are replaced by one Synthesis section: a Bite (message paragraph), then a Snack (bullets for Mathew, written to writing-for-policymakers principles): main findings, main questions. See [[nibble, bite and meal]], "Revising the structure". The Meal is V3's, unchanged. **The Synthesis is not yet claim-checked against the Meal: provisional, not to be cited as fact.** V3's claim check: [[experiment-2 claimcheck - bluesky custom feeds]].*

## Synthesis

Platforms' ranking for engagement promotes enragement, and hence does harm. Custom feeds are a solution, letting anyone build, share and fund an algorithm for themselves and/or their community. Open questions remain: cost, measurement and discovery for small feeds and for posters nobody sees.

* There's no such thing as a value-free algorithm, so 
	* allowing anyone to make their own means no one company owns the discovery layer. 
	* they can be shared and forked.
	* they can include features to bridge different perspectives, and allow users to further customise the feed to their own requirements
- Tools now exist to find feeds (Feed Me), run them as a business (Graze), although **cost is unsolved.** Indexing the whole network costs MySky thousands of dollars a month, and its builders are looking for philanthropists. Graze's per-feed budgets on AI nodes are a different answer to the same cost. Business models are still experimental: 
	- most: users pay to create for the benefit of themselves or others (community)
	- Skyfeed is free, but stats cost €5 a month
	- Graze: will also place ads and share revenue with you. It is "poised to expand thanks to a recent Flipboard acquisition".
	- idea: a feed that surfaces a paid article could earn a discovery fee
- **Communities want their own feeds.** Community builders asked for a way to pin feeds to Bluesky's community spaces, which are still prototypes. Blacksky's Acorn gives communities public and private feeds.
- **Feeds need checking and measurement.** AI-filtered feeds drift; your ESPON plan's fix is 15 minutes a week of checking. Graze's feed gym tests rankings by interleaving. 
- Open questions:
	- Are they filter bubbles/echo chambers?

## Meal

Feeds anyone can build and anyone can subscribe to, instead of one platform algorithm. They are the discovery layer of the Atmosphere.

### Anyone can build, find, run and fund a feed

- **Building.** SkyFeed is "An open visual feed builder for Bluesky and beyond". The community has built more than 75,000 feeds with it. [[2026-08-18 SkyFeed - Take Control of Your Feeds|SkyFeed]]
  - Its feeds are "open by design. Definitions live as public records on the AT Protocol network". [[2026-08-18 SkyFeed - Take Control of Your Feeds|SkyFeed]]
  - Feeds under OSI-approved licences "can be forked by the community". [[2026-08-18 SkyFeed - Take Control of Your Feeds|SkyFeed]]
  - So feed rules are as portable as a post. This is [[platform unbundling]] applied to feed rules.
- **Finding.** There are now too many feeds to browse, so discovery needs its own tools. Feed Me ranks feeds by what your network has created, liked, packed or shared. Its "Niche Lift" score weighs "Network Interest vs. Global Popularity", so niche community feeds beat generic ones. [[2026-08-21 Feed Me — Discover Bluesky Feeds Your Network Loves|Feed Me]]
- **As a business.** Graze Social's "Bluesky curation tool ... allows users to build (and monetize) their own feeds". It is "poised to expand thanks to a recent Flipboard acquisition". [[2026-09-09 How Graze Social’s Devin Gaffney wants to build a better internet|Graze]] *(Only the article's subtitle was clipped.)*
  - Ramos sees feeds as a shop's identity. One store ranks all products by price and reputation. Another "filters out all the product knockoffs and returns only options from local merchants". [[2026-09-06 The Atmosphere is the Amazon-Killer|Ramos]]
- **Funding.** SkyFeed is "Funded by Users, Not by Ads". All building features are free; stats cost €5 a month. [[2026-08-18 SkyFeed - Take Control of Your Feeds|SkyFeed]]
  - Basser says feeds have real leverage. They "influence discovery", and they hold it "before the engagement happens". So a feed that surfaces a paid article could earn a discovery fee. [[2026-09-18 Let's Talk Money|Basser]] See [[monetisation]].

### Engagement ranking does harm, and no ranking is neutral

- **Engagement ranking feeds outrage.** 404 Media reports a PNAS study of 715 American X users: "X’s algorithm learns what you hate and shows you more of it". [[2026-08-18 X's Algorithm Feeds Off Ragebait and Impacts Democrats|404 Media]]
  - Replies were "just 6.8% of the interactions". But X's ranking learned from them out of proportion to their number.
  - So users who argued with posts they disliked saw more of those posts: "So it’s this feedback loop of outrage baiting."
  - The effect hit self-described Democrats harder. The authors do not yet know why.
  - X's former head of product confirmed the reply weighting: "The largest contributor of seeing ragebait was the reply predictor". X has since changed it, by that account. [[2026-08-18 X's Algorithm Feeds Off Ragebait and Impacts Democrats|404 Media]]
- **Ranking shapes our picture of the public.** Resnikoff argues for leaving X, and quotes an *Unpopular Front* essay. The effect is less on our own beliefs than on our picture of the public. That picture is "shaped by algorithms that select on some aspects of the public, while sidelining others". [[2026-08-18 It Is Past Time for You to Quit Elon Musk's X|Resnikoff]]
- **No ranking is neutral.** Stray and DiResta: "there is no value-free algorithm in the first place". [[2026-09-21 🎛️📲 Meet the algorithm you can actually control and understand|Stray and DiResta]]

### MySky: users see and control every stage

MySky is a Bluesky feed by Jonathan Stray (UC Berkeley) and Renée DiResta (Georgetown). New_ Public publishes it. It has "a panel that shows you the whole pipeline, top to bottom, exactly as it runs". It claims more than 60,000 daily active users. [[2026-09-21 🎛️📲 Meet the algorithm you can actually control and understand|Stray and DiResta]]

- **Three stages, each with sliders.** [[2026-09-21 🎛️📲 Meet the algorithm you can actually control and understand|Stray and DiResta]]
  - *Sources*: people you follow, posts they liked, authors and topics you have liked, popular posts, and a time window.
  - *Ranking*: engagement and *constructiveness* have equal weight by default.
  - *Diversification*: penalties for repeated authors and topics.
- **Constructive is not polite.** "Passion and even anger can be constructive". What counts is "reasoned argument, personal experience, curiosity, respect, or a genuine attempt to communicate across difference". Ranking for this is *bridging*. Their earlier experiments found that bridging can improve relations between people who disagree. [[2026-09-21 🎛️📲 Meet the algorithm you can actually control and understand|Stray and DiResta]]
- **Chronological is not the answer either.** Whoever posts most wins, and discovery suffers. Experiments on Facebook and Instagram found that chronological feeds *increased* untrustworthy content. [[2026-09-21 🎛️📲 Meet the algorithm you can actually control and understand|Stray and DiResta]]
- **"Why Am I Seeing This?"** appears on every post. It shows where the post came from, and how each ranker and penalty scored it. [[2026-09-21 🎛️📲 Meet the algorithm you can actually control and understand|Stray and DiResta]]
- **Open source, an API, and open science.** MySky runs experiments only with consent. Commercial platforms "don’t tell them they are being studied or share the results publicly." [[2026-09-21 🎛️📲 Meet the algorithm you can actually control and understand|Stray and DiResta]]
- **Next.** Users will describe the feed they want in plain words ("more local news, less sports"), and MySky will create a slider. [[2026-09-21 🎛️📲 Meet the algorithm you can actually control and understand|Stray and DiResta]]
- **The cost.** "to run MySky we pay thousands of dollars a month for servers to index the entire ATmosphere (all ATProto content)". They are looking for philanthropists. [[2026-09-21 🎛️📲 Meet the algorithm you can actually control and understand|Stray and DiResta]] See [[how does the Atmosphere pay for itself]].

### Feeds need regular testing and checking

- **Graze's feed gym** (8 October 2026) is "an opt-in, fully automated AB testing framework for Graze users to jointly identify ways to improve the ranking and ordering of all feeds". [[2026-10-08 Graze Social (@graze.social)|Graze]]
  - It does not split users into groups: "Neither: it interleaves."
  - A few slots per page alternate between the current ranking and the candidate, "with a cap per reader so heavy users can’t swing it". [[2026-10-08 Graze Social (@graze.social)|Graze]]
- **Feeds drift.** Your ESPON launch plan: "AI-filtered feeds drift: new vocabulary appears, false positives creep in". So someone should check the feed regularly ("suggested: 15 minutes a week"). [[ESPON Bluesky Launch Plan - v1]]

### Communities want their own feeds

- **Bluesky's community spaces prototypes** (October 2026) are "places where people can gather around shared interests or social groups". The thread adds: "these are explorations, not polished or final". [[2026-10-08 alex benzer (@alexbenzer.com)|benzer thread]]
  - The prototypes put community spaces beside feeds: "spaces could live in a drawer right below your feeds, so you can hop between them easily." [[2026-10-08 alex benzer (@alexbenzer.com)|benzer thread]]
- **What community builders asked for in the replies**, as it bears on feeds: [[2026-10-08 alex benzer (@alexbenzer.com)|benzer thread]]
  - feeds and labellers attached to a community: "a way for communities to pin feeds and labelers" (shellhazard);
  - the workaround people use today: "custom handles under a shared domain, then a custom feed from members with the handle" (FexCollects);
  - starter packs as a way in: "feed starter packs into spaces" (Doll);
  - discovery, which feeds should solve, but have not solved for this user: "I don't understand how to get a post seen on this site." "I spend an hour on something: 1 like. Eventually I'm leaving." (Erik Kelly)
- **Blacksky's Acorn** gives communities "public + private feeds, member and moderation management, data hosting on their own servers (with their own branding), and more". [[2026-09-24 Blacksky Algorithms (@blackskyweb.xyz)|Blacksky]] See [[Blacksky]] and [[permissioned data]].

### A worked example: your ESPON feed

*Mathew's own project notes: a builder's view, not independent evidence.* A territorial-research feed, built in Graze for ESPON. The ESPON account will take it over. [[espon custom feeds]]

- **The theory of change.** Launch a feed good enough to promote to researchers and policymakers alike. Researchers join Bluesky because the feed has an audience. Then "as more researchers join, the feed becomes more interesting to policymakers, triggering, hopefully, a virtuous spiral". [[espon custom feeds]]
- **Trust, then topic.** Sources ranked by trust, lowest first: four outside starter packs, accounts Nikos follows, accounts ESPON follows, the ESPON starter pack. The #ESPON hashtag is the strongest topic signal, but only from trusted accounts. [[espon custom feeds]]
- **Tight rules gave an empty feed.** The v3 feed rules were a safety block, then trust group plus hashtag or keyword. They gave "almost zero content". Text similarity against one long description had to drop to 30% "to get any content". [[espon custom feeds]]
- **The fixes, from advice you were given.** [[espon custom feeds]]
  - Split the long description into four or five short ones, one idea each. "A long description that mixes topics tends to land close to" *EU policy in general*.
  - Drop the sentiment node ("sentiment analysis passed all sorts of shit").
  - Drop the image moderation node. It blocked every text-only post.
  - Add an *Ask a Question* node as the last, most expensive check.
- **Budgets.** Graze meters its language-model nodes per feed. *Natural Language*: "2,000 posts judged per feed per hour". *Ask a Question*: "500 questions asked per feed per hour". [[espon custom feeds]]
- **Handover.** In Graze, "there's no cross-account ownership transfer". So ESPON recreates (*remixes*) the public feed from its own account. [[espon custom feeds]]
- **The abuse case.** Anyone in a low-trust source "could use the hashtag indiscriminately". The only remedy would be to drop their whole starter pack. [[espon custom feeds]]

### Where the sources agree

- **Ranking for engagement alone is harmful.** The PNAS study, Stray and DiResta, and Resnikoff's source agree, from different angles. [[2026-08-18 X's Algorithm Feeds Off Ragebait and Impacts Democrats|404 Media]] [[2026-09-21 🎛️📲 Meet the algorithm you can actually control and understand|Stray and DiResta]] [[2026-08-18 It Is Past Time for You to Quit Elon Musk's X|Resnikoff]]
- **Feed rules should be visible and changeable.** SkyFeed publishes them as public, forkable records. MySky shows every stage on a panel. Epstein, the study's co-author: "we have very little transparency into how they operate". [[2026-08-18 SkyFeed - Take Control of Your Feeds|SkyFeed]] [[2026-09-21 🎛️📲 Meet the algorithm you can actually control and understand|Stray and DiResta]] [[2026-08-18 X's Algorithm Feeds Off Ragebait and Impacts Democrats|404 Media]]
- **Feeds need tuning, and tuning needs measurement.** Graze's feed gym, MySky's consented experiments, and your plan's 15 minutes a week. [[2026-10-08 Graze Social (@graze.social)|Graze]] [[2026-09-21 🎛️📲 Meet the algorithm you can actually control and understand|Stray and DiResta]] [[ESPON Bluesky Launch Plan - v1]]

### Where they disagree

- **Feeds that match your values: a fix or a trap?** MySky lets you set your own weights. Epstein, from the X study, warns: "we do have to be very aware of the potentials of value echo chambers". MySky's answer: rank for bridging by default, but let users turn it down. [[2026-09-21 🎛️📲 Meet the algorithm you can actually control and understand|Stray and DiResta]] [[2026-08-18 X's Algorithm Feeds Off Ragebait and Impacts Democrats|404 Media]]
- **Ranking or none?** MySky says chronological feeds are not the answer. One Bluesky user in the thread does without ranking, finding people "through Following only". Others cannot get seen without ranking. [[2026-09-21 🎛️📲 Meet the algorithm you can actually control and understand|Stray and DiResta]] [[2026-10-08 alex benzer (@alexbenzer.com)|benzer thread]]

### Open threads

- **Can a feed prove it caused a sale?** Basser's discovery fee assumes it can. Nothing in SkyFeed or Feed Me measures that today. SkyFeed's paid tier sells stats to the feed's *builder*, not to sellers.
- **Does the feed gym work on a small feed?** Interleaving needs users and engagement to compare. No source says how many a niche feed needs before the test means anything. The ESPON feed is in that situation at launch.
- **Who pays to index everything?** MySky indexes the whole network at thousands of dollars a month. [[2026-09-21 🎛️📲 Meet the algorithm you can actually control and understand|Stray and DiResta]] Graze's per-feed budgets on AI nodes are a different answer to the same cost. [[espon custom feeds]]
- **Bridging for a professional feed?** MySky's constructiveness score is built for political and social disagreement. Would it help a research feed? Or is topical relevance, which your ESPON feed filters for, the only thing that matters there?
- **Feeds inside communities.** If Bluesky's community spaces let communities pin feeds, ESPON's feed could become the front page of an ESPON space, not a stand-alone feed. Nothing has shipped yet. [[2026-10-08 alex benzer (@alexbenzer.com)|benzer thread]]

### Sources

- [[2026-08-18 SkyFeed - Take Control of Your Feeds]] — open, forkable feed rules; user-funded model
- [[2026-08-21 Feed Me — Discover Bluesky Feeds Your Network Loves]] — network-based feed discovery
- [[2026-09-18 Let's Talk Money]] — feeds' bargaining power; discovery fees
- [[2026-09-09 How Graze Social’s Devin Gaffney wants to build a better internet]] — monetised feeds; the Flipboard acquisition
- [[2026-09-06 The Atmosphere is the Amazon-Killer]] — feeds as storefront ranking
- [[2026-09-21 🎛️📲 Meet the algorithm you can actually control and understand]] — MySky: user-controlled ranking, bridging, explanations, open science, the cost of indexing
- [[2026-10-08 Graze Social (@graze.social)]] — the feed gym: A/B testing by interleaving
- [[2026-08-18 X's Algorithm Feeds Off Ragebait and Impacts Democrats]] — the PNAS study: engagement ranking and outrage
- [[2026-08-18 It Is Past Time for You to Quit Elon Musk's X]] — ranking shapes our picture of the public
- [[2026-10-08 alex benzer (@alexbenzer.com)]] — Bluesky's community spaces prototypes; community builders on feeds, labellers and starter packs
- [[2026-09-24 Blacksky Algorithms (@blackskyweb.xyz)]] — Acorn: public and private community feeds

**Mathew's own:**
- [[espon custom feeds]] — your ESPON feed, versions 1–7: trust groups, the empty-feed problem, AI nodes and their budgets, handover by remix
- [[ESPON Bluesky Launch Plan - v1]] — feeds drift; who checks them, and how often

### On the hub

*No overlaps in `/hub`.* The ESPON feed is client work, not a hub item. Could it become one, as the case study your notes hope for ("other EU research programs could follow")? [[espon custom feeds]]

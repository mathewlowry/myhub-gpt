---
type: concept
visibility: private
updated: 2026-10-22
sources: 13
project_tags: [atprotocol, client/espon]
hub_tags: [bluesky custom feeds, free our feeds, algorithm, community]
---
# bluesky custom feeds

*(copied from my personal LLMwiki to illustrate the content strategy I ask my personal agent to follow, as explained in [[Building a Karpathy LLMwiki inside my content pipeline]]. This file is a "raw" level 2 file created by my agent before the content strategy was refined using ASD-STE100 and the "nibble-bite-meal" structure, resulting in [[bluesky custom feeds - experiment 2 V4]]. As it is from my personal wiki no other links work.)*

---

Feeds anyone can build and anyone can subscribe to, instead of one platform algorithm. They're the discovery layer of the Atmosphere.

**Building them.** SkyFeed is "An open visual feed builder for Bluesky and beyond", with 75,000+ feeds built by the community. [[2026-08-18 SkyFeed - Take Control of Your Feeds|SkyFeed]] Its feeds are "open by design. Definitions live as public records on the AT Protocol network", and feeds under OSI-approved licences "can be forked by the community". [[2026-08-18 SkyFeed - Take Control of Your Feeds|SkyFeed]] So a feed's *rules* are as portable as a post, which is [[platform unbundling]] applied to the algorithm itself.

**Finding them.** There are now too many feeds to browse, so discovery needs its own tools. Feed Me ranks feeds by what your network has created, liked, packed or shared, using a "Niche Lift" score of "Network Interest vs. Global Popularity" so niche community feeds beat generic ones. [[2026-08-21 Feed Me — Discover Bluesky Feeds Your Network Loves|Feed Me]]

**Owning them as a business.** Graze Social's "Bluesky curation tool ... allows users to build (and monetize) their own feeds", and is "poised to expand thanks to a recent Flipboard acquisition". [[2026-09-09 How Graze Social’s Devin Gaffney wants to build a better internet|Graze]] *(Only the article's subtitle was clipped.)* Ramos imagines feeds as a shop's identity: one store ranks all products by price and reputation, another "filters out all the product knockoffs and returns only options from local merchants". [[2026-09-06 The Atmosphere is the Amazon-Killer|Ramos]]

**Paying for them.** SkyFeed is "Funded by Users, Not by Ads": free for all building features, €5 a month for stats. [[2026-08-18 SkyFeed - Take Control of Your Feeds|SkyFeed]] Basser argues feeds have real leverage, because they "influence discovery" and hold it "before the engagement happens", so a feed that surfaces a paid article could earn a discovery fee. [[2026-09-18 Let's Talk Money|Basser]] See [[monetisation]].

## Why the ranking matters

**What engagement ranking does.** A PNAS study of 715 American X users, reported by 404 Media: "X’s algorithm learns what you hate and shows you more of it". Replies were "just 6.8% of the interactions", but the algorithm learned disproportionately from them, so people who argued with posts they disliked were shown more of them: "So it’s this feedback loop of outrage baiting." It hit self-described Democrats harder, for reasons the authors don't yet know. X's former head of product confirmed the reply weighting, and says it has since been changed: "The largest contributor of seeing ragebait was the reply predictor". [[2026-08-18 X's Algorithm Feeds Off Ragebait and Impacts Democrats|404 Media]]

**What it does to what we think others think.** Resnikoff, arguing for leaving X, quotes an *Unpopular Front* essay: the effect is less on our own beliefs than on our picture of the public, which is "shaped by algorithms that select on some aspects of the public, while sidelining others". [[2026-08-18 It Is Past Time for You to Quit Elon Musk's X|Resnikoff]]

**No ranking is neutral.** Stray and DiResta: "there is no value-free algorithm in the first place". [[2026-09-21 🎛️📲 Meet the algorithm you can actually control and understand|Stray and DiResta]]

## Feeds as user control: MySky

MySky, by Jonathan Stray (UC Berkeley) and Renée DiResta (Georgetown), published by New_ Public, is a Bluesky feed with "a panel that shows you the whole pipeline, top to bottom, exactly as it runs". It claims more than 60,000 daily active users. [[2026-09-21 🎛️📲 Meet the algorithm you can actually control and understand|Stray and DiResta]]

- **Three stages, each with sliders.** *Sources* (people you follow, posts they liked, authors and topics you've liked, popular posts, and a time window); *ranking*, where engagement and *constructiveness* are weighted equally by default; and *diversification*, with penalties for repeated authors and topics. [[2026-09-21 🎛️📲 Meet the algorithm you can actually control and understand|Stray and DiResta]]
- **Constructive is not polite.** "Passion and even anger can be constructive". What counts is "reasoned argument, personal experience, curiosity, respect, or a genuine attempt to communicate across difference". This is *bridging*, which their earlier experiments found can improve relations between people who disagree. [[2026-09-21 🎛️📲 Meet the algorithm you can actually control and understand|Stray and DiResta]]
- **Chronological isn't the answer either.** Whoever posts most wins, discovery suffers, and experiments on Facebook and Instagram found chronological feeds *increased* untrustworthy content. [[2026-09-21 🎛️📲 Meet the algorithm you can actually control and understand|Stray and DiResta]]
- **"Why Am I Seeing This?"** on every post: where it came from, and how each ranker and penalty scored it. [[2026-09-21 🎛️📲 Meet the algorithm you can actually control and understand|Stray and DiResta]]
- **Open source, an API, and open science.** Experiments run only with consent, unlike commercial platforms, which "don’t tell them they are being studied or share the results publicly." Next: describe the feed you want in plain words ("more local news, less sports"), and it creates a slider. [[2026-09-21 🎛️📲 Meet the algorithm you can actually control and understand|Stray and DiResta]]
- **The cost.** "to run MySky we pay thousands of dollars a month for servers to index the entire ATmosphere (all ATProto content)", and they're looking for philanthropists. [[2026-09-21 🎛️📲 Meet the algorithm you can actually control and understand|Stray and DiResta]] See [[how does the Atmosphere pay for itself]].

## Testing and tuning them

**Graze's feed gym** (8 October 2026): "an opt-in, fully automated AB testing framework for Graze users to jointly identify ways to improve the ranking and ordering of all feeds". It doesn't split readers into groups: "Neither: it interleaves." A few slots per page alternate between the current ordering and the candidate, "with a cap per reader so heavy users can’t swing it". [[2026-10-08 Graze Social (@graze.social)|Graze]]

**Feeds drift.** Your ESPON launch plan: "AI-filtered feeds drift: new vocabulary appears, false positives creep in", so someone should check the feed regularly ("suggested: 15 minutes a week"). [[ESPON Bluesky Launch Plan - v1]]

## Feeds for communities

**Bluesky's own "spaces" prototypes** (October 2026): "places where people can gather around shared interests or social groups", and "these are explorations, not polished or final". In the prototypes, spaces sit beside feeds: "spaces could live in a drawer right below your feeds, so you can hop between them easily." [[2026-10-08 alex benzer (@alexbenzer.com)|benzer thread]] What community builders asked for in the replies, as it bears on feeds:

- feeds and labellers attached to a community: "a way for communities to pin feeds and labelers" (shellhazard);
- the workaround people use today: "custom handles under a shared domain, then a custom feed from members with the handle" (FexCollects);
- starter packs as a way in: being able to "feed starter packs into spaces" (Doll);
- and the discovery problem that feeds are meant to solve, unsolved for this user: "I don't understand how to get a post seen on this site." "I spend an hour on something: 1 like. Eventually I'm leaving." (Erik Kelly) [[2026-10-08 alex benzer (@alexbenzer.com)|benzer thread]]

**Blacksky's Acorn** gives communities "public + private feeds, member and moderation management, data hosting on their own servers (with their own branding), and more". [[2026-09-24 Blacksky Algorithms (@blackskyweb.xyz)|Blacksky]] See [[Blacksky]] and [[permissioned data]].

## A worked example: your ESPON feed

*Mathew's own project notes: a builder's view, not independent evidence.* A territorial-research feed built in Graze for ESPON, to be handed over to the ESPON account. [[espon custom feeds]]

- **The theory of change.** Launch a feed good enough to promote to researchers and policymakers alike; researchers join Bluesky because the feed has an audience, and "as more researchers join, the feed becomes more interesting to policymakers, triggering, hopefully, a virtuous spiral". [[espon custom feeds]]
- **Trust, then topic.** Sources ranked by trust: four outside starter packs (lowest), accounts Nikos follows, accounts ESPON follows, and the ESPON starter pack (highest). The #ESPON hashtag is the strongest topic signal, but only from trusted accounts. [[espon custom feeds]]
- **Tight rules, empty feed.** The v3 logic (safety block, then trust group plus hashtag or keyword) gave "almost zero content". Text similarity against one long description had to drop to 30% "to get any content". [[espon custom feeds]]
- **The fixes, from advice you were given.** Split the long description into four or five short ones, one idea each, because "A long description that mixes topics tends to land close to" *EU policy in general*. Drop the sentiment node ("sentiment analysis passed all sorts of shit") and the image moderation node, which blocked every text-only post. Add an *Ask a Question* node as the last, most expensive check. [[espon custom feeds]]
- **Budgets.** Graze meters its language-model nodes per feed: *Natural Language* at "2,000 posts judged per feed per hour", *Ask a Question* at "500 questions asked per feed per hour". [[espon custom feeds]]
- **Handover.** In Graze, "there's no cross-account ownership transfer": ESPON recreates (*remixes*) the public feed from its own account. [[espon custom feeds]]
- **The abuse case.** Anyone in a low-trust source "could use the hashtag indiscriminately", and the only remedy would be dropping their whole starter pack. [[espon custom feeds]]

## Where the sources agree

- **Optimising for engagement alone is harmful.** The PNAS study, Stray and DiResta, and Resnikoff's source, from different angles. [[2026-08-18 X's Algorithm Feeds Off Ragebait and Impacts Democrats|404 Media]] [[2026-09-21 🎛️📲 Meet the algorithm you can actually control and understand|Stray and DiResta]] [[2026-08-18 It Is Past Time for You to Quit Elon Musk's X|Resnikoff]]
- **Feed rules should be visible and changeable.** SkyFeed (definitions as public, forkable records), MySky (every stage on a panel), and Epstein, the study's co-author ("we have very little transparency into how they operate"). [[2026-08-18 SkyFeed - Take Control of Your Feeds|SkyFeed]] [[2026-09-21 🎛️📲 Meet the algorithm you can actually control and understand|Stray and DiResta]] [[2026-08-18 X's Algorithm Feeds Off Ragebait and Impacts Democrats|404 Media]]
- **Feeds need tuning, and tuning needs measurement.** Graze's feed gym, MySky's consented experiments, and your plan's 15 minutes a week. [[2026-10-08 Graze Social (@graze.social)|Graze]] [[2026-09-21 🎛️📲 Meet the algorithm you can actually control and understand|Stray and DiResta]] [[ESPON Bluesky Launch Plan - v1]]

## Where they disagree

- **Feeds that match your values: a fix or a trap?** MySky lets you set your own weights. Epstein, from the X study, warns "we do have to be very aware of the potentials of value echo chambers". MySky's answer is to rank for bridging by default, but users can turn it down. [[2026-09-21 🎛️📲 Meet the algorithm you can actually control and understand|Stray and DiResta]] [[2026-08-18 X's Algorithm Feeds Off Ragebait and Impacts Democrats|404 Media]]
- **Algorithm or none?** MySky: chronological feeds aren't the answer. Some Bluesky users like it because they find people "through Following only", while others can't get seen without an algorithm. [[2026-09-21 🎛️📲 Meet the algorithm you can actually control and understand|Stray and DiResta]] [[2026-10-08 alex benzer (@alexbenzer.com)|benzer thread]]

## Open threads

- Basser's discovery fee assumes feeds can prove they caused a sale. Nothing in SkyFeed or Feed Me measures that today; SkyFeed's paid tier sells stats to the feed's *builder*, not to sellers.
- **Does the feed gym work on a small feed?** Interleaving needs readers and engagement to compare. No source says how many a niche feed needs before the test means anything. That's the ESPON feed's situation at launch.
- **Who pays to index everything?** MySky indexes the whole network at thousands of dollars a month. [[2026-09-21 🎛️📲 Meet the algorithm you can actually control and understand|Stray and DiResta]] Graze's per-feed budgets on AI nodes are a different answer to the same cost. [[espon custom feeds]]
- **Constructiveness for a professional feed?** MySky's bridging score is built for political and social disagreement. Would it help a research feed, or is topical relevance, which your ESPON feed filters for, the only thing that matters there?
- **Feeds inside communities.** If Bluesky's spaces let communities pin feeds, a feed like ESPON's could become the front page of an ESPON space rather than a stand-alone feed. Nothing has shipped yet. [[2026-10-08 alex benzer (@alexbenzer.com)|benzer thread]]

## Sources

- [[2026-08-18 SkyFeed - Take Control of Your Feeds]] — open, forkable feed definitions; user-funded model
- [[2026-08-21 Feed Me — Discover Bluesky Feeds Your Network Loves]] — network-based feed discovery
- [[2026-09-18 Let's Talk Money]] — feeds' bargaining power; discovery fees
- [[2026-09-09 How Graze Social’s Devin Gaffney wants to build a better internet]] — monetised feeds; the Flipboard acquisition
- [[2026-09-06 The Atmosphere is the Amazon-Killer]] — feeds as storefront algorithms
- [[2026-09-21 🎛️📲 Meet the algorithm you can actually control and understand]] — MySky: user-controlled ranking, bridging, explanations, open science, the cost of indexing
- [[2026-10-08 Graze Social (@graze.social)]] — the feed gym: A/B testing by interleaving
- [[2026-08-18 X's Algorithm Feeds Off Ragebait and Impacts Democrats]] — the PNAS study: engagement ranking and outrage
- [[2026-08-18 It Is Past Time for You to Quit Elon Musk's X]] — algorithms shape our picture of the public
- [[2026-10-08 alex benzer (@alexbenzer.com)]] — Bluesky's spaces prototypes; community builders on feeds, labellers and starter packs
- [[2026-09-24 Blacksky Algorithms (@blackskyweb.xyz)]] — Acorn: public and private community feeds

**Mathew's own:**
- [[espon custom feeds]] — your ESPON feed, versions 1–7: trust groups, the empty-feed problem, AI nodes and their budgets, handover by remix
- [[ESPON Bluesky Launch Plan - v1]] — feeds drift; who checks them, and how often

## On the hub

*No overlaps in `/hub`.* The ESPON feed is client work, not a hub item. Could it become one, as the case study your notes hope for ("other EU research programs could follow")? [[espon custom feeds]]

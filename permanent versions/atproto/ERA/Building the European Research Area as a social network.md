---
tags:
  - status/draft
  - type/blog
  - topic/adoption
  - audience/science
  - audience/institutions
---
# Building the European Research Area as a social network 

**There are tens of thousands of researchers in Europe right now. They're producing knowledge, citing each other, following policy debates, and attending conferences. But as a community, their work is scattered across walled knowledge silos. A handful of first-generation Atmosphere apps could change that, without requiring any researcher to do anything they wouldn't want to do anyway.**

This post sets out how.

*(This is an early draft, written using the [permanent versions pattern](https://mathewlowry.medium.com/two-wiki-authors-and-a-blogger-walk-into-a-bar-7106c8376c6e). Details and version control in the footer.)*

## The Bluesky layer: making the community visible

The starting point is Bluesky, the most mature ATProtocol app. The building blocks here are ones most Atmosphere users already know: Starter Packs, Custom Feeds, and maybe Labels.

Each EU research project has the building blocks of community: participants, a topic, and a challenge. Bluesky's primitives map onto this naturally. 
### Project Starter Packs

Each project can create a **Starter Pack** containing all the researchers in the project, so anyone interested can follow the whole team in one click. The Pack also provides a feed of everything those researchers post... including snaps of pets and holidays. 
### High-value custom feeds

Hence the starter pack can also highlight up to three Custom Feeds, each driven by a Bluesky List and a hashtag. 

If the project has an official Atmosphere account, then it's Bluesky account can provide the official project news, while all three custom feeds can be high-value community conversations. I describe these in detail in [[How newsrooms, scientific institutions & governments can best use Bluesky]]), but the key think to know is that a well-designed Custom Feed is not a broadcast channel. It is a community space.

> a well-designed Custom Feed is not a broadcast channel. It is a community space.

A broadcast channel pushes the organisation's official content at followers. A high-value Custom Feed is where the organisation's experts hang out with each other *and* external experts they trust. Posts appear in the feed not because they're official, but because they're relevant and they come from accounts the project team respects.

This design has several consequences that compound over time:
- **Inclusion is a consecration of expertise**: being added to a feed signals that the community rates your work, so included accounts are incentivised to post well and stay there
- **Feeds grow through trust**: experts already in the feed can suggest people *they* trust, typically by quoteposting with the feed's hashtag — the community extends its own membership
- **Troll-free by design**: posts only appear if they come from listed accounts *and* carry the hashtag, so the feed stays high-signal regardless of what's happening in the wider Bluesky environment
- **Reach without virality**: researchers don't need to go viral to reach their audience — a well-curated, high-value feed attracts the audience to them

For research communities, this allows a project to use Bluesky not just to announce outputs, but also to convene a conversation with trusted experts around a research area — including voices from outside the project who are doing relevant work.

Note that Starter Packs can only lost three custom feeds, but a project can have as many as it likes.

### Project Clusters

Individual projects are the unit of work, but interesting things can also happen at a higher level. So consider Project Clusters - a group of projects relevant to a specific research strand of a research workprogramme, or a policy area. 

On the Atmosphere, a cluster can be managed by a single Cluster Account Manager, creating economies of scale: no need for each project to have its own official account, as the cluster manager handles all starter packs and feeds across all projects, and adds **cluster custom feeds** on top. 

Cluster custom feeds operate across all projects in the cluster, surfacing their *best* content for audiences — policymakers, non-scientific stakeholders, interested public — who want outcomes, not day-to-day project updates. Two useful algorithms spring to mind:

- **Cluster highlight feeds**: the best posts from across all project custom feeds, including relevant content from outside the projects
- **Cluster official feeds**: all posts from accounts carrying a Cluster label (see below).

As long as the researchers use Bluesky and use hashtags, and their handles are shared with the cluster manager, everything happens automatically.

The incentive for researchers is real: post about your project, get enough likes to be picked up in the cluster feed, and reach an audience you'd never reach otherwise. And, as set out below, researchers can be connected via another Atmosphere app (Sifa) to their organisation, so those benefits transfer to the researchers' organisation as well.

### Labels

A single labeller can serve many purposes across the research community - for example:

- **Global label** — *Horizon-funded*: applied to every project account and the personal accounts of each researcher in a Horizon project, making the whole community discoverable and filterable
- **Cluster labels**: applied to project accounts in a given cluster, automatically generating a feed of all posts by projects in that cluster

And, of course, the only people who see the labels are those who choose to. But if you're a researcher in one project, it is useful to see that the researcher you're replying to on Bluesky is actually involved in another project in the same Cluster. 

---

## The collective knowledge layer

Bluesky makes the community visible. Apps like Sill, Semble and Margin can make its knowledge accessible, while Sifa knits the social network together by providing community member profiles.

A few caveats before going further:

- These are all first-generation Atmosphere apps, interoperating extensively and evolving fast
- The ideas below describe what's possible now; by the time most research projects adopt them, the apps will be more capable and there will almost certainly be more like them
- Several of the more powerful features await **cross-lexicon groups**, which will allow group membership to be managed once and applied across multiple apps. Until then, Bluesky lists are the coordination mechanism

### Sill: discovery

Sill surfaces new content based on what people in your social graph are sharing, liking, and engaging with. For individual researchers, it's already valuable. Collectively, it becomes a knowledge discovery layer for the project.

If I was doing this right now, I'd ask everybody in a project to use Sill for their own benefit, and use Sill's bookmark feature to highlight content they think could be useful to the rest of the project and its community. That's because Sill bookmarks are written to the researcher's PDS (unlike Bluesky bookmarks, which stay on Bluesky's servers), so the resources bookmarked by every researcher in a project list can be aggregated into a **Project Library**, and the resources bookmarked by the wider project community can become a **Community Library**.

In the future, when cross-lexicon groups become available, Sill will roll out Sill Groups, a premium feature Tyler demoe'd at [my AtmosphereConf 2026 workshop](https://experiments.myhub.ai/the_atmosphere_as_research_infrastructure) last March in Vancouver. If everyone in a project or community is part of a cross-lexicon group, they can then be easily added to a Sill Group, giving all of them a shared discovery tool for project collective intelligence.

### Semble and Margin: organisation and annotation

Both Semble and Margin let researchers organise knowledge they discover online — saving, tagging, collecting, connecting. They interoperate extensively, with complementary strengths: Semble lets users connect resources to each other, for example, while Margin enables more granular organisation plus inline annotation, with notes presented on the original knowledge.

For the purposes of this post, the underlying idea is the same: if each researcher in a project uses Semble or Margin, whoever manages the project or community can aggregate across their PDSs to produce a shared Project Library or Community Library of everything the team has curated, collected and commented on. 

### SIFA: researcher profiles

SIFA is building into the space currently occupied by LinkedIn. In fact, you can import your LinkedIn data into SIFA to create a starting point for your Sifa profile. Unlike LinkedIn, however, SIFA is on the Atmosphere, so:

* if you come across a researcher on the Atmosphere, you can find their SIFA profile
* your SIFA profile can automatically pull in your activity from across the Atmosphere, as well as external sources like ORCID, giving a rich, automatically updated view of a researcher's work, interests, and connections.

SIFA accounts are therefore important connective tissue, providing the core product *all* communities need: community member profiles.

> discovering people through content, and discovering content through people

This is vital, because communities are all about discovering people through content, and discovering content through people. Those connections happen through community profiles - if you see something from somebody on any Atmosphere app that you find interesting, you can visit their Sifa profile and discover *everything* they find interesting. 

---

## Bringing it together: decentralised resource databases

Each of the above apps present the slice of the community's knowledge the app was used to create. But all this content is freely available on researchers' PDSs. And we know — via the project lists — who is in which project, and hence which project cluster.

That means all of the following can be brought together:

- Resources being discussed in project and cluster Bluesky custom feeds
- Resources bookmarked via Sill, curated via Semble and annotated via Margin by both project members and their wider communities.

Collected into a database (or via a live interface querying the PDSs directly — the architecture is an open choice), this content can be searched and filtered by:

- **Who interacted with it** — which researchers in which projects
- **Rank** — a composite metric of how many community members are connected to it
- **Topic** — via AI-powered classification
- **How they interacted with it** — which app, which action
- **Organisation** (future, pending SIFA Company Pages): filtering by institution across projects

The same sources can be used to create all sorts of project feeds:

- What this project's researchers are discovering right now
- Everything our community is reading, organising, and discussing
- Our community's favourites
- etc

### From Project to Cluster to the Horizon

While these databases can be localised to the project websites, there's nothing structurally different between doing this for one project, a cluster of projects, or entire research programmes. The same tools (centralised database or live PDS interface) just need to know the IDs of the relevant project and community lists.

In Europe, where so much research is funded by the EU programmes, it becomes feasible to create something genuinely new: the living, searchable collective intelligence of thousands of EU-funded researchers. Not a static publication database, but a real-time record of what the research community is discovering, reading, debating, and connecting, *right now* and in the past.

### Adding value for non-scientific audiences 

The above is already valuable, but principally for scientists. But the content assembled at Cluster level, in particular, creates  further opportunities by providing useful raw material which can be transformed. In particular:

* knowledge brokers synthesising the above collective intelligence for policymakers
* science communicators using it as raw material for the interested general public.

Researchers don't need to do anything to provide their knowledge - by using the project-level tools set out earlier, their work can be picked up and used by communications  specialists. But it does make them and their work more directly accessible to everyone, which cannot be a bad thing.

## What makes this possible

**None of the above requires researchers to do anything they wouldn't already want to do.**

Custom feeds are useful whether or not anyone is aggregating them. Sill bookmarks help you remember what you found. Semble and Margin help you organise what you know. SIFA gives you a better professional profile than LinkedIn. 

The added value policymaker/public-friendly knowledge layer is built on top by specialists using the knowledge created by researchers using tools that serve them individually. Everyone does their own thing, and they can because the knowledge flows seamlessly rather than being locked away in walled gardens.

>  the knowledge flows seamlessly rather than being locked away in walled gardens

What we could build: a living picture of what Europe's research community is discovering, reading, debating, and connecting *right now* — visible to other researchers, to policymakers, to science communicators, and to the next generation of researchers trying to find where the interesting conversations already are. Not a static project database, but a living, interactive community with a hugely powerful memory.

---

## Revision Notes

This is one of this wiki's pages managed with the **permanent versions pattern** described in  [Two wiki authors and a blogger walk into a bar…](https://mathewlowry.medium.com/two-wiki-authors-and-a-blogger-walk-into-a-bar-7106c8376c6e)  

- changes in this version: 
	- none, as it's version 1
- version control
    - this is version: 1
    - this is the current version: [[Building the European Research Area as a social network]]
    - here is the previous version: n/a

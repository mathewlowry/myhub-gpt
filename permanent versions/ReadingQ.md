---
creation date: 2026-08-24 11:34
modification date: 236 August 2026 11:34:51
---
# ReadingQ: building my first Obsidian plugin with Claude Code

**The Reading Queue Manager Obsidian plugin is a first step towards creating an entirely local-first publishing pipeline for my Hub, *and* publishing it onto the Atmosphere. It's also the first time in 15 years I've gotten something useful from AI.**

This is the beginning of a journey, which I'm taking with Loki, my personal knowledge management AI assistant, created as a result of [Peter Kaminiski](https://peterkaminski.ai/)'s generosity. If you'd like your own AI assistant that lives in your notes, learns as you work and helps you build whatever you need, you can [get started with Pete's approach for free](https://peterkaminski.ai/pkai-agent/), although I highly recommend becoming a [PKAI Insider](https://insiders.peterkaminski.ai/). 

*(Notes: This is version 3 of this post, covering version 2 of the ReadingQ Manager - more details in the footer. As before, if your first reaction is to dogpile me for using AI to create code for personal use, please hold your nose and read to the end.)*

## Why this plugin? 

I've been organizing my reading-thinking-writing-publishing-sharing process using a [content pipeline](https://medium.com/the-mission/why-you-need-a-personal-content-strategy-ff05c84fccfd) for well [over 10 years](https://medium.com/better-humans/manage-the-firehose-or-it-will-manage-you-791097bc53e2). I've barely tweaked it since 2013: 

* resources (potentially interesting things to read) still arrive in curated inboxes, 
* which I scan to select content for my Reading Queue; 
* then they're read, annotated, tagged and published onto my Hub as [Stuff I Like](https://myhub.ai/@mathewlowry/?quality=all&types=like&timeframe=anytime), 
* with most also informing the [Stuff I Think or Do](https://myhub.ai/@mathewlowry/?quality=all&types=do&types=think&timeframe=anytime) precisely *because* I spent that time annotating them, rather than just speedreading. 

The *tools* I use to move and develop knowledge through that pipeline, however, have evolved many times: Pocket & Raindrop (reading queues); delicious & diigo (personal libraries); ifttt, Tumblr, *Obsidian, MassiveWiki, MyHub, LinkedIn, Medium & Leaflet* (publishing systems); and Twitter, Facebook, *LinkedIn, Leaflet & Bluesky* (social distribution) have all played their part. Those in italics still do.

![[pipeline-plugins-1-rqm.png]]

*Image adapted from [[MyHub on the ATmosphere]].*

Throughout those years, however, the weakest pipeline link has remained unchanged: getting from *adding* something to my Reading Queue to actually *reading and annotating* it. This is not a tool problem, as an article I just dug up from my Reading Queue points out:

> "*a bookmark is a promise you make to a version of yourself who never shows up... capturing gives you the exact dopamine hit that thinking is supposed to give you, minus the work*" - [The Rise and Fall of the Second Brain](https://medium.com/health-science/the-rise-and-fall-of-the-second-brain-30d164b56750), Chris Ng, 6 August 2026.

A few weeks ago I would never have been able to find that article - my Reading Queue was a Raindrop account, so the only pipeline content I could actually find was the stuff I'd already read, annotated and tagged. 
## How ReadingQ Manager now works

**But I saw Chris' article just after I set up my plugin, so I shared it to my Obsidian vault, not Raindrop.** 

Here's what that looks like with v2 of the ReadingQ Manager:

* I was using a mobile phone, where "Share to Obsidian" allows me to append the URL to the bottom of my vault's daily note. I designed my daily note using [Templater](https://community.obsidian.md/plugins/templater-obsidian), so Chris' URL appeared under the last heading ("*shared from apps*") 
	* (note: if I had been using a browser, I've configured [Obsidian Web Clipper](https://obsidian.md/clipper) to do the same thing with a keystroke)
* sometime later that day my plug-in was activated, either by me opening Obsidian on either of my PCs, or triggering it manually from my phone
* it sent a chunk of Chris' article to Claude, which compares it to my project list (a semantically rich file in my Obsidian vault) and returns one or more **project tags**. The above article, for example, was tagged #productivity, which helped me find it for this post before I actually processed it fully
	* (note: if no project can be found, it returns #tagme)
* (NEW in v2) it then **clips the article itself into a note of its own** in my reading queue folder, using [Defuddle](https://github.com/kepano/defuddle) (the engine inside Obsidian Web Clipper) to grab the full text and convert it into markdown, under frontmatter recording the title, the original URL, the author, the site and the tags (this is the main upgrade since [[ReadingQ Manager - 2 - 2026-09-05|v2 of this post]])
* finally, it processes the line containing the URL in my daily note:
	* the line becomes a [Task](https://community.obsidian.md/plugins/obsidian-tasks-plugin) pointing at that new note and the original URL; 
	* the task also gets a deadline of tomorrow, the project tag(s) and the #readme tag; 
	* and it's moved up to the penultimate section of my daily note ("Added to readme today"), so the inbox empties itself and nothing is ever processed twice.

**As a result, the raw content of the article is now sitting in my vault, while the Tasks plugin ensures that the ToDo to read and (if useful) push it down my content pipeline appears:**

* in today's daily note (under "Added to readme today") and **tomorrow's daily note** (under "to read today") thanks to the auto-added deadline and my daily note template 
* in each **relevant project's ToDo list** (a section of each project's Map of Content), thanks to the auto-added project tag.
* in a **central Reading Queue**, where it can be easily filtered by tag (that's how I found Chris' article)

Note that **ReadingQ Manager is not a panacea:** it doesn't solve the underlying challenge of finding the time to read and annotate content on my Queue, as that's where I actually learn and generate many of my ideas. 

But it's still an improvement: **reading queue content now appears everywhere relevant** throughout my notes. And I am more likely to find time to read it if I've saved time to discover it, when I need it. 

## What's next
### Clipping for Karpathy

**Version 1 of this plugin turned *links* into tasks, so why does this version record a copy of the *content*? (Hint: I'm not republishing anyone's content on my Hub).**

My original reading queue, as Chris Ng would put it, was a list of promises I made my future self feel guilty for breaking. Version 1 of RQM (link in footer) improved how I tracked and found my reading queue content. With this new version, however, my reading queue has become a folder of content which my Loki can work with directly.

> my reading queue has become a folder of content which Loki can work with directly

This follows [the model Andrej Karpathy set out](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) last April. I'll be brief, as there's no shortage of articles summarising Karpathy's idea:

* most people using LLMs upload documents into a session, get an answer, and then do it all again next time. One session can't learn from previous ones, so **knowledge doesn't accumulate**. 
* Karpathy suggested grabbing and storing *everything* and getting your LLM to create and maintain **a wiki** from it, along with files telling it how the wiki's organised, and how to keep it that way. Your LLM agent then uses that wiki as a knowledgebase to answer your questions without you having to feed it everything each time. 
* As a result, your LLM compounds, building in value as you use it, exactly like Loki, m persistent agent.

V2 of ReadingQ Manager turns my reading queue into the raw material required for this model. 

### Hub Manager and the line AI won't cross

**Another plugin is coming for my content pipeline. But not for all of it.** 

ReadingQ Manager gets content into my library and adds a task to read it onto various reading queues. Then "Hub Manager" will take over, supporting the rest of the content pipeline until content is ready to publish on my Hub via a forked version of the [Obsidian-Standard-site plugin](https://github.com/SootyOwl/obsidian-standard-site) and 2-3 ATprotocol lexicons (two of which already exist):

![[content-pipeline-localfirst-all.png]]
*The Hub Manager plugin takes over where ReadingQ Manager stops, helping create and move content through my pipeline until it's ready to publish onto my Personal Data Server (PDS).*

I will publish more on Hub Manager when it's operational. For now, I'll just note where I've drawn the line AI shall *not* cross on my content pipeline. While Loki and the plugins it create will *support* the processes of curating other people's content, creating my own, and publishing everything onto my Hub, **AI will not do any writing for me, because writing = thinking**. 

> writing = thinking... If you rely on an AI to write ... none of that knowledge will actually get into your head

Not that AI can't write - it can, badly, but it's improving. But the process of writing is indispensable to both learning other people's ideas and coming up with your own. If you rely on an AI to write your notes, posts and articles for you, none of that knowledge will actually get into your head, where it can connect to everything else there to spark new ideas. As the authors of [a recent MIT report](https://aiandeducation.mit.edu/report/) put it, "Getting the right answer from a chatbot can create the illusion of learning".

So while Loki may help me organise, and write the software to help me publish, it's still me who identifies what's valuable and why, and writes every word. Otherwise I'll internalise, and publish, nothing of value.

## On vibe coding

**While Hub Manager is already being tested, I'll probably stumble at the final hurdles. But that's OK.** 

ReadingQ Manager and Hub Manager are internal tools - if they're poor quality code, I'm the only one who'll suffer. But creating a lexicon to support MyHub, forking someone else's plugin to publish from Obsidian to my PDS, and redeveloping MyHub to publish that content are entirely different tasks, and the code will be public. So I'm not sure to get there.

But even if I fail, I'll have learnt how to use Loki to improve my own productivity tools, rather than adopting and configuring someone else's. This "[malleable software" paradigm](https://www.inkandswitch.com/malleable-software/) promises to be quite revolutionary, and could lead to an extraordinary flourishing of creativity as the 99% of the population who can't code discover that they can nonetheless create new tools.

So before you condemn me for using AI, remember:

* **I'm not a developer**, so this could not exist otherwise. To be frank, I'm tired of describing systems I'll never see built because I can't raise the funds to pay developers to build them (I've been waiting for Create New Version, for example, [since early 2023](https://mathewlowry.medium.com/two-wiki-authors-and-a-blogger-walk-into-a-bar-7106c8376c6e))  
* This is **personal code**: a few Markdown files in a directory inside an Obsidian vault on 2 PCs and a phone. I don't intend releasing this to the world and am not committing to maintain it, so it doesn't matter if the code isn't elegant 

All that said, I'm still conflicted about using Claude and am [still thinking my way through this](https://mu.social/profile/mathewlowry.eurosky.social/post/3mutse4iesk2o). Technology isn't neutral: the way AI is being concentrated into a few massive companies is the very opposite of healthy; the entire product is based on theft; and the environmental costs are huge. On the other hand, the outpouring of creativity and productivity from letting everyone build software could be literally world-changing.

> I can't *not* know something about this

It's still too early to tell how these costs and benefits line up, but I do know that I can't *not* know something about this. The only way of really internalising what this technology means is to kick those tyres myself, so expect more news from my own personal coalface.

I also know that if I do ever release something, it'll only ever be a proof of concept, designed to show people what the ideas in my head actually look like. If that leads to enough interest to raise funds, **those funds will go to actual developers to sort out the slop.**

Having said all that, if you want to take a look at ReadingQ Manager or Hub Manager, hit me up and I'll pass them across. Just don't expect me to maintain or debug anything, and keep in mind that by the time you read this they'll probably have evolved.

---
## Revision Notes

This is one of this wiki's pages managed with the **permanent versions pattern** described in  [Two wiki authors and a blogger walk into a bar…](https://mathewlowry.medium.com/two-wiki-authors-and-a-blogger-walk-into-a-bar-7106c8376c6e)  

- changes in this version: (2026-09-05):
	- introduced the latest version of RQM (full content clipper)
	- added Karpathy, Hub Manager, more on using AI
- version control
    - this is version: 3
    - this is the current version: [[ReadingQ]]
    - here is the previous version:  [[ReadingQ 2]]